from flask import Flask, request
import requests
import json
 
app = Flask(__name__)
 
@app.route('/')
def index():
   return "Hello"
 
def send_msg(msg):
   headers = {
       'Authorization: EAAFkU0ZBKYc0BANAaYXRZA6WaPYRJSjCynouh3QLYQwdzBSRwPp6yCcLoTaKM7JvSCD6CnlyCZAPUepZB27TOZC1GTa81AesaivMTBZCEAZBk4P0oqy5m0HwBGfVZBJgFc4SALRzgZALslUKaKjO2IZAgjqY4mcGu6aolAixlONkCxX8Kh6D9ijbkTXrlEt9z3yCTPT1Woxm1AGmEP8OCuoKV4'
   }
   json_data = {
       'messaging_product': 'whatsapp',
       'to': '263782953086',
       'type': 'text',
       "text": {
           "body": msg
       }
   }
   data = json.dumps(json_data)
   response = requests.post('https://graph.facebook.com/v13.0/101931012658689/messages', headers=headers, json=data)
   print(response.text)
 
 
@app.route('/receive_msg', methods=['POST','GET'])
def webhook():
   #print(request)
   res = request.get_json()
   #print(res)
   res1 = res['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
   
   try:
       if res1 is not '':
        print(res1)
        return send_msg("Thank you for the response.")
   except:
       print('Not succesful')
   return '200 OK HTTPS.'
 


 
  
if __name__ == "__main__":
   app.run(debug=True)
