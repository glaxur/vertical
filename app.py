from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def index():

   input = request.args.get("position_right")
   print(input)

   position_left = "left"
   position_right = "right"

   # open file for reading, 'r'
   # file is saved to variable
   index_file = open('index.html', 'r')
   # read contents of the file
   my_html = index_file.read()

   if input:
       # add use input back into the html
       my_html = my_html.replace("{{position_left}}", position_left)
       my_html = my_html.replace("{{position_right}}", position_right)
   else:
       my_html = my_html.replace("{{position_right}}", position_left)
       my_html = my_html.replace("{{position_left}}", position_right)

   # close the file out when you're done
   index_file.close()

   return my_html