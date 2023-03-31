from linkedin_api import Linkedin
import json

# Terms to search relevant posts
search_profiles = ['isaac-geraldo']

# Get credentials from file to access the Linkedin API
with open('./.local/credentials.json') as file:
  data = json.load(file)

username = data["username"]
password = data["password"]

# Sign in on linkedin
linkedin = Linkedin(username, password)

# Colect posts from selected users and put it in a list
posts = []
for profile in search_profiles:
  results = linkedin.get_profile_posts(public_id=profile,post_count=100)
  for post in results:
    posts.append(post)
