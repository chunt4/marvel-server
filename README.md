# Web Server

OO Library API:
    The primary class of our OO API is _hero_database. This object opens the data file, 
    parses the information, and stores each hero's attributes in seperate attribute specific
    dictionarys with the id of each hero as the key. The _hero_database object has
    four functions. get_heroes returns the keys to the hero_names dictionary effectively 
    returning a list of the hero names, get_hero(hid) returns a list containing the hero
    name, alignment, living status, sex, and identity status by checking the respective
    attribute dictionaries with the hid as the key. set_hero(hid, hero) recieves an
    array "hero" and assigns the attributes listed in the array to each attributes specific
    dictionary under the hid key. Finally, delete_hero(hid) just calls del on all of the 
    attribute dictionaries at the specific hid. 