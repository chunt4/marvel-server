import cherrypy
from moviesController import MovieController
from marvel_library import _hero_database


def start_service():
        dispatcher = cherrypy.dispatch.RoutesDispatcher()


            hdb = _hero_database()

                heroController = HeroController(mdb=mdb) 

