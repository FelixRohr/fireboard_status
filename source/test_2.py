import xml.etree.ElementTree as et

def create_xml_body():
    operation = et.Element("fireboardOperation")
    operation.text = 'version="1.0.3"'
    return et.tostring(operation)

print(create_xml_body())