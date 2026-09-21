import iterating_xml as iterating

for x in storage:
    for i in valid_keys:
        if i not in storage[x]:
            raise KeyError(f"missing {i} key in object {x}")

