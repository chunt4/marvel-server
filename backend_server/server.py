import cherrypy
from heroesController import HeroController
from heroes_library import _hero_database

def start_service():

        dispatcher = cherrypy.dispatch.RoutesDispatcher()
        hdb = _hero_database()
        heroController = HeroController(hdb=hdb) 

        dispatcher.connect('hero_get', '/heroes/:hero_id', controller = heroController, action = 'GET_KEY', conditions=dict(method=['GET']))
        dispatcher.connect('hero_put', '/heroes/:hero_id', controller=heroController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
        dispatcher.connect('hero_delete', '/heroes/:hero_id', controller=heroController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
        dispatcher.connect('hero_index_get', '/heroes/', controller=heroController, action = 'GET_INDEX', conditions=dict(method=['GET']))
        dispatcher.connect('hero_index_post', '/heroes/', controller=heroController, action = 'POST_INDEX', conditions=dict(method=['POST']))
        dispatcher.connect('hero_index_delete', '/heroes/', controller=heroController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))
        dispatcher.connect('hero_search', '/heroes/query/:query', controller=heroController, action = 'GET_QUERY', conditions=dict(method=['GET']))
        
        # CORS related options connections
        dispatcher.connect('hero_key_options', '/heroes/:hero_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
        dispatcher.connect('hero_options', '/heroes/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
        dispatcher.connect('hero_search_options', '/heroes/query/:query', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
        dispatcher.connect('hero_post_options', '/heroes/', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
        #dispatcher.connect('reset_key_options', '/reset/:hero_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
        #dispatcher.connect('reset_options', '/reset/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
        #dispatcher.connect('rating_options', '/ratings/:hero_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))

        conf = {
            'global': {
                'server.thread_pool': 5,
                'server.socket_host': 'student04.cse.nd.edu',
                'server.socket_port': 51027, #change port number to your assigned
                },
            '/': {
                'request.dispatch': dispatcher,
                'tools.CORS.on':True,
            }
        }

        cherrypy.config.update(conf)
        app = cherrypy.tree.mount(None, config=conf)
        cherrypy.quickstart(app)


# end of start_service

# class for CORS
class optionsController:
    def OPTIONS(self, *args, **kwargs):
        return ""

# function for CORS
def CORS():
    cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
    cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
    cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"
    
if __name__ == '__main__':
    cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS) # CORS
    start_service()


