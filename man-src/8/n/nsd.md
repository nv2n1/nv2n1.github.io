---
title: "nsd(8)"
name: "nsd"
section: "8"
letter: "n"
url: "/docs/linux/man/8-nsd/"
description: "nsd – Name Server Daemon (NSD) version 4.1.14."
---

<p><code>nsd</code> &#8211; Name Server Daemon (NSD) version 4.1.14.</p>
<h2>Synopsis</h2>
<p><code>nsd</code> [<code>-4</code>] [<code>-6</code>] [<code>-a</code> <i>ip-address[@port]</i>] [<code>-c</code> <i>configfile</i>] [<code>-d</code>] [<code>-f</code> <i>database</i>] [<code>-h</code>] [<code>-i</code> <i>identity</i>] [<code>-I</code> <i>nsid</i>] [<code>-l</code> <i>logfile</i>] [<code>-N</code> <i>server-count</i>] [<code>-n</code> <i>noncurrent-tcp-count</i>] [<code>-P</code> <i>pidfile</i>] [<code>-p</code> <i>port</i>] [<code>-s</code> <i>seconds</i>] [<code>-t</code> <i>chrootdir</i>] [<code>-u</code> <i>username</i>] [<code>-V</code> <i>level</i>] [<code>-v</code>]</p>
<h2>Description</h2>
<p><code>NSD</code> is a complete implementation of an authoritative DNS nameserver. Upon startup, <code>NSD</code> will read the database specified with <code>-f</code> <i>database</i> argument and put itself into background and answers queries on port 53 or a different port specified with <code>-p</code> <i>port</i> option. The <i>database</i> is created if it does not exist. By default, <code>NSD </code> will bind to all local interfaces available. Use the <code>-a</code> <i>ip-address[@port]</i> option to specify a single particular interface address to be bound. If this option is given more than once, <code>NSD</code> will bind its UDP and TCP sockets to all the specified ip-addresses separately. If IPv6 is enabled when <code>NSD </code> is compiled an IPv6 address can also be specified. </p>
<h2>Options</h2>
<p>All the options can be specified in the configfile ( <code>-c </code> argument), except for the <code>-v </code> and <code>-h </code> options. If options are specified on the commandline, the options on the commandline take precedence over the options in the configfile. </p>
<p> Normally <code>NSD</code> should be started with the `<a href="/docs/linux/man/8-nsd-control/">nsd-control</a>(8) start` command invoked from a <i>/etc/rc.d/nsd.sh</i> script or similar at the operating system startup.</p>
<dl>
<dt><code>-4</code></p>
<dd>Only listen to IPv4 connections.</p>
<dt><code>-6</code></p>
<dd>Only listen to IPv6 connections.</p>
<dt><code>-a</code><i> ip-address[@port]</i></p>
<dd>Listen to the specified <i>ip-address</i>. The <i>ip-address</i> must be specified in numeric format (using the standard IPv4 or IPv6 notation). Optionally, a port number can be given. This flag can be specified multiple times to listen to multiple IP addresses. If this flag is not specified, <code>NSD</code> listens to the wildcard interface.</p>
<dt><code>-c</code><i> configfile</i></p>
<dd>Read specified <i>configfile</i> instead of the default <i>/etc/nsd/nsd.conf</i>. For format description see <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5).</p>
<dt><code>-d</code></p>
<dd>Do not fork, stay in the foreground.</p>
<dt><code>-f</code><i> database</i></p>
<dd>Use the specified <i>database</i> instead of the default of <i>&#8221;</i>. If a <code>zonesdir: </code> is specified in the config file this path can be relative to that directory.</p>
<dt><code>-h</code></p>
<dd>Print help information and exit.</p>
<dt><code>-i</code><i> identity</i></p>
<dd>Return the specified <i>identity</i> when asked for <i>CH TXT ID.SERVER</i> (This option is used to determine which server is answering the queries when they are anycast). The default is the name returned by <a href="/docs/linux/man/3-gethostname/">gethostname</a>(3).</p>
<dt><code>-I</code><i> nsid</i></p>
<dd>Add the specified <i>nsid</i> to the EDNS section of the answer when queried with an NSID EDNS enabled packet. As a sequence of hex characters or with ascii_ prefix and then an ascii string.</p>
<dt><code>-l</code><i> logfile</i></p>
<dd>Log messages to the specified <i>logfile</i>. The default is to log to stderr and syslog. If a <code>zonesdir: </code> is specified in the config file this path can be relative to that directory.</p>
<dt><code>-N</code><i> count</i></p>
<dd>Start <i>count</i> <code>NSD </code> servers. The default is 1. Starting more than a single server is only useful on machines with multiple CPUs and/or network adapters.</p>
<dt><code>-n</code><i> number</i></p>
<dd>The maximum <i>number</i> of concurrent TCP connection that can be handled by each server. The default is 100.</p>
<dt><code>-P</code><i> pidfile</i></p>
<dd>Use the specified <i>pidfile</i> instead of the platform specific default, which is mostly <i>/var/run/nsd/nsd.pid</i>. If a <code>zonesdir: </code> is specified in the config file, this path can be relative to that directory.</p>
<dt><code>-p</code><i> port</i></p>
<dd>Answer the queries on the specified <i>port</i>. Normally this is port 53.</p>
<dt><code>-s</code><i> seconds</i></p>
<dd>Produce statistics dump every <i>seconds</i> seconds. This is equal to sending <i>SIGUSR1</i> to the daemon periodically.</p>
<dt><code>-t</code><i> chroot</i></p>
<dd>Specifies a directory to <i>chroot </i> to upon startup. This option requires you to ensure that appropriate <a href="/docs/linux/man/8-syslogd/">syslogd</a>(8) socket (e.g. <i>chrootdir </i> /dev/log) is available, otherwise <code>NSD</code> won&#8217;t produce any log output.</p>
<dt><code>-u</code><i> username</i></p>
<dd>Drop user and group privileges to those of <i>username</i> after binding the socket. The <i>username</i> must be one of: username, id, or id.gid. For example: nsd, 80, or 80.80.</p>
<dt><code>-V</code><i> level</i></p>
<dd>This value specifies the verbosity level for (non-debug) logging. Default is 0.</p>
<dt><code>-v</code></p>
<dd>Print the version number of <code>NSD </code> to standard error and exit.</dl>
<p> <code>NSD</code> reacts to the following signals:</p>
<dl>
<dt>SIGTERM</p>
<dd>Stop answering queries, shutdown, and exit normally.</p>
<dt>SIGHUP</p>
<dd>Reload. Scans zone files and if changed (mtime) reads them in. Also reopens the logfile (assists logrotation).</p>
<dt>SIGUSR1</p>
<dd>Dump BIND8-style statistics into the log. Ignored otherwise.</dl>
<h2>Files</h2>
<dl>
<dt>&quot;&quot;</p>
<dd>default <code>NSD</code> database</p>
<dt>/var/run/nsd/nsd.pid</p>
<dd>the process id of the name server.</p>
<dt>/etc/nsd/nsd.conf</p>
<dd>default <code>NSD</code> configuration file</dl>
<h2>Diagnostics</h2>
<p><code>NSD</code> will log all the problems via the standard <a href="/docs/linux/man/8-syslog/">syslog</a>(8) <i>daemon</i> facility, unless the <code>-d</code> option is specified.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a></i>(5), <i><a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a></i>(8), <i><a href="/docs/linux/man/8-nsd-control/">nsd-control</a></i>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
