from flask import Flask, request, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/showdata',methods=['POST','GET'])
def show_data():
    data=request.form.get('data')
    with open(data,'r') as f:
        return f


if __name__=='__main__':
    app.run(host='0.0.0.0')