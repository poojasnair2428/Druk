import requests
from flask import Flask,request,jsonify

app = Flask(__name__)

api_url = 'https://api.gemini.com/v1/mental-wellness-chat'
api_key="AIzaSyCjnjgruISiMQYfPsK09_qmC13JqdmDbhc"

@app.route('/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')

    headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
    payload = {'message': user_msg}

    try:
        response=requests.post(api_key,json=payload,headers=headers)

        if response.status_code == 200:
            bot_reply = response.json()['response']
            return jsonify({'response': bot_reply})
        else:
            return jsonify({'response': "Sorry, I couldn't process your request. Please try again."}), 500
    except Exception as e:
        return jsonify({'response': f"Error: {str(e)}"}), 500



if __name__ == '__main__':
    app.run(debug=True)