import webapp2
import cgi

class MainPage(webapp2.RequestHandler):
    def get(self):
	username = cgi.escape(self.request.get("my_name"))
	if username:
	    title = 'Welcome'
	    heading = 'Hello there, {}!'.format(username)
	else:
	    title = 'Enter your name...'
	    heading = ''
	response_text = """
          <html>
            <head><title>{}</title>
		  <link type="text/css" rel="stylesheet" href="/stylesheets/main.css" />
	    </head>
            <body>
	      <h1>{}</h1>
              <form action="/" method="get">
                <input type="text" name="my_name"><br>
                <input type="submit" value="Sign In">
              </form>
            </body>
          </html>""".format(title, heading)

        self.response.headers["Content-Type"] = "text/html"
        self.response.write(response_text)


routes = [('/', MainPage)]
my_app = webapp2.WSGIApplication(routes, debug=True)
