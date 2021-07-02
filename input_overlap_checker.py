class InputOverlapChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        elements = self.find_elements()
        for i in range(len(elements)):
            for j in range(i + 1, len(elements)):
                if elements[i].location['y'] >= elements[j].location['y']:
                    if elements[i].location['y'] <= elements[j].location['y'] + elements[j].size['height']:
                        if elements[i].location['x'] >= elements[j].location['x']:
                            if elements[i].location['x'] <= elements[j].location['x'] + elements[j].size['width']:
                                print('There is an overlap between input elements at location ' +
                                      str(elements[i].location) + ' and location ' + str(elements[j].location))
                                self.count += 1

                        elif elements[i].location['x'] + elements[i].size['width'] >= elements[j].location['x']:
                            if elements[i].location['x'] + elements[i].size['width'] <= \
                                    elements[j].location['x'] + elements[j].size['width']:
                                print('There is an overlap between input elements at location ' +
                                      str(elements[i].location) + ' and location ' + str(elements[j].location))
                                self.count += 1

                elif elements[i].location['y'] + elements[i].size['height'] >= elements[j].location['y']:
                    if elements[i].location['y'] + elements[i].size['height'] <= \
                            elements[j].location['y'] + elements[j].size['height']:
                        if elements[i].location['x'] >= elements[j].location['x']:
                            if elements[i].location['x'] <= elements[j].location['x'] + elements[j].size['width']:
                                print('There is an overlap between input elements at location ' +
                                      str(elements[i].location) + ' and location ' + str(elements[j].location))
                                self.count += 1

                        elif elements[i].location['x'] + elements[i].size['width'] >= elements[j].location['x']:
                            if elements[i].location['x'] + elements[i].size['width'] <= \
                                    elements[j].location['x'] + elements[j].size['width']:
                                print('There is an overlap between input elements at location ' +
                                      str(elements[i].location) + ' and location ' + str(elements[j].location))
                                self.count += 1

        if self.count == 0:
            print("There is no overlap between the input elements on this page.")

    def find_elements(self):
        tags_list = ['input', 'select', 'textarea', 'button']
        elements = []
        for tag in tags_list:
            elements += self.driver.find_elements_by_xpath('//' + tag)

        return elements
