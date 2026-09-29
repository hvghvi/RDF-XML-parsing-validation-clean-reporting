import parse_cim as parse_cim

errors = []

def validate(storage, valid_keys):
    for x in storage:
        if storage[x]["tag"] in valid_keys:
            for y in valid_keys[storage[x]["tag"]]:
                if y not in storage[x]:
                    errors.append({  #each error has its own dictionary with uuid, tag and missing field. it helps identify easier.
                        "uuid": x,
                        "tag": storage[x]["tag"],
                        "missing_field": y
                    })
    return errors #returns an empty list if no errors
