
from flask import request,session,jsonify
from db_config import demo
from flask import Flask

app=Flask(__name__)

@app.route('/gettData', methods=['POST'])
def getdata():
        if request.method =='POST':
            data=demo.find()
            payload=request.get_json()
            print(payload)
            for i in data:

                    if payload['userId'] == str(i['_id']):

                        i['_id']=str(i['_id'])
                        response = jsonify([i])
                        response.headers.add('Access-Control-Allow-Origin', '*')
                        response.headers['Access-Control-Allow-Origin'] = '*'
                        print(response)
                        print(response.headers)
                        return response
                    else:
                        pass

            response = jsonify({'status':'no data found'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
            

if __name__ == '__main__':

    app.secret_key = 'some secret key'
    app.debug = True
    app.run(port=5001)
