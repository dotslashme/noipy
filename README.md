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

## Configuration
Insert values for username and password into the variables called noip_username and noip_password respectively. 

Set the host names for the hosts you need to update into the hostnames list.

Example:
```python
  noip_username = 'username'
  noip_password = 'password'
  noip_hostnames = ['example.org', 'server.example.org' 'example.com', 'example.net']
```
