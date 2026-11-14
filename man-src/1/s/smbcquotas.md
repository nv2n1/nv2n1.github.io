---
title: "smbcquotas(1)"
name: "smbcquotas"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbcquotas/"
description: "smbcquotas – Set or get QUOTAs of NTFS 5 shares"
---

<h2 class="name">NAME</h2>
<p> smbcquotas &#8211; Set or get QUOTAs of NTFS 5 shares </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>smbcquotas {//server/share} [-u|&#8211;user user] [-L|&#8211;list] [-F|&#8211;fs] [-S|&#8211;set QUOTA_SET_COMMAND] [-n|&#8211;numeric] [-t|&#8211;test-args] [-v|&#8211;verbose] [-d debuglevel] [-s configfile] [-l logdir] [-V] [-U username] [-m|&#8211;max-protocol LEVEL] [-N] [-k] [-A]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> The smbcquotas program manipulates NT Quotas on SMB file shares.</p>
<h2>OPTIONS</h2>
<p> The following options are available to the smbcquotas program. </p>
<p> -u|&#8211;user user</p>
<dl>
<dt>
<dd> Specifies the user of whom the quotas are get or set. By default the current user&#8217;s username will be used.</dl>
<p> -L|&#8211;list</p>
<dl>
<dt>
<dd> Lists all quota records of the share.</dl>
<p> -F|&#8211;fs</p>
<dl>
<dt>
<dd> Show the share quota status and default limits.</dl>
<p> -S|&#8211;set QUOTA_SET_COMMAND</p>
<dl>
<dt>
<dd> This command sets/modifies quotas for a user or on the share, depending on the QUOTA_SET_COMMAND parameter which is described later.</dl>
<p> -n|&#8211;numeric</p>
<dl>
<dt>
<dd> This option displays all QUOTA information in numeric format. The default is to convert SIDs to names and QUOTA limits to a readable string format.</dl>
<p> -m|&#8211;max-protocol PROTOCOL_NAME</p>
<dl>
<dt>
<dd> This allows the user to select the highest SMB protocol level that smbcquotas will use to connect to the server. By default this is set to NT1, which is the highest available SMB1 protocol. To connect using SMB2 or SMB3 protocol, use the strings SMB2 or SMB3 respectively.</dl>
<p> -t|&#8211;test-args</p>
<dl>
<dt>
<dd> Don&#8217;t actually do anything, only validate the correctness of the arguments.</dl>
<p> -v|&#8211;verbose</p>
<dl>
<dt>
<dd> Be verbose.</dl>
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
<p> -?|&#8211;help</p>
<dl>
<dt>
<dd> Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dt>
<dd> Display brief usage message.</dl>
<h2>QUOTA_SET_COMMAND</h2>
<p> The format of an the QUOTA_SET_COMMAND is an operation name followed by a set of parameters specific to that operation. </p>
<p> To set user quotas for the user specified by -u or for the current username: </p>
<p> <code> UQLIM:&lt;username&gt;:&lt;softlimit&gt;/&lt;hardlimit&gt; </code> </p>
<p> To set the default quotas for a share: </p>
<p> <code> FSQLIM:&lt;softlimit&gt;/&lt;hardlimit&gt; </code> </p>
<p> To change the share quota settings: </p>
<p> <code> FSQFLAGS:QUOTA_ENABLED/DENY_DISK/LOG_SOFTLIMIT/LOG_HARD_LIMIT </code> </p>
<p> All limits are specified as a number of bytes.</p>
<h2>EXIT STATUS</h2>
<p> The smbcquotas program sets the exit status depending on the success or otherwise of the operations performed. The exit status may be one of the following values. </p>
<p> If the operation succeeded, smbcquotas returns an exit status of 0. If smbcquotas couldn&#8217;t connect to the specified server, or when there was an error getting or setting the quota(s), an exit status of 1 is returned. If there was an error parsing any command line arguments, an exit status of 2 is returned.</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> smbcquotas was written by Stefan Metzmacher. </p>
<h2>Index</h2>
