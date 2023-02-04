from flask import Flask, render_template
from flask import request
from flask import json
from werkzeug.exceptions import HTTPException
from werkzeug.utils import secure_filename
from PIL import Image
import import_ipynb
#import Converting_Image_and_Evaluating_it #as nn
#%run Converting_Image_and_Evaluating_it.ipynb import main_func
#from Converting_Image_and_Evaluating_it import main_func
from evaluation import main_func
import urllib
app = Flask(__name__)

#with open('index.html', 'r') as f:
  #  html_string = f.read()
    
    
homepage = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=
    , initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="index.css">

    <style>

.header{
    height: 50px;
    width: 100%;
    text-align: center;
}

.body{
    padding: 20px;
    height: 500px;
    width: 900px;
    position: absolute;
    margin-left: 50%;
    margin-right: 50%;
    transform: translate(-50%,20%);
    /*background-color: green;*/
    background-color: whitesmoke;
    border-radius: 10px;
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);

}

body{
    background-image: url('https://media.istockphoto.com/id/536754333/vector/very-complicated-math-formula-on-blackboard.jpg?s=612x612&w=0&k=20&c=_ynD7iJIaB4nDY9TLw55A_jnV0143Z3rLwFyaI-Yd3o=');

}

.forms{
    margin-top: 10%;
    justify-content: space-around;
    display: flex;
}
input{
    display: none;
  }
.form{
    flex:1;
    height: 150px;
    width: 150px;
    background-color: beige;
}
label{
    height: 200px;
    width: 300px;
    text-align: center;
    
}
label[for=inputTag]{
    background-color: skyblue;
}
label[for=submitForm]{
    background-color: pink;
}
label{
    background-color: pink;
}
p{
    margin-top: 5%;
}

.image{
    height: 90px;
    width: 90px;
    margin-top: 5%;

}
.imageBox{
    margin-top: 15%;
    border-radius: 10px;
    height: 100px;
    width: 100px;
    background-color: white;
    margin-left: 25%;
}
    </style>
</head>
<body>
    <div class="page">
  

    <div class="body">

        <div class="header">
            <h1>Identifying Digits-inator</h1>
        </div>


        <div class="forms">
            <form class="postForm" action="/submit" method="post" enctype="multipart/form-data">

           
            <label for="inputTag" id="label1">
                <div class="imageBox">
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRjkXr96cRAhMzwBeIpwVJcICPRFO6tZ8h4ATmxYaWNyrMJzRT8NPd1PlIEG34l6V8f6os&usqp=CAU" class="image">
                </div>
  
                <p>     Select File Here</p>
                <input id="inputTag" type="file" class="form" name="file" />
              </label>


              <label for="submitForm" id="label2">
                <div class="imageBox">
                    <img src="http://cdn.onlinewebfonts.com/svg/img_326549.png" class="image">
                </div>

                <p>Submit</p>
            <input id="submitForm" type="submit" class="form" >
        </label>
    </form>
        </div>

    </div>
</div>
</body>
</html>
"""


def pop_result_page(num,fn):
    
    style = """
    <style>
   
  .header{
            margin-left: 30rem;
            color: blue;
            }
    
.data{
    background-color: whitesmoke;
    height: 30rem;
    width: 20rem;
    position: absolute;
    left: 50%;
    top: 50%;
    transform: translate(-50%, -50%);
}

.image{
    height 400px;
    width: 400px;
    margin-top: 50px;
    margin-left: 2%;
}
.images{
justify-content: space-evenly
display: flex;
height: 600px;
width: 900px;
}
.predicted_image{
flex:1;
margin-left:50%;
}
.actual_image{
flex:1;
}
h1{
text-align: center;
}

    </style>
    """
    img = ""
    if num == '0' or num == 0:
        img = 'https://cdn.pixabay.com/photo/2016/02/05/15/12/zero-1181084_960_720.png'
    elif num == '1' or num == 1:
        img = 'https://st.depositphotos.com/2036077/3580/i/600/depositphotos_35804245-stock-photo-3d-red-number-collection.jpg'
    elif num == '2' or num == 2:
        img = 'https://st.depositphotos.com/2036077/3580/i/600/depositphotos_35804245-stock-photo-3d-red-number-collection.jpg'
    
    elif num == '3' or num == 3:
        img = '/2.png'
    
    elif num == '4' or num ==4:
        img = '/2.png'
    elif num == '5' or num == 5:
        img = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQhMv-uOyvoqHUIW9iwzern6N-gu4S9kfXnEA&usqp=CAU'
    elif num == '6' or num == 6:
        img = 'https://svgsilh.com/svg/33769.svg'
        
    elif num == '7'  or num == 7:
        img = 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/69/Junction_2.svg/2560px-Junction_2.svg.png'
        
    elif num == '8' or num == 8:
        img = '/2.png'
    else:
        img = 'https://cdn.pixabay.com/photo/2015/04/04/19/13/nine-706889_1280.jpg'
    
    return f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stuff</title>

    <script src="script.js" defer></script>
    <link rel="stylesheet" href="style.css">
   
    {style}
</head>
<body>
    <div class="page">
    
        <div class="header">
                <h1></h1>
        </div>


        <div class="images">
        
        <div class = "predicted_image">
        
        <h1>IS YOUR IMAGE A... </h1>
        
        <img src={f'{img}'} class={'image'}> </img>
        
        </div>
        
       
        
        
        </div>

     

    </div>
   
</body>

</html>
"""



@app.route("/")
def post():
    if request.method == 'GET':
        return homepage
        #return render_template("home.html")
    #return render_template('index.html')
    #return "<p> Ya dumb</p>

@app.route("/submit", methods=['GET', 'POST'])
def upload_Shii():
    if request.method == 'POST': 
        #file = request.form.get("file")
        print(request.files)
        file = request.files['file']
        file.save(secure_filename(f'temp{file.filename}'))
        fname = file.filename.split('.')
        fname[1] = f'.{fname[1]}'
       # string = ''
       # for i in range(10):
       #  #   string+=f'<h1>{main_func(fname[0], fname[1])}</h1>'
       # return string
    
    
       # return f'<h1>{main_func(fname[0], fname[1])}</h1>'
        return pop_result_page(main_func(fname[0], fname[1]), (fname[0]+fname[1]))
       # if file and allowed_file(file.filename):
         #   filename = secure_filename(file.filename)
          #  file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        #fname = file.split('.')
        #text = request.form.get("text")
        #fileImage = Image.open(file)
        #fileImage.save(f'1{file})'
      

        #testfile = urllib.URLopener()
        #testfile.retrieve(f"{file}", "file.png")
        #print(type(file))
       # return f'<h1>{file}    yuh.      {text}            {request.form.get("file").name}</h1>'
        #return f'<h1>{main_func(fname[0],fname[1],int(text))}</h1>'
        #return html
        
        
    
    if request.method == 'GET':
        return '<h1>ur bad</h1>'

#@app.errorhandler(HTTPException)
#def handle_exception(e):
 #   print(e)
    
  #  return  '<h1>lol</h1>'



if __name__ == '__main__':
     app.run(debug = True)
        




       
