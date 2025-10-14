def allcaps(func):
    def wrapper():
        result = func()
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper



