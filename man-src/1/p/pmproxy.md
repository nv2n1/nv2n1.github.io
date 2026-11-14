---
title: "pmproxy(1)"
name: "pmproxy"
section: "1"
letter: "p"
url: "/docs/linux/man/1-pmproxy/"
description: "pmproxy – proxy for performance metrics collector daemon"
---

<h2>NAME</h2>
<p> <code>pmproxy</code> &#8211; proxy for performance metrics collector daemon</p>
<h2>SYNOPSIS</h2>
<p> <code>pmproxy</code> [<code>-Af</code>] [<code>-C</code> <i>dirname</i>] [<code>-i</code> <i>ipaddress</i>] [<code>-l</code> <i>logfile</i>] [<code>-L</code> <i>bytes</i>] [<code>-M</code> <i>certname</i>] [<code>-p</code> <i>port</i>[,<i>port</i> &#8230;] [<code>-P</code> <i>passfile</i>] [<code>-U</code> <i>username</i>] [<code>-x</code> <i>file</i>]</p>
<h2>DESCRIPTION</h2>
<p> <code>pmproxy</code> acts as a protocol proxy for <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), allowing Performance Co-Pilot (PCP) monitoring clients to connect to one or more <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) instances via <code>pmproxy</code>. </p>
<p> Normally <code>pmproxy</code> is deployed in a firewall domain, or on a &#8220;head&#8221; node of a cluster where the IP (Internet Protocol) address of the hosts where <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) is running may be unknown to the PCP monitoring clients, although the IP address of the host where <code>pmproxy</code> is running is known to these clients. Similarly, the clients may have network connectivity only to the host where <code>pmproxy</code> is running, while there is network connectivity from that host to the hosts of interest where <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) is running. </p>
<p> The behaviour of the PCP monitoring clients is controlled by either the <code>PMPROXY_HOST</code> environment variable or through the extended hostname specification (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for details). If neither of these mechanisms is used, clients will make their connections directly to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). If the proxy hostname syntax is used or <code>PMPROXY_HOST</code> is set, then this should be the hostname or IP address of the system where <code>pmproxy</code> is running, and the clients will connect to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) indirectly through the protocol proxy services of <code>pmproxy.</code> </p>
<p> The options to <code>pmproxy</code> are as follows.</p>
<dl>
<dt><code>-A</code></p>
<dd> Disable service advertisement. By default, <code>pmproxy</code> will advertise its presence on the network using any available mechanisms (such as Avahi/DNS-SD), assisting remote monitoring tools with finding it. These mechanisms are disabled with this option.</p>
<dt><code>-C</code> <i>dirname</i></p>
<dd> Specify the path to the Network Security Services certificate database, for (optional) secure connections. The default is <code>/etc/pki/nssdb</code>. Refer also to the <code>-P</code> option. If it does not already exist, this database can be created using the <code>certutil</code> utility. This process and other certificate database maintenance information is provided in the <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) manual page and the online PCP tutorials.</p>
<dt><code>-f</code></p>
<dd> By default <code>pmproxy</code> is started as a daemon. The <code>-f</code> option indicates that it should run in the foreground. This is most useful when trying to diagnose problems with establishing connections.</p>
<dt><code>-i</code> <i>ipaddress</i></p>
<dd> This option is usually only used on hosts with more than one network interface (very common for firewall and &#8220;head&#8221; node hosts where <code>pmproxy</code> is most likely to be deployed). If no <code>-i</code> options are specified <code>pmproxy</code> accepts PCP client connections on any of its host&#8217;s IP addresses. The <code>-i</code> option is used to specify explicitly an IP address that PCP client connections should be accepted on. <i>ipaddress</i> should be in the standard dotted form (e.g. 100.23.45.6). The <code>-i</code> option may be used multiple times to define a list of IP addresses. When one or more <code>-i</code> options is specified, attempted connections made on any other IP addresses will be refused.</p>
<dt><code>-l</code> <i>logfile</i></p>
<dd> By default a log file named <i>pmproxy.log</i> is written in the current directory. The <code>-l</code> option causes the log file to be written to <i>logfile</i> instead of the default. If the log file cannot be created or is not writable, output is written to the standard error instead.</p>
<dt><code>-L</code> <i>bytes</i></p>
<dd> <i>PDU</i>s received by <code>pmproxy </code> from PCP monitoring clients are restricted to a maximum size of 65536 bytes by default to defend against Denial of Service attacks. The <code>-L </code> option may be used to change the maximum incoming <i>PDU </i> size.</p>
<dt><code>-M</code> <i>certname</i></p>
<dd> By default, pmproxy will try to use a certificate called <code>PCP Collector certificate</code> in its server role. The <code>-M</code> option allows this to be changed.</p>
<dt><code>-P</code> <i>passfile</i></p>
<dd> Specify the path to a file containing the Network Security Services certificate database password for (optional) secure connections, and for databases that are password protected. Refer also to the <code>-C</code> option. When using this option, great care should be exercised to ensure appropriate ownership (&quot;pcp&quot; user, typically) and permissions on this file (0400, so as to be unreadable by any user other than the user running the <code>pmproxy</code> process).</p>
<dt><code>-U</code> <i>username</i></p>
<dd> Assume the identity of <i>username</i> before starting to accept incoming packets from PCP monitoring clients.</p>
<dt><code>-x</code> <i>file</i></p>
<dd> Before the <code>pmproxy</code> <i>logfile</i> can be opened, <code>pmproxy</code> may encounter a fatal error which prevents it from starting. By default, the output describing this error is sent to <code>/dev/tty</code> but it may redirected to <i>file</i>.</dl>
<h2>STARTING AND STOPPING PMPROXY</h2>
<p> Normally, <code>pmproxy</code> is started automatically at boot time and stopped when the system is being brought down. Under certain circumstances it is necessary to start or stop <code>pmproxy</code> manually. To do this one must become superuser and type </p>
<p> # $PCP_RC_DIR/pmproxy start </p>
<p> to start <code>pmproxy</code>, or </p>
<p> # $PCP_RC_DIR/pmproxy stop </p>
<p> to stop <code>pmproxy</code>. Starting <code>pmproxy</code> when it is already running is the same as stopping it and then starting it again. </p>
<p> Normally <code>pmproxy</code> listens for PCP client connections on TCP/IP port number 44322 (registered at <i><a rel="nofollow" href="http://www.iana.org/">http://www.iana.org/</a></i>). Either the environment variable <code>PMPROXY_PORT</code> <code>-p</code> command line option may be used to specify alternative port number(s) when <code>PMPROXY_PORT</code> or the <code>-p</code> command line option may be used to specify alternative port number(s) when <code>pmproxy</code> is started; in each case, the specification is a comma-separated list of one or more numerical port numbers. Should both methods be used or multiple <code>-p</code> options appear on the command line, <code>pmproxy</code> will listen on the union of the set of ports specified via all <code>-p</code> options and the <code>PMPROXY_PORT</code> environment variable. If non-default ports are used with <code>pmproxy</code> care should be taken to ensure that <code>PMPROXY_PORT</code> is also set in the environment of any client application that will connect to <code>pmproxy</code>, or that the extended host specification syntax is used (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for details).</p>
<h2>FILES</h2>
<dl>
<dt><code>PCP_PMPROXYOPTIONS_PATH</code></p>
<dd> command line options for <code>pmproxy</code> when launched from <code>$PCP_RC_DIR/pmproxy</code> All the command line option lines should start with a hyphen as the first character.</p>
<dt><code>$PCP_SYSCONFIG_DIR/pmproxy</code></p>
<dd> additional environment variables that will be set when <code>pmproxy</code> executes. Only settings of the form &quot;PMPROXY_VARIABLE=value&quot; will be honoured.</p>
<dt><code>./pmproxy.log</code></p>
<dd> (or <code>$PCP_LOG_DIR/pmproxy/pmproxy.log</code> when started automatically)<br />
 All messages and diagnostics are directed here</p>
<dt><code>/etc/pki/nssdb</code></p>
<dd> default Network Security Services (NSS) certificate database directory, used for optional Secure Socket Layer connections. This database can be created and queried using the NSS <code>certutil</code> tool, amongst others.</dl>
<h2>ENVIRONMENT</h2>
<p> In addition to the PCP environment variables described in the <code>PCP ENVIRONMENT</code> section below, there are several environment variables that influence the interactions between a PCP monitoring client, <code>pmcd</code> and <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1).</p>
<dl>
<dt><code>PMCD_PORT</code></p>
<dd> For the PCP monitoring client this (or the default port number) is passed to <code>pmproxy</code> and used to connect to <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1). In the environment of <code>pmproxy</code> <code>PMCD_PORT is not used.</code></p>
<dt><code>PMPROXY_HOST</code></p>
<dd> For the PCP monitoring client this is the hostname or IP address of the host where <code>pmproxy</code> is running. In recent versions of PCP (since version 3) this has been superseded by the extended hostname syntax (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1) for details).</p>
<dt><code>PMPROXY_PORT</code></p>
<dd> For the PCP monitoring client this is the port on which <code>pmproxy</code> will accept connections. The default is 44322.</p>
<dt><code>PMCD_CONNECT_TIMEOUT</code>, <code>PMCD_RECONNECT_TIMEOUT</code> and <code>PMCD_REQUEST_TIMEOUT</code></p>
<dd> (see <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1)) For the PCP monitoring client, setting these environment variables will modify the timeouts used for interactions between the client and <code>pmproxy</code> (independent of which <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) is being used). For <code>pmproxy</code> these same environment variables control the timeouts between <code>pmproxy</code> and all <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1) instances (independent of which monitoring client is involved).</dl>
<p> If set to the value 1, the <code>PMPROXY_LOCAL</code> environment variable will cause <code>pmproxy</code> to run in a localhost-only mode of operation, where it binds only to the loopback interface. </p>
<p> The <code>PMPROXY_MAXPENDING</code> variable can be set to indicate the maximum length to which the queue of pending client connections may grow.</p>
<h2>PCP ENVIRONMENT</h2>
<p> Environment variables with the prefix <code>PCP_</code> are used to parameterize the file and directory names used by PCP. On each installation, the file <code>/etc/pcp.conf</code> contains the local values for these variables. The <code>PCP_CONF</code> variable may be used to specify an alternative configuration file, as described in <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5).</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-pcpintro/">PCPIntro</a></code>(1), <code><a href="/docs/linux/man/1-pmcd/">pmcd</a></code>(1), <code><a href="/docs/linux/man/1-pmdbg/">pmdbg</a></code>(1), <code><a href="/docs/linux/man/5-pcp-conf/">pcp.conf</a></code>(5) and <code><a href="/docs/linux/man/5-pcp-env/">pcp.env</a></code>(5).</p>
<h2>DIAGNOSTICS</h2>
<p> If <code>pmproxy</code> is already running the message &quot;Error: OpenRequestSocket bind: Address already in use&quot; will appear. This may also appear if <code>pmproxy</code> was shutdown with an outstanding request from a client. In this case, a request socket has been left in the TIME_WAIT state and until the system closes it down (after some timeout period) it will not be possible to run <code>pmproxy</code>. </p>
<p> In addition to the standard <code>PCP</code> debugging flags, see <code><a href="/docs/linux/man/1-pmdbg/">pmdbg</a></code>(1), <code>pmproxy</code> currently uses <code>DBG_TRACE_CONTEXT</code> for tracing client connections and disconnections </p>
<h2>Index</h2>
