---
title: "smbclient(1)"
name: "smbclient"
section: "1"
letter: "s"
url: "/docs/linux/man/1-smbclient/"
description: "smbclient – ftp-like client to access SMB/CIFS resources on servers"
---

<h2 class="name">NAME</h2>
<p> smbclient &#8211; ftp-like client to access SMB/CIFS resources on servers </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>smbclient [-b&nbsp;&lt;buffer size&gt;] [-d debuglevel] [-e] [-L&nbsp;&lt;netbios name&gt;] [-U username] [-I destinationIP] [-M&nbsp;&lt;netbios name&gt;] [-m maxprotocol] [-A authfile] [-N] [-C] [-g] [-i scope] [-O&nbsp;&lt;socket options&gt;] [-p port] [-R&nbsp;&lt;name resolve order&gt;] [-s&nbsp;&lt;smb config file&gt;] [-t&nbsp;&lt;per-operation timeout in seconds&gt;] [-k] [-P] [-c&nbsp;&lt;command&gt;]</p>
<dt>
<dd>smbclient {servicename} [password] [-b&nbsp;&lt;buffer size&gt;] [-d debuglevel] [-e] [-D Directory] [-U username] [-W workgroup] [-M&nbsp;&lt;netbios name&gt;] [-m maxprotocol] [-A authfile] [-N] [-C] [-g] [-l log-basename] [-I destinationIP] [-E] [-c&nbsp;&lt;command string&gt;] [-i scope] [-O&nbsp;&lt;socket options&gt;] [-p port] [-R&nbsp;&lt;name resolve order&gt;] [-s&nbsp;&lt;smb config file&gt;] [-t&nbsp;&lt;per-operation timeout in seconds&gt;] [-T&lt;c|x&gt;IXFqgbNan] [-k]</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbclient is a client that can &#8216;talk&#8217; to an SMB/CIFS server. It offers an interface similar to that of the ftp program (see <code><a href="/docs/linux/man/1-ftp/">ftp</a></code>(1)). Operations include things like getting files from the server to the local machine, putting files from the local machine to the server, retrieving directory information from the server and so on.</p>
<h2>OPTIONS</h2>
<p> servicename</p>
<dl>
<dt>
<dd> servicename is the name of the service you want to use on the server. A service name takes the form //server/service where <i>server </i> is the NetBIOS name of the SMB/CIFS server offering the desired service and <i>service</i> is the name of the service offered. Thus to connect to the service &quot;printer&quot; on the SMB/CIFS server &quot;smbserver&quot;, you would use the servicename //smbserver/printer </p>
<p> Note that the server name required is NOT necessarily the IP (DNS) host name of the server ! The name required is a NetBIOS server name, which may or may not be the same as the IP hostname of the machine running the server. </p>
<p> The server name is looked up according to either the <i>-R</i> parameter to smbclient or using the name resolve order parameter in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file, allowing an administrator to change the order and methods by which server names are looked up.</dl>
<p> password</p>
<dl>
<dt>
<dd> The password required to access the specified service on the specified server. If this parameter is supplied, the <i>-N</i> option (suppress password prompt) is assumed. </p>
<p> There is no default password. If no password is supplied on the command line (either by using this parameter or adding a password to the <i>-U</i> option (see below)) and the <i>-N</i> option is not specified, the client will prompt for a password, even if the desired service does not require one. (If no password is required, simply press ENTER to provide a null password.) </p>
<p> Note: Some servers (including OS/2 and Windows for Workgroups) insist on an uppercase password. Lowercase or mixed case passwords may be rejected by these servers. </p>
<p> Be cautious about including passwords in scripts.</dl>
<p> -R|&#8211;name-resolve &lt;name resolve order&gt;</p>
<dl>
<dt>
<dd> This option is used by the programs in the Samba suite to determine what naming services and in what order to resolve host names to IP addresses. The option takes a space-separated string of different name resolution options. </p>
<p> The options are :&quot;lmhosts&quot;, &quot;host&quot;, &quot;wins&quot; and &quot;bcast&quot;. They cause names to be resolved as follows:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <code>lmhosts</code>: Lookup an IP address in the Samba lmhosts file. If the line in lmhosts has no name type attached to the NetBIOS name (see the <code><a href="/docs/linux/man/5-lmhosts/">lmhosts</a></code>(5) for details) then any name type matches for lookup.</dl>
<dl>
<dt>
<dd> &bull; <code>host</code>: Do a standard host name to IP address resolution, using the system /etc/hosts, NIS, or DNS lookups. This method of name resolution is operating system dependent, for instance on IRIX or Solaris this may be controlled by the /etc/nsswitch.conf file). Note that this method is only used if the NetBIOS name type being queried is the 0x20 (server) name type, otherwise it is ignored.</dl>
<dl>
<dt>
<dd> &bull; <code>wins</code>: Query a name with the IP address listed in the <i>wins server</i> parameter. If no WINS server has been specified this method will be ignored.</dl>
<dl>
<dt>
<dd> &bull; <code>bcast</code>: Do a broadcast on each of the known local interfaces listed in the <i>interfaces</i> parameter. This is the least reliable of the name resolution methods as it depends on the target host being on a locally connected subnet.</dl>
</dl>
<p> If this parameter is not set then the name resolve order defined in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file parameter (name resolve order) will be used. </p>
<p> The default order is lmhosts, host, wins, bcast and without this parameter or any entry in the <i>name resolve order </i> parameter of the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) file the name resolution methods will be attempted in this order.</dl>
<p> -M|&#8211;message NetBIOS name</p>
<dl>
<dt>
<dd> This options allows you to send messages, using the &quot;WinPopup&quot; protocol, to another computer. Once a connection is established you then type your message, pressing ^D (control-D) to end. </p>
<p> If the receiving computer is running WinPopup the user will receive the message and probably a beep. If they are not running WinPopup the message will be lost, and no error message will occur. </p>
<p> The message is also automatically truncated if the message is over 1600 bytes, as this is the limit of the protocol. </p>
<p> One useful trick is to pipe the message through smbclient. For example: smbclient -M FRED &lt; mymessage.txt will send the message in the file mymessage.txt to the machine FRED. </p>
<p> You may also find the <i>-U</i> and <i>-I</i> options useful, as they allow you to control the FROM and TO parts of the message. </p>
<p> See the <i>message command</i> parameter in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) for a description of how to handle incoming WinPopup messages in Samba. </p>
<p> <i>Note</i>: Copy WinPopup into the startup group on your WfWg PCs if you want them to always be able to receive messages.</dl>
<p> -p|&#8211;port port</p>
<dl>
<dt>
<dd> This number is the TCP port number that will be used when making connections to the server. The standard (well-known) TCP port number for an SMB/CIFS server is 139, which is the default.</dl>
<p> -g|&#8211;grepable</p>
<dl>
<dt>
<dd> This parameter provides combined with <i>-L</i> easy parseable output that allows processing with utilities such as grep and cut.</dl>
<p> -m|&#8211;max-protocol protocol</p>
<dl>
<dt>
<dd> This allows the user to select the highest SMB protocol level that smbclient will use to connect to the server. By default this is set to highest available SMB3 protocol version. To connect using SMB2 or SMB1 protocol, use the strings SMB2 or NT1 respectively. Note that to connect to a Windows 2012 server with encrypted transport selecting a max-protocol of SMB3 is required.</dl>
<p> -P|&#8211;machine-pass</p>
<dl>
<dt>
<dd> Make queries to the external server using the machine account of the local server.</dl>
<p> -I|&#8211;ip-address IP-address</p>
<dl>
<dt>
<dd> <i>IP address</i> is the address of the server to connect to. It should be specified in standard &quot;a.b.c.d&quot; notation. </p>
<p> Normally the client would attempt to locate a named SMB/CIFS server by looking it up via the NetBIOS name resolution mechanism described above in the <i>name resolve order</i> parameter above. Using this parameter will force the client to assume that the server is on the machine with the specified IP address and the NetBIOS name component of the resource being connected to will be ignored. </p>
<p> There is no default for this parameter. If not supplied, it will be determined automatically by the client as described above.</dl>
<p> -E|&#8211;stderr</p>
<dl>
<dt>
<dd> This parameter causes the client to write messages to the standard error stream (stderr) rather than to the standard output stream. </p>
<p> By default, the client writes messages to standard output &#8211; typically the user&#8217;s tty.</dl>
<p> -L|&#8211;list</p>
<dl>
<dt>
<dd> This option allows you to look at what services are available on a server. You use it as smbclient -L host and a list should appear. The <i>-I </i> option may be useful if your NetBIOS names don&#8217;t match your TCP/IP DNS host names or if you are trying to reach a host on another network.</dl>
<p> -b|&#8211;send-buffer buffersize</p>
<dl>
<dt>
<dd> When sending or receiving files, smbclient uses an internal buffer sized by the maximum number of allowed requests to the connected server. This command allows this size to be set to any range between 0 (which means use the default server controlled size) bytes and 16776960 (0xFFFF00) bytes. Using the server controlled size is the most efficient as smbclient will pipeline as many simultaneous reads or writes needed to keep the server as busy as possible. Setting this to any other size will slow down the transfer. This can also be set using the iosize command inside smbclient.</dl>
<p> -B|&#8211;browse</p>
<dl>
<dt>
<dd> Browse SMB servers using DNS.</dl>
<p> -d|&#8211;debuglevel=level</p>
<dl>
<dt>
<dd> <i>level</i> is an integer from 0 to 10. The default value if this parameter is not specified is 1. </p>
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
<p> -t|&#8211;timeout &lt;timeout-seconds&gt;</p>
<dl>
<dt>
<dd> This allows the user to tune the default timeout used for each SMB request. The default setting is 20 seconds. Increase it if requests to the server sometimes time out. This can happen when SMB3 encryption is selected and smbclient is overwhelming the server with requests. This can also be set using the timeout command inside smbclient.</dl>
<p> -T|&#8211;tar tar options</p>
<dl>
<dt>
<dd> smbclient may be used to create <a href="/docs/linux/man/1-tar/">tar</a>(1) compatible backups of all the files on an SMB/CIFS share. The secondary tar flags that can be given to this option are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>c</i> &#8211; Create a tar backup archive on the local system. Must be followed by the name of a tar file, tape device or &quot;-&quot; for standard output. If using standard output you must turn the log level to its lowest value -d0 to avoid corrupting your tar file. This flag is mutually exclusive with the <i>x</i> flag.</dl>
<dl>
<dt>
<dd> &bull; <i>n</i> &#8211; In combination with the <i>c</i> flag, do not actually create the archive, instead perform a dry run that attempts everything that involved in creation other than writing the file.</dl>
<dl>
<dt>
<dd> &bull; <i>x</i> &#8211; Extract (restore) a local tar file back to a share. Unless the -D option is given, the tar files will be restored from the top level of the share. Must be followed by the name of the tar file, device or &quot;-&quot; for standard input. Mutually exclusive with the <i>c</i> flag. Restored files have their creation times (mtime) set to the date saved in the tar file. Directories currently do not get their creation dates restored properly.</dl>
<dl>
<dt>
<dd> &bull; <i>I</i> &#8211; Include files and directories. Is the default behavior when filenames are specified above. Causes files to be included in an extract or create (and therefore everything else to be excluded). See example below. Filename globbing works in one of two ways. See <i>r</i> below.</dl>
<dl>
<dt>
<dd> &bull; <i>X</i> &#8211; Exclude files and directories. Causes files to be excluded from an extract or create. See example below. Filename globbing works in one of two ways. See <i>r</i> below.</dl>
<dl>
<dt>
<dd> &bull; <i>F</i> &#8211; File containing a list of files and directories. The <i>F</i> causes the name following the tarfile to create to be read as a filename that contains a list of files and directories to be included in an extract or create (and therefore everything else to be excluded). See example below. Filename globbing works in one of two ways. See <i>r</i> below.</dl>
<dl>
<dt>
<dd> &bull; <i>b</i> &#8211; Blocksize. Must be followed by a valid (greater than zero) blocksize. Causes tar file to be written out in blocksize*TBLOCK (512 byte) blocks.</dl>
<dl>
<dt>
<dd> &bull; <i>g</i> &#8211; Incremental. Only back up files that have the archive bit set. Useful only with the <i>c</i> flag.</dl>
<dl>
<dt>
<dd> &bull; <i>q</i> &#8211; Quiet. Keeps tar from printing diagnostics as it works. This is the same as tarmode quiet.</dl>
<dl>
<dt>
<dd> &bull; <i>r</i> &#8211; Use wildcard matching to include or exclude. Deprecated.</dl>
<dl>
<dt>
<dd> &bull; <i>N</i> &#8211; Newer than. Must be followed by the name of a file whose date is compared against files found on the share during a create. Only files newer than the file specified are backed up to the tar file. Useful only with the <i>c</i> flag.</dl>
<dl>
<dt>
<dd> &bull; <i>a</i> &#8211; Set archive bit. Causes the archive bit to be reset when a file is backed up. Useful with the <i>g</i> and <i>c</i> flags.</dl>
</dl>
<p> <i>Tar Long File Names</i> </p>
<p> smbclient&#8217;s tar option now supports long file names both on backup and restore. However, the full path name of the file must be less than 1024 bytes. Also, when a tar archive is created, smbclient&#8217;s tar option places all files in the archive with relative names, not absolute names. </p>
<p> <i>Tar Filenames</i> </p>
<p> All file names can be given as DOS path names (with &#8216;\&#8217; as the component separator) or as UNIX path names (with &#8216;/&#8217; as the component separator). </p>
<p> <i>Examples</i> </p>
<p> Restore from tar file backup.tar into myshare on mypc (no password on share). </p>
<p> smbclient //mypc/myshare &quot;&quot; -N -Tx backup.tar </p>
<p> Restore everything except users/docs </p>
<p> smbclient //mypc/myshare &quot;&quot; -N -TXx backup.tar users/docs </p>
<p> Create a tar file of the files beneath users/docs. </p>
<p> smbclient //mypc/myshare &quot;&quot; -N -Tc backup.tar users/docs </p>
<p> Create the same tar file as above, but now use a DOS path name. </p>
<p> smbclient //mypc/myshare &quot;&quot; -N -Tc backup.tar usersdocs </p>
<p> Create a tar file of the files listed in the file tarlist. </p>
<p> smbclient //mypc/myshare &quot;&quot; -N -TcF backup.tar tarlist </p>
<p> Create a tar file of all the files and directories in the share. </p>
<p> smbclient //mypc/myshare &quot;&quot; -N -Tc backup.tar *</dl>
<p> -D|&#8211;directory initial directory</p>
<dl>
<dt>
<dd> Change to initial directory before starting. Probably only of any use with the tar -T option.</dl>
<p> -c|&#8211;command command string</p>
<dl>
<dt>
<dd> command string is a semicolon-separated list of commands to be executed instead of prompting from stdin. <i> -N</i> is implied by <i>-c</i>. </p>
<p> This is particularly useful in scripts and for printing stdin to the server, e.g. -c &#8216;print -&#8216;.</dl>
<h2>OPERATIONS</h2>
<p> Once the client is running, the user is presented with a prompt : </p>
<p> smb:\&gt; </p>
<p> The backslash (&quot;\&quot;) indicates the current working directory on the server, and will change if the current working directory is changed. </p>
<p> The prompt indicates that the client is ready and waiting to carry out a user command. Each command is a single word, optionally followed by parameters specific to that command. Command and parameters are space-delimited unless these notes specifically state otherwise. All commands are case-insensitive. Parameters to commands may or may not be case sensitive, depending on the command. </p>
<p> You can specify file names which have spaces in them by quoting the name with double quotes, for example &quot;a long file name&quot;. </p>
<p> Parameters shown in square brackets (e.g., &quot;[parameter]&quot;) are optional. If not given, the command will use suitable defaults. Parameters shown in angle brackets (e.g., &quot;&lt;parameter&gt;&quot;) are required. </p>
<p> Note that all commands operating on the server are actually performed by issuing a request to the server. Thus the behavior may vary from server to server, depending on how the server was implemented. </p>
<p> The commands available are given here in alphabetical order. </p>
<p> ? [command]</p>
<dl>
<dt>
<dd> If <i>command</i> is specified, the ? command will display a brief informative message about the specified command. If no command is specified, a list of available commands will be displayed.</dl>
<p> ! [shell command]</p>
<dl>
<dt>
<dd> If <i>shell command</i> is specified, the ! command will execute a shell locally and run the specified shell command. If no command is specified, a local shell will be run.</dl>
<p> allinfo file</p>
<dl>
<dt>
<dd> The client will request that the server return all known information about a file or directory (including streams).</dl>
<p> altname file</p>
<dl>
<dt>
<dd> The client will request that the server return the &quot;alternate&quot; name (the 8.3 name) for a file or directory.</dl>
<p> archive &lt;number&gt;</p>
<dl>
<dt>
<dd> Sets the archive level when operating on files. 0 means ignore the archive bit, 1 means only operate on files with this bit set, 2 means only operate on files with this bit set and reset it after operation, 3 means operate on all files and reset it after operation. The default is 0.</dl>
<p> backup</p>
<dl>
<dt>
<dd> Toggle the state of the &quot;backup intent&quot; flag sent to the server on directory listings and file opens. If the &quot;backup intent&quot; flag is true, the server will try and bypass some file system checks if the user has been granted SE_BACKUP or SE_RESTORE privileges. This state is useful when performing a backup or restore operation.</dl>
<p> blocksize &lt;number&gt;</p>
<dl>
<dt>
<dd> Sets the blocksize parameter for a tar operation. The default is 20. Causes tar file to be written out in blocksize*TBLOCK (normally 512 byte) units.</dl>
<p> cancel jobid0 [jobid1] &#8230; [jobidN]</p>
<dl>
<dt>
<dd> The client will request that the server cancel the printjobs identified by the given numeric print job ids.</dl>
<p> case_sensitive</p>
<dl>
<dt>
<dd> Toggles the setting of the flag in SMB packets that tells the server to treat filenames as case sensitive. Set to OFF by default (tells file server to treat filenames as case insensitive). Only currently affects Samba 3.0.5 and above file servers with the case sensitive parameter set to auto in the smb.conf.</dl>
<p> cd &lt;directory name&gt;</p>
<dl>
<dt>
<dd> If &quot;directory name&quot; is specified, the current working directory on the server will be changed to the directory specified. This operation will fail if for any reason the specified directory is inaccessible. </p>
<p> If no directory name is specified, the current working directory on the server will be reported.</dl>
<p> chmod file mode in octal</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. The client requests that the server change the UNIX permissions to the given octal mode, in standard UNIX format.</dl>
<p> chown file uid gid</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. The client requests that the server change the UNIX user and group ownership to the given decimal values. Note there is currently no way to remotely look up the UNIX uid and gid values for a given name. This may be addressed in future versions of the CIFS UNIX extensions.</dl>
<p> close &lt;fileid&gt;</p>
<dl>
<dt>
<dd> Closes a file explicitly opened by the open command. Used for internal Samba testing purposes.</dl>
<p> del &lt;mask&gt;</p>
<dl>
<dt>
<dd> The client will request that the server attempt to delete all files matching <i>mask</i> from the current working directory on the server.</dl>
<p> deltree &lt;mask&gt;</p>
<dl>
<dt>
<dd> The client will request that the server attempt to delete all files and directories matching <i>mask</i> from the current working directory on the server. Note this will recursively delete files and directories within the directories selected even without the recurse command being set. If any of the delete requests fail the command will stop processing at that point, leaving files and directories not yet processed untouched. This is by design.</dl>
<p> dir &lt;mask&gt;</p>
<dl>
<dt>
<dd> A list of the files matching <i>mask</i> in the current working directory on the server will be retrieved from the server and displayed.</dl>
<p> du &lt;filename&gt;</p>
<dl>
<dt>
<dd> Does a directory listing and then prints out the current disk usage and free space on a share.</dl>
<p> echo &lt;number&gt; &lt;data&gt;</p>
<dl>
<dt>
<dd> Does an SMBecho request to ping the server. Used for internal Samba testing purposes.</dl>
<p> exit</p>
<dl>
<dt>
<dd> Terminate the connection with the server and exit from the program.</dl>
<p> get &lt;remote file name&gt; [local file name]</p>
<dl>
<dt>
<dd> Copy the file called remote file name from the server to the machine running the client. If specified, name the local copy local file name. Note that all transfers in smbclient are binary. See also the lowercase command.</dl>
<p> getfacl &lt;filename&gt;</p>
<dl>
<dt>
<dd> Requires the server support the UNIX extensions. Requests and prints the POSIX ACL on a file.</dl>
<p> hardlink &lt;src&gt; &lt;dest&gt;</p>
<dl>
<dt>
<dd> Creates a hardlink on the server using Windows CIFS semantics.</dl>
<p> help [command]</p>
<dl>
<dt>
<dd> See the ? command above.</dl>
<p> history</p>
<dl>
<dt>
<dd> Displays the command history.</dl>
<p> iosize &lt;bytes&gt;</p>
<dl>
<dt>
<dd> When sending or receiving files, smbclient uses an internal buffer sized by the maximum number of allowed requests to the connected server. This command allows this size to be set to any range between 0 (which means use the default server controlled size) bytes and 16776960 (0xFFFF00) bytes. Using the server controlled size is the most efficient as smbclient will pipeline as many simultaneous reads or writes needed to keep the server as busy as possible. Setting this to any other size will slow down the transfer.</dl>
<p> lcd [directory name]</p>
<dl>
<dt>
<dd> If <i>directory name</i> is specified, the current working directory on the local machine will be changed to the directory specified. This operation will fail if for any reason the specified directory is inaccessible. </p>
<p> If no directory name is specified, the name of the current working directory on the local machine will be reported.</dl>
<p> link target linkname</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. The client requests that the server create a hard link between the linkname and target files. The linkname file must not exist.</dl>
<p> listconnect</p>
<dl>
<dt>
<dd> Show the current connections held for DFS purposes.</dl>
<p> lock &lt;filenum&gt; &lt;r|w&gt; &lt;hex-start&gt; &lt;hex-len&gt;</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Tries to set a POSIX fcntl lock of the given type on the given range. Used for internal Samba testing purposes.</dl>
<p> logon &lt;username&gt; &lt;password&gt;</p>
<dl>
<dt>
<dd> Establishes a new vuid for this session by logging on again. Replaces the current vuid. Prints out the new vuid. Used for internal Samba testing purposes.</dl>
<p> logoff</p>
<dl>
<dt>
<dd> Logs the user off the server, closing the session. Used for internal Samba testing purposes.</dl>
<p> lowercase</p>
<dl>
<dt>
<dd> Toggle lowercasing of filenames for the get and mget commands. </p>
<p> When lowercasing is toggled ON, local filenames are converted to lowercase when using the get and mget commands. This is often useful when copying (say) MSDOS files from a server, because lowercase filenames are the norm on UNIX systems.</dl>
<p> ls &lt;mask&gt;</p>
<dl>
<dt>
<dd> See the dir command above.</dl>
<p> mask &lt;mask&gt;</p>
<dl>
<dt>
<dd> This command allows the user to set up a mask which will be used during recursive operation of the mget and mput commands. </p>
<p> The masks specified to the mget and mput commands act as filters for directories rather than files when recursion is toggled ON. </p>
<p> The mask specified with the mask command is necessary to filter files within those directories. For example, if the mask specified in an mget command is &quot;source*&quot; and the mask specified with the mask command is &quot;*.c&quot; and recursion is toggled ON, the mget command will retrieve all files matching &quot;*.c&quot; in all directories below and including all directories matching &quot;source*&quot; in the current working directory. </p>
<p> Note that the value for mask defaults to blank (equivalent to &quot;*&quot;) and remains so until the mask command is used to change it. It retains the most recently specified value indefinitely. To avoid unexpected results it would be wise to change the value of mask back to &quot;*&quot; after using the mget or mput commands.</dl>
<p> md &lt;directory name&gt;</p>
<dl>
<dt>
<dd> See the mkdir command.</dl>
<p> mget &lt;mask&gt;</p>
<dl>
<dt>
<dd> Copy all files matching <i>mask</i> from the server to the machine running the client. </p>
<p> Note that <i>mask</i> is interpreted differently during recursive operation and non-recursive operation &#8211; refer to the recurse and mask commands for more information. Note that all transfers in smbclient are binary. See also the lowercase command.</dl>
<p> mkdir &lt;directory name&gt;</p>
<dl>
<dt>
<dd> Create a new directory on the server (user access privileges permitting) with the specified name.</dl>
<p> more &lt;file name&gt;</p>
<dl>
<dt>
<dd> Fetch a remote file and view it with the contents of your PAGER environment variable.</dl>
<p> mput &lt;mask&gt;</p>
<dl>
<dt>
<dd> Copy all files matching <i>mask</i> in the current working directory on the local machine to the current working directory on the server. </p>
<p> Note that <i>mask</i> is interpreted differently during recursive operation and non-recursive operation &#8211; refer to the recurse and mask commands for more information. Note that all transfers in smbclient are binary.</dl>
<p> notify &lt;dir name&gt;</p>
<dl>
<dt>
<dd> Query a directory for change notifications. This command issues a recursive filechangenotify call for all possible changes. As changes come in will print one line per change. See <a rel="nofollow" href="https://msdn.microsoft.com/en-us/library/dn392331.aspx">https://msdn.microsoft.com/en-us/library/dn392331.aspx</a> for a description of the action numbers that this command prints. </p>
<p> This command never ends, it waits for event indefinitely.</dl>
<p> posix</p>
<dl>
<dt>
<dd> Query the remote server to see if it supports the CIFS UNIX extensions and prints out the list of capabilities supported. If so, turn on POSIX pathname processing and large file read/writes (if available),.</dl>
<p> posix_encrypt &lt;domain&gt; &lt;username&gt; &lt;password&gt;</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Attempt to negotiate SMB encryption on this connection. If smbclient connected with kerberos credentials (-k) the arguments to this command are ignored and the kerberos credentials are used to negotiate GSSAPI signing and sealing instead. See also the -e option to smbclient to force encryption on initial connection. This command is new with Samba 3.2.</dl>
<p> posix_open &lt;filename&gt; &lt;octal mode&gt;</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Opens a remote file using the CIFS UNIX extensions and prints a fileid. Used for internal Samba testing purposes.</dl>
<p> posix_mkdir &lt;directoryname&gt; &lt;octal mode&gt;</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Creates a remote directory using the CIFS UNIX extensions with the given mode.</dl>
<p> posix_rmdir &lt;directoryname&gt;</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Deletes a remote directory using the CIFS UNIX extensions.</dl>
<p> posix_unlink &lt;filename&gt;</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Deletes a remote file using the CIFS UNIX extensions.</dl>
<p> posix_whoami</p>
<dl>
<dt>
<dd> Query the remote server for the user token using the CIFS UNIX extensions WHOAMI call. Prints out the guest status, user, group, group list and sid list that the remote server is using on behalf of the logged on user.</dl>
<p> print &lt;file name&gt;</p>
<dl>
<dt>
<dd> Print the specified file from the local machine through a printable service on the server.</dl>
<p> prompt</p>
<dl>
<dt>
<dd> Toggle prompting for filenames during operation of the mget and mput commands. </p>
<p> When toggled ON, the user will be prompted to confirm the transfer of each file during these commands. When toggled OFF, all specified files will be transferred without prompting.</dl>
<p> put &lt;local file name&gt; [remote file name]</p>
<dl>
<dt>
<dd> Copy the file called local file name from the machine running the client to the server. If specified, name the remote copy remote file name. Note that all transfers in smbclient are binary. See also the lowercase command.</dl>
<p> queue</p>
<dl>
<dt>
<dd> Displays the print queue, showing the job id, name, size and current status.</dl>
<p> quit</p>
<dl>
<dt>
<dd> See the exit command.</dl>
<p> readlink symlinkname</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Print the value of the symlink &quot;symlinkname&quot;.</dl>
<p> rd &lt;directory name&gt;</p>
<dl>
<dt>
<dd> See the rmdir command.</dl>
<p> recurse</p>
<dl>
<dt>
<dd> Toggle directory recursion for the commands mget and mput. </p>
<p> When toggled ON, these commands will process all directories in the source directory (i.e., the directory they are copying from ) and will recurse into any that match the mask specified to the command. Only files that match the mask specified using the mask command will be retrieved. See also the mask command. </p>
<p> When recursion is toggled OFF, only files from the current working directory on the source machine that match the mask specified to the mget or mput commands will be copied, and any mask specified using the mask command will be ignored.</dl>
<p> rename &lt;old filename&gt; &lt;new filename&gt; [-f]</p>
<dl>
<dt>
<dd> Rename files in the current working directory on the server from <i>old filename</i> to <i>new filename</i>. The optional -f switch allows for superseding the destination file, if it exists. This is supported by NT1 protocol dialect and SMB2 protocol family.</dl>
<p> rm &lt;mask&gt;</p>
<dl>
<dt>
<dd> Remove all files matching <i>mask</i> from the current working directory on the server.</dl>
<p> rmdir &lt;directory name&gt;</p>
<dl>
<dt>
<dd> Remove the specified directory (user access privileges permitting) from the server.</dl>
<p> scopy &lt;source filename&gt; &lt;destination filename&gt;</p>
<dl>
<dt>
<dd> Attempt to copy a file on the server using the most efficient server-side copy calls. Falls back to using read then write if server doesn&#8217;t support server-side copy.</dl>
<p> setmode &lt;filename&gt; &lt;perm=[+|\-]rsha&gt;</p>
<dl>
<dt>
<dd> A version of the DOS attrib command to set file permissions. For example: </p>
<p> setmode myfile +r </p>
<p> would make myfile read only.</dl>
<p> showconnect</p>
<dl>
<dt>
<dd> Show the currently active connection held for DFS purposes.</dl>
<p> stat file</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. The client requests the UNIX basic info level and prints out the same info that the Linux stat command would about the file. This includes the size, blocks used on disk, file type, permissions, inode number, number of links and finally the three timestamps (access, modify and change). If the file is a special file (symlink, character or block device, fifo or socket) then extra information may also be printed.</dl>
<p> symlink target linkname</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. The client requests that the server create a symbolic hard link between the target and linkname files. The linkname file must not exist. Note that the server will not create a link to any path that lies outside the currently connected share. This is enforced by the Samba server.</dl>
<p> tar &lt;c|x&gt;[IXbgNa]</p>
<dl>
<dt>
<dd> Performs a tar operation &#8211; see the <i>-T</i> command line option above. Behavior may be affected by the tarmode command (see below). Using g (incremental) and N (newer) will affect tarmode settings. Note that using the &quot;-&quot; option with tar x may not work &#8211; use the command line option instead.</dl>
<p> blocksize &lt;blocksize&gt;</p>
<dl>
<dt>
<dd> Blocksize. Must be followed by a valid (greater than zero) blocksize. Causes tar file to be written out in <i>blocksize</i>*TBLOCK (512 byte) blocks.</dl>
<p> tarmode &lt;full|inc|reset|noreset|system|nosystem|hidden|nohidden&gt;</p>
<dl>
<dt>
<dd> Changes tar&#8217;s behavior with regard to DOS attributes. There are 4 modes which can be turned on or off. </p>
<p> Incremental mode (default off). When off (using full) tar will back up everything regardless of the <i>archive</i> bit setting. When on (using inc), tar will only back up files with the archive bit set. </p>
<p> Reset mode (default off). When on (using reset), tar will remove the archive bit on all files it backs up (implies read/write share). Use noreset to turn off. </p>
<p> System mode (default on). When off, tar will not backup system files. Use nosystem to turn off. </p>
<p> Hidden mode (default on). When off, tar will not backup hidden files. Use nohidden to turn off.</dl>
<p> timeout &lt;per-operation timeout in seconds&gt;</p>
<dl>
<dt>
<dd> This allows the user to tune the default timeout used for each SMB request. The default setting is 20 seconds. Increase it if requests to the server sometimes time out. This can happen when SMB3 encryption is selected and smbclient is overwhelming the server with requests.</dl>
<p> unlock &lt;filenum&gt; &lt;hex-start&gt; &lt;hex-len&gt;</p>
<dl>
<dt>
<dd> This command depends on the server supporting the CIFS UNIX extensions and will fail if the server does not. Tries to unlock a POSIX fcntl lock on the given range. Used for internal Samba testing purposes.</dl>
<p> volume</p>
<dl>
<dt>
<dd> Prints the current volume name of the share.</dl>
<p> vuid &lt;number&gt;</p>
<dl>
<dt>
<dd> Changes the currently used vuid in the protocol to the given arbitrary number. Without an argument prints out the current vuid being used. Used for internal Samba testing purposes.</dl>
<p> tcon &lt;sharename&gt;</p>
<dl>
<dt>
<dd> Establishes a new tree connect (connection to a share). Replaces the current tree connect. Prints the new tid (tree id). Used for internal Samba testing purposes.</dl>
<p> tdis</p>
<dl>
<dt>
<dd> Close the current share connection (tree disconnect). Used for internal Samba testing purposes.</dl>
<p> tid &lt;number&gt;</p>
<dl>
<dt>
<dd> Changes the current tree id (tid) in the protocol to a new arbitrary number. Without an argument, it prints out the tid currently used. Used for internal Samba testing purposes.</dl>
<p> utimes &lt;filename&gt; &lt;create time&gt; &lt;access time&gt; &lt;write time&gt; &lt; change time&gt;</p>
<dl>
<dt>
<dd> Changes the timestamps on a file by name. Times should be specified in the format YY:MM:DD-HH:MM:SS or -1 for no change.</dl>
<h2>NOTES</h2>
<p> Some servers are fussy about the case of supplied usernames, passwords, share names (AKA service names) and machine names. If you fail to connect try giving all parameters in uppercase. </p>
<p> It is often necessary to use the -n option when connecting to some types of servers. For example OS/2 LanManager insists on a valid NetBIOS name being used, so you need to supply a valid name that would be known to the server. </p>
<p> smbclient supports long file names where the server supports the LANMAN2 protocol or above.</p>
<h2>ENVIRONMENT VARIABLES</h2>
<p> The variable <code>USER</code> may contain the username of the person using the client. This information is used only if the protocol level is high enough to support session-level passwords. </p>
<p> The variable <code>PASSWD</code> may contain the password of the person using the client. This information is used only if the protocol level is high enough to support session-level passwords.</p>
<h2>INSTALLATION</h2>
<p> The location of the client program is a matter for individual system administrators. The following are thus suggestions only. </p>
<p> It is recommended that the smbclient software be installed in the /usr/local/samba/bin/ or /usr/samba/bin/ directory, this directory readable by all, writeable only by root. The client program itself should be executable by all. The client should <i>NOT</i> be setuid or setgid! </p>
<p> The client log files should be put in a directory readable and writeable only by the user. </p>
<p> To test the client, you will need to know the name of a running SMB/CIFS server. It is possible to run <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) as an ordinary user &#8211; running that server as a daemon on a user-accessible port (typically any port number over 1024) would provide a suitable test server.</p>
<h2>DIAGNOSTICS</h2>
<p> Most diagnostics issued by the client are logged in a specified log file. The log file name is specified at compile time, but may be overridden on the command line. </p>
<p> The number and nature of diagnostics available depends on the debug level used by the client. If you have problems, set the debug level to 3 and peruse the log files.</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<h2>Index</h2>
