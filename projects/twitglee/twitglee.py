
__author__ = 'Hrishikesh S. Bakshi'

import logging
import new
import os
import pickle
import sys
import traceback
import types
import wsgiref.handlers
import re

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.api.urlfetch import fetch
import config
import utils

_DEBUG = True

class FrontpageHandler(webapp.RequestHandler):
     def get(self):
        template_name = os.path.join("twitglee", "index.html")
        self.response.out.write(utils.render_template(template_name))

class SearchHandler(webapp.RequestHandler):
    def get(self):
        template_name = os.path.join("twitglee", "search.html")
        q = self.request.get("q")
        template_vals = { 'q': q,}
        self.response.out.write(utils.render_template(template_name, 
                                                        template_vals))

class TwitSearchHandler(webapp.RequestHandler):
    def get(self):
        template_name = os.path.join("twitglee", "twitsearch.html")
        q = self.request.get("q")
        template_vals = { 'q': q,}
        self.response.out.write(utils.render_template(template_name, 
                                                        template_vals))
class ToppartHandler(webapp.RequestHandler):
    def get(self):
        template_name = os.path.join("twitglee", "top.html")
        template_vals = { 'q': self.request.get("q"),}
        self.response.out.write(utils.render_template(template_name, 
                                                        template_vals))

def main():
  application = webapp.WSGIApplication(
    [
    ('/twitglee/twitsearch$', TwitSearchHandler),
    ('/twitglee/search$', SearchHandler),
    ('/twitglee/top$', ToppartHandler),
    ('/twitglee.*', FrontpageHandler),
    ], debug=_DEBUG)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
