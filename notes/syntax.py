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



## step by step breakdown for argparse

# 1, initialise the parser = parser = argparse.ArgumentParser(description="")
    import argparse
    parser = argparse.ArgumentParser(description="A tool to compress images.")

# 2, define rules (.add_argument) (You register the flags you want to accept. This is where you set types, defaults, and requirements.)
    # A required positional argument
    parser.add_argument("filename") 

    # An optional argument that converts the input to an integer
    parser.add_argument("-c", "--count", type=int, default=1) 

# 3, Parse the Command Line (.parse_args()) When you call parse_args(), Python inspects sys.argv (the raw list of strings sent by PowerShell or Bash), bundles them into an object.
    args = parser.parse_args()

# 4, Extract and Use (The bundled object (args) holds your inputs as clean Python properties.)\
    print(args.filename)  # e.g., "photo.jpg"
    print(args.count)     # e.g., 5 (already converted to a native integer)
