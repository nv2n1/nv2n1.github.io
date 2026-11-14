---
title: "smbldap-useradd(8)"
name: "smbldap-useradd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-useradd/"
---

smbldap-useradd - Create a new user

<h2>Synopsis</h2>

smbldap-useradd [-abinwPW] [-c comment] [-d home_dir] [-g initial_group] [-m [-k skeleton_dir]] [-o user_ou] [-s shell] [-t time] [-u uid] [-A canchange] [-B mustchange] [-C smbhome] [-D homedrive] [-E scriptpath] [-F profilepath] [-G group[,...]] [-H acctflags] [-M mailaddr[,...]] [-N givenname] [-O mailaddr[,...]] [-S surname] [-T mailaddr[,...]] [-X encoding] [-Z name=value[,...]] login

<h2>Description</h2>

Creating New Users The smbldap-useradd command creates a new user account using the values specified on the command line and the default values from the system and from the configuration files (in the /etc/smbldap-tools directory). 

 Without any option, the account created will be a Unix (Posix) account. The following options may be used to add information: 

 -a 
The user will have a Samba account&nbsp;<wbr>(and Unix). 

 -A 
Can change password?&nbsp;<wbr>0 if no, 1 if yes. 

 -b 
The user is an&nbsp;<wbr><font SIZE="-1">AIX</font>&nbsp;<wbr>account. 

 -B 
Must change password?&nbsp;<wbr>0 if no, 1 if yes. 

 -c ``comment'' 
The new user's comment field&nbsp;<wbr>(gecos). This option is for gecos only!&nbsp;<wbr>To set as user's full name use the -N and -S options. 

 -C sambaHomePath 
<font SIZE="-1">SMB</font>&nbsp;<wbr>home share, like&nbsp;<wbr>'\\\\PDC-SRV\\homes'. 

 -d home_dir 
The new user will be created using home_dir for the user's login directory. The default is to append the login name to userHomePrefix&nbsp;<wbr>(defined in the configuration file)&nbsp;<wbr>and use that as the login directory name. 

 -D sambaHomeDrive 
Letter associated with home share, like&nbsp;<wbr>'H:'. 

 -E sambaLogonScript 
Relative to the&nbsp;<wbr>[netlogon]&nbsp;<wbr>share&nbsp;<wbr>(<font SIZE="-1">DOS</font>&nbsp;<wbr>script to execute on login, like&nbsp;<wbr>'foo.bat'. 

 -F sambaProfilePath 
Profile directory, like&nbsp;<wbr>'\\\\PDC-SRV\\profiles\\foo'. 

 -g initial_group 
The group name or number of the user's initial login group. The group name must exist. A group number must refer to an already existing group. The default group number is defined in the configuration file&nbsp;<wbr>(defaultUserGid=``513''). 

 -G group,[...] 
A list of supplementary groups that the user is also a member of. Each group is separated from the next by a comma, with no intervening whitespace. The groups are subject to the same restrictions as the group given with the -g option. The default is for the user to belong only to the initial group. 

 -H sambaAcctFlags 
Spaces and trailing bracket are ignored&nbsp;<wbr>(samba account control bits like&nbsp;<wbr>'[<font SIZE="-1">NDHTUMWSLKI</font>]'). 

 -i 
Creates an interdomain trust account&nbsp;<wbr>(machine Workstation). A password will be asked for the trust account. 

 -k skeletonDir 
When creating the user's home directory, copy files and directories from skeletonDir rather than&nbsp;<wbr>/etc/skel. The -k option is only valid in conjunction with the -m option. The default is not to create the directory and not to copy any files. 

 -m 
The user's home directory will be created if it does not exist. The files contained in skeletonDir will be copied to the home directory if the -k option is used, otherwise the files contained in&nbsp;<wbr>/etc/skel will be used instead.&nbsp;<wbr>&nbsp;<wbr>Any directories contained in skeletonDir or&nbsp;<wbr>/etc/skel will be created in the user's home directory as well. 

 -M mail 
E-mail addresses&nbsp;<wbr>(multiple addresses are separated by commas). 

 --non-unique 
Allow the creation of a user account with a duplicate&nbsp;<wbr>(non-unique)&nbsp;<wbr><font SIZE="-1">UID.</font> 

 -n 
Do not print banner message. 

 -N givenname 
Family name. Defaults to username. 

 -o node 
The user's account will be created in the specified organizational unit. It is relative to the user suffix dn&nbsp;<wbr>($usersdn)&nbsp;<wbr>defined in the configuration file. Ex: 'ou=admin,ou=all' 

 -O localMailAddress 
localMailAddresses&nbsp;<wbr>(multiple addresses are separated by commas). 

 -P 
Ends by invoking smbldap-passwd. 

 -p 
Read password from&nbsp;<wbr><font SIZE="-1">STDIN</font>&nbsp;<wbr>without verification. 

 -s shell 
The name of the user's login shell. The default is to leave this field blank, which causes the system to select the default login shell. 

 -S surname 
Defaults to username. 

 -t time 
Wait&nbsp;<wbr>&lt;time&gt;&nbsp;<wbr>seconds before exiting script when adding computer's account. This is useful when Master/PDC and Slaves/BDCs are connected through the Internet&nbsp;<wbr>(replication is not real time). 

 -T mailToAddress 
Forward address&nbsp;<wbr>(multiple addresses are separated by commas). 

 -u uid 
The numerical value of the user's&nbsp;<wbr><font SIZE="-1">ID.</font>&nbsp;<wbr>This value must be unique, unless the --non-unique option is used. The value must be non-negative. The default is to use the smallest&nbsp;<wbr><font SIZE="-1">ID</font>&nbsp;<wbr>value greater than 1000 and greater than every other user. 

 -w/-W 
Creates an account for a Samba machine&nbsp;<wbr>(Workstation), so that it can join a sambaDomainName. Normally -w is used for adding machines through Samba but -W can be used for manual addition of samba attributes. 

 -X encoding 
Specify input encoding for givenname and surname&nbsp;<wbr>(default&nbsp;<wbr><font SIZE="-1">UTF-8</font>). 

 -Z name=value 
Specify custom&nbsp;<wbr><font SIZE="-1">LDAP</font>&nbsp;<wbr>attributes, using comma-separated name=value pairs.

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-useradd/">useradd</a></i>(1) 
