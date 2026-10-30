def is_missing(obj, field):
    value = obj.get(field)
    return value is None or (isinstance(value, str) and value.strip() == "")


def validate(storage, valid_keys):
    errors = []
    for x in storage:
        obj = storage[x]
        if obj["tag"] in valid_keys:
            for y in valid_keys[obj["tag"]]:
                if is_missing(obj, y):
                    errors.append({
                        "uuid": x,
                        "tag": obj["tag"],
                        "missing_field": y
                    })

        for field, value in obj.items():
            if field == "tag" or not isinstance(value, str):
                continue
            looks_like_reference = (
                value in storage
                or value.startswith(("urn:uuid:", "#"))
            )
            if looks_like_reference and value not in storage:
                errors.append({
                    "uuid": x,
                    "tag": obj["tag"],
                    "reference_field": field,
                    "missing_reference": value,
                })
    return errors