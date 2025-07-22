from datetime import datetime
from typing import List, Union


### **Основные использования Pydantic**  

#### **1. Валидация данных**  
#Pydantic позволяет определять модели данных с аннотациями типов и автоматически проверяет их корректность.  

from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    is_active: bool = True

user = User(name="Alice", age=25)  # Автоматическая валидация
print(user.model_dump())  # {'name': 'Alice', 'age': 25, 'is_active': True}


#### **2. Работа с конфигурациями (Settings Management)**  
# Pydantic упрощает загрузку и валидацию настроек приложения, например, из переменных окружения.  

from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "My App"
    db_url: str = "postgres://user:pass@localhost/db"

    class Config:
        env_file = ".env"

settings = Settings()
print(settings.db_url)


#### **3. Валидация запросов и ответов в FastAPI**  
# Pydantic интегрирован в FastAPI для автоматической валидации входных и выходных данных API.  

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.model_dump()}

#### **4. Парсинг JSON и других форматов**  
#Pydantic может автоматически преобразовывать JSON, YAML и другие форматы в Python-объекты.  

import json
from pydantic import BaseModel

class Data(BaseModel):
    id: int
    value: str

json_data = '{"id": 1, "value": "test"}'
data = Data.model_validate_json(json_data)
print(data.value)  # "test"


#### **5. Сериализация и десериализация (Dump/Load)**  
#Pydantic предоставляет методы для преобразования моделей в словари (`model_dump()`) и JSON (`model_dump_json()`).  

user = User(name="Bob", age=30)
user_dict = user.model_dump()  # {'name': 'Bob', 'age': 30, 'is_active': True}
user_json = user.model_dump_json()  # '{"name":"Bob","age":30,"is_active":true}'


#### **6. Кастомные валидаторы**  
#Можно добавлять свои правила валидации с помощью декоратора `@validator`.  

from pydantic import BaseModel, validator

class Person(BaseModel):
    name: str
    age: int

    @validator("age")
    def check_age(cls, v):
        if v < 0:
            raise ValueError("Age cannot be negative")
        return v

person = Person(name="John", age=-5)  # ValueError: Age cannot be negative


#### **7. Работа с динамическими моделями (`create_model`)**  
# Pydantic позволяет создавать модели динамически.  

from pydantic import BaseModel, create_model

DynamicModel = create_model("DynamicModel", field1=(str, ...), field2=(int, 0))
obj = DynamicModel(field1="test")
print(obj)  # DynamicModel field1='test' field2=0


#### **8. Валидация URL, Email, UUID и других сложных типов**  
## Pydantic поддерживает специализированные типы (`EmailStr`, `UrlStr`, `UUID`, `SecretStr` и др.).  

from pydantic import BaseModel, EmailStr

class Contact(BaseModel):
    email: EmailStr
    website: str  # Можно добавить валидацию URL

contact = Contact(email="user@example.com", website="https://example.com")


#### **9. Интеграция с ORM (SQLAlchemy, TortoiseORM и др.)**  
# Pydantic может работать с ORM-моделями, преобразовывая их в схемы данных.  

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)

class UserSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True  # Ранее `orm_mode = True`

db_user = UserDB(id=1, name="Alice")
schema_user = UserSchema.model_validate(db_user)


#### **10. Валидация данных в CLI-приложениях (например, с Typer)**  

import typer
from pydantic import BaseModel

class Args(BaseModel):
    name: str
    count: int = 1

def main(name: str, count: int = 1):
    args = Args(name=name, count=count)
    print(args.model_dump())

typer.run(main)
