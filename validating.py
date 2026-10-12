import parse_cim as parse_cim


def is_missing(obj, field):
    value = obj.get(field)
    return value is None or (isinstance(value, str) and value.strip() == "")


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