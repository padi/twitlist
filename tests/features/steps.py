from lettuce import *
from splinter.browser import Browser
from nose.tools import assert_equals

@before.all
def set_browser():
  world.browser = Browser()

@after.all
def kill_browser(total):
  world.browser.quit()

@step(u'Given I access the url "([^"]*)"')
def access_url(step, directory):
  url = "localhost:8080" + directory
  world.browser.visit(url)

@step(u'Then I see the header "([^"]*)"')
def see_header(step, text):
  assert world.browser.is_text_present('TwitList'), "header 'Twitlist' not found"