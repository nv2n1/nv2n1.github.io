---
title: "pmsocks(1)"
name: "pmsocks"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmsocks/"
description: "pmsocks – shell wrapper for performance monitoring across firewalls"
---

<h2>NAME</h2>
<p> <code>pmsocks</code> &#8211; shell wrapper for performance monitoring across firewalls</p>
<h2>SYNOPSIS</h2>
<p> <code>pmsocks</code> <i>path</i> [<i>args</i> &#8230;]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmsocks</code> allows Performance Co-Pilot (PCP) clients running on hosts located on the internal side of a TCP/IP firewall to monitor remote hosts on the other side of the firewall. This assumes the firewall has been configured with a compliant <code>sockd</code> daemon and the necessary access controls are satisfied.</p>
<h2>CONFIGURATION</h2>
<p> <code>pmsocks</code> uses the <code><a href="/docs/linux/man/5-tsocks/">tsocks</a></code>(5) library, which is not included with PCP. You can get <code>tsocks </code> from <i><a rel="nofollow" href="http://www.progsoc.uts.edu.au/~delius/">http://www.progsoc.uts.edu.au/~delius/</a></i>.</p>
<h2>IRIX CONFIGURATION</h2>
<p> On IRIX, <code>pmsocks</code> is simply a shell wrapper that sets the appropriate environment variables and then executes the <i>path </i> program with <i>args</i> arguments (if any). <code>pmsocks</code> works by setting the <code>_RLD_LIST</code> environment variable (see <code><a href="/docs/linux/man/1-rld/">rld</a></code>(1)) to load a dynamic shared library (see <code><a href="/docs/linux/man/5-dso/">dso</a></code>(5)) containing stubs for &#8220;socksified&#8221; network library functions; This &#8220;socksified&#8221; library is installed at <i>/usr/pcp/lib/libpcp_socks.so</i>. </p>
<p> There are a number of conditions required for this to be successful and the user is strongly advised to read this whole manual page (in particular the <code>CAVEAT</code> section below) before attempting to use <code>pmsocks</code>. </p>
<p> When <code>pmsocks</code> is installed, the <i>/etc/pcp_socks.conf</i> configuration file is also installed with minimum default settings. These settings specify that socket connections to the local host should be made directly, without contacting any socks server daemon. This is necessary so that PCP clients will be able to establish a local connection to the <code><a href="/docs/linux/man/1-x/">X</a></code>(1) server, and use PCP connections, possibly via a <code>sockd</code> daemon, to monitor remote hosts. In the present implementation of <code>pmsocks</code>, non-direct connections to the <code><a href="/docs/linux/man/1-x/">X</a></code>(1) server do not work, hence if the display is remote, then the remote host must be on the same side of the firewall and <i>/etc/pcp_socks.conf</i> must be configured to connect directly to that host. </p>
<p> The format of <i>/etc/pcp_socks.conf </i> is identical to <i>/etc/socks.conf</i> as documented in the <i>CSTC-4.2</i> socks distribution. This distribution may be obtained via information contained in the socks FAQ at <center> <a href="ftp://coast.cs.purdue.edu/pub/tools/unix/socks/">ftp://coast.cs.purdue.edu/pub/tools/unix/socks/</a><br />
 </center> </p>
<p> If other socks clients are being used, then it is generally safe to remove <i>/etc/pcp_socks.conf</i> and instead make a symbolic link to <i>/etc/socks.conf</i>. The file formats are identical. </p>
<p> The default configuration should be customized to suit the local environment so that connections to hosts located on the same side of the firewall as the local host do not use the socks daemon unnecessarily. The default configuration is </p>
<p> direct LOCALHOSTNAME 255.255.255.255 # direct localhost<br />
 sockd 0.0.0.0 0.0.0.0 # contact sockd everywhere else </p>
<p> Note that the string <code>LOCALHOSTNAME</code> is dynamically substituted at run time with the name of the local host, as obtained by a call to <code><a href="/docs/linux/man/2-gethostname/">gethostname</a></code>(2). Assuming the real IP address of the local host is <code>1.2.3.4</code> and that a normal class-c subnet is used locally, the most common customization would be to specify direct connections for all hosts on the local subnet, by inserting another &#8220;direct&#8221; line as follows: </p>
<p> direct LOCALHOSTNAME 255.255.255.255 # direct localhost<br />
 direct 1.2.3.0 255.255.255.0 # direct on local subnet<br />
 sockd 0.0.0.0 0.0.0.0 # contact sockd everywhere else </p>
<p> The order of lines is important &#8211; the first line matching the requested destination IP address during a <code><a href="/docs/linux/man/2-connect/">connect</a></code>(2) call (after the requested IP address has been masked by the third parameter of the <i>/etc/pcp_socks.conf</i> line), specifies via the first parameter whether to contact the socks daemon or whether to attempt a direct connection.</p>
<h2>IRIX ENVIRONMENT VARIABLES</h2>
<p> There are several environment variables used by <code>pmsocks</code> as follows:</p>
<dl>
<dt><code>SOCKS_SERVER</code></p>
<dd> Specifies the host name or IP address of the host running the <code>sockd</code> daemon. Usually this is the name of the firewall host.</p>
<dt><code>SOCKS_PORT</code></p>
<dd> The TCP/IP port to use when contacting <code>sockd</code> on the <code>SOCKS_SERVER</code> host. The default is <code>1080</code>.</p>
<dt><code>SOCKS_NS</code></p>
<dd> The host name of the name server to use, usually to resolve the IP address of <code>SOCKS_SERVER</code>.</p>
<dt><code>SOCKS_DEBUG</code></p>
<dd> If present in the environment, <code>libpcp_socks</code> will print debugging information to the <i>stderr</i> stream. There are only two levels of debugging, on or off. This is only really useful for the developers because the debugging information assumes knowledge of the <code>libpcp_socks</code> source code.</p>
<dt><code>SOCKS_BANNER</code></p>
<dd> If this is set, whenever a client calls <code>libpcp_socks</code> it will echo a message to <i>stdout</i> containing version information. This can be useful to check <code>libpcp_socks</code> is working in the absence of verbose logging.</p>
<dt><code>_RLD_LIST</code></p>
<dd> <code>pmsocks</code> sets this to exactly <code>/usr/pcp/lib/libpcp_socks.so:DEFAULT</code><br />
 It is strongly recommended this NOT be set in the environment of interactive shells.</p>
<dt><code>PMCD_CONNECT_TIMEOUT</code></p>
<dd> Specifies the time-out, in seconds, for connections to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). When using <code>pmsocks</code>, this may need to be increased from the default (5 seconds) due to the additional delays introduced as a result of using <code>sockd</code>. See <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) for further details about this variable.</dl>
<h2>CAVEAT</h2>
<p> The following notes should be considered carefully:</p>
<dl>
<dt>0)</p>
<dd> Because <code>sockd</code> can only handle TCP/IP sockets, <code>pmsocks</code> never attempts to use <code>sockd</code> for sockets of type <code>SOCK_DGRAM</code> or if the <code>domain</code> parameter in a call to <code><a href="/docs/linux/man/2-socket/">socket</a></code>(2) is <code>PF_UNIX</code> (unix domain sockets should never need to use <code>sockd</code> anyway).</p>
<dt>1)</p>
<dd> Some firewall products do not support &#8220;socksified&#8221; applications, and in these cases, <code>pmsocks</code> cannot be used. In this case, it will be necessary to configure the firewall to allow connections through the firewall for the PMCD communications port, typically tcp/4321.</p>
<dt>2)</p>
<dd> The PCP protocol is TPC/IP-based and works with the socks protocol, but connections which use UDP/DATAGRAM sockets or remote X11 connections via <code>sockd</code> may not work. If the remote display host is on the same side of the firewall as the application, this may be circumvented by configuring the remote display host to use direct connections &#8211; see above. Also, using X11 display options which use shared memory may hang the X server when used with <code>pmsocks</code>.</p>
<dt>3)</p>
<dd> If the <code>pmsocks</code> configuration file is not present, then <code>pmsocks</code> will exit with an error message.</p>
<dt>4)</p>
<dd> <code>pmsocks</code> uses the locally configured name server or resolver (see <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5)) to resolve host names to IP addresses. This may or may not be capable of resolving host names on the other side of the firewall.</p>
<dt>5)</p>
<dd> When used over a WAN, often the <code>sockd</code> daemon will be a long way from the application. This may result in PCP client connections timing out before connecting to the remote <code>pmcd</code>. If this is occurring, set the environment variable <code>PMCD_CONNECT_TIMEOUT</code> to a higher value than the default (5 seconds). Refer to <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3) for further details about this variable.</p>
<dt>6)</p>
<dd> When using <code>pmsocks</code> to connect to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), but <i>&#8220;Connection Refused&#8221;</i> error messages are returned, it is not immediately obvious whether <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) is returning the error or <code>sockd</code>.</dl>
<h2>COPYRIGHT NOTICE</h2>
<p> <code>tsocks</code> is covered by the GPL license and is copyright Shaun Clowes (delius [at] progsoc.org).</p>
<h2>FILES</h2>
<dl>
<dt><code>/etc/tsocks.conf</code></p>
<dd> configuration file</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pminfo/">pminfo</a></code>(1), <code><a href="/docs/linux/man/1-pmlogger/">pmlogger</a></code>(1), <code><a href="/docs/linux/man/1-pmval/">pmval</a></code>(1), <code><a href="/docs/linux/man/1-x/">X</a></code>(1), <code><a href="/docs/linux/man/3-pmapi/">PMAPI</a></code>(3), <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5), and <code><a href="/docs/linux/man/5-tsocks/">tsocks</a></code>(5). </p>
<h2>Index</h2>
