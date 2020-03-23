import graph_tool.all as gt
# from graph_tool.all import *
import math
import matplotlib

g = gt.load_graph_from_csv(
  "csv/graphdata_test.csv",
  hashed=True,
  eprop_types=[
    'string',
    'string'
  ],
  eprop_names=[
    "source_handle",
    "target_handle",
    "weight"
  ])

# import pdb; pdb.set_trace()
source_handle = g.ep["source_handle"]
weight = g.ep["weight"]

gt.graph_draw(g,
  vertex_font_size=12, 
  vertex_text="g.ep.source_handle", 
  vertex_shape="double_circle",
  vertex_fill_color="#729fcf", 
  vertex_pen_width=3, 
  edge_pen_width=1,
  output="graph-draw.png", 
  output_size=(4000, 4000)
)

