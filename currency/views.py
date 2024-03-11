from django.shortcuts import render
import currencyapicom



def index_view(request):
    client = currencyapicom.Client('XXXX')
    result = client.latest()
    # print(result)
    print(result['data']['AZN'])

    azn_value = result['data']['AZN']['value']
    rub_value = result['data']['RUB']['value']
    eur_value = result['data']['EUR']['value']
    usd_value = result['data']['USD']['value']

    context = {

        "azn_value": azn_value,
        "rub_value": rub_value,
        "eur_value": eur_value,
        "usd_value": usd_value,


    }

    return render(request, "index.html", context)
