from selenium import webdriver
from image_link_checker import ImageLinkChecker
from deprecated_attribute_checker import DeprecatedAttributeChecker
from identical_link_checker import IdenticalLinkChecker
from meta_refresh_checker import MetaRefreshChecker

PATH = "C:\Program Files (x86)\chromedriver\chromedriver.exe"
driver = webdriver.Chrome()

# webpage = input("Please enter the web page address: ")
webpage = 'file:/home/Arya/Work/PyCharm/project/software_testing_prj2/sl.html'
driver.get(webpage)

image_link_checker = ImageLinkChecker(driver)
deprecated_attribute_checker = DeprecatedAttributeChecker(driver)
identical_link_checker = IdenticalLinkChecker(driver)
meta_refresh_checker = MetaRefreshChecker(driver)


# image_link_checker.check()
# deprecated_attribute_checker.check()
# identical_link_checker.check()
meta_refresh_checker.check()
