# Web Server

OO Library API:
    The primary class of our OO API is _hero_database. This object opens the data file, 
    parses the information, and stores each hero's attributes in seperate attribute specific
    dictionarys with the id of each hero as the key. The _hero_database object has
    four functions. get_heroes returns the keys to the hero_names dictionary effectively 
    returning a list of the hero names, get_hero(hid) returns a list containing the hero's
    name, alignment, living status, sex, and identity status by checking the respective
    attribute dictionaries with the hid as the key. set_hero(hid, hero) recieves an
    array "hero" and assigns the attributes listed in the array to each attributes specific
    dictionary under the hid key. Finally, delete_hero(hid) just calls del on all of the 
    attribute dictionaries at the specific hid. This database is created to be able to 
    enter the id of a hero and for it to return the hero's name, alignment, 
    living status, sex, and identity status as well as make adjustments/additions
    to the current heroes in the database.
    
    Instructions: The library can be tested by executing test_api.py using the command "python3 test_api.py". 
    
OO Server:
    The server utilizes cherrypy and a specific controller called HeroController 
    from heroesController.py to connect the url of the request to the execution
    code. The controller has the functions GET_KEY, PUT_KEY, DELETE_KEY, GET_INDEX,
    POST_INDEX, and DELETE_INDEX. GET_KEY is connected to /heroes/:hero_id and 
    returns the attributes of the hero as key and value pairs in a dictionary
    corresponding to the hero's id that matches the hero_id provided using 
    the get_hero(hero_id) function. PUT_KEY is connected to /heroes/:hero_id and 
    creates a list of the of hero info taken from the request body which is then passed
    into set_hero(hero_id, list_of_hero_attributes) and returns an output dictionary
    with 'success' under the 'result' key. DELETE_KEY is connected to /heroes/:hero_id
    and calls delete_hero(hero_id) to delete that Hero from the database returning an output dictionary
    with 'success' under the 'result' key. GET_INDEX is connected to /heroes/ and 
    returns a list under the 'heroes' key which contains a
    dictionary of each hero's information and 'success' under the 'result' key. 
    POST_INDEX decodes the request body and
    and parses the body for a hero's attributes. It then creates a list containing those 
    attributes and uses set_hero(max_id + 1, hero_list) to add the hero and returns
    an output dictionary with 'success' under the 'result' key.Finally, DELETE_INDEX
    iterates over every hero in the database and calls delete_hero(hid) which deletes
    all the heros and returns success under the key result upon success. Our webservice
    uses port 51027 and should be used as described by the functions and the connected
    urls from the heroesController object HeroController.