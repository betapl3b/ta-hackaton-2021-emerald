from hm_3_page_object.base_objects.elements.base_element import BaseElement


class Sidebar(BaseElement):
    """
    Класс, описывающий сайдбар
    """

    def __len__(self):
        return len(self.elements)

    @property
    def elements(self):
        return self.text.split('\n')
