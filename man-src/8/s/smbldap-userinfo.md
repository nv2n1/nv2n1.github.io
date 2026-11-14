---
title: "smbldap-userinfo(8)"
name: "smbldap-userinfo"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-userinfo/"
---

smbldap-userinfo - change user real name, information and shell

<h2>Synopsis</h2>

smbldap-userinfo [-f full_name] [-r room_no] [-w work_ph] [-h home_ph] [-o other] [-s login_shell] [-l] [-?] [-v]

<h2>Description</h2>

This command changes user gecos fields and login shell. The normal user can change only the fields for his own account, the super user may change the fiels for any account. If none of the options are selected, the command is run in an interactive mode for the current user account. User is asked for all fields. To accept a default value you should just press &lt;<font SIZE="-1">ENTER</font>&gt;, otherwise write text and press &lt;<font SIZE="-1">ENTER</font>&gt;. posixAccount objectClasses has to be present in the modified entry. If inetOrgPerson objectClass is also present additional attributes will be changed (givenName,sn,roomNumber,telephoneNumber, homePhone) -l 
&nbsp;<wbr>Display users informations and password status. -f full_name 
&nbsp;<wbr>affected attributes:&nbsp;<wbr>'gecos',&nbsp;<wbr>'cn'&nbsp;<wbr>(and&nbsp;<wbr>'givenName',&nbsp;<wbr>'sn' 
&nbsp;<wbr>if inetOrgPerson is present) -r room_number 
&nbsp;<wbr>affected attributes:&nbsp;<wbr>'gecos'&nbsp;<wbr>(and&nbsp;<wbr>'roomNumber' 
&nbsp;<wbr>if inetOrgPerson is present) -w work_phone 
&nbsp;<wbr>affected attributes:&nbsp;<wbr>'gecos'&nbsp;<wbr>(and&nbsp;<wbr>'telephoneNumber' 
&nbsp;<wbr>if inetOrgPerson is present) -h home_phone 
&nbsp;<wbr>affected attributes:&nbsp;<wbr>'gecos'&nbsp;<wbr>(and&nbsp;<wbr>'homePhone' 
&nbsp;<wbr>if inetOrgPerson is present) -o other 
&nbsp;<wbr>affected attributes:&nbsp;<wbr>'gecos' -s login_shell 
&nbsp;<wbr>affected attributes:&nbsp;<wbr>'loginShell' -? show the help message -v verbose - show modified user entry 
