import xml.etree.ElementTree as et # You can use lowercase 'et' or uppercase 'ET'
# In this context, et is just a short nickname (called an alias) 
# given to the xml.etree.ElementTree module when importing it


# From a file
tree = et.parse('data.xml') # opens and parses your XML file, returns a tree object
root = tree.getroot()  #gets the top level node and then you walk

# From a string
xml_data = "<data><item id='1'>Hello</item></data>"
root = et.fromstring(xml_data)

# Loop through every element in the tree, print its tag and text
for element in root.iter():
    print(element.tag, element.text)

#for something like rdf:about="urn:uuid:bfaee055..."
element.get('{full_url_for_data#}about')
#returns the UUID string, "urn:uuid:bfaee055-4440-4173-9b95-615b6fafd523".

#for something like <cim:IdentifiedObject.name>Fdr 3A</cim:IdentifiedObject.name>, 
# Fdr 3A isn't an attribute
#it's the actual text content
element.text
#returns "Fdr 3A".\

#So the distinction is: 
# attribute = sits inside the tag's own brackets (tag attribute="value"),
#  text = sits between the opening and closing tag (<tag>text</tag>