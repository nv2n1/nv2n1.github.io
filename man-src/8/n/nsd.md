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
<dt><code>-4</code></dt>
<dd>Only listen to IPv4 connections.</dd>
<dt><code>-6</code></dt>
<dd>Only listen to IPv6 connections.</dd>
<dt><code>-a</code><i> ip-address[@port]</i></dt>
<dd>Listen to the specified <i>ip-address</i>. The <i>ip-address</i> must be specified in numeric format (using the standard IPv4 or IPv6 notation). Optionally, a port number can be given. This flag can be specified multiple times to listen to multiple IP addresses. If this flag is not specified, <code>NSD</code> listens to the wildcard interface.</dd>
<dt><code>-c</code><i> configfile</i></dt>
<dd>Read specified <i>configfile</i> instead of the default <i>/etc/nsd/nsd.conf</i>. For format description see <a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a>(5).</dd>
<dt><code>-d</code></dt>
<dd>Do not fork, stay in the foreground.</dd>
<dt><code>-f</code><i> database</i></dt>
<dd>Use the specified <i>database</i> instead of the default of <i>&#8221;</i>. If a <code>zonesdir: </code> is specified in the config file this path can be relative to that directory.</dd>
<dt><code>-h</code></dt>
<dd>Print help information and exit.</dd>
<dt><code>-i</code><i> identity</i></dt>
<dd>Return the specified <i>identity</i> when asked for <i>CH TXT ID.SERVER</i> (This option is used to determine which server is answering the queries when they are anycast). The default is the name returned by gethostname(3).</dd>
<dt><code>-I</code><i> nsid</i></dt>
<dd>Add the specified <i>nsid</i> to the EDNS section of the answer when queried with an NSID EDNS enabled packet. As a sequence of hex characters or with ascii_ prefix and then an ascii string.</dd>
<dt><code>-l</code><i> logfile</i></dt>
<dd>Log messages to the specified <i>logfile</i>. The default is to log to stderr and syslog. If a <code>zonesdir: </code> is specified in the config file this path can be relative to that directory.</dd>
<dt><code>-N</code><i> count</i></dt>
<dd>Start <i>count</i> <code>NSD </code> servers. The default is 1. Starting more than a single server is only useful on machines with multiple CPUs and/or network adapters.</dd>
<dt><code>-n</code><i> number</i></dt>
<dd>The maximum <i>number</i> of concurrent TCP connection that can be handled by each server. The default is 100.</dd>
<dt><code>-P</code><i> pidfile</i></dt>
<dd>Use the specified <i>pidfile</i> instead of the platform specific default, which is mostly <i>/var/run/nsd/nsd.pid</i>. If a <code>zonesdir: </code> is specified in the config file, this path can be relative to that directory.</dd>
<dt><code>-p</code><i> port</i></dt>
<dd>Answer the queries on the specified <i>port</i>. Normally this is port 53.</dd>
<dt><code>-s</code><i> seconds</i></dt>
<dd>Produce statistics dump every <i>seconds</i> seconds. This is equal to sending <i>SIGUSR1</i> to the daemon periodically.</dd>
<dt><code>-t</code><i> chroot</i></dt>
<dd>Specifies a directory to <i>chroot </i> to upon startup. This option requires you to ensure that appropriate syslogd(8) socket (e.g. <i>chrootdir </i> /dev/log) is available, otherwise <code>NSD</code> won&#8217;t produce any log output.</dd>
<dt><code>-u</code><i> username</i></dt>
<dd>Drop user and group privileges to those of <i>username</i> after binding the socket. The <i>username</i> must be one of: username, id, or id.gid. For example: nsd, 80, or 80.80.</dd>
<dt><code>-V</code><i> level</i></dt>
<dd>This value specifies the verbosity level for (non-debug) logging. Default is 0.</dd>
<dt><code>-v</code></dt>
<dd>Print the version number of <code>NSD </code> to standard error and exit.</dd></dl>
<p> <code>NSD</code> reacts to the following signals:</p>
<dl>
<dt>SIGTERM</dt>
<dd>Stop answering queries, shutdown, and exit normally.</dd>
<dt>SIGHUP</dt>
<dd>Reload. Scans zone files and if changed (mtime) reads them in. Also reopens the logfile (assists logrotation).</dd>
<dt>SIGUSR1</dt>
<dd>Dump BIND8-style statistics into the log. Ignored otherwise.</dd></dl>
<h2>Files</h2>
<dl>
<dt>&quot;&quot;</dt>
<dd>default <code>NSD</code> database</dd>
<dt>/var/run/nsd/nsd.pid</dt>
<dd>the process id of the name server.</dd>
<dt>/etc/nsd/nsd.conf</dt>
<dd>default <code>NSD</code> configuration file</dd></dl>
<h2>Diagnostics</h2>
<p><code>NSD</code> will log all the problems via the standard syslog(8) <i>daemon</i> facility, unless the <code>-d</code> option is specified.</p>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/5-nsd-conf/">nsd.conf</a></i>(5), <i><a href="/docs/linux/man/8-nsd-checkconf/">nsd-checkconf</a></i>(8), <i><a href="/docs/linux/man/8-nsd-control/">nsd-control</a></i>(8)</p>
<h2>Authors</h2>
<p><code>NSD</code> was written by NLnet Labs and RIPE NCC joint team. Please see CREDITS file in the distribution for further details.</p>
