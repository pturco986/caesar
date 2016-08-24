#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi
from caesar import encrypt


# => prints Jgnnq, Bcej!

# class Rot13(BaseHandler):
#     def get(self):
#         self.render('rot13-form.html')
#
#     def post(self):
#         rot13 = ''
#         text = self.request.get('text')
#         if text:
#             rot13 = text.encode('rot13')
#
#         self.render('rot13-form.html', text = rot13)

header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Caesar</title>
        <style>
        form{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        textarea {
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }
        p.error {
            color: red;
        }
        </style>
    </head>
    <body>
"""

footer = """
    </body>
</html>
"""

form = """
<form method = "post">
Enter the number of letters you want to rotate by:
<input name="numrotate" type="text" value="0"/>
<div>
Input the text you want to encrypt:
<br>
<textarea name="text" method="post" placeholder="Enter text here">{}</textarea>
</div>
<input type="submit"/>
</form>
"""



class Rot13(webapp2.RequestHandler):
    def get(self):

        response = header + form.format("") + footer
        self.response.write(response)

    def post(self):

        text = self.request.get("text")
        text_escaped = cgi.escape(text, quote=True)

        numrotate = self.request.get("numrotate")

        result = encrypt(text, int(numrotate))


        response = header + form.format(result) + footer
        self.response.write(response)

app = webapp2.WSGIApplication([
    ('/', Rot13)
], debug=True)
