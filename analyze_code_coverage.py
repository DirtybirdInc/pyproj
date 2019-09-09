import xml.etree.ElementTree as ET

if __name__ == '__main__':

    # get root element
    root = ET.parse("coverage.xml").getroot()

    failed = False

    # iterate news items
    for package in root.findall('./packages/package'):
        for cls in package.findall('./classes/class'):
            if float(cls.attrib['line-rate']) < 0.5:
                print(False)
                failed = True
                break

        if failed:
            break

    if not failed:
        print(True)


            #raise Exception("File '%s' failed the coverage check. Code coverage must be above 50%%." % cls.attrib['filename'])
