from hm_3_page_object.helpers.classproperty import classproperty

BASE_URL = "https://jdi-testing.github.io/jdi-light"


class UrlFactory:
    """
    Фабрика URL адресов
    """

    @classproperty
    def urls(cls):
        return {'IndexPage': '/index.html',
                'DifferentElementsPage': '/different-elements.html'}

    @classmethod
    def get_url(cls, page):
        return f'{BASE_URL}{cls.urls[page.__class__.__name__]}'
