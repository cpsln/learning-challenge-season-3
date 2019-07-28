from flask import request,session,jsonify
from flask import Flask
from db_config import demo

app=Flask(__name__)
               

@app.route('/personal',methods = ['POST'])
def personal():

        if request.method == 'POST':

            payload=request.get_json()
            print(payload)
            for pId in demo.find():

                if payload['pId'] == str(pId['_id']):
                        del payload['pId']
                        demo.update_one({
                                    '_id':pId['_id']
                            },{
                                '$set':{
                                'Gender':payload['Gender'],
                                'Birthdate':payload['date'],
                                'Blood':payload['Blood'],
                                'status':payload['status']
                                }
                            }
                        )
                        response = jsonify({'status':'save contact'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
            
            response = jsonify({'status':'Not save contact'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response

if __name__ == '__main__':

    app.secret_key = 'some secret key'
    app.debug = True
    app.run(port=5001)
    