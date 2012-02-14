import cherrypy

class TwitListSite:
  _cp_config = {'tools.staticdir.on': True,
                'tools.staticdir.root': "/Users/marcrendlignacio/pystuff/twitlist",
                'tools.staticdir.dir': 'public'}
  # tried this, didn't work: @cherrypy.tools.staticdir(root="/Users/marcrendlignacio/pystuff/twitlist", dir='public')
  @cherrypy.expose
  def index(self):
    return '''
      <h2>TwitList<h2>
      <a href="/oauth/twitter/login" id="sign-in-button">
        <img src="/images/sign-in-with-twitter.png" alt="Sign in with Twitter" />
      </a>
    '''

cherrypy.quickstart(TwitListSite())