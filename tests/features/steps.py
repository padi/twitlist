from lettuce import *
from splinter.browser import Browser
from nose.tools import assert_equals
import re

@before.all
def set_browser():
  world.browser = Browser('chrome')

@after.all
def kill_browser(total):
  world.browser.quit()

@step(u'Given I access the url "([^"]*)"')
def access_url(step, directory):
  url = "localhost:8080" + directory
  world.browser.visit(url)

@step(u'Then I should see the header "([^"]*)"')
def should_see_header(step, text):
  assert world.browser.is_text_present('TwitList'), "header 'Twitlist' not found"

@step(u'(?:Then|And) I should see the Twitter sign in button')
def should_see_twitter_sign_in(step):
    element = world.browser.find_by_id('sign-in-button').first
    assert re.search('/oauth/twitter/login', element['href']) , element['href'] + " did not match with '/oauth/twitter/login'"

@step(u'When I click the Twitter sign in button')
def click_twitter_sign_in_button(step):
    world.browser.find_by_css('#sign-in-button').click()