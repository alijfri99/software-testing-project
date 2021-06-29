class ImageLinkChecker:
    def __init__(self, driver):
        self.driver = driver
        self.count = 0

    def check(self):
        print("Checking if rule 1 is violated...")

        image_formats = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif', '.pjpeg', '.pjp', '.png', '.svg', '.webp',
                         '.bmp', '.ico', '.cur', '.tif', '.tiff']

        links = self.driver.find_elements_by_xpath('//a')
        for link in links:
            for image_format in image_formats:
                if str(link.get_attribute('href'))[-len(image_format):] == image_format:
                    print("Found a link that points directly to an image (violates rule 1):",
                          link.get_attribute('href'))
                    self.count = self.count + 1
                    break

        if self.count == 0:
            print("There are no links in this web page that point directly to an image (rule 1 is satisfied).")

