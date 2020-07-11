import cherrypy
from heroesController import HeroController
from marvel_library import _hero_database


def start_service():

        dispatcher = cherrypy.dispatch.RoutesDispatcher()
        hdb = _hero_database()
        heroController = HeroController(mdb=mdb) 

        dispatcher.connect('hero_get', '/marvel/:hero_id', controller = heroController, action = 'GET_KEY', conditions=dict(method=['GET']))
        dispatcher.connect('hero_put', '/marvel/:hero_id', controller=heroController, action = 'PUT_KEY', conditions=dict(method=['PUT']))
        dispatcher.connect('hero_delete', '/marvel/:hero_id', controller=heroController, action = 'DELETE_KEY', conditions=dict(method=['DELETE']))
        dispatcher.connect('hero_index_get', '/marvel/', controller=heroController, action = 'GET_INDEX', conditions=dict(method=['GET']))
        dispatcher.connect('hero_index_post', '/marvel/', controller=heroController, action = 'POST_INDEX', conditions=dict(method=['POST']))
        dispatcher.connect('hero_index_delete', '/marvel/', controller=heroController, action = 'DELETE_INDEX', conditions=dict(method=['DELETE']))

        # CORS related options connections
        dispatcher.connect('hero_key_options', '/marvel/:hero_id', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
        dispatcher.connect('hero_options', '/marvel/', controller=optionsController, action = 'OPTIONS', conditions=dict(method=['OPTIONS']))
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


