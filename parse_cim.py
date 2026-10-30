import xml.etree.ElementTree as ET

RDF_NS = '{http://www.w3.org/1999/02/22-rdf-syntax-ns#}'

def _local_name(tag):
    return tag.split('}')[-1] if '}' in tag else tag


def parse_cim(filepath):
    storage = {}
    object_stack = []

    for event, element in ET.iterparse(filepath, events=('start', 'end')):
        about = element.get(RDF_NS + 'about')

        if event == 'start':
            if about is not None:
                storage.setdefault(about, {})
                storage[about]['tag'] = _local_name(element.tag)
                object_stack.append(about)
                continue

            if object_stack: #fail safe making sure that there IS a parent object and an empty stack says there isnt one or its the root
                tag_name = _local_name(element.tag) #the child
                resource = element.get(RDF_NS + 'resource') #get what its pointing to
                text = element.text.strip() if element.text is not None and element.text.strip() else None

                if resource is not None:
                    storage[object_stack[-1]][tag_name] = resource
                elif text is not None:
                    storage[object_stack[-1]][tag_name] = text

        elif about is not None and object_stack and object_stack[-1] == about:
            object_stack.pop()

    return storage

    """
    Reason for strip:
    This is a known quirk of XML in general — pretty-printed/indented XML files (with line breaks for readability)
    that's really just whitespace left over from how the file was formatted, not meaningful data.
    """
    