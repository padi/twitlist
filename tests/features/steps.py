from lettuce import *
from selenium import webdriver
from nose.tools import assert_equals

@before.all
def set_browser():
	world.browser = webdriver.Firefox()
	print "SET BROWSER"

@after.all
def kill_browser(total):
	world.browser.close()

@step(u'Given I access the url "([^"]*)"')
def access_url(step, directory):
	url = "localhost:8080" + directory
	world.browser.get(url)

@step(u'Then I see the header "([^"]*)"')
def see_header(step, text):
	assert False, 'This step must be implemented'
	# header = world.dom.cssselect('h1')[0]
	# assert header.text == text