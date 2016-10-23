class Alien:
    """ Class that defines an alien"""
    def __init__(self, color, weight):
        """ Constructor. Set name and color"""
        self.color = color
        self.weight = weight
        
def has_property(my_alien):
    """ Check to see if an item has a property.
    In this case, is the alien green? """
    if my_alien.color.upper() == "GREEN":
        return True
    else:
        return False        
    
def check_if_one_item_has_property_v1(my_list):
    """ Return true if at least one item has a
    property. """
    i = 0
    while i < len(my_list) and not has_property(my_list[i]):
        i += 1

    if i < len(my_list):
        # Found an item with the property
        return True
    else:
        # There is no item with the property
        return False    
    
def check_if_one_item_has_property_v2(my_list):
    """ Return true if at least one item has a
    property. Works the same as v1, but less code. """
    for item in my_list:
        if has_property(item):
            return True
    return False    

def check_if_all_items_have_property(my_list):
    """ Return true if at ALL items have a property. """
    for item in my_list:
        if not has_property(item):
            return False
    return True

def get_matching_items(list):
    """ Build a brand new list that holds all the items
    that match our property. """
    matching_list = []
    for item in list:
        if has_property(item):
            matching_list.append(item)
    return matching_list

def main():
    """ Test everything out. """
    alien_list = []
    alien_list.append(Alien("Green", 42))
    alien_list.append(Alien("Red", 40))
    alien_list.append(Alien("Blue", 41))
    alien_list.append(Alien("Purple", 40))
    
    result = check_if_one_item_has_property_v1(alien_list)
    print("Result of test check_if_one_item_has_property_v1:", result)
    
    result = check_if_one_item_has_property_v2(alien_list)
    print("Result of test check_if_one_item_has_property_v2:", result)
    
    result = check_if_all_items_have_property(alien_list)
    print("Result of test check_if_all_items_have_property:", result)
    
    result = get_matching_items(alien_list)
    print("Number of items returned from test get_matching_items:", len(result))
    
if __name__ == "__main__":
    main()
