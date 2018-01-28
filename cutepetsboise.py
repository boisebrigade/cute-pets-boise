#External imports
import twitter

#Internal imports
import random
from urllib import urlopen
import json
from apikeys import pet_finder_key, twitter_consumer_key, twitter_consumer_secret, twitter_access_token_key, twitter_access_token_secret 
from greetings import greeting_strings
from shelters import shelter_ids

# Get the breed tag of the pet info recieved from petfinder api
def getBreed(petData):
   if (petData["breeds"]["breed"] is not None):
    if (isinstance(petData["breeds"]["breed"], list)):
        return  "Mixed Breed"
    else:
      return petData["breeds"]["breed"]["$t"]

# Get the large image associated with the pet info received from petfinder api
def getImage(petData):
    if (petData["media"] is None):
        print("No image.")
    else:
        return petData["media"]["photos"]["photo"][2]["$t"]

# Initialize twitter API with keys supplied from apikeys.py
twitterApi = twitter.Api(consumer_key=twitter_consumer_key,
		  consumer_secret=twitter_consumer_secret,
		  access_token_key=twitter_access_token_key,
		  access_token_secret=twitter_access_token_secret)

# Grab a random shelter Id from the list of shelter Ids
shelterId = shelter_ids[random.randint(0, len(shelter_ids) - 1)]

# Make the call to petfinder using the shelter ID and pet_finder_key from apikeys.py and read response
url = urlopen('http://api.petfinder.com/pet.getRandom?shelterid=' + shelterId + '&output=basic&format=json&key=' + pet_finder_key).read()
data= json.loads(url)

if (data["petfinder"] is None):
    print("No data found.")
else:
    petData = data["petfinder"]["pet"]

# Get the ID of the pet for future use and builds the link
id = petData["id"]["$t"]
link = 'http://www.petfinder.com/petdetail/' + id

# Get the information we need to construct the proper post
name = petData["name"]["$t"]
breed = getBreed(petData)
image = getImage(petData)
greeting = greeting_strings[random.randint(0, len(greeting_strings) - 1)]

# Construct the post
postString = greeting + name  + '. I am a ' + breed + '. Adopt me here! ' + link + '.'

# Send it off
if (image is None):
    twitterApi.PostUpdate(postString)
else:
    twitterApi.PostUpdate(postString, media=image)