from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, Text, Float, DateTime, func

class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now()) #func.now() - текущее время и дата
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    #onupdate автоматически обновляет дату при обновлении какого-либо поля таблицы
    

class Product(Base):
    __tablename__ = 'product'

    #аннотация типов для каждого поля
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    description: Mapped[str] = mapped_column(Text)

    #asdecimal=True - преобразует float питона в sql DECIMAL
    price: Mapped[float] = mapped_column(Float(asdecimal=True), nullable=False) 
    image: Mapped[str] = mapped_column(String(150))