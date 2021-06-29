class MetaRefreshChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("Checking if rule 3 is violated...")

        metas = self.driver.find_elements_by_xpath('//meta')
        for meta in metas:
            if meta.get_attribute("http-equiv") == "refresh":
                print(f"Found a meta that has the 'refresh' value for 'http-equiv' (violates rule 3): {meta}")
                self.count += 1

        if self.count == 0:
            print("There are no metas that has the 'refresh' value for 'http-equiv' (rule 3 is satisfied).")
