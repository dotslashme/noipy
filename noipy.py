import re
import requests

''' Left to do:
        - implement logging
        - implement tmp file to avoid unneccessary api updates
        - Proper parsing of result
'''

noip_username = ''  # Your no-ip.com username/email
noip_password = ''  # Your no-ip.com password
host_names = []  # The host or hosts to update

api_url = 'https://dynupdate.no-ip.com/nic/update'
client_agent_name = 'NoIpy ddns update client'
client_agent_version = '0.0.1'
client_agent_maintainer = 'christian@dotslashme.com'
ip_resolvers = [
    'http://icanhazip.com/'
]


def get_external_ip():
    for resolver in ip_resolvers:
        try:
            response = requests.get(resolver)
        except requests.exceptions.RequestException as e:
            print(e)
            continue
        else:
            data = response.text
            break

    return data


def parse_data_to_ip(data):
    regex = re.compile('([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
    match = re.search(regex, data)
    return match.group(0)


def update_api(ip):
    user_agent = client_agent_name
    + '/'
    + client_agent_version
    + ' '
    + client_agent_maintainer

    headers = {'user-agent': user_agent}
    payload = {'myip': ip, 'hostname': host_names}
    try:
        response = requests.get(
            api_url,
            headers=headers,
            params=payload,
            auth=(noip_username, noip_password)
        )
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print(response.url)
        print(response.status_code)
        print(response.text)


data = get_external_ip()
ip = parse_data_to_ip(data)
update_api(ip)
