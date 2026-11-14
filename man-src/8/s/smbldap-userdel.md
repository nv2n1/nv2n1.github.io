---
title: "smbldap-userdel(8)"
name: "smbldap-userdel"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-userdel/"
---

smbldap-userdel - Delete a user account and related files

<h2>Synopsis</h2>

smbldap-userdel [-r] login

<h2>Description</h2>

The smbldap-userdel command modifies the system account files, deleting all entries that refer to user defined in ``login''. The named user must exist. 

 -r Files in the user's home directory will be removed along with the home directory itself. Files located in other file systems will have to be searched for and deleted manually.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-userdel/">userdel</a></i>(1) 
