from selenium.webdriver.common.by import By
from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.base_objects.elements.list import List


class NavigationBar(BaseElement):
    NAVI_ELEMENTS = "//ul[contains(@class, 'nav__links--products js-offcanvas-links')]/li/span/a"
    NAVI_ELEMENT_TEMPLATE = NAVI_ELEMENTS + "[contains(text(), {title})]"
    MENU_LIST = NAVI_ELEMENT_TEMPLATE + "/../..//div[contains(@class, 'sub-navigation-section col-md-')]/div"
    BRANDS_LIST = "//span/a[contains(text(), 'Brands')]/../..//ul[@class='sub-navigation-list has-title']/li/a"
    SUB_ELEMENT_LIST = "//span/a[contains(text(), '{menu}}')]/../..//div[@class='title']" \
                       "[contains(text(), '{submenu}')]/../ul[@class='sub-navigation-list has-title']/li/a"
    #

    _links = {}

    @property
    def rows(self):
        return [title.text for title in self._element.find_elements_by_xpath(self.NAVI_ELEMENTS)]

    def goto(self, title):
        return self._element.find_element_by_xpath(self.NAVI_ELEMENT_TEMPLATE.format(title=title)).click()

    def hover(self, title):
        return self._element.find_element_by_xpath(self.NAVI_ELEMENT_TEMPLATE.format(title=title)).hover()

    @property
    def elements(self):
        result = {}

        for link in self.rows:
            if link.upper() == 'BRANDS':
                result.update({
                    link: {
                        'All brands': {
                            elem.text: elem for elem in self._element.find_elements_by_xpath(self.BRANDS_LIST)
                        }
                    }
                })
            else:
                for submenu in self._element.find_elements_by_xpath(self.MENU_LIST.format(title=link)):
                    for subelem in self._element.find_elements_by_xpath(
                            self.SUB_ELEMENT_LIST.format(menu=link, submenu=submenu)
                    ):
                        result[link][submenu.text].update({subelem.text: subelem})
        return result