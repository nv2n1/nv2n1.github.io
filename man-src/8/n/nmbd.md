---
title: "nmbd(8)"
name: "nmbd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nmbd/"
description: "nmbd – NetBIOS name server to provide NetBIOS over IP naming services to clients"
---

<p>nmbd &#8211; NetBIOS name server to provide NetBIOS over IP naming services to clients</p>
<h2>Synopsis</h2>
<dl>
<dd>nmbd [-D|&#8211;daemon] [-F|&#8211;foreground] [-S|&#8211;log-stdout] [-i|&#8211;interactive] [-V] [-d&nbsp;<wbr>&lt;debug level&gt;] [-H|&#8211;hosts&nbsp;<wbr>&lt;lmhosts file&gt;] [-l&nbsp;<wbr>&lt;log directory&gt;] [-p|&#8211;port&nbsp;<wbr>&lt;port number&gt;] [-s&nbsp;<wbr>&lt;configuration file&gt;] [&#8211;no-process-group]</dl>
<h2>Description</h2>
<p>This program is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> nmbd is a server that understands and can reply to NetBIOS over IP name service requests, like those produced by SMB/CIFS clients such as Windows 95/98/ME, Windows NT, Windows 2000, Windows XP and LanManager clients. It also participates in the browsing protocols which make up the Windows &quot;Network Neighborhood&quot; view. </p>
<p> SMB/CIFS clients, when they start up, may wish to locate an SMB/CIFS server. That is, they wish to know what IP number a specified host is using. </p>
<p> Amongst other services, nmbd will listen for such requests, and if its own NetBIOS name is specified it will respond with the IP number of the host it is running on. Its &quot;own NetBIOS name&quot; is by default the primary DNS name of the host it is running on, but this can be overridden by the m[blue]<code>netbios name</code>m[] in smb.conf. Thus nmbd will reply to broadcast queries for its own name(s). Additional names for nmbd to respond on can be set via parameters in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) configuration file. </p>
<p> nmbd can also be used as a WINS (Windows Internet Name Server) server. What this basically means is that it will act as a WINS database server, creating a database from name registration requests that it receives and replying to queries from clients for these names. </p>
<p> In addition, nmbd can act as a WINS proxy, relaying broadcast queries from clients that do not understand how to talk the WINS protocol to a WINS server.</p>
<h2>Options</h2>
<p>-D|&#8211;daemon</p>
<dl>
<dd>If specified, this parameter causes nmbd to operate as a daemon. That is, it detaches itself and runs in the background, fielding requests on the appropriate port. By default, nmbd will operate as a daemon if launched from a command shell. nmbd can also be operated from the inetd meta-daemon, although this is not recommended.</dl>
<p> -F|&#8211;foreground</p>
<dl>
<dd>If specified, this parameter causes the main nmbd process to not daemonize, i.e. double-fork and disassociate with the terminal. Child processes are still created as normal to service each connection request, but the main process does not exit. This operation mode is suitable for running nmbd under process supervisors such as supervise and svscan from Daniel J. Bernstein&#8217;s daemontools package, or the AIX process monitor.</dl>
<p> -S|&#8211;log-stdout</p>
<dl>
<dd>If specified, this parameter causes nmbd to log to standard output rather than a file.</dl>
<p> -i|&#8211;interactive</p>
<dl>
<dd>If this parameter is specified it causes the server to run &quot;interactively&quot;, not as a daemon, even if the server is executed on the command line of a shell. Setting this parameter negates the implicit daemon mode when run from the command line. nmbd also logs to standard output, as if the <code>-S</code> parameter had been given.</dl>
<p> -?|&#8211;help</p>
<dl>
<dd>Print a summary of command line options.</dl>
<p> &#8211;usage</p>
<dl>
<dd>Display brief usage message.</dl>
<p> -H|&#8211;hosts &lt;filename&gt;</p>
<dl>
<dd>NetBIOS lmhosts file. The lmhosts file is a list of NetBIOS names to IP addresses that is loaded by the nmbd server and used via the name resolution mechanism m[blue]<code>name resolve order</code>m[] described in <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) to resolve any NetBIOS name queries needed by the server. Note that the contents of this file are <i>NOT</i> used by nmbd to answer any name queries. Adding a line to this file affects name NetBIOS resolution from this host <i>ONLY</i>. </p>
<p> The default path to this file is compiled into Samba as part of the build process. Common defaults are /usr/local/samba/lib/lmhosts, /usr/samba/lib/lmhosts or /etc/samba/lmhosts. See the <code><a href="/docs/linux/man/5-lmhosts/">lmhosts</a></code>(5) man page for details on the contents of this file.</dl>
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
<p> -p|&#8211;port &lt;UDP port number&gt;</p>
<dl>
<dd>UDP port number is a positive integer value. This option changes the default UDP port number (normally 137) that nmbd responds to name queries on. Don&#8217;t use this option unless you are an expert, in which case you won&#8217;t need help!</dl>
<p> &#8211;no-process-group</p>
<dl>
<dd>Do not create a new process group for nmbd.</dl>
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
<p> When run as a WINS server (see the m[blue]<code>wins support</code>m[] parameter in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) man page), nmbd will store the WINS database in the file wins.dat in the var/locks directory configured under wherever Samba was configured to install itself. </p>
<p> If nmbd is acting as a <i> browse master</i> (see the m[blue]<code>local master</code>m[] parameter in the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) man page, nmbd will store the browsing database in the file browse.dat in the var/locks directory configured under wherever Samba was configured to install itself.</dl>
<h2>Signals</h2>
<p>To shut down an nmbd process it is recommended that SIGKILL (-9) <i>NOT</i> be used, except as a last resort, as this may leave the name database in an inconsistent state. The correct way to terminate nmbd is to send it a SIGTERM (-15) signal and wait for it to die on its own. </p>
<p> nmbd will accept SIGHUP, which will cause it to dump out its namelists into the file namelist.debug in the /usr/local/samba/var/locks directory (or the var/locks directory configured under wherever Samba was configured to install itself). This will also cause nmbd to dump out its server database in the log.nmb file. </p>
<p> The debug log level of nmbd may be raised or lowered using <code><a href="/docs/linux/man/1-smbcontrol/">smbcontrol</a></code>(1) (SIGUSR[1|2] signals are no longer used since Samba 2.2). This is to allow transient problems to be diagnosed, whilst still running at a normally low log level.</p>
<h2>Version</h2>
<p>This man page is correct for version 3 of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8), <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8), <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5), <code><a href="/docs/linux/man/1-smbclient/">smbclient</a></code>(1), <code><a href="/docs/linux/man/1-testparm/">testparm</a></code>(1), and the Internet RFC&#8217;s rfc1001.txt, rfc1002.txt. In addition the CIFS (formerly SMB) specification is available as a link from the Web page <a rel="nofollow" href="https://www.samba.org/cifs/.">https://www.samba.org/cifs/.</a></p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed. </p>
<p> The original Samba man pages were written by Karl Auer. The man page sources were converted to YODL format (another excellent piece of Open Source software, available at <a href="ftp://ftp.icce.rug.nl/pub/unix/)">ftp://ftp.icce.rug.nl/pub/unix/)</a> and updated for the Samba 2.0 release by Jeremy Allison. The conversion to DocBook for Samba 2.2 was done by Gerald Carter. The conversion to DocBook XML 4.2 for Samba 3.0 was done by Alexander Bokovoy.</p>
