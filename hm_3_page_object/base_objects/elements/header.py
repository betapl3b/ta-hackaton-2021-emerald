from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.navigation_bar import NavigationBar


class Header(BaseElement):
    """
    Header class
    """
    naviagation_bar = NavigationBar("//ul[contains(@class, 'nav__links--products js-offcanvas-links')]", name='navi', by='xpath')

