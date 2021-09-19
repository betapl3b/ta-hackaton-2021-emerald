from src.helpers.classproperty import classproperty

BASE_URL = "https://apparel-uk.local:9002/ucstorefront/en"


class UrlFactory:
    """
    Фабрика URL адресов
    """

    @classproperty
    def urls(cls):
        return {
            'BasePage': '',
            'HomePage': '',
            'LoginPage': '/login.html',
            'CartPage': '/cart.html',
            'StoreFinderPage': '/store-finder.html',
            'CategoriesPage': '/search'
        }

    @classmethod
    def get_url(cls, page):
        return f'{BASE_URL}{cls.urls[page.__class__.__name__]}'
