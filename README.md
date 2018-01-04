# NoIpy

## General description
This script serves the purpose of updating DNS entries with noip.com

## Flaws
The current flaws include, but are not limited to:

- Printing to the terminal
- No logging
- Lookup can be done better

## Configuration
Insert values for username and password into the variables called noip_username and noip_password respectively. 

Set the host names for the hosts you need to update into the host_names list.

Example:
```python
  noip_username = 'username'
  noip_password = 'password'
  host_names = ['example.org', 'example.com', 'example.net']
```
