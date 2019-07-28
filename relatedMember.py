from flask import render_template, request,session,jsonify
from flask import Flask
from db_config import demo

app=Flask(__name__)

@app.route('/relatedMember',methods = ['POST'])
def relatedMember():
        if request.method == 'POST':
 
            payload=request.get_json()
            
            for pId in demo.find():

                if payload['pId'] == str(pId['_id']):
                        del payload['pId']
                        try:
                            
                            pId['relatedMember'].append(payload)
                            demo.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                
                                        'relatedMember':pId['relatedMember']
                                        }
                                    }
                                )
                        except KeyError:
                        
                            demo.update_one({
                                    '_id':pId['_id']
                                },{
                                    '$set':{
                                            'relatedMember':[payload]
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
            
