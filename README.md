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
    to the current heroes in the database. There are also three functions declared in the library. 
    The first of which is search_compare(s1, s2, {"match":"false"}) which utilizes a second     function string_compare(s1, s2). The purpose of search compare is to determine if two strings match and rate the match if they do. It does this by iterating through each of the letters of s1 and comparing them to the first letter in s2. If they match, then string compare is called to evaluate how many characters in a row match and return a dictionary with match true and the rate. Search compare then returns that same dictionary. If they don't match, then search_compare calls search_compare(s1[1:], s2, match_dict) which iterates through the string to catch every possibility and does the same upon s2[1:]. Finally, sort_key(match_dict) just returns the rate of the inserted dictionary in order to sort the list of match results.
    
    Instructions: The library can be tested by executing test_api.py using the command "python3 test_api.py". 
    
OO Server:
    The server utilizes cherrypy and a specific controller called HeroController 
    from heroesController.py to connect the url of the request to the execution
    code. The controller has the functions GET_KEY, PUT_KEY, DELETE_KEY, GET_INDEX, GET_QUERY,
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
    GET_QUERY is connected to /heroes/query/:query and iterates through every hero in the database
    and uses search_compare to determine whether the specific character matches the search query.
    If it does, all of the character's information including it's rate is appended to a list.
    The list is finally sorted and output is returned with a key pairs 'results':'success' and
    'hero_list':'[{...}, ...]'. POST_INDEX decodes the request body and
    and parses the body for a hero's attributes. It then creates a list containing those 
    attributes and uses set_hero(max_id + 1, hero_list) to add the hero and returns
    an output dictionary with 'success' under the 'result' key.Finally, DELETE_INDEX
    iterates over every hero in the database and calls delete_hero(hid) which deletes
    all the heros and returns success under the key result upon success. Our webservice
    uses port 51022 and should be used as described by the functions and the connected
    urls from the heroesController object HeroController.
    
    Instructions: The webservice can be tested using the command "python3 test_ws.py".
    Be sure that a server is running on student04.cse.nd.edu:51027 and to ensure all the test
    work, start the server just before running the test.

Steps to run all tests:
    Navigate to web-server/backend_server/ and execute "python3 test_api.py"
    Navigate to web-server/backend_server/ and execute "python3 server.py" and then in another
    terminal, navigate to the same place and execute "python3 test_ws.py"
    Keep the server running or restart it. In the other terminal, navigate to student04.cse.nd.edu/chunt4/rest_client/index.html. Select "good characters" as the filter and press apply filter. Then enter "iron man" into the search text field and press the search button. The screen will display a series of characters below the filter menu. The first of which will be name: iron man. Next select the Create Hero tab, and enter the new heros information in the given text fields/select buttons. Click create hero. Then navigate to the search hero page and enter the new character's name in the text field, select no filter, click apply filter, and finally press search. The newly created character will appear. Finally navigate to the character randmoizer page. Select the random button and a random character will be displayed on the screen. These tests exemplify all of the functionality of the frontend.