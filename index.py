import os
import requests
import telebot
import json

server_id = os.environ.get('SERVER_ID')
# put  list user_id
user_ids = [] #<--------id user in telegram
url = 'https://compute.api.cloud.yandex.net/compute/v1/instances/'+server_id
token = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(token)
folder_id= os.environ.get('FOLDER_ID')
headers = ''


def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot' + token + '/' + 'sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, data=data)



def handler(event, context):
    global headers
    api_key = context.token['access_token']
    headers = {'Authorization': 'Bearer '+api_key,
               'Content-Type': 'application/json'}
    body = json.loads(event['body'])
    chat_id = body['message']['from']['id']
    if (chat_id not in user_ids):
        return {'statusCode': 200,'body': '!'}
    text = body['message']['text']




    message = telebot.types.Update.de_json(event['body'])
    bot.process_new_updates([message])

        
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])
    return {
            'statusCode': 200,
            'body': '!',
        }
@bot.message_handler(commands=['poweron'])
def start_server(message):
    bot.send_message(message.chat.id, 'Це команда для запуску сервера')
    if (message.from_user.id in user_ids):
        answer = server_start()
    else:
        answer = 'Вам не дозволено:'+str(message.from_user.id)
    bot.send_message(message.from_user.id, answer)

@bot.message_handler(commands=['poweroff'])
def stop_server(message):
    bot.send_message(message.chat.id, 'Це команда для зупинки сервера')
    if (message.from_user.id in user_ids):
        answer = server_stop()
    else:
        answer = 'Вам не дозволено це робити:'+str(message.from_user.id)
    bot.send_message(message.from_user.id, answer)



def server_start():
    uri = url + ':start'
    response = requests.post(uri, headers=headers)

    json_response = response.json()
    print(json_response)
    #status = json_response["action"]["type"]

    return 'start'

def server_stop():
    uri = url + ':stop'
    response = requests.post(uri, headers=headers)

    json_response = response.json()
    print(json_response)
    #status = json_response["action"]["type"]

    return 'stop'

