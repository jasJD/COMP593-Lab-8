import requests

def get_poke_info(name):

    print("Getting information...", end='')
    
    url="https://pokeapi.co/api/v2/pokemon/" + name
    resp_msg = requests.get(url)
    
    if resp_msg.status_code == 200:
        print("success")
        return resp_msg.json()
    else:
        print("failed code:", resp_msg.status_code)
        return