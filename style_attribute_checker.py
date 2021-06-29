class StyleAttributeChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("Checking if rule 4 is violated...")

        styles = self.driver.find_elements_by_xpath('//*[@style]')

        if len(styles) == 0:
            print("There are no tags that have the 'style' attribute (rule 4 is satisfied).")
        else:
            for style in styles:
                print(f"Found a tag that has the 'style' attribute (violates rule 4): '{style.tag_name}' tag")
                self.count += 1