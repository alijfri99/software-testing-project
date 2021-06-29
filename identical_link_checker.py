class IdenticalLinkChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("\nChecking if rule 5 is violated...")

        links = self.driver.find_elements_by_xpath('//a')

        for i in range(len(links)):
            if links[i].get_attribute('href') == None or links[i].text == "":
                continue

            for j in range(i + 1, len(links)):
                if i == j or links[j].get_attribute('href') == None or links[j].text == "":
                    continue

                if links[i].text == links[j].text:
                    if links[i].get_attribute('href') != links[j].get_attribute('href'):
                        print("Links " + str(links[i].get_attribute('href')) + " (" + links[i].text + ") and " +
                              str(links[j].get_attribute('href')) + " (" + links[j].text +
                              ") have identical texts but point to different pages.")
                        self.count += 1

        if self.count == 0:
            print("There are no identical links in this page that point to different pages (rule 5 is satisfied).")
