from flask import Flask,render_template,request
from flask_mysqldb import MySQL
app=Flask(__name__)
app.config["MYSQL_HOST"]= 'localhost'
app.config["MYSQL_USER"]= 'root'
app.config["MYSQL_PASSWORD"]= '123456789'
app.config["MYSQL_DB"]= 'flaskcontacts'
mysql=MySQL(app)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_contact', methods=['POST'])
def addcontact():
    if request.method == 'POST':
        fullname=request.form['fullname']
        email=request.form['email']
        phone=request.form['phone']
        cur=mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname,phone,email) VALUES(%s,%s,%s)',(fullname, phone, email))
        mysql.connection.commit()

        return  "recibido"


@app.route('/edit_contact')
def editcontact():
    return "contacto editado"

@app.route('/delete_contact')
def detecontact():
    return "contacto eliminado"

if __name__=='__main__':
    app.run(port=3000,debug=True)

