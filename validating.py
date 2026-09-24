import parse_cim as parse_cim

errors = []

def validate(storage, valid_keys):
    for x in storage:
        if storage[x]["tag"] in valid_keys:
            for y in valid_keys[storage[x]["tag"]]:
                if y not in storage[x]:
                    errors.append({})


    if not errors:
        return ("All required keys are present in the storage dictionary.")

    return errors
