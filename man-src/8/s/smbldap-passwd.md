---
title: "smbldap-passwd(8)"
name: "smbldap-passwd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-passwd/"
---

smbldap-passwd - change user password

<h2>Synopsis</h2>

smbldap-passwd [-?|--help|-s|-u] [name]

<h2>Description</h2>

smbldap-passwd changes passwords for user accounts. A normal user may only change the password for their own account, the super user may change the password for any account. 

 If option -s specified then changed only samba password. If options -u specified then changed only <font SIZE="-1">UNIX</font> password. With no options then changed both - <font SIZE="-1">UNIX</font> and samba passwords. 

 Password Changes The user is first prompted for their old password, if one is present. This password is then tested against the stored password by binding to the server. The user has only one chance to enter the correct passwword. The super user is permitted to bypass this step so that forgotten passwords may be changed. The user is then prompted for a replacement password. As a general guideline, passwords should consist of 6 to 8 characters including one or more from each of following sets: 

 Lower case alphabetics 

 Upper case alphabetics 

 Digits 0 thru 9 

 Punctuation marks 

 Password will prompt again and compare the second entry against the first. Both entries are require to match in order for the password to be changed.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-passwd/">passwd</a></i>(1) 
