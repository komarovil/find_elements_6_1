import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions, FirefoxOptions
import sys


@pytest.mark.skipif(not "--chrome" in sys.argv, reason="chrome")
def test_chrome_positive(chrome_browser, url):
    chrome_browser.get(url)
    chrome_browser.find_element_by_link_text('My Account').click()
    chrome_browser.find_element_by_link_text('Login').click()
    inputlogint = chrome_browser.find_element_by_css_selector('#input-email')
    inputlogint.send_keys('admin')
    inputpassword = chrome_browser.find_element_by_css_selector("#input-password")
    inputpassword.send_keys("password")
    chrome_browser.find_element_by_link_text('Login').click()
    assert chrome_browser.find_element_by_css_selector('input.btn')


@pytest.mark.skipif(not "--chrome" in sys.argv, reason="chrome")
def test_chrome_negarive(chrome_browser, url):
    chrome_browser.get(url)
    chrome_browser.find_element_by_link_text('My Account').click()
    chrome_browser.find_element_by_link_text('Login').click()
    inputlogint = chrome_browser.find_element_by_css_selector('#input-email')
    inputlogint.send_keys('12321312312311232131231231212321312312312123213123123123123213231232132123213123123123123213231232132212321312312312123213123123123123213231232132123213123123123123213231232132')
    inputpassword = chrome_browser.find_element_by_css_selector("#input-password")
    inputpassword.send_keys('12321312312311232131231231212321312312312123213123123123123213231232132123213123123123123213231232132212321312312312123213123123123123213231232132123213123123123123213231232132')
    chrome_browser.find_element_by_link_text('Login').click()


@pytest.mark.skipif(not "--firefox" in sys.argv, reason="firefox")
def test_firefox_positive(firefox_browser, url):
    firefox_browser.get(url)
    firefox_browser.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a/span[1]').click()
    firefox_browser.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a').click()
    inputlogint = firefox_browser.find_element_by_xpath('//*[@id="input-email"]')
    inputlogint.send_keys('admin')
    inputpassword = firefox_browser.find_element_by_xpath('//*[@id="input-password"]')
    inputpassword.send_keys('password')
    firefox_browser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/form/input').click()
    assert firefox_browser.find_element_by_xpath('/html/body/div[2]/div[1]')


@pytest.mark.skipif(not "--firefox" in sys.argv, reason="firefox")
def test_firefox_negative(firefox_browser, url):
    firefox_browser.get(url)
    firefox_browser.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/a/span[1]').click()
    firefox_browser.find_element_by_xpath('/html/body/nav/div/div[2]/ul/li[2]/ul/li[2]/a').click()
    inputlogint = firefox_browser.find_element_by_xpath('//*[@id="input-email"]')
    inputlogint.send_keys('')
    inputpassword = firefox_browser.find_element_by_xpath('//*[@id="input-password"]')
    inputpassword.send_keys('')
    firefox_browser.find_element_by_link_text('Login').click()