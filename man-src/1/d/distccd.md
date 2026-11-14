---
title: "distccd(1)"
name: "distccd"
section: "1"
letter: "d"
url: "/docs/linux/man/1-distccd/"
description: "distccd – distributed C/C++ compiler server"
---

<h2>NAME</h2>
<p> distccd &#8211; distributed C/C++ compiler server</p>
<h2>SYNOPSIS</h2>
<p> <code>distccd &#8211;daemon </code> <i>[OPTIONS]</i></p>
<h2>DESCRIPTION</h2>
<p> <i>distccd </i> is the server for the <a href="/docs/linux/man/1-distcc/">distcc</a>(1) distributed compiler. It accepts and runs compilation jobs for network clients. </p>
<p> distcc can run over either TCP or a connection command such as <a href="/docs/linux/man/1-ssh/">ssh</a>(1). TCP connections are fast but relatively insecure. SSH connections are secure but slower. </p>
<p> For SSH connections, distccd must be installed on the volunteer but should not run as a daemon &#8212; it will be started over SSH as needed. SSH connections have several advantages: neither the client nor server listens on any new ports; compilations run with the privileges of the user that requested them; unauthorized users cannot access the server; and source and output is protected in transit. </p>
<p> For TCP connections, distccd can run either from an inetd-style program, or as a standalone server. Standalone mode is recommended because it is slightly more efficient and allows distccd to regulate the number of incoming jobs. The <code>&#8211;listen</code> and <code>&#8211;allow</code> options can be used for simple IP-based access control. </p>
<p> distcc may be started either by root or any other user. If run by root, it gives away privileges and changes to the user specified by the <code>&#8211;user</code> option, or the user called &quot;distcc&quot;, or the user called &quot;nobody&quot;. </p>
<p> distccd does not have a configuration file; it&#8217;s behaviour is controlled only by command-line options and requests from clients.</p>
<h2>STANDALONE SERVER</h2>
<p> The recommended method for running distccd is as a standalone server. distccd will listen for network connections and fork several child processes to serve them. </p>
<p> If you installed distcc using a packaged version you may be able to start the server using the standard mechanism for your operating system, such as</p>
<dl>
<dt>
<dd>
<p> # service distcc start</dl>
<p> To start distccd as a standalone service, run a command like this either as root or an ordinary user:</p>
<dl>
<dt>
<dd>
<p> # distccd &#8211;daemon</dl>
<h2>RUNNING FROM INIT</h2>
<p> distccd may be run as a standalone daemon under the control of another program like <a href="/docs/linux/man/8-init/">init</a>(8) or daemontools. The super-server starts distccd when the system boots, and whenever it exits. </p>
<p> distccd should be started just as for a standalone server, except that the <code>&#8211;no-detach</code> option should be used so that the super-server can monitor it. </p>
<p> For example, to add distccd as a process to Linux sysvinit, add this line to <i>/etc/inittab</i></p>
<dl>
<dt>
<dd>
<p> dscc:2345:respawn:/usr/local/bin/distccd &#8211;verbose &#8211;no-detach &#8211;daemon</dl>
<h2>RUNNING FROM INETD</h2>
<p> distccd may be started from a network super-server such as inetd or xinetd. In this case inetd listens for network connections and invokes distccd when one arrives. </p>
<p> This is slightly less efficient than running a standalone distccd daemon. distccd is not able to regulate the number of concurrent jobs accepted, but there may be an option in your inetd configuration to do so. </p>
<p> For traditional Unix inetd, a line like this can be added to /etc/inetd.conf:</p>
<dl>
<dt>
<dd>
<p> distcc stream tcp nowait.6000 root /usr/local/bin/distccd distccd &#8211;inetd</dl>
<p> inetd imposes a limit on the rate of connections to a service to protect against accidental or intentional overuse. The default in Linux NetKit inetd is 40 per minute, which is far too low for distccd. The .6000 option raises the limit to 6000 per minute.</p>
<h2>TERMINATING DISTCCD</h2>
<p> To shut down a standalone server, send a SIGTERM signal to the parent process. The most reliable way to do this from a script is to use the <i>&#8211;pid-file</i> option to record its process ID. Shutting down the server in this way should allow any jobs currently in progress to complete.</p>
<h2>OPTIONS</h2>
<dl>
<dt><code>&#8211;help</code></p>
<dd> Display summary usage information.</p>
<dt><code>&#8211;version</code></p>
<dd> Shows the daemon version and exits.</p>
<dt><code>-j, &#8211;jobs JOBS</code></p>
<dd> Sets a limit on the number of jobs that can be accepted at any time. By default this is set to two greater than the number of CPUs on the machine, to allow for some processes being blocked on network IO. (Daemon mode only.)</p>
<dt><code>-N, &#8211;nice NICENESS</code></p>
<dd> Makes the daemon more nice about giving up the CPU to other tasks on the machine. NICENESS is an increment to the current priority of the process. The range of priorities depends on the operating system but is typically 0 to 20. By default the niceness is increased by 5.</p>
<dt><code>-p, &#8211;port PORT</code></p>
<dd> Set the TCP port to listen on, rather than the default of 3632. (Daemon mode only.)</p>
<dt><code>&#8211;listen ADDRESS</code></p>
<dd> Instructs the distccd daemon to listen on the IP address ADDRESS. This can be useful for access control on dual-homed hosts. (Daemon mode only.)</p>
<dt><code>-P, &#8211;pid-file FILE</code></p>
<dd> Save daemon process id to file FILE. (Daemon mode only.)</p>
<dt><code>&#8211;user USER</code></p>
<dd> If distccd gets executed as root, change to user USER.</p>
<dt><code>-a, &#8211;allow IPADDR[/MASK]</code></p>
<dd> Instructs distccd to accept connections from the IP address IPADDR. A CIDR mask length can be supplied optionally after a trailing slash, e.g. 192.168.0.0/24, in which case addresses that match in the most significant MASK bits will be allowed. If no &#8211;allow options are specified, distccd will exit immediately! Unauthorized connections are rejected by closing the TCP connection immediately. A warning is logged on the server but nothing is sent to the client.</p>
<dt><code>&#8211;job-lifetime SECONDS</code></p>
<dd> Kills a distccd job if it runs for more than SECONDS seconds. This prevents denial of service from clients that don&#8217;t properly disconnect and compilers that fail to terminate. By default this is turned off.</p>
<dt><code>&#8211;no-detach</code></p>
<dd> Do not detach from the shell that started the daemon.</p>
<dt><code>&#8211;no-fork</code></p>
<dd> Don&#8217;t fork children for each connection, to allow attaching gdb. Don&#8217;t use this if you don&#8217;t understand it!</p>
<dt><code>&#8211;log-file FILE</code></p>
<dd> Send messages to file FILE instead of syslog. Logging directly to a file is significantly faster than going via syslog and is recommended.</p>
<dt><code>&#8211;log-level LEVEL</code></p>
<dd> Set the minimum severity of error that will be included in the log file. Useful if you only want to see error messages rather than an entry for each connection. LEVEL can be any of the standard syslog levels, and in particular <i>critical, error, warning, notice, info, </i> or <i>debug.</i></p>
<dt><code>&#8211;log-stderr</code></p>
<dd> Send log messages to stderr, rather than to a file or syslog. This is mainly intended for use in debugging. Do not use in inetd mode.</p>
<dt><code>&#8211;verbose</code></p>
<dd> Include debug messages in log. Equivalent to <code>&#8211;log-level=debug</code></p>
<dt><code>&#8211;wizard</code></p>
<dd> Turn on all options appropriate for starting distccd under gdb: run as a daemon, log verbosely to stderr, and do not detach or fork. For wizards only.</p>
<dt><code>&#8211;stats</code></p>
<dd> Turn on the statistics HTTP server. By default it is off. (Daemon mode only.)</p>
<dt><code>&#8211;stats-port PORT</code></p>
<dd> Set the TCP port to listen on for HTTP requests, rather than the default of 3633. (Daemon mode only.)</p>
<dt><code>&#8211;inetd</code></p>
<dd> Serve a client connected to stdin/stdout. As the name suggests, this option should be used when distccd is run from within a super-server like inetd. distccd assumes inetd mode when stdin is a socket.</p>
<dt><code>&#8211;daemon</code></p>
<dd> Bind and listen on a socket, rather than running from inetd. This is used for standalone mode. distccd assumes daemon mode at startup if stdin is a tty, so &#8211;daemon should be explicitly specified when starting distccd from a script or in a non-interactive ssh connection.</p>
<dt><code>&#8211;zeroconf</code></p>
<dd> Register the availability of this distccd server using Avahi Zeroconf DNS Service Discovery (DNS-SD). This allows distcc clients on the local network to access this distccd server without explicitly listing its host name or IP address in their distcc host list: the distcc clients can just use &quot;+zeroconf&quot; in their distcc host lists. <code>This option is only available if distccd was compiled with</code> <code>Avahi support enabled.</code></p>
<dt><code>&#8211;auth</code></p>
<dd> Peform GSS-API based mutual authentication. <code>This option is only available if distccd was compiled with</code> <code>the &#8211;with-auth configure option.</code></p>
<dt><code>&#8211;show-principal</code></p>
<dd> Displays the name of the distccd security principal extracted from the environment. <code>This option is only available if distccd was compiled with</code> <code>the &#8211;with-auth configure option.</code></p>
<dt><code>&#8211;blacklist=FILE</code></p>
<dd> Instruct distccd to reject connections from users whose principal names are listed in FILE. <code>This option is only available if distccd was compiled with</code> <code>the &#8211;with-auth configure option and if distccd is run with the</code> <code>&#8211;auth option.</code></p>
<dt><code>&#8211;whitelist=FILE</code></p>
<dd> Instruct distccd to accept connections only from users whose principal names are listed in FILE. <code>This option is only available if distccd was compiled with</code> <code>the &#8211;with-auth configure option and if distccd is run with the</code> <code>&#8211;auth option.</code></dl>
<h2>SEARCH PATHS</h2>
<p> distcc can pass either a relative or an absolute name for the compiler to distccd. If distcc is given an explicit absolute compiler filename, that name is used verbatim on both the client and server. If the compiler name is not an absolute path, or if the client is used in masquerade mode, then the server&#8217;s PATH is searched. </p>
<p> distccd inherits its search path from its parent process. By default distccd tries to remove directories that seem to contain distccd masquerade links, to guard against inadvertent recursion. The <code>DISTCCD_PATH</code> environment variable may be used to set the path. </p>
<p> The search path is logged when &#8211;verbose is given. In case of confusion, check the logs. </p>
<p> When distccd is run over ssh, the <i>$HOME/.ssh/environment </i> file may be useful in setting the path. See <code><a href="/docs/linux/man/1-ssh/">ssh</a>(1).</code></p>
<h2>DIAGNOSTICS</h2>
<p> distccd logs messages to syslog&#8217;s <i>daemon</i> facility by default, which normally writes to <i>/var/log/daemon </i> or <i>/var/log/messages. </i> Log messages can be sent to a different file using the <code>&#8211;log-file option.</code></p>
<h2>ENVIRONMENT VARIABLES</h2>
<dl>
<dt><code>DISTCC_CMDLIST</code></p>
<dd> If the environment variable DISTCC_CMDLIST is set, load a list of supported commands from the file named by DISTCC_CMDLIST, and refuse to serve any command whose last DISTCC_CMDLIST_MATCHWORDS last words do not match those of a command in that list. See the comments in src/serve.c.</p>
<dt><code>DISTCC_CMDLIST_NUMWORDS</code></p>
<dd> The number of words, from the end of the command, to match. The default is 1.</p>
<dt><code>DISTCCD_PATH</code></p>
<dd> When starting distccd, if this value is set it will be used unaltered for the command-execution PATH. The code that normally tries to remove masquerade directories from the path is skipped.</p>
<dt><code>DISTCC_SAVE_TEMPS</code></p>
<dd> If set to 1, temporary files are not deleted after use.</dl>
<p> Note that <code>DISTCC_LOG</code> does not affect the log destination for the server.</p>
<dl>
<dt><code>DISTCC_TCP_DEFER_ACCEPT</code></p>
<dd> On Linux, turn on the TCP_DEFER_ACCEPT socket option. Defaults to on.</p>
<dt><code>TMPDIR</code></p>
<dd> Directory for temporary files such as preprocessor output. By default /tmp/ is used.</p>
<dt><code>DISTCCD_PRINCIPAL</code></p>
<dd> If set, specifies the name of the principal that distccd runs under, and is used to authenticate with the client. <code>This environment variable is only used if distccd was compiled with</code> <code>the &#8211;with-auth configure option and if distccd is run with the &#8211;auth option.</code></dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-distcc/">distcc</a></code>(1), <code><a href="/docs/linux/man/1-pump/">pump</a></code>(1), <code><a href="/docs/linux/man/1-include_server/">include_server</a></code>(1), <code><a href="/docs/linux/man/1-gcc/">gcc</a></code>(1), <code><a href="/docs/linux/man/1-make/">make</a></code>(1), and <code><a href="/docs/linux/man/1-ccache/">ccache</a></code>(1) <i><a rel="nofollow" href="http://code.google.com/p/distcc/">http://code.google.com/p/distcc/</a></i></p>
<h2>BUGS</h2>
<p> IP-based access control is not secure against attackers able to spoof TCP connections, and cannot discriminate different users on a client. </p>
<p> TCP connections are not secure against attackers able to observe or modify network traffic. </p>
<p> Because ccache does not cache compilation from <code>.i</code> files, it is not useful to call it from distccd.</p>
<h2>LICENCE</h2>
<p> You are free to use distcc. distcc (including this manual) may be copied, modified or distributed only under the terms of the GNU General Public Licence version 2 or later. distcc comes with absolutely no warrany. A copy of the GPL is included in the file COPYING.</p>
<h2>AUTHOR</h2>
<p> distcc was written by Martin Pool &lt;mbp [at] sourcefrog.net&gt;, with the co-operation of many scholars including Wayne Davison, Frerich Raabe, Dimitri Papadopoulos and others noted in the NEWS file. See <code><a href="/docs/linux/man/1-pump/">pump</a></code>(1) for the authors of pump mode. Please report bugs to &lt;distcc [at] lists.samba.org&gt;. </p>
<h2>Index</h2>
