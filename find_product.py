def find_product(name):
    for p in catalog.products:
        if p.name == name:
            return p
    return None