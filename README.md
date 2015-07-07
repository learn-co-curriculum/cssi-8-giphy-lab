##Giphy Lab for Google CSSI Day 8

* Clone this repo
* 
Use inline html to add some styling and the actual gif appear. You’ll need to use the <img> tag.

Example:
# Starter code
```python
base_url = "http://api.giphy.com/v1/gifs/search?q="
api_key_url = "&api_key=dc6zaTOxFJmzC&limit=10"
self.response.out.write(
            '<!doctype html><html><body><p>Hi there!</p></body></html>')
```
Now let’s make our search term a variable
```python
# Declare a variable called search_term and initialize it as "puppy".
class MainHandler(webapp2.RequestHandler):
    def get(self):
        search_term='puppy'
```
Search with the search term, save the data in a variable:
`parsed_data = json.loads(urllib.urlopen(base_url + search_term + api_key_url).read())`

Next, let’s make the search term come from the user or a request

Use the get method to grab the search_term from the url so that localhost:3030/?term='penguin'  would pull up the a new url of a penguin gif.
`search_term=self.request.get('term')`

Add some conditional logic to main.py so that  localhost:3030/ returns “Please enter a search term”
```python
class MainHandler(webapp2.RequestHandler):
    base_url = "http://api.giphy.com/v1/gifs/search?q="
    api_key_url = "&api_key=dc6zaTOxFJmzC&limit=10"
    def get(self):
                search_term=self.request.get('term')
        if search_term:
            url = base_url + search_term + api_key_url
            parsed_data = json.loads(urllib.urlopen(url).read())
            gif_url = parsed_data['data'][0]['images']['original']['url']
            self.response.out.write("<html><body><p>Here's your gif about: "+search_term+"</p><img src=\""+gif_url +"\"</p></body></html>")
        else:
            self.response.write(('Please enter a search term'))
```
Finally, use your resources from the templating lessons to make a search.html and a results.html [Use the code/examples that you wrote yesterday to help you!]

* Create a new file, templates/search.html with a form so that users can post their search term.
* Under the self.get method of your handler, use the template.render() method to render that file.
* Create a new file, templates/results.html that displays the resulting gif.
* Make a new self.post method that uses the form variable from search.html and renders the results.html with the correct gif.


