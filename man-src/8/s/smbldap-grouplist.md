---
title: "smbldap-grouplist(8)"
name: "smbldap-grouplist"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-grouplist/"
---

smbldap-grouplist - list groups

<h2>Synopsis</h2>

smbldap-grouplist [-S] [group template]

<h2>Description</h2>

-d Show displayName 

 -S Show samba <font SIZE="-1">SID</font> entry 

 -? show the help message

<h2>Example</h2>

smbldap-grouplist -dS smbldap-grouplist ``*ourn*'' 
