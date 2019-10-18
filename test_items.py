link_template = 'http://selenium1py.pythonanywhere.com/{}/catalogue/coders-at-work_207/'
add_to_basket_button_xpath = '//button[@type="submit" and @class="btn btn-lg btn-primary btn-add-to-basket"]'

def test_add_to_basket_button_exist(browser, language):
    browser.get(link_template.format(language))
    browser.find_element_by_xpath(add_to_basket_button_xpath)
    # if nothing raised everything is good