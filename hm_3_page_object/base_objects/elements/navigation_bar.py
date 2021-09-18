from selenium.webdriver import ActionChains

from hm_3_page_object.base_objects.elements.base_element import BaseElement
from hm_3_page_object.helpers.browser import Browser


class NavigationBar(BaseElement):
    NAVI_ELEMENTS = "//ul[contains(@class, 'nav__links--products js-offcanvas-links')]/li/span/a"
    NAVI_ELEMENT_TEMPLATE = NAVI_ELEMENTS + "[contains(text(), '{title}')]"
    "//ul[contains(@class, 'nav__links--products js-offcanvas-links')]/li/span/a[contains(text(), '{title}')]"
    "/../..//div[contains(@class, 'sub-navigation-section col-md-')]/div"
    MENU_LIST = NAVI_ELEMENT_TEMPLATE + "/../..//div[contains(@class, 'sub-navigation-section col-md-')]/div"
    BRANDS_LIST = "//span/a[contains(text(), 'Brands')]/../..//ul[@class='sub-navigation-list has-title']/li/a"
    SUB_ELEMENT_LIST = "//span/a[contains(text(), '{menu}')]/../..//div[@class='title']" \
                       "[contains(text(), '{submenu}')]/../ul[@class='sub-navigation-list has-title']/li/a"

    @property
    def rows(self):
        return [title.get_attribute('textContent') for title in
                self._element.find_elements_by_xpath(self.NAVI_ELEMENTS)]

    def goto(self, title):
        return self._element.find_element_by_xpath(self.NAVI_ELEMENT_TEMPLATE.format(title=title.capitalize())).click()

    def hover(self, title):
        elem = self._element.find_element_by_xpath(self.NAVI_ELEMENT_TEMPLATE.format(title=title.capitalize()))
        hover = ActionChains(Browser().driver).move_to_element(elem)
        hover.perform()

    @property
    def elements(self):
        result = {}

        for link in self.rows:
            if link.upper() == 'BRANDS':
                result.update({
                    link: {
                        'All brands': {
                            elem.get_attribute('textContent'): elem for elem in
                            self._element.find_elements_by_xpath(self.BRANDS_LIST)
                        }
                    }
                })
            else:
                result.update({link: {}})
                for submenu in self._element.find_elements_by_xpath(self.MENU_LIST.format(title=link)):
                    result[link].update({submenu.get_attribute('textContent'): {}})
                    for subelem in submenu.find_elements_by_xpath(
                            self.SUB_ELEMENT_LIST.format(menu=link, submenu=submenu.get_attribute('textContent'))
                    ):
                        result[link][submenu.get_attribute('textContent')].update(
                            {subelem.get_attribute('textContent'): subelem})
        return result
