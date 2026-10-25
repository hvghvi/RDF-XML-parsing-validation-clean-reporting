import parse_cim as parse_cim

def validate(storage, valid_keys):
    errors = []
    for x in storage:
        if storage[x]["tag"] in valid_keys:
            for y in valid_keys[storage[x]["tag"]]:
                if is_missing(storage[x], y): 
                    errors.append({
                        "uuid": x,
                        "tag": storage[x]["tag"],
                        "missing_field": y
                    })
    return errors