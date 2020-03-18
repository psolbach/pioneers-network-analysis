# import pdb; pdb.set_trace()

import csv
import json

from os import listdir
from os.path import isfile, join

CSV_PATH_E = "csv/graphdata_e.csv"
CSV_PATH_V = "csv/graphdata_v.csv"
USERDATA_PATH = "userdata/"

def string_to_hash(string, length=8):
  return abs(hash(string)) % (10 ** length)


def get_graph_data(path, filter_common=True):
  vertex_counts = {}
  vertices = []
  edges = []

  files = [f for f in listdir(path) if isfile(join(path, f))]

  for fname in files:
    username = fname.split(".")[0]
    vertices.append([username.lower()]) # append original node
    
    if fname[0] is ".": continue
    f = open(USERDATA_PATH + fname, 'r') 
    
    try:
      lines = f.readlines()
    except:
      print(f"Error reading file {fname}")
    
    for line in lines:
      user_json = json.loads(line)
      follower = fname.split(".")[0].lower()
      followee = user_json["username"].lower()

      if not vertex_counts.get(followee):
        vertex_counts[followee] = 0

      vertex_counts[followee] += 1

      if vertex_counts.get(followee) > 1:
        vertices.append([followee]) # append follow node

      edges.append([
        string_to_hash(follower),
        string_to_hash(followee),
        follower,
        followee
        ]) # append edge values

  common_edges = []
  for edge in edges:
    if vertex_counts.get(edge[3]) and vertex_counts.get(edge[3]) > 1:
      common_edges.append(edge)

  for vertex in vertices:
    vertex.append(vertex_counts.get(vertex[0])) # add weight

  return {
    "v": vertices,
    "e": common_edges if filter_common else edges
  }


def write_to_csv(data, csv_path): 
  print("Writing graph data to .csv file")

  with open(csv_path, 'w+', newline='') as csvfile:
    graphwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for i, line in enumerate(data):
      graphwriter.writerow(data[i])

  return True


graph_data = get_graph_data(path=USERDATA_PATH)
write_result_v = write_to_csv(data=graph_data["v"], csv_path=CSV_PATH_V)
write_result_e = write_to_csv(data=graph_data["e"], csv_path=CSV_PATH_E)

print("Finished writing {} vertices with message {}".format(len(graph_data["v"]), write_result_v))
print("Finished writing {} edges with message {}".format(len(graph_data["e"]), write_result_e))
