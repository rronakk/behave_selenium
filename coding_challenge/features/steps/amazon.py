from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

@when(u'I go to the amazon home page')
def step_impl(context):
    context.browser.get('https://www.amazon.com')

@when(u'I enter search text "{search_item}" in search field and click submit')
def step_impl(context, search_item):
    br = context.browser
    search_field = br.find_element_by_id("twotabsearchtextbox")
    search_field.send_keys(search_item)
    br.find_element_by_class_name("nav-input").click()

@then(u'I should see search result "{search_item}"')
def step_imp(context, search_item):
    br = context.browser
    WebDriverWait(br, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shoppingEngineSectionHeaders")))
    assert "Amazon.com: " + search_item in br.title

@then(u'Total number of search result is a positive integer')
def step_imp(context):
    br = context.browser
    # check if the search result matches the regex defined.
    assert re.search(r'[\w\s,-]+', br.find_element_by_id("s-result-count").text)

@then(u'No search result should be displayed')
def step_imp(context):
    br = context.browser
    # current page just refresh, when user just click submit
    assert "Amazon.com: Online Shopping for Electronics, Apparel, Computers, Books, DVDs & more" in br.title


