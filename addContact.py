from flask import render_template, request,session,jsonify
from flask import Flask
from db_config import demo

app=Flask(__name__)
               



@app.route('/ContactDetail',methods = ['POST'])
def ContactDetail():
        if request.method == 'POST':
 
            payload=request.get_json()

            for pId in patient.find():
                if payload['UserId'] == str(pId['_id']):
                    
                        del payload['pId']
                        patient.update_one({
                                    '_id':pId['_id']
                            },{
                            
                                '$set':{
                                
                                        'Adresss':payload
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
    