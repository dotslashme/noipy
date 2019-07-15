# NoIpy

## General description

This script serves the purpose of updating DNS entries with noip.com

## Requirements

- Python 3
- Python modules
  - requests
  - logging
  - re
  - os
  - datetime

## Flaws

The current flaws include, but are not limited to:

- Lookup can be done better

## Configuration bare metal

Insert values for username and password into the variables called noip_username and noip_password respectively. 

Set the host names for the hosts you need to update into the hostnames list.

Example:
```python
  noip_username = 'username'
  noip_password = 'password'
  noip_hostnames = ['example.org', 'server.example.org' 'example.com', 'example.net']
```

## Configuration Docker

The repository contain a Dockerfile that can be used to build an image
```bash
  docker build -t dotslashme/noipy:latest .
```

Have a look at the `docker-compose.yml` file for an example on how to use the image after build. The username / password for noip are set as docker secrets using the names:

- `noip-username`
- `noip-password`

Hostnames that should be updated are configured through the environment variable `NOIP_HOSTS`.