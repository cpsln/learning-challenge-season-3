from flask import render_template, request,session,jsonify
from flask import Flask
from db_config import demo

app=Flask(__name__)


@app.route('/login',methods = ['POST', 'GET'])
def login():
            if request.method == 'POST':
                
                eml=demo.find()
                payload=request.get_json()
                

                for i in eml:
                        if payload["Username"] == i["email"] and payload['Password'] == i['password']:
                            
                                response = jsonify({'UserId':str(i["_id"]),'name':i["Firstname"]+' '+i["Lastname"]})
                                response.headers.add('Access-Control-Allow-Origin', '*')
                                response.headers['Access-Control-Allow-Origin'] = '*'
                                print(response)
                                print(response.headers)
                                return response
                        else:
                                pass
                        
                response = jsonify({'wrong':'worng email/password'})
                response.headers.add('Access-Control-Allow-Origin', '*')
                response.headers['Access-Control-Allow-Origin'] = '*'
                print(response)
                print(response.headers)
                return response,202    

if __name__ == '__main__':

    app.secret_key = 'some secret key'
    app.debug = True
    app.run(port=5001)