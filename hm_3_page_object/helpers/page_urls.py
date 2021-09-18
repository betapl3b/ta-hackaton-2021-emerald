from hm_3_page_object.helpers.classproperty import classproperty

BASE_URL = "https://apparel-uk.local:9002/ucstorefront/en"


class UrlFactory:
    """
    Фабрика URL адресов
    """

    @classproperty
    def urls(cls):
        return {'LoginPage': '/login.html',
                'DifferentElementsPage': '/different-elements.html'}

    @classmethod
    def get_url(cls, page):
        return f'{BASE_URL}{cls.urls[page.__class__.__name__]}'
