from src.base_objects.elements.base_element import BaseElement
from src.base_objects.elements.clickable_element import ClickableElement
from selenium.webdriver.common.by import By


class Footer(BaseElement):
    """
    Class for Footer
    """
    copyright_text: str = 'Copyright © 2021 SAP SE or an SAP affiliate company. All rights reserved.'

    accelerator = BaseElement(by=By.XPATH, value='//div[contains(text(), "Accelerator")]',
                              name='Footer column name "Accelerator"')
    about_sap = ClickableElement(by=By.XPATH, value='//a[contains(text(), "About SAP")]',
                                 name='Footer link "About SAP"')
    faq = ClickableElement(by=By.XPATH, value='//a[contains(text(), "FAQ")]',
                           name='Footer link "FAQ"')

    sap_customer_experience = BaseElement(by=By.XPATH, value='//div[contains(text(), "SAP Customer Experience")]',
                                          name='Footer column name "SAP Customer Experience"')
    visit_sap = ClickableElement(by=By.XPATH, value='//a[contains(text(), "Visit SAP")]',
                                 name='Footer link "Visit SAP"')
    contact_us = ClickableElement(by=By.XPATH, value='//a[contains(text(), "Contact Us")]',
                                  name='Footer link "Contact Us"')

    follow_us = BaseElement(by=By.XPATH, value='//div[contains(text(), "Follow Us")]',
                            name='Footer column name "Follow Us"')
    agile_commerce_blog = ClickableElement(by=By.XPATH, value='//a[contains(text(), "Agile Commerce Blog")]',
                                           name='Footer link "Agile Commerce Blog"')
    linked_in = ClickableElement(by=By.XPATH, value='//a[contains(text(), "Linked In")]',
                                 name='Footer link "Linked In"')
    twitter = ClickableElement(by=By.XPATH, value='//a[contains(text(), "Twitter")]',
                               name='Footer link "Twitter"')
