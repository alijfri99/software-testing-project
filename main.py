from selenium import webdriver
from image_link_checker import ImageLinkChecker
from deprecated_attribute_checker import DeprecatedAttributeChecker
from meta_refresh_checker import MetaRefreshChecker
from style_attribute_checker import StyleAttributeChecker
from identical_link_checker import IdenticalLinkChecker
from input_overlap_checker import InputOverlapChecker


PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# webpage = input("Please enter the web page address: ")
webpage = 'file://C:/Users/Ali/IdeaProjects/software-testing-project/sample2.htm'
driver.get(webpage)

image_link_checker = ImageLinkChecker(driver)
deprecated_attribute_checker = DeprecatedAttributeChecker(driver)
identical_link_checker = IdenticalLinkChecker(driver)
meta_refresh_checker = MetaRefreshChecker(driver)
style_attribute_checker = StyleAttributeChecker(driver)
input_overlap_checker = InputOverlapChecker(driver)

'''
image_link_checker.check()
deprecated_attribute_checker.check()
meta_refresh_checker.check()
style_attribute_checker.check()
identical_link_checker.check()
'''
input_overlap_checker.check()