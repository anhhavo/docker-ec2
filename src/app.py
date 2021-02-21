import os
from io import BytesIO
from flask import Flask, render_template, send_file
import pandas as pd 
import matplotlib.pyplot as plt
import jinja2

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
#socketio = SocketIO(app, cors_allowed_origins='*')

my_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader('/'),
])
app.jinja_loader = my_loader


def get_first_csv():
    #read data from my S3 Bucket
    first_data = pd.read_csv('s3://cse427-ahvo/lab1/number1.csv')
    #first_data = pd.read_csv('first.csv')
    #print(first_data)
    fig, ax = plt.subplots()
    fig.set_size_inches(len(first_data['sepal.length']) *  0.1, len(first_data['sepal.width'] ) * 0.1)
    # scatter the data and color by variety type.
    #Setosa = red / Versicolor = Yellow / Virgincia = Blue
    colors = {'Setosa':'r', 'Versicolor':'y', 'Virginica':'b'}
    for i in range(len(first_data['sepal.length'])):
        ax.scatter(first_data['sepal.length'][i], first_data['sepal.width'][i], c=colors[first_data['variety'][i]]) 
        ax.scatter(first_data['petal.length'][i], first_data['petal.width'][i], c=colors[first_data['variety'][i]])
    # set a title and labels
    ax.set_title('First Dataset')
    ax.set_xlabel('length')
    ax.set_ylabel('width')
    #save to image.
    img = BytesIO()
    fig.savefig(img)
    img.seek(0)
    #return send_file(img, mimitype='image/png')
    #encoded_img = base64.encodebytes(img.getvalue()).decode('ascii')
    return img

def get_second_csv():
    second_data = pd.read_csv('s3://cse427-ahvo/lab1/number2.csv')
    second_data = second_data.drop(['Unnamed: 0'], axis=1).drop(['variety'], axis=1)
    second_data.plot.line(title='Second Dataset')
    img = BytesIO()
    plt.savefig(img)
    img.seek(0)
    return img

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/second.png', methods= ['GET'])
def second_csv():
    img = get_second_csv()
    return send_file(img, mimetype='image/png', cache_timeout=0)
    
@app.route('/first.png')
def first_csv():
    img = get_first_csv()
    return send_file(img, mimetype='image/png', cache_timeout=0)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)          

