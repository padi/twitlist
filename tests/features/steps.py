from lettuce import *
from selenium import webdriver

browser = webdriver.Firefox()

@step(u'Given I visit the index page')
def given_i_visit_the_index_page(step):
    browser.get("localhost:8080")

@step(u'Then I see "([^"]*)"')
def then_i_see_group1(step, group1):
    assert False, 'This step must be implemented'
    # assert "TwitList" == browser.find_element_by_name('h2')

browser.close()