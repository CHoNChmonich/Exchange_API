Для запуска проекта введите команду: "dcoker-compose up --build"
Запрос для конвертации одной валюты  в другую, необходимо отправлять на страницу "http://localhost:8000/api/v1/rates" передав следующие параметры запроса:
from - какую валюту надо перевести в другую, например from=USD
to - в какую валюту необходимо перевести первую валюту, например to=RUB
value - значение первой валюты, для перевода  в другуюЮ например value=1
Запрос в адресной строке для перевода одного доллара в рубли будет выглядеть следующим образом:
http://localhost:8000/api/v1/rates?from=USD&to=RUB&value=1
Ответ на него будет передан в виде JSON файла, который будет выглядеть следующим образом:
{
    "result": 105.00
}