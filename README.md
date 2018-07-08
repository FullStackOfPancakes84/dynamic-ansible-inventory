# dynamic-ansible-inventory
Dynamically generating an Ansible inventory file from a generic server inventory CSV with backups

---
## Who should use this?
> * Do you have your servers listed in an spreadsheet, but too lazy to manually update your .ini file every time it changes?
> * Freaked out about breaking something?
> * Python nerd?

**This script is for you!**

Depending on how you've structured your server inventory spreadsheet, you'll probably need to tweak this code a bit. It should serve
as a great jump off point for you though! Or, y'know... you could always alter your spreadsheet to line up with the _example.csv_.

Right now, the script assumes the following column structure in your server inventory CSV

    hostname | ip | address | model | location 

# Enjoy !
    
