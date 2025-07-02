


def floatConvertible(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
