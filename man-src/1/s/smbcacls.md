---
title: "smbcacls(1)"
name: "smbcacls"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbcacls/"
description: "smbcacls – Set or get ACLs on an NT file or directory names"
---

<h2 class="name">NAME</h2>
<p> smbcacls &#8211; Set or get ACLs on an NT file or directory names </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>smbcacls {//server/share} {/filename} [-D|&#8211;delete acl] [-M|&#8211;modify acl] [-a|&#8211;add acl] [-S|&#8211;set acl] [-C|&#8211;chown name] [-G|&#8211;chgrp name] [-I allow|remove|copy] [&#8211;numeric] [-t] [-U username] [-d] [-e] [-m|&#8211;max-protocol LEVEL] [&#8211;query-security-info FLAGS] [&#8211;set-security-info FLAGS] [&#8211;sddl] [&#8211;domain-sid SID] [-x|&#8211;maximum-access]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The smbcacls program manipulates NT Access Control Lists (ACLs) on SMB file shares. An ACL is comprised zero or more Access Control Entries (ACEs), which define access restrictions for a specific user or group.</p>
<h2>OPTIONS</h2>
<p> The following options are available to the smbcacls program. The format of ACLs is described in the section ACL FORMAT </p>
<p> -a|&#8211;add acl</p>
<dl>
<dt>
<dd> Add the entries specified to the ACL. Existing access control entries are unchanged.</dl>
<p> -M|&#8211;modify acl</p>
<dl>
<dt>
<dd> Modify the mask value (permissions) for the ACEs specified on the command line. An error will be printed for each ACE specified that was not already present in the object&#8217;s ACL.</dl>
<p> -D|&#8211;delete acl</p>
<dl>
<dt>
<dd> Delete any ACEs specified on the command line. An error will be printed for each ACE specified that was not already present in the object&#8217;s ACL.</dl>
<p> -S|&#8211;set acl</p>
<dl>
<dt>
<dd> This command sets the ACL on the object with only what is specified on the command line. Any existing ACL is erased. Note that the ACL specified must contain at least a revision, type, owner and group for the call to succeed.</dl>
<p> -C|&#8211;chown name</p>
<dl>
<dt>
<dd> The owner of a file or directory can be changed to the name given using the <i>-C</i> option. The name can be a sid in the form S-1-x-y-z or a name resolved against the server specified in the first argument. </p>
<p> This command is a shortcut for -M OWNER:name.</dl>
<p> -G|&#8211;chgrp name</p>
<dl>
<dt>
<dd> The group owner of a file or directory can be changed to the name given using the <i>-G</i> option. The name can be a sid in the form S-1-x-y-z or a name resolved against the server specified n the first argument. </p>
<p> This command is a shortcut for -M GROUP:name.</dl>
<p> -I|&#8211;inherit allow|remove|copy</p>
<dl>
<dt>
<dd> Set or unset the windows &quot;Allow inheritable permissions&quot; check box using the <i>-I</i> option. To set the check box pass allow. To unset the check box pass either remove or copy. Remove will remove all inherited acls. Copy will copy all the inherited acls.</dl>
<p> &#8211;numeric</p>
<dl>
<dt>
<dd> This option displays all ACL information in numeric format. The default is to convert SIDs to names and ACE types and masks to a readable string format.</dl>
<p> -m|&#8211;max-protocol PROTOCOL_NAME</p>
<dl>
<dt>
<dd> This allows the user to select the highest SMB protocol level that smbcacls will use to connect to the server. By default this is set to NT1, which is the highest available SMB1 protocol. To connect using SMB2 or SMB3 protocol, use the strings SMB2 or SMB3 respectively. Note that to connect to a Windows 2012 server with encrypted transport selecting a max-protocol of SMB3 is required.</dl>
<p> -t|&#8211;test-args</p>
<dl>
<dt>
<dd> Don&#8217;t actually do anything, only validate the correctness of the arguments.</dl>
<p> &#8211;query-security-info FLAGS</p>
<dl>
<dt>
<dd> The security-info flags for queries.</dl>
<p> &#8211;set-security-info FLAGS</p>
<dl>
<dt>
<dd> The security-info flags for queries.</dl>
<p> &#8211;sddl</p>
<dl>
<dt>
<dd> Output and input acls in sddl format.</dl>
<p> &#8211;domain-sid SID</p>
<dl>
<dt>
<dd> SID used for sddl processing.</dl>
<p> -x|&#8211;maximum-access</p>
<dl>
<dt>
<dd> When displaying an ACL additionally query the server for effective maximum permissions. Note that this is only supported with SMB protocol version 2 or higher.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dt>
<dd> <i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 0. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> -V|&#8211;version</p>
<dl>
<dt>
<dd> Prints the program version number.</dl>
<p> -s|&#8211;configfile=&lt;configuration file&gt;</p>
<dl>
<dt>
<dd> The file specified contains the configuration details required by the server. The information in this file includes server-specific information such as what printcap file to use, as well as descriptions of all the services that the server is to provide. See smb.conf for more information. The default configuration file name is determined at compile time.</dl>
<p> -l|&#8211;log-basename=logdirectory</p>
<dl>
<dt>
<dd> Base directory name for log/debug files. The extension <code>&quot;.progname&quot;</code> will be appended (e.g. log.smbclient, log.smbd, etc&#8230;). The log file is never removed by the client.</dl>
<p> &#8211;option=&lt;name&gt;=&lt;value&gt;</p>
<dl>
<dt>
<dd> Set the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) option &quot;&lt;name&gt;&quot; to value &quot;&lt;value&gt;&quot; from the command line. This overrides compiled-in defaults and options read from the configuration file.</dl>
<p> -N|&#8211;no-pass</p>
<dl>
<dt>
<dd> If specified, this parameter suppresses the normal password prompt from the client to the user. This is useful when accessing a service that does not require a password. </p>
<p> Unless a password is specified on the command line or this parameter is specified, the client will request a password. </p>
<p> If a password is specified on the command line and this option is also defined the password on the command line will be silently ingnored and no password will be used.</dl>
<p> -k|&#8211;kerberos</p>
<dl>
<dt>
<dd> Try to authenticate with kerberos. Only useful in an Active Directory environment.</dl>
<p> -C|&#8211;use-ccache</p>
<dl>
<dt>
<dd> Try to use the credentials cached by winbind.</dl>
<p> -A|&#8211;authentication-file=filename</p>
<dl>
<dt>
<dd> This option allows you to specify a file from which to read the username and password used in the connection. The format of the file is </p>
<dl>
<dt>
<dd>
<pre>
username = &lt;value&gt;
password = &lt;value&gt;
domain   = &lt;value&gt;
</pre>
</dl>
<p> Make certain that the permissions on the file restrict access from unwanted users.</dl>
<p> -U|&#8211;user=username[%password]</p>
<dl>
<dt>
<dd> Sets the SMB username or username and password. </p>
<p> If %password is not specified, the user will be prompted. The client will first check the <code>USER</code> environment variable, then the <code>LOGNAME</code> variable and if either exists, the string is uppercased. If these environmental variables are not found, the username <code>GUEST</code> is used. </p>
<p> A third option is to use a credentials file which contains the plaintext of the username and password. This option is mainly provided for scripts where the admin does not wish to pass the credentials on the command line or via environment variables. If this method is used, make certain that the permissions on the file restrict access from unwanted users. See the <i>-A</i> for more details. </p>
<p> Be cautious about including passwords in scripts. Also, on many systems the command line of a running process may be seen via the ps command. To be safe always allow rpcclient to prompt for a password and type it in directly.</dl>
<p> -S|&#8211;signing on|off|required</p>
<dl>
<dt>
<dd> Set the client signing state.</dl>
<p> -P|&#8211;machine-pass</p>
<dl>
<dt>
<dd> Use stored machine account password.</dl>
<p> -e|&#8211;encrypt</p>
<dl>
<dt>
<dd> This command line parameter requires the remote server support the UNIX extensions or that the SMB3 protocol has been selected. Requests that the connection be encrypted. Negotiates SMB encryption using either SMB3 or POSIX extensions via GSSAPI. Uses the given credentials for the encryption negotiation (either kerberos or NTLMv1/v2 if given domain/username/password triple. Fails the connection if encryption cannot be negotiated.</dl>
<p> &#8211;pw-nt-hash</p>
<dl>
<dt>
<dd> The supplied password is the NT hash.</dl>
<p> -n|&#8211;netbiosname &lt;primary NetBIOS name&gt;</p>
<dl>
<dt>
<dd> This option allows you to override the NetBIOS name that Samba uses for itself. This is identical to setting the m[blue]<code>netbios name</code>m[] parameter in the smb.conf file. However, a command line setting will take precedence over settings in smb.conf.</dl>
<p> -i|&#8211;scope &lt;scope&gt;</p>
<dl>
<dt>
<dd> This specifies a NetBIOS scope that nmblookup will use to communicate with when generating NetBIOS names. For details on the use of NetBIOS scopes, see rfc1001.txt and rfc1002.txt. NetBIOS scopes are <i>very</i> rarely used, only set this parameter if you are the system administrator in charge of all the NetBIOS systems you communicate with.</dl>
<p> -W|&#8211;workgroup=domain</p>
<dl>
<dt>
<dd> Set the SMB domain of the username. This overrides the default domain which is the domain defined in smb.conf. If the domain specified is the same as the servers NetBIOS name, it causes the client to log on using the servers local SAM (as opposed to the Domain SAM).</dl>
<p> -O|&#8211;socket-options socket options</p>
<dl>
<dt>
<dd> TCP socket options to set on the client socket. See the socket options parameter in the smb.conf manual page for the list of valid options.</dl>
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message.</dl>
<h2>ACL FORMAT</h2>
<p> The format of an ACL is one or more entries separated by either commas or newlines. An ACL entry is one of the following: </p>
<dl>
<dt>
<dd>
<pre>
 
REVISION:&lt;revision number&gt;
OWNER:&lt;sid or name&gt;
GROUP:&lt;sid or name&gt;
ACL:&lt;sid or name&gt;:&lt;type&gt;/&lt;flags&gt;/&lt;mask&gt;
</pre>
</dl>
<p> The revision of the ACL specifies the internal Windows NT ACL revision for the security descriptor. If not specified it defaults to 1. Using values other than 1 may cause strange behaviour. </p>
<p> The owner and group specify the owner and group sids for the object. If a SID in the format S-1-x-y-z is specified this is used, otherwise the name specified is resolved using the server on which the file or directory resides. </p>
<p> ACEs are specified with an &quot;ACL:&quot; prefix, and define permissions granted to an SID. The SID again can be specified in S-1-x-y-z format or as a name in which case it is resolved against the server on which the file or directory resides. The type, flags and mask values determine the type of access granted to the SID. </p>
<p> The type can be either ALLOWED or DENIED to allow/deny access to the SID. The flags values are generally zero for file ACEs and either 9 or 2 for directory ACEs. Some common flags are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <code>#define SEC_ACE_FLAG_OBJECT_INHERIT 0x1</code></dl>
<dl>
<dt>
<dd> &bull; <code>#define SEC_ACE_FLAG_CONTAINER_INHERIT 0x2</code></dl>
<dl>
<dt>
<dd> &bull; <code>#define SEC_ACE_FLAG_NO_PROPAGATE_INHERIT 0x4</code></dl>
<dl>
<dt>
<dd> &bull; <code>#define SEC_ACE_FLAG_INHERIT_ONLY 0x8</code></dl>
</dl>
<p> At present, flags can only be specified as decimal or hexadecimal values. </p>
<p> The mask is a value which expresses the access right granted to the SID. It can be given as a decimal or hexadecimal value, or by using one of the following text strings which map to the NT file permissions of the same name.</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>R</i> &#8211; Allow read access</dl>
<dl>
<dt>
<dd> &bull; <i>W</i> &#8211; Allow write access</dl>
<dl>
<dt>
<dd> &bull; <i>X</i> &#8211; Execute permission on the object</dl>
<dl>
<dt>
<dd> &bull; <i>D</i> &#8211; Delete the object</dl>
<dl>
<dt>
<dd> &bull; <i>P</i> &#8211; Change permissions</dl>
<dl>
<dt>
<dd> &bull; <i>O</i> &#8211; Take ownership</dl>
</dl>
<p> The following combined permissions can be specified:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>READ</i> &#8211; Equivalent to &#8216;RX&#8217; permissions</dl>
<dl>
<dt>
<dd> &bull; <i>CHANGE</i> &#8211; Equivalent to &#8216;RXWD&#8217; permissions</dl>
<dl>
<dt>
<dd> &bull; <i>FULL</i> &#8211; Equivalent to &#8216;RWXDPO&#8217; permissions</dl>
</dl>
<h2>EXIT STATUS</h2>
<p> The smbcacls program sets the exit status depending on the success or otherwise of the operations performed. The exit status may be one of the following values. </p>
<p> If the operation succeeded, smbcacls returns and exit status of 0. If smbcacls couldn&#8217;t connect to the specified server, or there was an error getting or setting the ACLs, an exit status of 1 is returned. If there was an error parsing any command line arguments, an exit status of 2 is returned.</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> smbcacls was written by Andrew Tridgell and Tim Potter. </p>
<p> The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy. </p>
<h2>Index</h2>
