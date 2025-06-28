import requests
import os
from dotenv import load_dotenv


load_dotenv()


class CallMeBoot:

    def __init__(self):
        self.__base_url = 'https://api.callmebot.com/whatsapp.php'
        self.__api_key = os.getenv('CALLMEBOT_API_KEY')
        self.__phone_number = os.getenv('PHONE_NUMER')

        if not self.__api_key:
            raise ValueError('API Key not found')

    def send_message(self, message):
        response = requests.get(
            url = f'{self.__base_url}?phone={self.__phone_number}&text={message}&apikey={self.__api_key}'
        )

        print(response.status_code)
        print(response.url)
        return response.text

if __name__ == '__main__':
    wpp_service = CallMeBoot()
    wpp_service.send_message(
        'Teste de mensagem'
    )
