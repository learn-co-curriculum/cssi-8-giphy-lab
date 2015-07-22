##Giphy Lab for Google CSSI Day 8

First clone this repo so you have our starter code. You should be familiar with the contents of main.py after today's lesson.

If you are having trouble cloning the repo, the boilerplate code for main.py is below.
```python
import webapp2
import json
import random
from google.appengine.api import urlfetch

class MainHandler(webapp2.RequestHandler):
    def get(self):
            giphy_data_source = urlfetch.fetch("http://api.giphy.com/v1/gifs/search?q=+ryan+goslin&api_key=dc6zaTOxFJmzC&limit=10")
            giphy_json_content = giphy_data_source.content
            parsed_giphy_dictionary = json.loads(giphy_json_content)
            gif_url= parsed_giphy_dictionary['data'][0]['images']['original']['url']
            self.response.write(gif_url)


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

```

Your goal during your lab time is to

1. Actually show the gif using HTML
2. Make the search term dynamic
3. Add a search page so users can enter a search term

####Clean up the URL
Let's break apart our long url intro three parts. 
* The base url
* The api key 
* The search term. 

For now we'll hard code the search term as puppy, because puppies make the world smile. 
```python
# Declare a variable called search_term and initialize it as "puppy".
class MainHandler(webapp2.RequestHandler):
    def get(self):
        base_url = "http://api.giphy.com/v1/gifs/search?q="
        api_key_url = "&api_key=dc6zaTOxFJmzC&limit=10"
        search_term='puppy'
```
Now we can open our url by concatenating our variables together:
`giphy_data_source = urlfetch.fetch(base_url + search_term + api_key_url).content))`
            
Refresh your webapp page so that you know this first step is working. Remember, we always want to build and test one step at a time.

#### Show the actual GIF
Let's make this puppy show up. Use inline html and the `<img>` tag to add some styling and the actual gif appear. You will have to use string concatination to use your the `gif_url` variable 
> Example: `self.response.out.write('<!doctype html><html><body><p>Hi there!</p></body></html>')`


#### Get the search term from the user

The next part of your lab is to make the search term dynamic. 

* Use the get method to grab the search_term from the url.
* Check if your app works, by navigating to `localhost:3030/?term='penguin'` Do you see a cute penguin?




#### Deal with a url without a search term
Add some conditional logic to main.py so that  `localhost:3030/` returns “Please enter a search term”

#### Add a search page 

Finally, use your resources from the templating lessons to make a search.html and a results.html [Use the code/examples that you wrote yesterday to help you!]

* Create a new file, templates/search.html with a form so that users can enter their search term.
  
    ```
    <form method="get" action=results>
		<p>Question <input type="text" name="answer"/></p>
		<p><input type="submit"></p>
	</form>
   ```
   
#### Render your search page as a template   
Look at the templating lesson from yesterday to help you render a new html file - search.html. Some hints are below, but use your QuizApp from yesterday or the lecture notes to help you figure it out. 
* Make a new handler, SearchHandler
* Under the self.get method Search Handler, use the template.render() method to render that file.
* You'll have to use jinja and import jinja2 and os 
* Don't forget to change your libraries in app.yaml
* Add to your routes so that `/search` goes to SearchHandler
* Go to `http://localhost:8080/search` to make sure your new search page come up. 

#### Create a results page
* Create a new file, templates/results.html that displays the resulting gif.
* Render results.html in the MainHandler, or you can rename MainHandler to ResultsHandler [and change the routes]
* You will need to pass the template two variables: search_term and gif_url



#### STRETCH 
#####Option 1: Use POST instead of GET for your form input
* Make a new self.post method that uses the form variable from search.html and renders the results.html with the correct gif.

#####Option 2: Get a random GIF
Look at the [Giphy API Documentation](https://github.com/giphy/GiphyAPI) to find a way to get a JSON URL with a random gif

or

Import the [random library](https://docs.python.org/2/library/random.html) to make a random index. Instead of indexing the parsed_data at [0], index at [rand\_num]. Set the variable rand_num to be a random integer  from 1-10. 


