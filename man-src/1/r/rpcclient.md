---
title: "rpcclient(1)"
name: "rpcclient"
section: "1"
letter: "r"
url: "/docs/linux/man/1-rpcclient/"
description: "rpcclient – tool for executing client side MS-RPC functions"
---

<h2 class="name">NAME</h2>
<p> rpcclient &#8211; tool for executing client side MS-RPC functions </p>
<h2>SYNOPSIS</h2>
<dl>
<dt>
<dd>rpcclient [-A authfile] [-c&nbsp;&lt;command string&gt;] [-d debuglevel] [-l logdir] [-N] [-s&nbsp;&lt;smb config file&gt;] [-U username[%password]] [-W workgroup] [-I destinationIP] {BINDING-STRING|HOST}</dl>
<h2>DESCRIPTION</h2>
<p> This tool is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> rpcclient is a utility initially developed to test MS-RPC functionality in Samba itself. It has undergone several stages of development and stability. Many system administrators have now written scripts around it to manage Windows NT clients from their UNIX workstation.</p>
<h2>OPTIONS</h2>
<p> BINDING-STRING|HOST</p>
<dl>
<dt>
<dd> When connecting to a dcerpc service you need to specify a binding string. </p>
<p> The format is: </p>
<p> TRANSPORT:host[options] </p>
<p> where TRANSPORT is either ncacn_np (named pipes) for SMB or ncacn_ip_tcp for DCERPC over TCP/IP. </p>
<p> &quot;host&quot; is an IP or hostname or netbios name. If the binding string identifies the server side of an endpoint, &quot;host&quot; may be an empty string. See below for more details. </p>
<p> &quot;options&quot; can include a SMB pipe name if using the ncacn_np transport or a TCP port number if using the ncacn_ip_tcp transport, otherwise they will be auto-determined. </p>
<p> Examples:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>ncacn_ip_tcp:samba.example.com[1024]</i></dl>
<dl>
<dt>
<dd> &bull; <i>ncacn_ip_tcp:samba.example.com[sign,seal,krb5]</i></dl>
<dl>
<dt>
<dd> &bull; <i>ncacn_ip_tcp:samba.example.com[sign,spnego]</i></dl>
<dl>
<dt>
<dd> &bull; <i>ncacn_np:samba.example.com</i></dl>
<dl>
<dt>
<dd> &bull; <i>ncacn_np:samba.example.com[samr]</i></dl>
<dl>
<dt>
<dd> &bull; <i>ncacn_np:samba.example.com[samr,sign,print]</i></dl>
<dl>
<dt>
<dd> &bull; <i>ncalrpc:/path/to/unix/socket</i></dl>
<dl>
<dt>
<dd> &bull; <i>//SAMBA</i></dl>
</dl>
<p> The supported transports are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>ncacn_np</i> &#8211; Connect using named pipes</dl>
<dl>
<dt>
<dd> &bull; <i>ncacn_ip_tcp</i> &#8211; Connect over TCP/IP</dl>
<dl>
<dt>
<dd> &bull; <i>ncalrpc</i> &#8211; Connect over local RPC (unix sockets)</dl>
</dl>
<p> The supported options are:</p>
<dl>
<dt>
<dd>
<dl>
<dt>
<dd> &bull; <i>sign</i> &#8211; Use RPC integrety autentication level</dl>
<dl>
<dt>
<dd> &bull; <i>seal</i> &#8211; Enable RPC privacy (encryption) autentication level</dl>
<dl>
<dt>
<dd> &bull; <i>connect</i> &#8211; Use RPC connect level authentication (auth, but no sign or seal)</dl>
<dl>
<dt>
<dd> &bull; <i>packet</i> &#8211; Use RPC packet authentication level</dl>
<dl>
<dt>
<dd> &bull; <i>spnego</i> &#8211; Use SPNEGO instead of NTLMSSP authentication</dl>
<dl>
<dt>
<dd> &bull; <i>ntlm</i> &#8211; Use plain NTLM instead of SPNEGO or NTLMSSP</dl>
<dl>
<dt>
<dd> &bull; <i>krb5</i> &#8211; Use Kerberos instead of NTLMSSP authentication</dl>
<dl>
<dt>
<dd> &bull; <i>schannel</i> &#8211; Create a schannel connection</dl>
<dl>
<dt>
<dd> &bull; <i>smb1</i> &#8211; Use SMB1 for named pipes</dl>
<dl>
<dt>
<dd> &bull; <i>smb2</i> &#8211; Use SMB2/3 for named pipes</dl>
<dl>
<dt>
<dd> &bull; <i>validate</i> &#8211; Enable the NDR validator</dl>
<dl>
<dt>
<dd> &bull; <i>print</i> &#8211; Enable debug output of packets</dl>
<dl>
<dt>
<dd> &bull; <i>padcheck</i> &#8211; Check reply data for non-zero pad bytes</dl>
<dl>
<dt>
<dd> &bull; <i>bigendian</i> &#8211; Use big endian for RPC</dl>
<dl>
<dt>
<dd> &bull; <i>ndr64</i> &#8211; Use NDR64 for RPC</dl>
</dl>
</dl>
<p> -c|&#8211;command=&lt;command string&gt;</p>
<dl>
<dt>
<dd> Execute semicolon separated commands (listed below)</dl>
<p> -I|&#8211;dest-ip IP-address</p>
<dl>
<dt>
<dd> <i>IP address</i> is the address of the server to connect to. It should be specified in standard &quot;a.b.c.d&quot; notation. </p>
<p> Normally the client would attempt to locate a named SMB/CIFS server by looking it up via the NetBIOS name resolution mechanism described above in the <i>name resolve order</i> parameter above. Using this parameter will force the client to assume that the server is on the machine with the specified IP address and the NetBIOS name component of the resource being connected to will be ignored. </p>
<p> There is no default for this parameter. If not supplied, it will be determined automatically by the client as described above.</dl>
<p> -p|&#8211;port port</p>
<dl>
<dt>
<dd> This number is the TCP port number that will be used when making connections to the server. The standard (well-known) TCP port number for an SMB/CIFS server is 139, which is the default.</dl>
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
<h2>COMMANDS</h2>
<h3>LSARPC</h3>
<p> lsaquery</p>
<dl>
<dt>
<dd> Query info policy</dl>
<p> lookupsids</p>
<dl>
<dt>
<dd> Resolve a list of SIDs to usernames.</dl>
<p> lookupnames</p>
<dl>
<dt>
<dd> Resolve a list of usernames to SIDs.</dl>
<p> enumtrust</p>
<dl>
<dt>
<dd> Enumerate trusted domains</dl>
<p> enumprivs</p>
<dl>
<dt>
<dd> Enumerate privileges</dl>
<p> getdispname</p>
<dl>
<dt>
<dd> Get the privilege name</dl>
<p> lsaenumsid</p>
<dl>
<dt>
<dd> Enumerate the LSA SIDS</dl>
<p> lsaenumprivsaccount</p>
<dl>
<dt>
<dd> Enumerate the privileges of an SID</dl>
<p> lsaenumacctrights</p>
<dl>
<dt>
<dd> Enumerate the rights of an SID</dl>
<p> lsaenumacctwithright</p>
<dl>
<dt>
<dd> Enumerate accounts with a right</dl>
<p> lsaaddacctrights</p>
<dl>
<dt>
<dd> Add rights to an account</dl>
<p> lsaremoveacctrights</p>
<dl>
<dt>
<dd> Remove rights from an account</dl>
<p> lsalookupprivvalue</p>
<dl>
<dt>
<dd> Get a privilege value given its name</dl>
<p> lsaquerysecobj</p>
<dl>
<dt>
<dd> Query LSA security object</dl>
<h3>LSARPC-DS</h3>
<p> dsroledominfo</p>
<dl>
<dt>
<dd> Get Primary Domain Information</dl>
<p> <i>DFS</i> </p>
<p> dfsexist</p>
<dl>
<dt>
<dd> Query DFS support</dl>
<p> dfsadd</p>
<dl>
<dt>
<dd> Add a DFS share</dl>
<p> dfsremove</p>
<dl>
<dt>
<dd> Remove a DFS share</dl>
<p> dfsgetinfo</p>
<dl>
<dt>
<dd> Query DFS share info</dl>
<p> dfsenum</p>
<dl>
<dt>
<dd> Enumerate dfs shares</dl>
<h3>REG</h3>
<p> shutdown</p>
<dl>
<dt>
<dd> Remote Shutdown</dl>
<p> abortshutdown</p>
<dl>
<dt>
<dd> Abort Shutdown</dl>
<h3>SRVSVC</h3>
<p> srvinfo</p>
<dl>
<dt>
<dd> Server query info</dl>
<p> netshareenum</p>
<dl>
<dt>
<dd> Enumerate shares</dl>
<p> netshareenumall</p>
<dl>
<dt>
<dd> Enumerate all shares</dl>
<p> netsharegetinfo</p>
<dl>
<dt>
<dd> Get Share Info</dl>
<p> netsharesetinfo</p>
<dl>
<dt>
<dd> Set Share Info</dl>
<p> netsharesetdfsflags</p>
<dl>
<dt>
<dd> Set DFS flags</dl>
<p> netfileenum</p>
<dl>
<dt>
<dd> Enumerate open files</dl>
<p> netremotetod</p>
<dl>
<dt>
<dd> Fetch remote time of day</dl>
<p> netnamevalidate</p>
<dl>
<dt>
<dd> Validate sharename</dl>
<p> netfilegetsec</p>
<dl>
<dt>
<dd> Get File security</dl>
<p> netsessdel</p>
<dl>
<dt>
<dd> Delete Session</dl>
<p> netsessenum</p>
<dl>
<dt>
<dd> Enumerate Sessions</dl>
<p> netdiskenum</p>
<dl>
<dt>
<dd> Enumerate Disks</dl>
<p> netconnenum</p>
<dl>
<dt>
<dd> Enumerate Connections</dl>
<p> netshareadd</p>
<dl>
<dt>
<dd> Add share</dl>
<p> netsharedel</p>
<dl>
<dt>
<dd> Delete share</dl>
<h3>SAMR</h3>
<p> queryuser</p>
<dl>
<dt>
<dd> Query user info</dl>
<p> querygroup</p>
<dl>
<dt>
<dd> Query group info</dl>
<p> queryusergroups</p>
<dl>
<dt>
<dd> Query user groups</dl>
<p> querygroupmem</p>
<dl>
<dt>
<dd> Query group membership</dl>
<p> queryaliasmem</p>
<dl>
<dt>
<dd> Query alias membership</dl>
<p> querydispinfo</p>
<dl>
<dt>
<dd> Query display info</dl>
<p> querydominfo</p>
<dl>
<dt>
<dd> Query domain info</dl>
<p> enumdomusers</p>
<dl>
<dt>
<dd> Enumerate domain users</dl>
<p> enumdomgroups</p>
<dl>
<dt>
<dd> Enumerate domain groups</dl>
<p> enumalsgroups</p>
<dl>
<dt>
<dd> Enumerate alias groups</dl>
<p> createdomuser</p>
<dl>
<dt>
<dd> Create domain user</dl>
<p> samlookupnames</p>
<dl>
<dt>
<dd> Look up names</dl>
<p> samlookuprids</p>
<dl>
<dt>
<dd> Look up names</dl>
<p> deletedomuser</p>
<dl>
<dt>
<dd> Delete domain user</dl>
<p> samquerysecobj</p>
<dl>
<dt>
<dd> Query SAMR security object</dl>
<p> getdompwinfo</p>
<dl>
<dt>
<dd> Retrieve domain password info</dl>
<p> lookupdomain</p>
<dl>
<dt>
<dd> Look up domain</dl>
<h3>SPOOLSS</h3>
<p> adddriver &lt;arch&gt; &lt;config&gt; [&lt;version&gt;]</p>
<dl>
<dt>
<dd> Execute an AddPrinterDriver() RPC to install the printer driver information on the server. Note that the driver files should already exist in the directory returned by getdriverdir. Possible values for <i>arch</i> are the same as those for the getdriverdir command. The <i>config</i> parameter is defined as follows: </p>
<dl>
<dt>
<dd>
<pre>
Long Driver Name:\
Driver File Name:\
Data File Name:\
Config File Name:\
Help File Name:\
Language Monitor Name:\
Default Data Type:\
Comma Separated list of Files
</pre>
</dl>
<p> Any empty fields should be enter as the string &quot;NULL&quot;. </p>
<p> Samba does not need to support the concept of Print Monitors since these only apply to local printers whose driver can make use of a bi-directional link for communication. This field should be &quot;NULL&quot;. On a remote NT print server, the Print Monitor for a driver must already be installed prior to adding the driver or else the RPC will fail. </p>
<p> The <i>version</i> parameter lets you specify the printer driver version number. If omitted, the default driver version for the specified architecture will be used. This option can be used to upload Windows 2000 (version 3) printer drivers.</dl>
<p> addprinter &lt;printername&gt; &lt;sharename&gt; &lt;drivername&gt; &lt;port&gt;</p>
<dl>
<dt>
<dd> Add a printer on the remote server. This printer will be automatically shared. Be aware that the printer driver must already be installed on the server (see adddriver) and the <i>port</i>must be a valid port name (see enumports.</dl>
<p> deldriver &lt;driver&gt;</p>
<dl>
<dt>
<dd> Delete the specified printer driver for all architectures. This does not delete the actual driver files from the server, only the entry from the server&#8217;s list of drivers.</dl>
<p> deldriverex &lt;driver&gt; [architecture] [version] [flags]</p>
<dl>
<dt>
<dd> Delete the specified printer driver and optionally files associated with the driver. You can limit this action to a specific architecture and a specific version. If no architecture is given, all driver files of that driver will be deleted. <i>flags</i> correspond to numeric DPD_* values, i.e. a value of 3 requests (DPD_DELETE_UNUSED_FILES | DPD_DELETE_SPECIFIC_VERSION).</dl>
<p> enumdata</p>
<dl>
<dt>
<dd> Enumerate all printer setting data stored on the server. On Windows NT clients, these values are stored in the registry, while Samba servers store them in the printers TDB. This command corresponds to the MS Platform SDK GetPrinterData() function (* This command is currently unimplemented).</dl>
<p> enumdataex</p>
<dl>
<dt>
<dd> Enumerate printer data for a key</dl>
<p> enumjobs &lt;printer&gt;</p>
<dl>
<dt>
<dd> List the jobs and status of a given printer. This command corresponds to the MS Platform SDK EnumJobs() function</dl>
<p> enumkey</p>
<dl>
<dt>
<dd> Enumerate printer keys</dl>
<p> enumports [level]</p>
<dl>
<dt>
<dd> Executes an EnumPorts() call using the specified info level. Currently only info levels 1 and 2 are supported.</dl>
<p> enumdrivers [level]</p>
<dl>
<dt>
<dd> Execute an EnumPrinterDrivers() call. This lists the various installed printer drivers for all architectures. Refer to the MS Platform SDK documentation for more details of the various flags and calling options. Currently supported info levels are 1, 2, and 3.</dl>
<p> enumprinters [level]</p>
<dl>
<dt>
<dd> Execute an EnumPrinters() call. This lists the various installed and share printers. Refer to the MS Platform SDK documentation for more details of the various flags and calling options. Currently supported info levels are 1, 2 and 5.</dl>
<p> getdata &lt;printername&gt; &lt;valuename;&gt;</p>
<dl>
<dt>
<dd> Retrieve the data for a given printer setting. See the enumdata command for more information. This command corresponds to the GetPrinterData() MS Platform SDK function.</dl>
<p> getdataex</p>
<dl>
<dt>
<dd> Get printer driver data with keyname</dl>
<p> getdriver &lt;printername&gt;</p>
<dl>
<dt>
<dd> Retrieve the printer driver information (such as driver file, config file, dependent files, etc&#8230;) for the given printer. This command corresponds to the GetPrinterDriver() MS Platform SDK function. Currently info level 1, 2, and 3 are supported.</dl>
<p> getdriverdir &lt;arch&gt;</p>
<dl>
<dt>
<dd> Execute a GetPrinterDriverDirectory() RPC to retrieve the SMB share name and subdirectory for storing printer driver files for a given architecture. Possible values for <i>arch</i> are &quot;Windows 4.0&quot; (for Windows 95/98), &quot;Windows NT x86&quot;, &quot;Windows NT PowerPC&quot;, &quot;Windows Alpha_AXP&quot;, and &quot;Windows NT R4000&quot;.</dl>
<p> getprinter &lt;printername&gt;</p>
<dl>
<dt>
<dd> Retrieve the current printer information. This command corresponds to the GetPrinter() MS Platform SDK function.</dl>
<p> getprintprocdir</p>
<dl>
<dt>
<dd> Get print processor directory</dl>
<p> openprinter &lt;printername&gt;</p>
<dl>
<dt>
<dd> Execute an OpenPrinterEx() and ClosePrinter() RPC against a given printer.</dl>
<p> setdriver &lt;printername&gt; &lt;drivername&gt;</p>
<dl>
<dt>
<dd> Execute a SetPrinter() command to update the printer driver associated with an installed printer. The printer driver must already be correctly installed on the print server. </p>
<p> See also the enumprinters and enumdrivers commands for obtaining a list of of installed printers and drivers.</dl>
<p> addform</p>
<dl>
<dt>
<dd> Add form</dl>
<p> setform</p>
<dl>
<dt>
<dd> Set form</dl>
<p> getform</p>
<dl>
<dt>
<dd> Get form</dl>
<p> deleteform</p>
<dl>
<dt>
<dd> Delete form</dl>
<p> enumforms</p>
<dl>
<dt>
<dd> Enumerate form</dl>
<p> setprinter</p>
<dl>
<dt>
<dd> Set printer comment</dl>
<p> setprinterdata</p>
<dl>
<dt>
<dd> Set REG_SZ printer data</dl>
<p> setprintername &lt;printername&gt; &lt;newprintername&gt;</p>
<dl>
<dt>
<dd> Set printer name</dl>
<p> rffpcnex</p>
<dl>
<dt>
<dd> Rffpcnex test</dl>
<h3>NETLOGON</h3>
<p> logonctrl2</p>
<dl>
<dt>
<dd> Logon Control 2</dl>
<p> logonctrl</p>
<dl>
<dt>
<dd> Logon Control</dl>
<p> samsync</p>
<dl>
<dt>
<dd> Sam Synchronisation</dl>
<p> samdeltas</p>
<dl>
<dt>
<dd> Query Sam Deltas</dl>
<p> samlogon</p>
<dl>
<dt>
<dd> Sam Logon</dl>
<h3>FSRVP</h3>
<p> fss_is_path_sup &lt;share&gt;</p>
<dl>
<dt>
<dd> Check whether a share supports shadow-copy requests</dl>
<p> fss_get_sup_version</p>
<dl>
<dt>
<dd> Get supported FSRVP version from server</dl>
<p> fss_create_expose &lt;context&gt; &lt;[ro|rw]&gt; &lt;share1&gt; [share2] &#8230; [shareN]</p>
<dl>
<dt>
<dd> Request shadow-copy creation and exposure as a new share</dl>
<p> fss_delete &lt;base_share&gt; &lt;shadow_copy_set_id&gt; &lt;shadow_copy_id&gt;</p>
<dl>
<dt>
<dd> Request shadow-copy share deletion</dl>
<p> fss_has_shadow_copy &lt;base_share&gt;</p>
<dl>
<dt>
<dd> Check for an associated share shadow-copy</dl>
<p> fss_get_mapping &lt;base_share&gt; &lt;shadow_copy_set_id&gt; &lt;shadow_copy_id&gt;</p>
<dl>
<dt>
<dd> Get shadow-copy share mapping information</dl>
<p> fss_recovery_complete &lt;shadow_copy_set_id&gt;</p>
<dl>
<dt>
<dd> Flag read-write shadow-copy as recovery complete, allowing further shadow-copy requests</dl>
<h3>GENERAL COMMANDS</h3>
<p> debuglevel</p>
<dl>
<dt>
<dd> Set the current debug level used to log information.</dl>
<p> help (?)</p>
<dl>
<dt>
<dd> Print a listing of all known commands or extended help on a particular command.</dl>
<p> quit (exit)</p>
<dl>
<dt>
<dd> Exit rpcclient.</dl>
<h2>BUGS</h2>
<p> rpcclient is designed as a developer testing tool and may not be robust in certain areas (such as command line parsing). It has been known to generate a core dump upon failures when invalid parameters where passed to the interpreter. </p>
<p> From Luke Leighton&#8217;s original rpcclient man page: </p>
<p> <i>WARNING!</i> The MSRPC over SMB code has been developed from examining Network traces. No documentation is available from the original creators (Microsoft) on how MSRPC over SMB works, or how the individual MSRPC services work. Microsoft&#8217;s implementation of these services has been demonstrated (and reported) to be&#8230; a bit flaky in places. </p>
<p> The development of Samba&#8217;s implementation is also a bit rough, and as more of the services are understood, it can even result in versions of <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8) and <code><a href="/docs/linux/man/1-rpcclient/">rpcclient</a></code>(1) that are incompatible for some commands or services. Additionally, the developers are sending reports to Microsoft, and problems found or reported to Microsoft are fixed in Service Packs, which may result in incompatibilities.</p>
<h2>VERSION</h2>
<p> This man page is part of version 4.11.6-Ubuntu of the Samba suite.</p>
<h2>AUTHOR</h2>
<p> The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original rpcclient man page was written by Matthew Geddes, Luke Kenneth Casson Leighton, and rewritten by Gerald Carter. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy. </p>
<h2>Index</h2>
