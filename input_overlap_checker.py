class InputOverlapChecker:
    def __init__(self, driver):
        self.driver = driver

    def check(self):
        input_elements = self.driver.find_elements_by_xpath("//input")
        input_elements += self.driver.find_elements_by_xpath("//select")
        for input_element in input_elements:
            print(input_element.location, input_element.size)
