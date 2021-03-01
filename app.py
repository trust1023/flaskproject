from flask import Flask,request,jsonify
import json

app = Flask('myflask')



@app.route('/')
def hello():
    return 'hello worlds'

@app.route('/user/<username>/')
def show_username(username):
    res = 'your username is ' + username
    return res

@app.route('/users/<int:userid>/')
def show_userid(userid):
    print(type(userid))
    c = 'haha'
    return 'your userid is %s'%userid

@app.route('/userinfo/',methods=['GET','POST'])
def show_userinfo():
    data = request.get_data()
    print(type(data)) #bytes 适合post请求的raw 通过form-data传参的话效果如下
    #b'----------------------------734294754423042296651103\r\nContent-Disposition: form-data; name="username"\r\n\r\ndonglinwei\r\n----------------------------734294754423042296651103\r\nContent-Disposition: form-data; name="age"\r\n\r\n18\r\n----------------------------734294754423042296651103--\r\n'
    print(data)
    print('data is %s'%(json.loads(data.decode()))) #data不能为空否则会报错
    data1 = request.data
    print(type(data1)) #bytes 同get_data()
    print(data1)
    data2 = request.values
    print(type(data2)) #CombinedMultiDict 适合get请求的params和post请求的form-data
    print(data2)
    #print(data2.get('username'))
    return jsonify({"msg":"ok"})


if __name__ == '__main__':
    app.run(debug=True)