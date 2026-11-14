---
title: "pdbedit(8)"
name: "pdbedit"
section: "8"
letter: "p"
url: "/docs/linux/man/8-pdbedit/"
description: "pdbedit – manage the SAM database (Database of Samba Users)"
---

<p>pdbedit &#8211; manage the SAM database (Database of Samba Users)</p>
<h2>Synopsis</h2>
<dl>
<dd>pdbedit [-a] [-b passdb-backend] [-c account-control] [-C value] [-d debuglevel] [-D drive] [-e passdb-backend] [-f fullname] [&#8211;force-initialized-passwords] [-g] [-h homedir] [-i passdb-backend] [-I domain] [-K] [-L] [-m] [-M SID|RID] [-N description] [-P account-policy] [-p profile] [&#8211;policies-reset] [-r] [-s configfile] [-S script] [&#8211;set-nt-hash] [-t] [&#8211;time-format] [-u username] [-U SID|RID] [-v] [-V] [-w] [-x] [-y] [-z] [-Z]</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The pdbedit program is used to manage the users accounts stored in the sam database and can only be run by root. </p>
<p> The pdbedit tool uses the passdb modular interface and is independent from the kind of users database used (currently there are smbpasswd, ldap, nis+ and tdb based and more can be added without changing the tool). </p>
<p> There are five main ways to use pdbedit: adding a user account, removing a user account, modifying a user account, listing user accounts, importing users accounts.</p>
<h2>Options</h2>
<p>-L|&#8211;list</p>
<dl>
<dd>This option lists all the user accounts present in the users database. This option prints a list of user/uid pairs separated by the &#8216;:&#8217; character. </p>
<p> Example: pdbedit -L </p>
<dl>
<dd>
<pre>sorce:500:Simo Sorce
samba:45:Test User</pre>
</dl>
</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dd>This option enables the verbose listing format. It causes pdbedit to list the users in the database, printing out the account fields in a descriptive format. Used together with -w also shows passwords hashes. </p>
<p> Example: pdbedit -L -v </p>
<dl>
<dd>
<pre>---------------
username: sorce
user ID/Group: 500/500
user RID/GRID: 2000/2001
Full Name: Simo Sorce
Home Directory: \BERSERKER\sorce
HomeDir Drive: H:
Logon Script: \BERSERKER
etlogon\sorce.bat
Profile Path: \BERSERKER\profile
---------------
username: samba
user ID/Group: 45/45
user RID/GRID: 1090/1091
Full Name: Test User
Home Directory: \BERSERKER\samba
HomeDir Drive: 
Logon Script: 
Profile Path: \BERSERKER\profile</pre>
</dl>
</dl>
<p> -w|&#8211;smbpasswd-style</p>
<dl>
<dd>This option sets the &quot;smbpasswd&quot; listing format. It will make pdbedit list the users in the database, printing out the account fields in a format compatible with the smbpasswd file format. (see the <code><a href="/docs/linux/man/5-smbpasswd/">smbpasswd</a></code>(5) for details). Instead used together with (-v) displays the passwords hashes in verbose output. </p>
<p> Example: pdbedit -L -w </p>
<dl>
<dd>
<pre>sorce:500:508818B733CE64BEAAD3B435B51404EE:
 D2A2418EFC466A8A0F6B1DBB5C3DB80C:
 [UX ]:LCT-00000000:
samba:45:0F2B255F7B67A7A9AAD3B435B51404EE:
 BC281CE3F53B6A5146629CD4751D3490:
 [UX ]:LCT-3BFA1E8D:</pre>
</dl>
</dl>
<p> -u|&#8211;user username</p>
<dl>
<dd>This option specifies the username to be used for the operation requested (listing, adding, removing). It is <i>required</i> in add, remove and modify operations and <i>optional</i> in list operations.</dl>
<p> -f|&#8211;fullname fullname</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the user&#8217;s full name. </p>
<p> Example: -f &quot;Simo Sorce&quot;</dl>
<p> -h|&#8211;homedir homedir</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the user&#8217;s home directory network path. </p>
<p> Example: -h &quot;\\BERSERKER\sorce&quot;</dl>
<p> -D|&#8211;drive drive</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the windows drive letter to be used to map the home directory. </p>
<p> Example: -D &quot;H:&quot;</dl>
<p> -S|&#8211;script script</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the user&#8217;s logon script path. </p>
<p> Example: -S &quot;\\BERSERKER\netlogon\sorce.bat&quot;</dl>
<p> &#8211;set-nt-hash</p>
<dl>
<dd>This option can be used while modifying a user account. It will set the user&#8217;s password using the nt-hash value given as hexadecimal string. Useful to synchronize passwords. </p>
<p> Example: &#8211;set-nt-hash 8846F7EAEE8FB117AD06BDD830B7586C</dl>
<p> -p|&#8211;profile profile</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the user&#8217;s profile directory. </p>
<p> Example: -p &quot;\\BERSERKER\netlogon&quot;</dl>
<p> -M|&#8217;&#8211;machine SID&#8217; SID|rid</p>
<dl>
<dd>This option can be used while adding or modifying a machine account. It will specify the machines&#8217; new primary group SID (Security Identifier) or rid. </p>
<p> Example: -M S-1-5-21-2447931902-1787058256-3961074038-1201</dl>
<p> -U|&#8217;&#8211;user SID&#8217; SID|rid</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the users&#8217; new SID (Security Identifier) or rid. </p>
<p> Example: -U S-1-5-21-2447931902-1787058256-3961074038-5004 </p>
<p> Example: &#8216;&#8211;user SID&#8217; S-1-5-21-2447931902-1787058256-3961074038-5004 </p>
<p> Example: -U 5004 </p>
<p> Example: &#8216;&#8211;user SID&#8217; 5004</dl>
<p> -c|&#8211;account-control account-control</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the users&#8217; account control property. Possible flags are listed below. </p>
<dl>
<dd>&bull; N: No password required</dl>
<dl>
<dd>&bull; D: Account disabled</dl>
<dl>
<dd>&bull; H: Home directory required</dl>
<dl>
<dd>&bull; T: Temporary duplicate of other account</dl>
<dl>
<dd>&bull; U: Regular user account</dl>
<dl>
<dd>&bull; M: MNS logon user account</dl>
<dl>
<dd>&bull; W: Workstation Trust Account</dl>
<dl>
<dd>&bull; S: Server Trust Account</dl>
<dl>
<dd>&bull; L: Automatic Locking</dl>
<dl>
<dd>&bull; X: Password does not expire</dl>
<dl>
<dd>&bull; I: Domain Trust Account</dl>
</dl>
<p> Example: -c &quot;[X ]&quot; </p>
<p> -K|&#8211;kickoff-time</p>
<dl>
<dd>This option is used to modify the kickoff time for a certain user. Use &quot;never&quot; as argument to set the kickoff time to unlimited. </p>
<p> Example: pdbedit -K never user</dl>
<p> -a|&#8211;create</p>
<dl>
<dd>This option is used to add a user into the database. This command needs a user name specified with the -u switch. When adding a new user, pdbedit will also ask for the password to be used. </p>
<p> Example: pdbedit -a -u sorce </p>
<dl>
<dd>
<pre>new password:
retype new password</pre>
</dl>
<dl>
<dd><font SIZE="+1"> <code>Note</code> </font><br />
 pdbedit does not call the unix password synchronization script if m[blue]<code>unix password sync</code>m[] has been set. It only updates the data in the Samba user database. </p>
<p> If you wish to add a user and synchronise the password that immediately, use smbpasswd&#8217;s <code>-a</code> option. </p>
</dl>
</dl>
<p> -t|&#8211;password-from-stdin</p>
<dl>
<dd>This option causes pdbedit to read the password from standard input, rather than from /dev/tty (like the <a href="/docs/linux/man/1-passwd/">passwd</a>(1) program does). The password has to be submitted twice and terminated by a newline each.</dl>
<p> -r|&#8211;modify</p>
<dl>
<dd>This option is used to modify an existing user in the database. This command needs a user name specified with the -u switch. Other options can be specified to modify the properties of the specified user. This flag is kept for backwards compatibility, but it is no longer necessary to specify it.</dl>
<p> -m|&#8211;machine</p>
<dl>
<dd>This option may only be used in conjunction with the <i>-a</i> option. It will make pdbedit to add a machine trust account instead of a user account (-u username will provide the machine name). </p>
<p> Example: pdbedit -a -m -u w2k-wks</dl>
<p> -x|&#8211;delete</p>
<dl>
<dd>This option causes pdbedit to delete an account from the database. It needs a username specified with the -u switch. </p>
<p> Example: pdbedit -x -u bob</dl>
<p> -i|&#8211;import passdb-backend</p>
<dl>
<dd>Use a different passdb backend to retrieve users than the one specified in smb.conf. Can be used to import data into your local user database. </p>
<p> This option will ease migration from one passdb backend to another. </p>
<p> Example: pdbedit -i smbpasswd:/etc/smbpasswd.old</dl>
<p> -e|&#8211;export passdb-backend</p>
<dl>
<dd>Exports all currently available users to the specified password database backend. </p>
<p> This option will ease migration from one passdb backend to another and will ease backing up. </p>
<p> Example: pdbedit -e smbpasswd:/root/samba-users.backup</dl>
<p> -g|&#8211;group</p>
<dl>
<dd>If you specify <i>-g</i>, then <i>-i in-backend -e out-backend</i> applies to the group mapping instead of the user database. </p>
<p> This option will ease migration from one passdb backend to another and will ease backing up.</dl>
<p> -b|&#8211;backend passdb-backend</p>
<dl>
<dd>Use a different default passdb backend. </p>
<p> Example: pdbedit -b xml:/root/pdb-backup.xml -l</dl>
<p> -P|&#8211;account-policy account-policy</p>
<dl>
<dd>Display an account policy </p>
<p> Valid policies are: minimum password age, reset count minutes, disconnect time, user must logon to change password, password history, lockout duration, min password length, maximum password age and bad lockout attempt. </p>
<p> Example: pdbedit -P &quot;bad lockout attempt&quot; </p>
<dl>
<dd>
<pre>account policy value for bad lockout attempt is 0</pre>
</dl>
</dl>
<p> -C|&#8211;value account-policy-value</p>
<dl>
<dd>Sets an account policy to a specified value. This option may only be used in conjunction with the <i>-P</i> option. </p>
<p> Example: pdbedit -P &quot;bad lockout attempt&quot; -C 3 </p>
<dl>
<dd>
<pre>account policy value for bad lockout attempt was 0
account policy value for bad lockout attempt is now 3</pre>
</dl>
</dl>
<p> -y|&#8211;policies</p>
<dl>
<dd>If you specify <i>-y</i>, then <i>-i in-backend -e out-backend</i> applies to the account policies instead of the user database. </p>
<p> This option will allow one to migrate account policies from their default tdb-store into a passdb backend, e.g. an LDAP directory server. </p>
<p> Example: pdbedit -y -i tdbsam: -e ldapsam:<a href="ldap://my.ldap.host">ldap://my.ldap.host</a></dl>
<p> &#8211;force-initialized-passwords</p>
<dl>
<dd>This option forces all users to change their password upon next login.</dl>
<p> -N|&#8211;account-desc description</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the user&#8217;s description field. </p>
<p> Example: -N &quot;test description&quot;</dl>
<p> -Z|&#8211;logon-hours-reset</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will reset the user&#8217;s allowed logon hours. A user may login at any time afterwards. </p>
<p> Example: -Z</dl>
<p> -z|&#8211;bad-password-count-reset</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will reset the stored bad login counter from a specified user. </p>
<p> Example: -z</dl>
<p> &#8211;policies-reset</p>
<dl>
<dd>This option can be used to reset the general password policies stored for a domain to their default values. </p>
<p> Example: &#8211;policies-reset</dl>
<p> -I|&#8211;domain</p>
<dl>
<dd>This option can be used while adding or modifying a user account. It will specify the user&#8217;s domain field. </p>
<p> Example: -I &quot;MYDOMAIN&quot;</dl>
<p> &#8211;time-format</p>
<dl>
<dd>This option is currently not being used.</dl>
<p> -?|&#8211;help</p>
<dl>
<dd>Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dd>Display brief usage message.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dd><i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 0. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -V|&#8211;version</p>
<dl>
<dd>Prints the program version number.</dl>
<p> -s|&#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dd>The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dl>
<p> -l|&#8211;log-basename=logdirectory</p>
<dl>
<dd>Base directory name for log/debug files. The extension <code>&quot;.progname&quot;</code> will be appended (e.g. log.smbclient, log.smbd, etc&#8230;). The log file is never removed by the client.</dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dd>Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dl>
<h2>Notes</h2>
<p>This command may be used only by root.</p>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-smbpasswd/">smbpasswd</a></code>(5), <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7)</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The pdbedit manpage was written by Simo Sorce and Jelmer Vernooij.</p>
