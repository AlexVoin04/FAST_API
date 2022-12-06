import datetime
import uuid
from fa_learn_app.models.product import ProductStorage,ProductOut, ProductIn


def convert_product_storage_to_out(product : ProductStorage) -> ProductOut:
    """Производит конвертацию ProductStorage --> ProductOut"""

    tmp_dict:dict = product.dict()
    tmp_dict.pop("secret_token", None)
    return ProductOut(**tmp_dict)

def convert_product_in_to_storage(product :ProductIn) -> ProductStorage:
    """Производит конвертацию ProductIn --> ProductStorage"""

    tmp_dict :dict = product.dict()
    product_storage = ProductStorage(id = uuid.uuid4(),
                                    create_at = datetime.datetime.now(),
                                    **tmp_dict)
    return product_storage

def update_product_in_to_storage(old_id :uuid.UUID, product_update :ProductIn) -> ProductStorage:

    tmp_dict :dict = product_update.dict()
    product_storage = ProductStorage(id = old_id,
                                    create_at = datetime.datetime.now(),
                                    **tmp_dict)
    return product_storage
                                    