class DeprecatedAttributeChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("Checking if rule 2 is violated...")

        attribute_checks = [self.check_accept, self.check_align, self.check_alink]

        for attribute_check in attribute_checks:
            attribute_check()

        if self.count == 0:
            print("There are no deprecated HTML5 attributes in this page (rule 2 is satisfied).")

    def check_accept(self):
        accepts = self.driver.find_elements_by_xpath('//form[@accept]')

        if len(accepts) != 0:
            self.count += 1
            print("Found " + str(len(accepts)) + " forms that contain an accept attribute (violates rule 2).")

    def check_align(self):
        tags = ["caption", "col", "div", "embed", "h1", "h2", "h3", "h4", "h5", "h6", "hr", "iframe", "img", "input",
                "legend", "object", "p", "table", "tbody", "thead", "tfoot", "td", "th", "tr"]

        for tag in tags:
            aligns = self.driver.find_elements_by_xpath('//' + tag + '[@align]')
            if len(aligns) != 0:
                self.count += 1
                print('Found ' + str(len(aligns)) + ' ' + tag +
                      ' tags that contain an align attribute (violates rule 2).')

    def check_alink(self):
        alinks = self.driver.find_elements_by_xpath('//body[@alink]')

        if len(alinks) != 0:
            self.count += 1
            print("Found " + str(len(alinks)) + " body tags that contain an alink attribute (violates rule 2).")
