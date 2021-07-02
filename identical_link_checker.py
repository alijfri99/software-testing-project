class IdenticalLinkChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("\nChecking if rule 5 is violated...")
        links = self.driver.find_elements_by_xpath('//a')
        links_dict = dict()

        for link in links:
            if link.text not in links_dict:
                links_dict[link.text] = []
            links_dict[link.text].append(link.get_attribute('href'))

        for link_text in links_dict.keys():
            for i in range(len(links_dict[link_text])):
                for j in range(i + 1, len(links_dict[link_text])):
                    if links_dict[link_text][i] != links_dict[link_text][j]:
                        print('Links ' + str(links_dict[link_text][i]) + ' (' + link_text + ') and ' +
                              str(links_dict[link_text][j]) +
                              ' (' + link_text + ') have identical texts but point to different pages.')
                        self.count += 1

        if self.count == 0:
            print('There are no identical links in this page that point to different pages (rule 5 is satisfied).')
