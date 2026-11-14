---
title: "smbldap-groupadd(8)"
name: "smbldap-groupadd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-groupadd/"
---

smbldap-groupadd - Create a new group

<h2>Synopsis</h2>

smbldap-groupadd [-g gid ] [-a] [-o] [-r rid] [-s sid] [-t group type] [-p] group

<h2>Description</h2>

The smbldap-groupadd command creates a new group account using the values specified on the command line and the default values from the configuration file. The new group will be entered into the system files as needed. Available options are : 

 -g gid 
The numerical value of the group's&nbsp;<wbr><font SIZE="-1">ID.</font>&nbsp;<wbr>This value must be 
unique, unless the -o option is used. The value must be non- 
negative. The default is to use the smallest&nbsp;<wbr><font SIZE="-1">ID</font>&nbsp;<wbr>value greater 
than 1000 and greater than every other group. 

 -a 
add an automatic Security&nbsp;<wbr><font SIZE="-1">ID</font>&nbsp;<wbr>for the group&nbsp;<wbr>(<font SIZE="-1">SID</font>). 

 -b 
the group is also a&nbsp;<wbr><font SIZE="-1">AIX</font>&nbsp;<wbr>group 

 -o 
gid is not unique 

 -p 
print the gidNumber to stdout 

 -s sid 
set the group&nbsp;<wbr><font SIZE="-1">SID. 
&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>The&nbsp;<wbr><font SIZE="-1">SID</font>&nbsp;<wbr>must be unique and defined with the domain Security&nbsp;<wbr><font SIZE="-1">ID 
</font>($SID)&nbsp;<wbr>like sid=$SID-rid where rid is the group rid. 

 -r rid 
set the group rid. 
The&nbsp;<wbr><font SIZE="-1">SID</font>&nbsp;<wbr>is then calculated as sid=$SID-rid where&nbsp;<wbr><tt>$SID</tt>&nbsp;<wbr>is the 
domain Security&nbsp;<wbr><font SIZE="-1">ID.</font> 

 -t group type 
set the&nbsp;<wbr><font SIZE="-1">NT</font>&nbsp;<wbr>Group type for the new group. Available values are 
2&nbsp;<wbr>(domain group), 4&nbsp;<wbr>(local group)&nbsp;<wbr>and 5&nbsp;<wbr>(builtin group). 
The default group type is 2.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-groupadd/">groupadd</a></i>(1) 
