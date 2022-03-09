import os
import json
import time

from twarc.client2 import Twarc2
from twarc.expansions import ensure_flattened
from seed_accounts import users

# Your bearer token here
t = Twarc2(bearer_token=os.environ['TWITTER_BEARER_TOKEN'])

for i, user in enumerate(users):
  print(f"Fetching follows {i+1}/{len(users)} for username {user}")

  username = user.lower()
  filepath = f"userdata/{username}.json"

  if not os.path.exists(filepath):
    with open(filepath, 'w+'): pass

  if os.path.getsize(filepath) > 0:
    continue
  
  try:
    follows = []
    follows_generator = t.following(user=username)
    
    for i, follower_page in enumerate(follows_generator):
      print(f"Processing page {i+1} for {username}")
      follows = follows + follower_page["data"]

    with open(filepath, 'w+') as f:
      f.write(json.dumps(follows))

  except e:
    print(f"Collecting follows for {username} failed with {e}")

  print(f"Sleeping for 6 minutes to avoid throttling")
  time.sleep(60*6)
