---
title: "samba-regedit(8)"
name: "samba-regedit"
section: "8"
letter: "s"
url: "/docs/linux/man/8-samba-regedit/"
description: "samba-regedit – ncurses based tool to manage the Samba registry"
---

<p>samba-regedit &#8211; ncurses based tool to manage the Samba registry</p>
<h2>Synopsis</h2>
<dl>
<dd>samba-regedit [&#8211;help] [&#8211;usage] [-d&nbsp;&lt;debug level&gt;] [-s&nbsp;&lt;configuration file&gt;] [-l&nbsp;&lt;log directory&gt;] [-V] [&#8211;option=&lt;parameter&gt;=&lt;value&gt;] [&#8211;socket-options=&lt;SOCKETOPTIONS&gt;] [&#8211;netbiosname=&lt;NETBIOSNAME&gt;] [&#8211;workgroup=&lt;WORKGROUP&gt;] [&#8211;scope=&lt;SCOPE&gt;] [&#8211;user=&lt;USERNAME&gt;] [-N] [-k] [&#8211;authentication-file=&lt;FILE&gt;] [&#8211;signing=[on|off|required]] [-P] [-e] [-C] [&#8211;pw-nt-hash]</dl>
<h2>Description</h2>
<p>This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> samba-regedit is a ncurses based tool to manage the Samba registry. It can be used to show/edit registry keys/subkeys and their values.</p>
<h2>Options</h2>
<p>-?|&#8211;help</p>
<dl>
<dd>Print a summary of command line options.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dd><i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 1. </p>
<p> The higher this value, the more detail will be logged to the log files about the activities of the server. At level 0, only critical errors and serious warnings will be logged. Level 1 is a reasonable level for day-to-day running &#8211; it generates a small amount of information about operations carried out. </p>
<p> Levels above 1 will generate considerable amounts of log data, and should only be used when investigating a problem. Levels above 3 are designed for use only by developers and generate HUGE amounts of log data, most of which is extremely cryptic. </p>
<p> Note that specifying this parameter here will override the m[blue]<code>log level</code>m[] parameter in the smb.conf file.</dl>
<p> &#8211;usage</p>
<dl>
<dd>Display brief usage message.</dl>
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
<p> -n|&#8211;netbiosname &lt;primary NetBIOS name&gt;</p>
<dl>
<dd>This option allows you to override the NetBIOS name that Samba uses for itself. This is identical to setting the m[blue]<code>netbios name</code>m[] parameter in the smb.conf file. However, a command line setting will take precedence over settings in smb.conf.</dl>
<p> -i|&#8211;scope &lt;scope&gt;</p>
<dl>
<dd>This specifies a NetBIOS scope that nmblookup will use to communicate with when generating NetBIOS names. For details on the use of NetBIOS scopes, see rfc1001.txt and rfc1002.txt. NetBIOS scopes are <i>very</i> rarely used, only set this parameter if you are the system administrator in charge of all the NetBIOS systems you communicate with.</dl>
<p> -W|&#8211;workgroup=domain</p>
<dl>
<dd>Set the SMB domain of the username. This overrides the default domain which is the domain defined in smb.conf. If the domain specified is the same as the servers NetBIOS name, it causes the client to log on using the servers local SAM (as opposed to the Domain SAM).</dl>
<p> -O|&#8211;socket-options socket options</p>
<dl>
<dd>TCP socket options to set on the client socket. See the socket options parameter in the smb.conf manual page for the list of valid options.</dl>
<p> -N|&#8211;no-pass</p>
<dl>
<dd>If specified, this parameter suppresses the normal password prompt from the client to the user. This is useful when accessing a service that does not require a password. </p>
<p> Unless a password is specified on the command line or this parameter is specified, the client will request a password. </p>
<p> If a password is specified on the command line and this option is also defined the password on the command line will be silently ingnored and no password will be used.</dl>
<p> -k|&#8211;kerberos</p>
<dl>
<dd>Try to authenticate with kerberos. Only useful in an Active Directory environment.</dl>
<p> -C|&#8211;use-ccache</p>
<dl>
<dd>Try to use the credentials cached by winbind.</dl>
<p> -A|&#8211;authentication-file=filename</p>
<dl>
<dd>This option allows you to specify a file from which to read the username and password used in the connection. The format of the file is </p>
<dl>
<dd>
<pre>username = &lt;value&gt;
password = &lt;value&gt;
domain = &lt;value&gt;</pre>
</dl>
<p> Make certain that the permissions on the file restrict access from unwanted users.</dl>
<p> -U|&#8211;user=username[%password]</p>
<dl>
<dd>Sets the SMB username or username and password. </p>
<p> If %password is not specified, the user will be prompted. The client will first check the <code>USER</code> environment variable, then the <code>LOGNAME</code> variable and if either exists, the string is uppercased. If these environmental variables are not found, the username <code>GUEST</code> is used. </p>
<p> A third option is to use a credentials file which contains the plaintext of the username and password. This option is mainly provided for scripts where the admin does not wish to pass the credentials on the command line or via environment variables. If this method is used, make certain that the permissions on the file restrict access from unwanted users. See the <i>-A</i> for more details. </p>
<p> Be cautious about including passwords in scripts. Also, on many systems the command line of a running process may be seen via the ps command. To be safe always allow rpcclient to prompt for a password and type it in directly.</dl>
<p> -S|&#8211;signing on|off|required</p>
<dl>
<dd>Set the client signing state.</dl>
<p> -P|&#8211;machine-pass</p>
<dl>
<dd>Use stored machine account password.</dl>
<p> -e|&#8211;encrypt</p>
<dl>
<dd>This command line parameter requires the remote server support the UNIX extensions or that the SMB3 protocol has been selected. Requests that the connection be encrypted. Negotiates SMB encryption using either SMB3 or POSIX extensions via GSSAPI. Uses the given credentials for the encryption negotiation (either kerberos or NTLMv1/v2 if given domain/username/password triple. Fails the connection if encryption cannot be negotiated.</dl>
<p> &#8211;pw-nt-hash</p>
<dl>
<dd>The supplied password is the NT hash.</dl>
<h2>Version</h2>
<p>This man page is correct for version 4 of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8), <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) and <code><a href="/docs/linux/man/8-net/">net</a></code>(8).</p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The samba-regedit man page was written by Karolin Seeger.</p>
