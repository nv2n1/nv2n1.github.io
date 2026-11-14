---
title: "smbldap-groupmod(8)"
name: "smbldap-groupmod"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-groupmod/"
---

smbldap-groupmod - Modify a group

<h2>Synopsis</h2>

smbldap-groupmod [-g gid [-o]] [-a] [-r rid] [-s sid] [-t group type] [-n group_name ] [-m members(,)] [-x members (,)] group

<h2>Description</h2>

The smbldap-groupmod command modifies the system account files to reflect the changes that are specified on the command line. The options which apply to the smbldap-groupmod command are 

 -g gid The numerical value of the group's <font SIZE="-1">ID.</font> This value must be unique, unless the -o option is used. The value must be non negative. Any files which the old group <font SIZE="-1">ID</font> is the file roup <font SIZE="-1">ID</font> must have the file group <font SIZE="-1">ID</font> changed manually. 

 -n group_name 
The name of the group will be changed from group to group_name. 

 -m members 
The members to be added to the group in comma-delimeted form. 

 -x members 
The members to be removed from the group in comma-delimted form. 

 -a 
add an automatic Security&nbsp;<wbr><font SIZE="-1">ID</font>&nbsp;<wbr>for the group&nbsp;<wbr>(<font SIZE="-1">SID</font>). 

 -s sid 
set the group&nbsp;<wbr><font SIZE="-1">SID. 
&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>The&nbsp;<wbr><font SIZE="-1">SID</font>&nbsp;<wbr>must be unique and defined with the domain Security&nbsp;<wbr><font SIZE="-1">ID&nbsp;<wbr></font>($SID)&nbsp;<wbr>like sid=$SID-rid where rid is the group rid. 

 -r rid 
set the group rid. 
The&nbsp;<wbr><font SIZE="-1">SID</font>&nbsp;<wbr>is then calculated as sid=$SID-rid where&nbsp;<wbr><tt>$SID</tt>&nbsp;<wbr>is the domain Security&nbsp;<wbr><font SIZE="-1">ID.</font> 

 -t group type 
set the&nbsp;<wbr><font SIZE="-1">NT</font>&nbsp;<wbr>Group type for the new group. Available values are 2&nbsp;<wbr>(domain group), 4&nbsp;<wbr>(local group)&nbsp;<wbr>and 5&nbsp;<wbr>(builtin group). The default group type is 2.

<h2>Examples</h2>

smbldap-groupmod -g 253 development This will change the <font SIZE="-1">GID</font> of the 'development' group to '253'. 

 smbldap-groupmod -n Idiots Managers This will change the name of the 'Managers' group to 'Idiots'. 

 smbldap-groupmod -m ``jdoe,jsmith'' ``Domain Admins'' This will add 'jdoe' and 'jsmith' to the 'Domain Admins' group. 

 smbldap-groupmod -x ``jdoe,jsmith'' ``Domain Admins'' This will remove 'jdoe' and 'jsmith' from the 'Domain Admins' group.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-groupmod/">groupmod</a></i>(1) 
