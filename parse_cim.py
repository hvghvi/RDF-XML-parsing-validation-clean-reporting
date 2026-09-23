import xml.etree.ElementTree as ET


def parse_cim(filepath):
    # Parse the XML file
    tree = ET.parse(filepath)

    # Get the root element
    root = tree.getroot()
    current_object = None
    current_uuid = None
    storage={}

    for element in root.iter():
        uuid = element.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}about')

        if uuid:
            current_object = element
            current_uuid = uuid
            print()
            print(element.tag, uuid)
            if uuid not in storage:
                storage[uuid] = {}
                storage[current_uuid]["tag"] = element.tag.split('}')[-1]  # Store the tag name without the namespace
        else:
            if current_uuid == None:
                pass #skips root as it doesnt contain anything important
            else:
                print(element.tag, element.text.strip() if element.text else element.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')) 

                if element.text != None:
                    storage[current_uuid][element.tag] = element.text.strip()
                else:
                    storage[current_uuid][element.tag] = element.get('{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource')

    return storage

    """
    Reason for strip:
    This is a known quirk of XML in general — pretty-printed/indented XML files (with line breaks for readability) 
    that's really just whitespace left over from how the file was formatted, not meaningful data.
    """
