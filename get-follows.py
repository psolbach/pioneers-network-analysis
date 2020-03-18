import os
import twint
from users import users

# curl 'https://tweeterid.com/ajax.php' --data 'input=1plusx'

for i, user in enumerate(users):
  print(f"Fetching follows {i}/{len(users)} with username {user}")

  username = user.lower()
  filepath = f"userdata/{username}.json"

  if not os.path.exists(filepath):
    with open(filepath, 'w+'): pass

  if os.path.getsize(filepath) > 0:
    continue

  c = twint.Config()
  c.Username = username
  c.Store_json = True
  c.Custom["user"] = ["id", "username"]
  c.Output = filepath

  print(username)
  
  try:
    twint.run.Following(c)
  except:
    print(f"Collecting follows for {username} failed with")