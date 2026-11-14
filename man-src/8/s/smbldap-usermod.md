---
title: "smbldap-usermod(8)"
name: "smbldap-usermod"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbldap-usermod/"
---

smbldap-usermod - Modify a user account

<h2>Synopsis</h2>

smbldap-usermod [-c gecos] [-d home_dir] [-r login_name] [-u uid] [-g gid] [-o] [-G group[,...]] [-s shell] [-N first_name] [-S surname] [-P] [-M mail[,...]] [-T mail,[..]] [--shadowExpire date/n] [--shadowMax n] [--shadowMin n] [--shadowInactive n] [--shadowWarning n] [-L] [-U] [-a] [-e expiration_date/n] [--sambaExpire date/n] [-A canchange] [-B mustchange] [-C smbhome] [-D homedrive] [-E scriptpath] [-F profilepath] [-H acctflags] [-I] [-J] [-h] login

<h2>Description</h2>

The smbldap-usermod command modifies the system account files to reflect the changes that are specified on the command line.

<h3><font SIZE="-1">UNIX</font> options</h3>

-c, --gecos gecos 
&nbsp;<wbr>The new value of the user's comment field&nbsp;<wbr>(gecos).&nbsp;<wbr>(Don't use this to modify displayName or cn. Use -N and -S options combined instead). 

 -d, --homedir home_dir 
&nbsp;<wbr>The user's new login directory. 

 -r, --rename new_user 
&nbsp;<wbr>Allow to rename a user. This option will update the dn attribute for the user. You can also update others attributes using the corresponding script options. 

 -u, --uid uid 
&nbsp;<wbr>The numerical&nbsp;<wbr>&nbsp;<wbr>value&nbsp;<wbr>&nbsp;<wbr>of&nbsp;<wbr>&nbsp;<wbr>the&nbsp;<wbr>&nbsp;<wbr>user's&nbsp;<wbr>&nbsp;<wbr><font SIZE="-1">ID.&nbsp;<wbr>&nbsp;<wbr></font>&nbsp;<wbr>This value must be unique, unless the -o option is used.&nbsp;<wbr>&nbsp;<wbr>The value must&nbsp;<wbr>&nbsp;<wbr>be&nbsp;<wbr>&nbsp;<wbr>non negative.&nbsp;<wbr>&nbsp;<wbr>Any files which the user owns&nbsp;<wbr>&nbsp;<wbr>and&nbsp;<wbr>&nbsp;<wbr>which&nbsp;<wbr>&nbsp;<wbr>are located&nbsp;<wbr>&nbsp;<wbr>in&nbsp;<wbr>&nbsp;<wbr>the directory tree rooted at the user's home directory will have the file user&nbsp;<wbr><font SIZE="-1">ID&nbsp;<wbr></font>&nbsp;<wbr>changed&nbsp;<wbr>&nbsp;<wbr>automatically.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Files outside of the user's home directory must be altered manually. 

 -o, --canBeNotUnique 
&nbsp;<wbr>uidNumber can be non unique 

 -g, --gid initial_group 
&nbsp;<wbr>The group name or number of the user's new initial login&nbsp;<wbr>&nbsp;<wbr>group. The&nbsp;<wbr>&nbsp;<wbr>group&nbsp;<wbr>&nbsp;<wbr>name&nbsp;<wbr>&nbsp;<wbr>must&nbsp;<wbr>&nbsp;<wbr>exist. A group number must refer to an already existing group.&nbsp;<wbr>&nbsp;<wbr>The default group number is 1. 

 -G, --group [+-]group,[...] 
&nbsp;<wbr>A list of supplementary groups which the user is also&nbsp;<wbr>&nbsp;<wbr>a&nbsp;<wbr>&nbsp;<wbr>member of.&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Each&nbsp;<wbr>&nbsp;<wbr>group is separated from the next by a comma, with no intervening whitespace.&nbsp;<wbr>&nbsp;<wbr>The groups&nbsp;<wbr>&nbsp;<wbr>are&nbsp;<wbr>&nbsp;<wbr>subject&nbsp;<wbr>&nbsp;<wbr>to&nbsp;<wbr>&nbsp;<wbr>the&nbsp;<wbr>&nbsp;<wbr>same restrictions as the group given with the -g option.&nbsp;<wbr>&nbsp;<wbr>If the user is currently a member of a group which is not listed, the user will be removed from the group, unless the&nbsp;<wbr>'+'&nbsp;<wbr>or&nbsp;<wbr>'-'&nbsp;<wbr>caracter is used to add or remove groups to inital ones. 

 -s, --shel shell 
&nbsp;<wbr>The name of the user's new login shell.&nbsp;<wbr>&nbsp;<wbr>Setting this&nbsp;<wbr>&nbsp;<wbr>field&nbsp;<wbr>&nbsp;<wbr>to blank causes the system to select the default 
&nbsp;<wbr>login shell. 

 -N, --givenName 
&nbsp;<wbr>set the user's given name&nbsp;<wbr>(attribute givenName). Additionally used to set the first name in displayName and cn. 

 -S, --surname 
&nbsp;<wbr>Set the user's surname&nbsp;<wbr>(attribute sn). Additionally used to set the last name in displayName and cn. 

 -P 
&nbsp;<wbr>End by invoking smbldap-passwd to change the user password&nbsp;<wbr>(both unix and samba passwords) 

 -M, --mailAddresses mail,[...] 
&nbsp;<wbr>mailAddresses&nbsp;<wbr>(comma seperated) 

 -T, --mailToAddress mail,[...] 
&nbsp;<wbr>mailToAddress&nbsp;<wbr>(forward address)&nbsp;<wbr>(comma seperated) 

 --shadowExpire &lt;YYYY-MM-DD/n&gt; 
&nbsp;<wbr>Set the expiration date for the user password. This only affect unix account. The date may be specified as either YYYY-MM-DD or&nbsp;<wbr>'n'&nbsp;<wbr>days from day. The&nbsp;<wbr>'n'&nbsp;<wbr>syntax also supports the extended format&nbsp;<wbr>(#y)(#m)(#d)&nbsp;<wbr>for years, months, and days from today. One need not specify all three, so all of the following are examples of valid input:&nbsp;<wbr>'5y4m2d'&nbsp;<wbr>(5 years, 4 months, and 2 days),&nbsp;<wbr>'5y'&nbsp;<wbr>(5 years),&nbsp;<wbr>'5y2d'&nbsp;<wbr>(5 years and 2 days), and&nbsp;<wbr>'3'&nbsp;<wbr>(3 days). This option calls the internal&nbsp;<wbr>'timelocal'&nbsp;<wbr>command to set calculate the number of seconds from Junary 1 1970 to the specified date. 

 --shadowMax &lt;n&gt; 
&nbsp;<wbr>User must change the password, at least, every&nbsp;<wbr>'n'&nbsp;<wbr>days 

 --shadowMin &lt;n&gt; 
&nbsp;<wbr>User must wait&nbsp;<wbr>'n'&nbsp;<wbr>days once the password has changed before changing it again 

 --shadowInactive &lt;n&gt; 
&nbsp;<wbr>Number of days of inactivity allowed for the specified user 

 --shadowWarning &lt;n&gt; 
&nbsp;<wbr>User is warned that the password must be changed four days before the password expires 

 -L, --shadowLock 
&nbsp;<wbr>Lock unix user's password. This puts a&nbsp;<wbr>'!'&nbsp;<wbr>in front of the encrypted password, effectively disabling the password. 

 -U, --shadowUnlock 
&nbsp;<wbr>Unlock unix user's password. This removes the&nbsp;<wbr>'!'&nbsp;<wbr>in front of the encrypted password.

<h3><font SIZE="-1">SAMBA</font> options</h3>

-a, --addsambaSAMAccount 
&nbsp;<wbr>Add the sambaSAMAccount objectclass to the specified user account. This allow the user to become a samba user. 

 -e, --expire &lt;<font SIZE="-1">YYYY-MM-DD</font>(<font SIZE="-1">HH:MM:SS</font>)/n&gt; 
&nbsp;<wbr>Sets the expiration for both samba&nbsp;<wbr>(--sambaExpire)&nbsp;<wbr>and shadow&nbsp;<wbr>(--shadowExpire). 

 --ou node 
&nbsp;<wbr>The user's account will be moved to the specified organazional unit. It is relative to the user suffix dn&nbsp;<wbr>($usersdn)&nbsp;<wbr>defined in the configuration file. 
&nbsp;<wbr>Ex:&nbsp;<wbr>'ou=admin,ou=all' 

 --sambaExpire &lt;<font SIZE="-1">YYYY-MM-DD</font> HH:MM:SS/n&gt; 
&nbsp;<wbr>Set the expiration date for the user account. This only affects the samba account. The date must be in the following format: YYYY-MM-DD&nbsp;<wbr><font SIZE="-1">HH:MM:SS.</font>&nbsp;<wbr>The n-days format of shadowExpire is also supported. This option uses the internal&nbsp;<wbr>'timelocal'&nbsp;<wbr>command to set calculate the number of seconds from Junary 1 1970 to the specified date. 

 -A, --sambaPwdCanChange 
&nbsp;<wbr>can change password&nbsp;<wbr>?&nbsp;<wbr>0 if no, 1 if yes 

 -B, --sambaPwdMustChange 
&nbsp;<wbr>must change password&nbsp;<wbr>?&nbsp;<wbr>0 if no, 1 if yes 

 -C, --sambaHomePath path 
&nbsp;<wbr>sambaHomePath&nbsp;<wbr>(<font SIZE="-1">SMB</font>&nbsp;<wbr>home share, like&nbsp;<wbr>'\\\\PDC-SRV\\homes') 

 -D, --sambaHomeDrive drive 
&nbsp;<wbr>sambaHomeDrive&nbsp;<wbr>(letter associated with home share, like&nbsp;<wbr>'H:') 

 -E, --sambaLogonScript script 
&nbsp;<wbr>sambaLogonScript, relative to the&nbsp;<wbr>[netlogon]&nbsp;<wbr>share&nbsp;<wbr>(<font SIZE="-1">DOS</font>&nbsp;<wbr>script to execute on login, like&nbsp;<wbr>'foo.bat') 

 -F, --sambaProfilePath path 
&nbsp;<wbr>sambaProfilePath&nbsp;<wbr>(profile directory, like&nbsp;<wbr>'\\\\PDC-SRV\\profiles\\foo') 

 -H, --sambaAcctFlags flags 
&nbsp;<wbr>sambaAcctFlags, spaces and trailing bracket are ignored&nbsp;<wbr>(samba account control bits like&nbsp;<wbr>'[<font SIZE="-1">NDHTUMWSLKI</font>]') 

 -I, --sambaDisable 
&nbsp;<wbr>disable user. Can't be used with -H or -J 

 -J, --sambaEnable 
&nbsp;<wbr>enable user. Can't be used with -H or -I 

 -h, --help 
&nbsp;<wbr>print this help

<h2>See Also</h2>

<i><a HREF="/docs/linux/man/1-usermod/">usermod</a></i>(1) 
