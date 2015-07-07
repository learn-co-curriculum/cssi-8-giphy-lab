##Giphy Lab for Google CSSI Day 8

First clone this repo so you have our starter code, which your MI has gone over.

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
`parsed_data = json.loads(urllib.urlopen(base_url + search_term + api_key_url).read())`
#### Show the actual GIF
Use inline html to add some styling and the actual gif appear. You’ll need to use the `<img>` tag.

#### Get the search term from the user

The next part of your lab is to make the search term dynamic. 

* Use the get method to grab the search_term from the url.
* `localhost:3030/?term='penguin'`  should pull up the a new url of a penguin gif.

#### Deal with a url without a search term
Add some conditional logic to main.py so that  `localhost:3030/` returns “Please enter a search term”

#### Add a search page and a results page

Finally, use your resources from the templating lessons to make a search.html and a results.html [Use the code/examples that you wrote yesterday to help you!]

* Create a new file, templates/search.html with a form so that users can enter their search term.
  
    ```
    <form method="get" action=results>
		<p>Question <input type="text" name="answer"/></p>
		<p><input type="submit"></p>
	</form>
   ```
   
* Under the self.get method of your handler, use the template.render() method to render that file.
* Create a new file, templates/results.html that displays the resulting gif.


#### STRETCH - Use POST instead of GET for your form input
* Make a new self.post method that uses the form variable from search.html and renders the results.html with the correct gif.


