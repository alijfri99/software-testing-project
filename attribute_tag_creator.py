import pickle


class AttributeTagCreator:
    def __init__(self, driver):
        self.driver = driver

    def create(self):
        self.driver.get('https://rules.sonarsource.com/html/type/Code%20Smell/RSPEC-1827')
        attribute_tags = dict()
        for i in range(2, 71):
            tags_query = '//*[@id="root"]/div/div[2]/nav/main/div/section[2]/table/tbody/tr[' + str(i) + ']/td[2]/code'
            tags = self.driver.find_elements_by_xpath(tags_query)

            attribute_query = '//*[@id="root"]/div/div[2]/nav/main/div/section[2]/table/tbody/tr[' + str(i) \
                              + ']/td[1]/code'
            attribute = self.driver.find_element_by_xpath(attribute_query).text

            attribute_tags[attribute] = list()
            for tag in tags:
                attribute_tags[attribute].append(tag.text)

        print(attribute_tags)
        attribute_tags_output = open('attribute_tags.bin', 'wb')
        pickle.dump(attribute_tags, attribute_tags_output)
        attribute_tags_output.close()

    def process_attribute_tags(self):
        attribute_tags_file = open('attribute_tags.bin', 'rb')
        attribute_tags = pickle.load(attribute_tags_file)
        attribute_tags_file.close()

        attribute_tags['align'].remove('h1-h6')
        attribute_tags['align'] += ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        attribute_tags['border'].remove('border="0"')
        attribute_tags['language'] = attribute_tags['langauge']
        del attribute_tags['langauge']
        attribute_tags['language'].remove('language="javascript"')
        attribute_tags['name'].remove('name="[a\'s element id]"')

        print(attribute_tags)
        attribute_tags_output = open('attribute_tags.bin', 'wb')
        pickle.dump(attribute_tags, attribute_tags_output)
        attribute_tags_output.close()


