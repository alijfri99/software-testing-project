from attribute_tag_creator import AttributeTagCreator


class DeprecatedAttributeChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("\nChecking if rule 2 is violated...")
        attribute_tags = AttributeTagCreator.create()

        for attribute_tag in attribute_tags:
            self.check_attribute(attribute_tag[0], attribute_tag[1])

        if self.count == 0:
            print("There are no deprecated HTML5 attributes in this page (rule 2 is satisfied).")

    def check_attribute(self, tags, attribute):
        if attribute[0] in ['a', 'e', 'i', 'o', 'u']:
            article = 'an'
        else:
            article = 'a'

        for tag in tags:
            elements = self.driver.find_elements_by_xpath('//' + tag + '[@' + attribute + ']')
            if len(elements) != 0:
                if len(elements) == 1:
                    contain = "contains"
                    tag_word = "tag"
                else:
                    contain = "contain"
                    tag_word = "tags"
                print("Found " + str(len(elements)) + " " + tag + " " + tag_word + " that " + contain + " " + article
                      + " " + attribute + " attribute (violates rule 2).")
                self.count += 1

