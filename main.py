from flask import Flask, request, render_template, redirect, url_for, send_from_directory
import os
import json

app = Flask(__name__)

@app.route('/')
def index():
    page = '''
<!DOCTYPE html>
<html>
<title>File Upload</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
<body style="padding:25px;">
<div class="w3-card-4">
  <div class="w3-container w3-brown">
    <h2>View your Aquatics SDHM</h2>
    <p>The output of your model included a GeoJSON file, please select that file to continue.</p>
    </div>
  <form class="w3-container" action="/map" method="post" enctype="multipart/form-data">
    <p>      
    <label class="w3-text-brown"><b>Upload File</b></label>
    <input class="w3-input w3-border w3-sand" name="file" type="file" required></p>
    <p>
    <button class="w3-btn w3-brown">Submit</button></p>
  </form>
</div>
</body>
</html> 
    '''
    return page

@app.route('/map',methods=["POST"])
def upload():
    try:
        if request.method == 'POST':
            contents = json.loads(request.files['file'])
            return render_template('map.html',data=contents)
            
    except Exception as e:
        return str(e)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
