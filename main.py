#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import urllib,json
import jinja2
import os

jinja_environment = jinja2.Environment(loader=
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

class SearchHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/search.html')
        self.response.out.write(template.render())

class MainHandler(webapp2.RequestHandler):

     def get(self):
         base_url = "http://api.giphy.com/v1/gifs/search?q="
         api_key_url = "&api_key=dc6zaTOxFJmzC&limit=10"
         search_term=self.request.get('term')
         if search_term:
            url = base_url + search_term + api_key_url
            parsed_data = json.loads(urllib.urlopen(url).read())
            gif_url = parsed_data['data'][0]['images']['original']['url']
            template = jinja_environment.get_template('templates/results.html')
            self.response.out.write(template.render({"search_term" : search_term, "url" : gif_url}))
         else:
            self.response.write(('Please enter a search term'))


app = webapp2.WSGIApplication([
    ('/results', MainHandler),
    ('/search', SearchHandler)
], debug=True)
