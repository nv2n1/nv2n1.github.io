---
title: "smbd(8)"
name: "smbd"
section: "8"
letter: "s"
url: "/docs/linux/man/8-smbd/"
description: "smbd – server to provide SMB/CIFS services to clients"
---

<p>smbd &#8211; server to provide SMB/CIFS services to clients</p>
<h2>Synopsis</h2>
<dl>
<dd>smbd [-D|&#8211;daemon] [-F|&#8211;foreground] [-S|&#8211;log-stdout] [-i|&#8211;interactive] [-V] [-b|&#8211;build-options] [-d&nbsp;<wbr>&lt;debug level&gt;] [-l|&#8211;log-basename&nbsp;<wbr>&lt;log directory&gt;] [-p&nbsp;<wbr>&lt;port number(s)&gt;] [-P&nbsp;<wbr>&lt;profiling level&gt;] [-s&nbsp;<wbr>&lt;configuration file&gt;] [&#8211;no-process-group]</dl>
<h2>Description</h2>
<p>This program is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> smbd is the server daemon that provides filesharing and printing services to Windows clients. The server provides filespace and printer services to clients using the SMB (or CIFS) protocol. This is compatible with the LanManager protocol, and can service LanManager clients. These include MSCLIENT 3.0 for DOS, Windows for Workgroups, Windows 95/98/ME, Windows NT, Windows 2000, OS/2, DAVE for Macintosh, and smbfs for Linux. </p>
<p> An extensive description of the services that the server can provide is given in the man page for the configuration file controlling the attributes of those services (see <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5). This man page will not describe the services, but will concentrate on the administrative aspects of running the server. </p>
<p> Please note that there are significant security implications to running this server, and the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) manual page should be regarded as mandatory reading before proceeding with installation. </p>
<p> A session is created whenever a client requests one. Each client gets a copy of the server for each session. This copy then services all connections made by the client during that session. When all connections from its client are closed, the copy of the server for that client terminates. </p>
<p> The configuration file, and any files that it includes, are automatically reloaded every minute, if they change. You can force a reload by sending a SIGHUP to the server. Reloading the configuration file will not affect connections to any service that is already established. Either the user will have to disconnect from the service, or smbd killed and restarted.</p>
<h2>Options</h2>
<p>-D|&#8211;daemon</p>
<dl>
<dd>If specified, this parameter causes the server to operate as a daemon. That is, it detaches itself and runs in the background, fielding requests on the appropriate port. Operating the server as a daemon is the recommended way of running smbd for servers that provide more than casual use file and print services. This switch is assumed if smbd is executed on the command line of a shell.</dl>
<p> -F|&#8211;foreground</p>
<dl>
<dd>If specified, this parameter causes the main smbd process to not daemonize, i.e. double-fork and disassociate with the terminal. Child processes are still created as normal to service each connection request, but the main process does not exit. This operation mode is suitable for running smbd under process supervisors such as supervise and svscan from Daniel J. Bernstein&#8217;s daemontools package, or the AIX process monitor.</dl>
<p> -S|&#8211;log-stdout</p>
<dl>
<dd>If specified, this parameter causes smbd to log to standard output rather than a file.</dl>
<p> -i|&#8211;interactive</p>
<dl>
<dd>If this parameter is specified it causes the server to run &quot;interactively&quot;, not as a daemon, even if the server is executed on the command line of a shell. Setting this parameter negates the implicit daemon mode when run from the command line. smbd will only accept one connection and terminate. It will also log to standard output, as if the -S parameter had been given.</dl>
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
<p> -?|&#8211;help</p>
<dl>
<dd>Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dd>Display brief usage message.</dl>
<p> &#8211;no-process-group</p>
<dl>
<dd>Do not create a new process group for smbd.</dl>
<p> -b|&#8211;build-options</p>
<dl>
<dd>Prints information about how Samba was built.</dl>
<p> -p|&#8211;port&lt;port number(s)&gt;</p>
<dl>
<dd><i>port number(s)</i> is a space or comma-separated list of TCP ports smbd should listen on. The default value is taken from the m[blue]<code>ports</code>m[] parameter in smb.conf </p>
<p> The default ports are 139 (used for SMB over NetBIOS over TCP) and port 445 (used for plain SMB over TCP).</dl>
<p> -P|&#8211;profiling-level&lt;profiling level&gt;</p>
<dl>
<dd><i>profiling level</i> is a number specifying the level of profiling data to be collected. 0 turns off profiling, 1 turns on counter profiling only, 2 turns on complete profiling, and 3 resets all profiling data.</dl>
<h2>Files</h2>
<p>/etc/inetd.conf</p>
<dl>
<dd>If the server is to be run by the inetd meta-daemon, this file must contain suitable startup information for the meta-daemon.</dl>
<p> /etc/rc</p>
<dl>
<dd>or whatever initialization script your system uses). </p>
<p> If running the server as a daemon at startup, this file will need to contain an appropriate startup sequence for the server.</dl>
<p> /etc/services</p>
<dl>
<dd>If running the server via the meta-daemon inetd, this file must contain a mapping of service name (e.g., netbios-ssn) to service port (e.g., 139) and protocol type (e.g., tcp).</dl>
<p> /usr/local/samba/lib/smb.conf</p>
<dl>
<dd>This is the default location of the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) server configuration file. Other common places that systems install this file are /usr/samba/lib/smb.conf and /etc/samba/smb.conf. </p>
<p> This file describes all the services the server is to make available to clients. See <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) for more information.</dl>
<h2>Limitations</h2>
<p>On some systems smbd cannot change uid back to root after a setuid() call. Such systems are called trapdoor uid systems. If you have such a system, you will be unable to connect from a client (such as a PC) as two different users at once. Attempts to connect the second user will result in access denied or similar.</p>
<h2>Environment Variables</h2>
<p><code>PRINTER</code></p>
<dl>
<dd>If no printer name is specified to printable services, most systems will use the value of this variable (or <code>lp</code> if this variable is not defined) as the name of the printer to use. This is not specific to the server, however.</dl>
<h2>Pam Interaction</h2>
<p>Samba uses PAM for authentication (when presented with a plaintext password), for account checking (is this account disabled?) and for session management. The degree too which samba supports PAM is restricted by the limitations of the SMB protocol and the m[blue]<code>obey pam restrictions</code>m[]<code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) parameter. When this is set, the following restrictions apply: </p>
<dl>
<dd>&bull; <i>Account Validation</i>: All accesses to a samba server are checked against PAM to see if the account is valid, not disabled and is permitted to login at this time. This also applies to encrypted logins.</dl>
<dl>
<dd>&bull; <i>Session Management</i>: When not using share level security, users must pass PAM&#8217;s session checks before access is granted. Note however, that this is bypassed in share level security. Note also that some older pam configuration files may need a line added for session support.</dl>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>Diagnostics</h2>
<p>Most diagnostics issued by the server are logged in a specified log file. The log file name is specified at compile time, but may be overridden on the command line. </p>
<p> The number and nature of diagnostics available depends on the debug level used by the server. If you have problems, set the debug level to 3 and peruse the log files. </p>
<p> Most messages are reasonably self-explanatory. Unfortunately, at the time this man page was created, there are too many diagnostics available in the source code to warrant describing each and every diagnostic. At this stage your best bet is still to grep the source code and inspect the conditions that gave rise to the diagnostics you are seeing.</p>
<h2>Tdb Files</h2>
<p>Samba stores it&#8217;s data in several TDB (Trivial Database) files, usually located in /var/lib/samba. </p>
<p> (*) information persistent across restarts (but not necessarily important to backup). </p>
<p> account_policy.tdb*</p>
<dl>
<dd>NT account policy settings such as pw expiration, etc&#8230;</dl>
<p> brlock.tdb</p>
<dl>
<dd>byte range locks</dl>
<p> browse.dat</p>
<dl>
<dd>browse lists</dl>
<p> gencache.tdb</p>
<dl>
<dd>generic caching db</dl>
<p> group_mapping.tdb*</p>
<dl>
<dd>group mapping information</dl>
<p> locking.tdb</p>
<dl>
<dd>share modes &amp; oplocks</dl>
<p> login_cache.tdb*</p>
<dl>
<dd>bad pw attempts</dl>
<p> messages.tdb</p>
<dl>
<dd>Samba messaging system</dl>
<p> netsamlogon_cache.tdb*</p>
<dl>
<dd>cache of user net_info_3 struct from net_samlogon() request (as a domain member)</dl>
<p> ntdrivers.tdb*</p>
<dl>
<dd>installed printer drivers</dl>
<p> ntforms.tdb*</p>
<dl>
<dd>installed printer forms</dl>
<p> ntprinters.tdb*</p>
<dl>
<dd>installed printer information</dl>
<p> printing/</p>
<dl>
<dd>directory containing tdb per print queue of cached lpq output</dl>
<p> registry.tdb</p>
<dl>
<dd>Windows registry skeleton (connect via regedit.exe)</dl>
<p> smbXsrv_session_global.tdb</p>
<dl>
<dd>session information (e.g. support for &#8216;utmp = yes&#8217;)</dl>
<p> smbXsrv_tcon_global.tdb</p>
<dl>
<dd>share connections (used to enforce max connections, etc&#8230;)</dl>
<p> smbXsrv_open_global.tdb</p>
<dl>
<dd>open file handles (used durable handles, etc&#8230;)</dl>
<p> share_info.tdb*</p>
<dl>
<dd>share acls</dl>
<p> winbindd_cache.tdb</p>
<dl>
<dd>winbindd&#8217;s cache of user lists, etc&#8230;</dl>
<p> winbindd_idmap.tdb*</p>
<dl>
<dd>winbindd&#8217;s local idmap db</dl>
<p> wins.dat*</p>
<dl>
<dd>wins database when &#8216;wins support = yes&#8217;</dl>
<h2>Signals</h2>
<p>Sending the smbd a SIGHUP will cause it to reload its smb.conf configuration file within a short period of time. </p>
<p> To shut down a user&#8217;s smbd process it is recommended that SIGKILL (-9)<i>NOT</i> be used, except as a last resort, as this may leave the shared memory area in an inconsistent state. The safe way to terminate an smbd is to send it a SIGTERM (-15) signal and wait for it to die on its own. </p>
<p> The debug log level of smbd may be raised or lowered using <code><a href="/docs/linux/man/1-smbcontrol/">smbcontrol</a></code>(1) program (SIGUSR[1|2] signals are no longer used since Samba 2.2). This is to allow transient problems to be diagnosed, whilst still running at a normally low log level. </p>
<p> Note that as the signal handlers send a debug write, they are not re-entrant in smbd. This you should wait until smbd is in a state of waiting for an incoming SMB before issuing them. It is possible to make the signal handlers safe by un-blocking the signals before the select call and re-blocking them after, however this would affect performance.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5), <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5), <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1), <code><a href="/docs/linux/man/1-testparm/">testparm</a></code>(1), and the Internet RFC&#8217;s rfc1001.txt, rfc1002.txt. In addition the CIFS (formerly SMB) specification is available as a link from the Web page <a rel="nofollow" href="https://www.samba.org/cifs/.">https://www.samba.org/cifs/.</a></p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original Samba man pages were written by Karl Auer. The man page sources were converted to YODL format (another excellent piece of Open Source software, available at <a href="ftp://ftp.icce.rug.nl/pub/unix/)">ftp://ftp.icce.rug.nl/pub/unix/)</a> and updated for the Samba 2.0 release by Jeremy Allison. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy.</p>
