import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class BaseProduct(BaseModel):
    """Базовый класс для описагия продукта"""

    name :str
    description :Optional[str] = None


class ProductIn(BaseProduct):
    """Класс описывает продукт, отправляемый от пользователя"""

    secret_token :str


class ProductOut(BaseProduct):
    """Класс описывает продукт, который отправляется пользователю (без секретной информации)"""

    id :uuid.UUID
    create_at :datetime.datetime

class ProductStorage(BaseProduct):
    """Класс описывает хранение продукта в хранилище"""

    id :uuid.UUID
    create_at :datetime.datetime
    secret_token :str