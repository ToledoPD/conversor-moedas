from clients.callmebot_service import CallMeBoot
from clients.conversor_service import CoinConversorService


conversor_service = CoinConversorService()
origin = 'USD'
target = 'BRL'
conversion = conversor_service.converter(origin, target)

wpp_service = CallMeBoot()
wpp_service.send_message(
    f'Cotação do {origin}: R$ {round(float(conversion), 2)}'
)
