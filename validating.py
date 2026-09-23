import parse_cim as parse_cim

errors = []
storage = parse_cim('data/TD Basic Golden InstanceSet.xml')

def validate(storage, valid_keys):
    for x in storage:
        for i in valid_keys:
            if i not in storage[x]:
                errors.append(f"missing {i} key in object {x}")

