import xml.etree.ElementTree as ET

if __name__ == '__main__':

    # get root element
    root = ET.parse("coverage.xml").getroot()

    min_coverage = 0.5

    # iterate news items
    for package in root.findall('./packages/package'):
        for cls in package.findall('./classes/class'):
            if float(cls.attrib['line-rate']) < min_coverage:
                raise Exception("File '%s' has failed the test coverage check (%s%%). "
                                "A minimum coverage of %s%% is required." % (
                                    cls.attrib['filename'],
                                    float(cls.attrib['line-rate'])*100,
                                    min_coverage*100,
                                ))
