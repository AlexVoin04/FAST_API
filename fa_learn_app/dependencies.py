from fa_learn_app.repositories.product import ProductTmpRepository

TMP_PEROSITORY = ProductTmpRepository()

def get_product_repo() -> ProductTmpRepository:
    """Получение Product репозитория"""

    return TMP_PEROSITORY