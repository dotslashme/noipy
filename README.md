# NoIpy

## General description

This script was mostly done as an exercise while I'm learning Python properly, as a means to keep my skills alive, but also as a proper tool to update my host dns pointers without manual attention.

The script have several flaws, not limited to printing to the terminal, no proper logging and always assuming all went well, but it may be used or improved as one sees fit. Just don't expect me to offer support if you get into trouble.

## Configuration

Insert values for username and password into the variables called noip_username and noip_password respectively. 

Set the host names for the hosts you need to update into the host_names list.

Example:

  noip_username = 'username'
  noip_password = 'password'
  host_names = ['example.org', 'example.com', 'example.net']
