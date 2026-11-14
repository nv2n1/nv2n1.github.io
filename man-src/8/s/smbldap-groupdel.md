---
title: "smbldap-groupdel(8)"
name: "smbldap-groupdel"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-groupdel/"
---

smbldap-groupdel - Delete a group

<h2>Synopsis</h2>

smbldap-groupdel group

<h2>Description</h2>

The smbldap-groupdel command modifies the system account files, deleting all entries that refer to a group. The named group must exist. 

 You must manually check all filesystems to insure that no files remain with the named group as the file group <font SIZE="-1">ID.</font>

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-groupdel/">groupdel</a></i>(1) 
