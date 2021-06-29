class StyleAttributeChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("\nChecking if rule 4 is violated...")

        styles = self.driver.find_elements_by_xpath('//*[@style]')

        if len(styles) == 0:
            print("There are no tags that have the 'style' attribute (rule 4 is satisfied).")
        else:
            self.count = len(styles)
            print(f"Found {str(len(styles))} tags that have the 'style' attribute (violates rule 4)")