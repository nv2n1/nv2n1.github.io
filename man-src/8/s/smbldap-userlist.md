---
title: "smbldap-userlist(8)"
name: "smbldap-userlist"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-userlist/"
---

smbldap-userlist - list users or machines with some info

<h2>Synopsis</h2>

smbldap-userlist [-a] [-g] [-d] [-e] [-l] [-m] [user template]

<h2>Description</h2>

-a Show gecos, password last change, expiration date and account status 

 -g Show gecos entry 

 -d Show last modification password date 

 -e Show the expiration date 

 -l Show account status (locl/unlock) 

 -m Only list machines 

 -u Only list users 

 -? show the help message

<h2>Example</h2>

smbldap-userlist -a smbldap-userlist -a jtournier smbldap-userlist -a ``*ourn*'' 
