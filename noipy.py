import re
import requests
import os
from datetime import datetime, timedelta


''' Left to do:
        - implement logging
        - implement tmp file to avoid unneccessary api updates
'''

noip_username = ''  # Your no-ip.com username/email
noip_password = ''  # Your no-ip.com password
host_names = ['']  # The host or hosts to update


def get_external_ip():
    '''Get the external ip of the client'''

    ip_resolvers = [
        'http://icanhazip.com/'
    ]

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
    api_url = 'https://dynupdate.no-ip.com/nic/update'
    user_agent = 'NoIpy ddns update client/0.0.1 christian@dotslashme.com'

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
        return response.text


def check_response(response, ip):
    if ip in response:
        process_success(response, ip)
    else:
        process_error(response)


def process_success(response, ip):
    fp = open('/tmp/ip.noipy', 'w')
    fp.write(ip)
    fp.close()
    print('The job completed successfully')


def process_error(response):
    if 'nohost' in response:
        print('There is no DNS record for one or more hostnames. Check config')
    elif 'badauth' in response:
        print('The supplied credentials seems to be invalid. Check config')
    elif 'badagent' in response:
        print('This update agent has been banned, setting up quarantine')
        quarantine_client()
    elif '!donator' in response:
        print('Update operation not supported by your subscription')
    elif 'abuse' in response:
        print('Abuse reported for this user, setting up quarantine')
        quarantine_client()
    else:  # 911
        print('The noip server has issues, setting temporary quarantine')
        now = datetime.now()
        quarantined_until = now + timedelta(minutes=45)
        quarantine_client(str(quarantined_until))


def is_quarantined():
    quarantine_file = '/tmp/quarantined.noipy'

    if os.path.isfile(quarantine_file):
        if os.stat(quarantine_file).st_size == 0:
            return True
        else:
            fh = open(quarantine_file, 'r')
            data = fh.read()
            now = datetime.now()
            quarantined_until = datetime.strptime(data, '%Y-%m-%d %H:%M:%S.%f')

            if quarantined_until < now:
                fh.close()
                os.remove(quarantine_file)
                return False
            else:
                fh.close()
                return True


def quarantine_client(time=None):
    fp = open('/tmp/quarantined.noipy', 'w')
    if time is not None:
        fp.write(time)
    fp.close()


if __name__ == '__main__':
    if is_quarantined():
        print('This client has been quarantined - exiting')
    else:
        data = get_external_ip()
        ip = parse_data_to_ip(data)
        response = update_api(ip)
        check_response(response, ip)
