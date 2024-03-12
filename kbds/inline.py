from aiogram.types import InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallback(CallbackData, prefix='menu'):
    level: int
    menu_name: str
    category: int | None = None #категория может быть(int) или не быть. По умолчанию её нет
    page: int = 1
    product_id: int | None = None


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Товары 🍕": "catalog",
        "Корзина 🛒": "cart",
        "О нас ℹ️": "about",
        "Оплата 💰": "payment",
        "Доставка ⛵": "shipping",
    }
    for text, menu_name in btns.items():
        if menu_name == 'catalog':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallback(level=level+1, menu_name=menu_name).pack())) 
                    #pack() формирует строку из callback_data
        elif menu_name == 'cart':
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallback(level=3, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                    callback_data=MenuCallback(level=level, menu_name=menu_name).pack()))
            
    return keyboard.adjust(*sizes).as_markup()


def get_user_catalog_btns(*, level: int, categories: list, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text='Назад',
                callback_data=MenuCallback(level=level-1, menu_name='main').pack()))
    keyboard.add(InlineKeyboardButton(text='Корзина 🛒',
                callback_data=MenuCallback(level=3, menu_name='cart').pack()))
    
    for c in categories:
        keyboard.add(InlineKeyboardButton(text=c.name,
                callback_data=MenuCallback(level=level+1, menu_name=c.name, category=c.id).pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_products_btns(
    *,
    level: int,
    category: int,
    page: int,
    pagination_btns: dict,
    product_id: int,
    sizes: tuple[int] = (2, 1)
):
    keyboard = InlineKeyboardBuilder()

    keyboard.add(InlineKeyboardButton(text='Назад',
                callback_data=MenuCallback(level=level-1, menu_name='catalog').pack()))
    keyboard.add(InlineKeyboardButton(text='Корзина 🛒',
                callback_data=MenuCallback(level=3, menu_name='cart').pack()))
    keyboard.add(InlineKeyboardButton(text='Купить 💵',
                callback_data=MenuCallback(level=level, menu_name='add_to_cart', product_id=product_id).pack()))

    keyboard.adjust(*sizes)

    row = []
    for text, menu_name in pagination_btns.items():
        if menu_name == "next":
            row.append(InlineKeyboardButton(text=text,
                    callback_data=MenuCallback(
                        level=level,
                        menu_name=menu_name,
                        category=category,
                        page=page + 1).pack()))
        
        elif menu_name == "previous":
            row.append(InlineKeyboardButton(text=text,
                    callback_data=MenuCallback(
                        level=level,
                        menu_name=menu_name,
                        category=category,
                        page=page - 1).pack()))

    return keyboard.row(*row).as_markup()


def get_user_cart(
    *,
    level: int,
    page: int | None,
    pagination_btns: dict | None,
    product_id: int | None,
    sizes: tuple[int] = (3,)
):
    keyboard = InlineKeyboardBuilder()
    if page:
        keyboard.add(InlineKeyboardButton(text='Удалить',
                    callback_data=MenuCallback(level=level, menu_name='delete', product_id=product_id, page=page).pack()))
        keyboard.add(InlineKeyboardButton(text='-1',
                    callback_data=MenuCallback(level=level, menu_name='decrement', product_id=product_id, page=page).pack()))
        keyboard.add(InlineKeyboardButton(text='+1',
                    callback_data=MenuCallback(level=level, menu_name='increment', product_id=product_id, page=page).pack()))

        keyboard.adjust(*sizes)

        row = []
        for text, menu_name in pagination_btns.items():
            if menu_name == "next":
                row.append(InlineKeyboardButton(text=text,
                        callback_data=MenuCallback(level=level, menu_name=menu_name, page=page + 1).pack()))
            elif menu_name == "previous":
                row.append(InlineKeyboardButton(text=text,
                        callback_data=MenuCallback(level=level, menu_name=menu_name, page=page - 1).pack()))

        keyboard.row(*row)

        row2 = [
        InlineKeyboardButton(text='На главную 🏠',
                    callback_data=MenuCallback(level=0, menu_name='main').pack()),
        InlineKeyboardButton(text='Заказать',
                    callback_data=MenuCallback(level=0, menu_name='order').pack()),
        ]
        return keyboard.row(*row2).as_markup()
    else:
        keyboard.add(
            InlineKeyboardButton(text='На главную 🏠',
                    callback_data=MenuCallback(level=0, menu_name='main').pack()))
        
        return keyboard.adjust(*sizes).as_markup()


def get_callback_btns(
    *,
    btns: dict[str, str],
    sizes: tuple[int] = (2,)):

    keyboard = InlineKeyboardBuilder()

    for text, data in btns.items():
        
        keyboard.add(InlineKeyboardButton(text=text, callback_data=data))

    return keyboard.adjust(*sizes).as_markup()




# def get_url_btns(
#     *,
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):

#     keyboard = InlineKeyboardBuilder()

#     for text, url in btns.items():
        
#         keyboard.add(InlineKeyboardButton(text=text, url=url))

#     return keyboard.adjust(*sizes).as_markup()


# #Создать микс из CallBack и URL кнопок
# def get_inlineMix_btns(
#     *,
#     btns: dict[str, str],
#     sizes: tuple[int] = (2,)):

#     keyboard = InlineKeyboardBuilder()

#     for text, value in btns.items():
#         if '://' in value:
#             keyboard.add(InlineKeyboardButton(text=text, url=value))
#         else:
#             keyboard.add(InlineKeyboardButton(text=text, callback_data=value))

#     return keyboard.adjust(*sizes).as_markup()