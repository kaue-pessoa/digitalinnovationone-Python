import requests

def retorno_dado_cep(cep):
    response = requests.get('https://viacep.com.br/ws/{}/json'.format(cep))
    print(response.status_code)
    print(response.json())
    dados_cep = response.json()
    print(dados_cep['logradouro'])
    print(dados_cep['complemento'])
    return dados_cep

def retorno_dado_pokemen(pokemon):
    response = requests.get('http://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemen = response.json()
    return dados_pokemen

def retorna_reponse(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = retorna_reponse('https://iin.digitalinnovation.one/tag/globallabs/')
    print(response)
     #retorno_dado_cep('01001000')
     #dados_pokemen = retorno_dado_pokemen(25)
     #print(dados_pokemen)
