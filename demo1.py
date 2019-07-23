from flask import request,session,jsonify
from flask import Flask


from db_config import demo

app=Flask(__name__)

@app.route('/signup',methods = ['POST'])
def signup():
        if request.method == 'POST':

            payload=request.get_json()
            
            for i in demo.find():
                if payload['email'] == i['email']:
                    response = jsonify({'status':'Allready present email'})
                    response.headers.add('Access-Control-Allow-Origin', '*')
                    response.headers['Access-Control-Allow-Origin'] = '*'
                    print(response)
                    print(response.headers)
                    return response,204
                else:
                    pass

            demo.insert_one(payload)
            response = jsonify({'status':'Signup Success'})
            response.headers.add('Access-Control-Allow-Origin', '*')
            response.headers['Access-Control-Allow-Origin'] = '*'
            print(response)
            print(response.headers)
            return response
            

if __name__ == '__main__':

    app.secret_key = 'some secret key'
    app.debug = True
    app.run(port=5001)

