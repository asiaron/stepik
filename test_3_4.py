import pytest
import selenium.webdriver as wd
import time
import math

optional_feedback_class = ".smart-hints__feedback.hints__component.hints__component_showed.ember-view"

pages = ["https://stepik.org/lesson/{}/step/1".format(i) for i in [
    236895, 236896, 236897, 236898, 236899, 236903, 236904, 236905
]]

class Test_pages:

    @classmethod
    def setup_class(self):
        print('\nclass setuped\n')
        self.dr = wd.Chrome()
        self.dr.implicitly_wait(5)

    @classmethod
    def teardown_class(self):
        print('\nclass closed\n')
        self.dr.quit()

    @pytest.mark.parametrize('page', pages)
    def test_is_correct(self, page):
        self.dr.get(page)
        
        answer = math.log(int(time.time()))
        self.dr.find_element_by_tag_name('textarea').send_keys(str(answer))
        self.dr.find_element_by_class_name('submit-submission').click()
        
        result = self.dr.find_element_by_css_selector(optional_feedback_class).text
        
        assert result == "Correct!", result

import pytest
import time
from selenium import webdriver

def test_find_button_add_to_basket(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    assert len(button.text) > 0, 'No Button!'