# vmikach-vm
Проста безсерверна функція для YC для перемикання віртуального екземпляра
### TODO
тут красива інструкція по створенню функції через Yandex CLI із зазначенням змінних середовища оточення, яких теж виходять через jq

https://cloud.yandex.ru/docs/functions/operations/function/environment-variables-add

yc serverless function create --name=vmikach

yc serverless function version create \
  --function-name=vmikach \
  --runtime python39 \
  --entrypoint index.handler \
  --memory 128m \
  --execution-timeout 5s \
  --environment FOLDER_ID=(yc init | jq folder_id), SERVER_ID (yc compute instance get --name) , BOT_TOKEN (from botFather)
  
  source.zip
