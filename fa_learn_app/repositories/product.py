from typing import List, Dict, Optional
import uuid
from fa_learn_app.models.product import ProductIn, ProductOut, ProductStorage
from fa_learn_app.utils.repository_utils import convert_product_storage_to_out, convert_product_in_to_storage
_

class BaseProductRepository:
    """Базовый класс для реализации функционала работы с продуктами"""

    def get_by_id(self, id :uuid.UUID | int) -> ProductOut:
        raise NotImplementedError

    def get_all(self, limit :int, skip :int) -> List[ProductOut]:
        raise NotImplementedError

    def create(self, product :ProductIn) -> ProductOut:
        raise NotImplementedError

class ProductTmpRepository(BaseProductRepository):
    """Реализация продукта с временным хранилищем в объектк Dict"""

    def __init__(self,):

        #Временное хранилище
        self._dict_products :Dict[uuid.UUID, ProductStorage] = {}

    def get_by_id(self, id :uuid.UUID) -> Optional[ProductOut]:
        """Получение проукта по id"""

        product :ProductStorage = self._dict_products.get(id, None)
        if product is None:
            return None
        product_out :ProductOut = convert_product_storage_to_out(product)
        return product_out

    def get_all(self, limit: int, skip: int) -> List[ProductOut]:
        """Получение всех продуктов"""

        product_out_list :List[ProductOut] = []
        for _, product in self._dict_products.items():
            product_out_list.append(convert_product_storage_to_out(product))
        return product_out_list[skip:skip+limit]

    def create(self, product: ProductIn) -> ProductOut:
        """Создание продукта"""

        product_storage :ProductStorage = convert_product_in_to_storage(product)
        self._dict_products.update({product_storage.id: product_storage})
        product_out :ProductOut = convert_product_storage_to_out(product_storage)
        return product_out