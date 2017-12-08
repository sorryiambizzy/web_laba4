from webob import Request, Response
from jinja2 import Environment, FileSystemLoader

assets = [
  'app.js',
  'react.js',
  'leaflet.js',
  'D3.js',
  'moment.js',
  'math.js',
  'main.css',
  'bootstrap.css',
  'normalize.css',
]

css = []
js = []

for element in assets:
    element_split = element.split('.')
    if element_split[1] == 'js':
        js.append(element)
    elif element_split[1] == 'css':
        css.append(element)

class WsgiTopBottomMiddleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
      response = self.app(environ, start_response).decode()

      if response.find('<head>' and '<body>') > -1:
        html, head = response.split('<head>')
        datahead, body = head.split('</head>')
        head1, bodytag = body.split('<body>')
        databody, end = bodytag.split('</body>')
        
        yield (html + data + end).encode() 
      else:
        yield (response).encode()

def app(environ, start_response):
  response_code = '200 OK'
  response_type = ('Content-Type', 'text/HTML')
  start_response(response_code, [response_type])
  return ''''''

app = WsgiTopBottomMiddleware(app)

request = Request.blank('/index.html')

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('index.html')
print(template.render(javascripts=js, styles=css))

print(request.get_response(app))
