from flask import request,session,jsonify
from flask import Flask
from db_config import demo

app=Flask(__name__)



@app.route('/changePassword',methods = ['POST'])
def changePassword():

        if request.method == 'POST':

            payload=request.get_json()
            print(payload)

            for dId in demo.find():

                if payload['UserId'] == str(dId['_id']):
                    if payload['Passwordnew'] == payload['Passwordconf']:
                        doctor.update_one({
                                    '_id':dId['_id']
                            },{
                                '$set':{
                                'password':payload['Passwordnew']
                                }
                            }
                        )
                        response = jsonify({'status':'save password'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
                    else:
                        response = jsonify({'status':'password not match'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response,201

            response = jsonify({'status':'Not save password'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response,205


if __name__ == '__main__':

    app.secret_key = 'some secret key'
    app.debug = True
    app.run(port=5001)
