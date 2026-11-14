---
title: "smbldap-populate(8)"
name: "smbldap-populate"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-populate/"
---

smbldap-populate - Populate your LDAP database

<h2>Synopsis</h2>

smbldap-populate [ldif-file]

<h2>Description</h2>

The smbldap-populate command helps to populate an <font SIZE="-1">LDAP</font> server by adding the necessary entries : base suffix (doesn't abort if already there), organizational units for users, groups and computers, builtin users : Administrator and guest, builtin groups (though posixAccount only, no SambaTNG support). 

 -a name Your local administrator login name (default: root) 

 -b name Your local guest login name (default: nobody) 

 -e file export an ldif file 

 -i file import an ldif file (Options -a and -b will be ignored)

<h2>Files</h2>

/etc/smbldap-tools/smbldap.conf : main configuration /etc/smbldap-tools/smbldap_bind.conf : credentials for binding to the directory

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/5-smb-conf/">smb.conf</a></i>(5) 
