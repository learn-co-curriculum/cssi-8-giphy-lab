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

class MainHandler(webapp2.RequestHandler):
    def get(self):
            ##(2)use self.request.get() to make the search_term come from the url
            ##(3) use string concatenation to change +ryan+goslin to the search_term
            #search_term=

            parsed_data = json.loads(urllib.urlopen(
            "http://api.giphy.com/v1/gifs/search?q=+ryan+goslin&api_key=dc6zaTOxFJmzC&limit=10").read())
            gif_url = parsed_data['data'][0]['images']['original']['url']

            ##(1)Use inline html and the <img> tag to make the actual gif appear
            self.response.write(gif_url)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
