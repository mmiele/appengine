from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app


class MainPage(webapp.RequestHandler):
    
  def get(self):
        
        self.response.out.write("<html><body>")
        self.response.out.write("<h2>Greetings</h2>")
        self.response.out.write("<p><b>Hello, World!<//b></p>")
        self.response.out.write("<p style='color:red'>Enjoy your day.</p>")
        self.response.out.write("</body></html>")
        expires_date = datetime.datetime.utcnow() + datetime.timedelta(365)
        expires_str = expires_date.strftime("%d %b %Y %H:%M:%S GMT")
        self.response.headers.add_header("Expires", expires_str)

application = webapp.WSGIApplication([('/', MainPage)], debug=True)


def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
