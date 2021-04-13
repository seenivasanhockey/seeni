from flask import Flask,render_template,request,url_for
from flask_ngrok import run_with_ngrok
import mysql.connector
app=Flask(__name__)
run_with_ngrok(app)




@app.route("/")
@app.route("/12c")
def home():
    return render_template("index.html")

@app.route('/vvv',methods=['POST','GET'])
def see():
    mydb = mysql.connector.connect(
        host='sql5.freesqldatabase.com',
        user='sql5405412',
        password='KWGNNejk9p',
        database='sql5405412'
    )
    mycursor = mydb.cursor()

    if request.method=="POST" and request.form['upswd'] == 'seenI@123':
       singu = request.form
       #k=request.form.get('uname')
       #m=request.form.get('upswd')
       a = singu["uname"]
       b = singu["upswd"]
       mycursor.execute('insert into seen(uname,upswd) values(%s,%s)',(a, b))
       mydb.commit()
       mycursor.close()
       return  render_template('re.html')
    else:
       return render_template('aa.html')



@app.route('/vsa',methods=['POST','GET'])
def vasan():
    mydb = mysql.connector.connect(
        host='sql5.freesqldatabase.com',
        user='sql5405412',
        password='KWGNNejk9p',
        database='sql5405412'
    )
    #Database user: sql5405412
    #Database password: KWGNNejk9p
    mycursor=mydb.cursor()
    if request.method == "POST":
        singup=request.form
        a = singup["selate"]
        b = singup["age"]
        c = singup["date"]
        d = singup["yes"]
        e = singup["college"]
        f = singup["phone"]
        mycursor.execute('insert into seeni(selate,age,date,yes,college,phone) values(%s,%s,%s,%s,%s,%s)', (a, b, c, d, e, f))
        mydb.commit()
        mycursor.close()
        return render_template('seeni.html', selate=a, age=b, date=c,yes=d, college=e, phone=f)






@app.route('/ere', methods=['POST', 'GET'])
def gd():

    if request.method == "POST":
        ww=request.form.get('ee')

        return render_template('qw.html')



if (__name__)==('__main__'):
    app.run()




