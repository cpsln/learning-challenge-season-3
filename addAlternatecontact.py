from flask import render_template, request,session,jsonify
from flask import Flask
from db_config import demo

app=Flask(__name__)


@app.route('/AlternateContact',methods = ['POST'])
def AlternateContact():
        if request.method == 'POST':
 
            

            payload=request.get_json()
            
            for pId in demo.find():

                if payload['UserId'] == str(pId['_id']):
                        del payload['pId']
                        try:
                            
                            pId['AlternateContact'].append(payload)
                            demo.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                        'AlternateContact':pId['AlternateContact']
                                        }
                                    }
                                )
                        except KeyError:
                        
                            demo.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                            'AlternateContact':[payload]
                                        }
                                    }
                            )
                        
                        response = jsonify({'status':'save contact'})
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
                else:
                        pass
            
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
