from flask import Flask, render_template, send_from_directory
app2 = Flask(__name__)


@app2.route('/')
def index():
       return render_template('index.html')


@app2.route('/images/<path:path>')
def index2(path):
       return send_from_directory('static/images',path)
       
@app2.route('/static/<path:path>')
def index3(path):
     return app2.send_static_file(path)
        
if __name__ == '__main__':

    #app.run(host='127.0.0.1',port='5000',debug = True,use_reloader=False)
    app2.run(threaded=True, port='5000')