from flask import Flask, jsonify

from pyngrok import ngrok

#kết nối với DATABASE_URL
import os
import psycopg2

url = ngrok.connect(6868).public_url
print('Henzy Tunnel URL:', url)


#kết nối với DATABASE_URLmã của bạn.
DATABASE_URL = os.environ['DATABASE_URL']
conn = psycopg2.connect(DATABASE_URL, sslmode='require')


app = Flask(__name__) #tao mot instance cua class flask

app.config['JSON_SORT_KEYS'] = False
@app.route('/detect',methods=['GET']) #chi ra url cua api
def hello_world():
    return jsonify([
        {
            "id": 1,
            "name": "Car",
            "mean": "O to",
            "path": "null"
        }
    ])

# Start Backend
if __name__ == '__main__':

    app.run(host='0.0.0.0', port='5000',debug=True)


