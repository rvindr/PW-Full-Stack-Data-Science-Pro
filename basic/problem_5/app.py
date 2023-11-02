from flask import Flask, render_template, request, url_for, redirect, session

app=Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def home():
    if 'name' in session:
        return render_template('index.html',name=session['name'],
        mail=session['mail'],address=session['address'])
    
    return render_template('form.html')


@app.route('/session',methods=['GET','POST'])
def session_data():
    session['name']=request.form.get('name')
    session['mail']=request.form.get('mail')
    session['address']=request.form.get('address')
    return redirect(url_for('home'))

@app.route('/remove_data')
def remove_data():
    session.pop('name')
    session.pop('mail')
    session.pop('address')

    return redirect(url_for('home'))




if __name__=='__main__':
    app.run(host='0.0.0.0', debug=True)