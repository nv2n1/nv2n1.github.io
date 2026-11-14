---
title: "samba(8)"
name: "samba"
section: "8"
letter: "s"
url: "/docs/linux/man/8-samba/"
description: "samba – Server to provide AD and SMB/CIFS services to clients"
---

<p>samba &#8211; Server to provide AD and SMB/CIFS services to clients</p>
<h2>Synopsis</h2>
<dl>
<dd>samba [-D] [-i] [-M&nbsp;<wbr>&lt;model&gt;] [&#8211;maximum-runtime=&lt;seconds&gt;] [-b] [&#8211;help] [&#8211;usage] [-d&nbsp;<wbr>&lt;debug level&gt;] [&#8211;debug-stderr] [-s&nbsp;<wbr>&lt;configuration file&gt;] [&#8211;option=&lt;smb_conf_param&gt;=&lt;value&gt;] [-l&nbsp;<wbr>&lt;log directory&gt;] [&#8211;leak-report] [&#8211;leak-report-full] [-V]</dl>
<h2>Description</h2>
<p>This program is part of the <code><a href="/docs/linux/man/7-samba/">samba</a></code>(7) suite. </p>
<p> samba is the server daemon that provides Active Directory, filesharing and printing services to clients. The server provides filespace and directory services to clients using the SMB (or CIFS) protocol and other related protocols such as DCE/RPC, LDAP and Kerberos. </p>
<p> Clients supported include MSCLIENT 3.0 for DOS, Windows for Workgroups, Windows 95/98/ME, Windows NT, Windows 2000/XP/2003, OS/2, DAVE for Macintosh, and cifsfs for Linux. </p>
<p> An extensive description of the services that the server can provide is given in the man page for the configuration file controlling the attributes of those services (see <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5). This man page will not describe the services, but will concentrate on the administrative aspects of running the server. </p>
<p> Please note that there are significant security implications to running this server, and the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) manual page should be regarded as mandatory reading before proceeding with installation.</p>
<h2>Options</h2>
<p>-D|&#8211;daemon</p>
<dl>
<dd>If specified, this parameter causes the server to operate as a daemon. That is, it detaches itself and runs in the background, fielding requests on the appropriate ports. Operating the server as a daemon is the recommended way of running samba for servers that provide more than casual use file and print services. This switch is assumed if samba is executed on the command line of a shell.</dl>
<p> -i|&#8211;interactive</p>
<dl>
<dd>If this parameter is specified it causes the server to run &quot;interactively&quot;, not as a daemon, even if the server is executed on the command line of a shell. Setting this parameter negates the implicit daemon mode when run from the command line. samba also logs to standard output, as if the -S parameter had been given.</dl>
<p> -M model</p>
<dl>
<dd>This parameter can be used to specify the &quot;process model&quot; samba should use. This determines how concurrent clients are handled. Available process models include <i>single</i> (everything in a single process), <i>standard</i> (similar behaviour to that of Samba 3), <i>thread</i> (single process, different threads.</dl>
<p> &#8211;maximum-runtime=seconds</p>
<dl>
<dd>Set maximum runtime of the server process till autotermination in seconds.</dl>
<p> -b|&#8211;show-build</p>
<dl>
<dd>Print information about how Samba was built.</dl>
<p> &#8211;usage</p>
<dl>
<dd>Display brief usage message.</dl>
<p> &#8211;debug-stderr</p>
<dl>
<dd>Send debug output to STDERR.</dl>
<p> &#8211;leak-report</p>
<dl>
<dd>Enable talloc leak reporting on exit.</dl>
<p> &#8211;leak-report-full</p>
<dl>
<dd>Enable full talloc leak reporting on exit.</dl>
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
<h2>Files</h2>
<p>/etc/rc</p>
<dl>
<dd>or whatever initialization script your system uses. </p>
<p> If running the server as a daemon at startup, this file will need to contain an appropriate startup sequence for the server.</dl>
<p> /etc/services</p>
<dl>
<dd>If running the server via the meta-daemon inetd, this file must contain a mapping of service name (e.g., netbios-ssn) to service port (e.g., 139) and protocol type (e.g., tcp).</dl>
<p> /usr/local/samba/lib/smb.conf</p>
<dl>
<dd>This is the default location of the <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) server configuration file. Other common places that systems install this file are /usr/samba/lib/smb.conf and /etc/samba/smb.conf. </p>
<p> This file describes all the services the server is to make available to clients. See <code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5) for more information.</dl>
<h2>Diagnostics</h2>
<p>Most diagnostics issued by the server are logged in a specified log file. The log file name is specified at compile time, but may be overridden on the command line. </p>
<p> The number and nature of diagnostics available depends on the debug level used by the server. If you have problems, set the debug level to 3 and peruse the log files. </p>
<p> Most messages are reasonably self-explanatory. Unfortunately, at the time this man page was created, there are too many diagnostics available in the source code to warrant describing each and every diagnostic. At this stage your best bet is still to grep the source code and inspect the conditions that gave rise to the diagnostics you are seeing.</p>
<h2>Version</h2>
<p>This man page is correct for version 4 of the Samba suite.</p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-hosts_access/">hosts_access</a></code>(5)<code><a href="/docs/linux/man/5-smb-conf/">smb.conf</a></code>(5), <code><a href="/docs/linux/man/8-smbclient/">smbclient</a></code>(8), <code><a href="/docs/linux/man/8-samba-tool/">samba-tool</a></code>(8), <code><a href="/docs/linux/man/8-smbd/">smbd</a></code>(8), <code><a href="/docs/linux/man/8-nmbd/">nmbd</a></code>(8), <code><a href="/docs/linux/man/1-winbindd/">winbindd</a></code>(1), and the Internet RFC&#8217;s rfc1001.txt, rfc1002.txt. In addition the CIFS (formerly SMB) specification is available as a link from the Web page <a rel="nofollow" href="http://samba.org/cifs/.">http://samba.org/cifs/.</a></p>
<h2>Author</h2>
<p>The original Samba software and related utilities were created by Andrew Tridgell. Samba is now developed by the Samba Team as an Open Source project similar to the way the Linux kernel is developed.</p>
