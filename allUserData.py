
from flask import request,session,jsonify
from db_config import demo
from flask import Flask

app=Flask(__name__)

@app.route('/allUserData', methods=['GET'])
def allUser():
        if request.method =='GET':
            data=demo.find()
            payload=request.get_json()
            print(payload)
            alldata=[]
            for i in data:


                        i['_id']=str(i['_id'])
                        response = jsonify(alldata)
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
