from flask import Flask, redirect, url_for, request, jsonify
app = Flask(__name__)


# import functools
# def return_json(f):
#     @functools.wraps(f)
#     def inner(**kwargs):
#         return jsonify(f(**kwargs))
#     return inner

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name
  
@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

class user:
   def __init__(self,username,password):
      self.username=username
      self.password=password
import mysql.connector
conn = mysql.connector.connect(
   host="socialviuni.cqxwfymphxwv.ap-southeast-1.rds.amazonaws.com",
   user="root",
   password="socialviuni"
   )
sql = conn.cursor()
sql.execute("use socialviuni")

@app.route('/object')
def object():
   arr = []
   sql.execute("select username,password from user")
   result = sql.fetchall()
   for i in result:
      arr.append(user(i[0],i[1]).__dict__)
   return jsonify(arr)
if __name__ == '__main__':
   # app.run(debug = True)

   import requests
   headers = {
      'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsImV4cCI6MTY0ODY0ODkyOCwiaWF0IjoxNjQ4NjMwOTI4fQ.okLQLDg5dVmJoZG4KvQJTlg8hd0MmHBdiM-hbVlyKEh_PRCpTtJomuFmSK1a_4alx5WxRagwY0Yu3rAWOZxAKg',
      'X-FORWARDED-FOR': 'ga'
   }
   p = requests.get("http://localhost/user/me", headers= headers)
   print(p.text)