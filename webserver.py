from flask import Flask, render_template, request
from gpiozero import LED
app = Flask(__name__)

led = LED(4)

@app.route('/',methods = ['POST', 'GET'])
def hello_world():

   return render_template("index.html")

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form.get("open")
      print(result)
      if(result=="Open"):
         led.on()
         print("open")

      if(result=="close"):
         led.off()
         print("close")

      return render_template("index.html",result = result)

if __name__ == '__main__':
   app.run(host="0.0.0.0")


