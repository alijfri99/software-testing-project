from selenium import webdriver
from attribute_tag_creator import AttributeTagCreator
from image_link_checker import ImageLinkChecker
from deprecated_attribute_checker import DeprecatedAttributeChecker
from meta_refresh_checker import MetaRefreshChecker
from style_attribute_checker import StyleAttributeChecker
from identical_link_checker import IdenticalLinkChecker
from input_overlap_checker import InputOverlapChecker


PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"

# attribute_tag_creator = AttributeTagCreator(driver)
# attribute_tag_creator.create()
# attribute_tag_creator.process_attribute_tags()
# input()

webpage = input("Please enter the web page address: ")
driver = webdriver.Chrome(PATH)
driver.get(webpage)

image_link_checker = ImageLinkChecker(driver)
deprecated_attribute_checker = DeprecatedAttributeChecker(driver)
identical_link_checker = IdenticalLinkChecker(driver)
meta_refresh_checker = MetaRefreshChecker(driver)
style_attribute_checker = StyleAttributeChecker(driver)
input_overlap_checker = InputOverlapChecker(driver)

image_link_checker.check()
deprecated_attribute_checker.check()
meta_refresh_checker.check()
style_attribute_checker.check()
identical_link_checker.check()
input_overlap_checker.check()