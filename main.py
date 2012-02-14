import cherrypy

class TwitListSite:
  def index(self):
    return "<h2>TwitList<h2>"
  index.exposed = True
cherrypy.quickstart(TwitListSite())