import requests


class CoinConversorService:

    def __init__(self):
        self.__base_url = 'https://economia.awesomeapi.com.br/last/'
    
    def converter(self, coin_origin, coin_target):
        response = requests.get(
            url = f'{self.__base_url}{coin_origin}-{coin_target}'
        )
        if response.status_code == 404:
            return response.json().get('message')
        dados = response.json()
        print(dados)
        par_moeda = dados[f'{coin_origin}{coin_target}']
        print(par_moeda)
        valor_bid = par_moeda['bid']
        print(valor_bid)
        return response.json().get(f'{coin_origin}{coin_target}').get('bid')


if __name__ == '__main__':
    conversor_service = CoinConversorService()
    conversion = conversor_service.converter('BTC', 'BRL')
    print(conversion)
 