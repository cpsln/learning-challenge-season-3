from flask import render_template, request,session,jsonify
from flask import Flask
from db_config import demo

app=Flask(__name__)
               


@app.after_request
def apply_caching(response):
            response.headers["Content-Type"] = "application/json"
            response.headers['Access-Control-Allow-Origin'] = '*'
            response.headers['Access-Control-Allow-Headers'] = 'content-type'
            return response

@app.route('/editProfile',methods = ['POST'])
def editProfile():

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
                                'FirstName':payload['FirstName'],
                                'LastName':payload['LastName'],
                                'phoneno':payload['phoneno'],
                                'email':payload['email']
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


    