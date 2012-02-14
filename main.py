import cherrypy
from mako.template import Template

class TwitListSite:
  _cp_config = {'tools.staticdir.on': True,
                'tools.staticdir.root': "/Users/marcrendlignacio/pystuff/twitlist",
                'tools.staticdir.dir': 'public'}
  # tried this, didn't work: @cherrypy.tools.staticdir(root="/Users/marcrendlignacio/pystuff/twitlist", dir='public')
  @cherrypy.expose
  def index(self):
    template = Template(filename='./templates/index.html')
    return template.render()

cherrypy.quickstart(TwitListSite())