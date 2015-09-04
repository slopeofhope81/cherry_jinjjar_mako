#Mental notes for using different template engine: MAKO and JinJJA with Cherrypy

from mako.lookup import TemplateLookup
import cherrypy

TEMPLATE_BASE = #path to where the template directory is located
template_cache = #path to where the cache directory is located
template_lookup = TemplateLookup(directories = [TEMPLATE_BASE], 
				module_directory = template_cache, 
				collection_size = 500, 
				imports = [], 
				defaults_filters = ['toUnicode'], 
				input_encoding='utf-8', 
				output_encoding='utf-8')

class RootObj():
	def __init__(self):
		self.tools = Tools()
		self.tools.exposed = True

class Tools():
	def __init__(self):
		self.hipchat = hipchat
    
    def render(self, fname, **kwargs):
        args = {}
        args.update(kwargs)
        cherrypy.response.headers['Content-Type']= 'text/html'
        template = template_lookup.get_template(fname)
        content = template.render(**args)
        return [content]

    @cherrypy.expose
    def index(self, **kwargs):
        model = {}
        names = fetch_ctids() #some db reads
        if names is not None:
            model = {'ctid': names }
        return self.render("index.html", **model)	

basic_auth = {'tools.auth_basic.on': True, 
  			  'tools.auth_basic.realm': "", 
  			  'tools.auth_basic.checkpassword': ""}
  			  'tools.auth_basic.debug': True"}
no_auth = {'tools.auth_basic.on': False}

session_required = {'tools.sessions.on': True, 
 					'tools.sessions.storage_type': 'file', 
 					'tools.session.storage_path': ''#path to the session folder
 					} 			  

cherry.application(RootObj(), 
					config= {'/': basic_auth, 
					         '/tools/hipchat': no_auth, 
					         '/tools/session': session_required, })
