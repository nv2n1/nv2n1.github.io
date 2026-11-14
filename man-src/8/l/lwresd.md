---
title: "lwresd(8)"
name: "lwresd"
section: "8"
letter: "l"
url: "/docs/linux/man/8-lwresd/"
description: "lwresd – lightweight resolver daemon"
---

<p>lwresd &#8211; lightweight resolver daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>lwresd</code> [<code>-c&nbsp;<wbr></code><i>config-file</i>] [<code>-C&nbsp;<wbr></code><i>config-file</i>] [<code>-d&nbsp;<wbr></code><i>debug-level</i>] [<code>-f</code>] [<code>-g</code>] [<code>-i&nbsp;<wbr></code><i>pid-file</i>] [<code>-m&nbsp;<wbr></code><i>flag</i>] [<code>-n&nbsp;<wbr></code><i>#cpus</i>] [<code>-P&nbsp;<wbr></code><i>port</i>] [<code>-p&nbsp;<wbr></code><i>port</i>] [<code>-s</code>] [<code>-t&nbsp;<wbr></code><i>directory</i>] [<code>-u&nbsp;<wbr></code><i>user</i>] [<code>-v</code>] [<code>-4</code>] [<code>-6</code>]</dl>
<h2>Description</h2>
<p><code>lwresd</code></p>
<dd>is the daemon providing name lookup services to clients that use the BIND 9 lightweight resolver library. It is essentially a stripped-down, caching-only name server that answers queries using the BIND 9 lightweight resolver protocol rather than the DNS protocol. </p>
<p> <code>lwresd</code> listens for resolver queries on a UDP port on the IPv4 loopback interface, 127.0.0.1. This means that <code>lwresd</code> can only be used by processes running on the local machine. By default, UDP port number 921 is used for lightweight resolver requests and responses. </p>
<p> Incoming lightweight resolver requests are decoded by the server which then resolves them using the DNS protocol. When the DNS lookup completes, <code>lwresd</code> encodes the answers in the lightweight resolver format and returns them to the client that made the request. </p>
<p> If <i>/etc/resolv.conf</i> contains any <code>nameserver</code> entries, <code>lwresd</code> sends recursive DNS queries to those servers. This is similar to the use of forwarders in a caching name server. If no <code>nameserver</code> entries are present, or if forwarding fails, <code>lwresd</code> resolves the queries autonomously starting at the root name servers, using a built-in list of root server hints.</p>
<h2>Options</h2>
<p>-4</p>
<dl>
<dd>Use IPv4 only even if the host machine is capable of IPv6. <code>-4</code> and <code>-6</code> are mutually exclusive.</dl>
<p> -6</p>
<dl>
<dd>Use IPv6 only even if the host machine is capable of IPv4. <code>-4</code> and <code>-6</code> are mutually exclusive.</dl>
<p> -c <i>config-file</i></p>
<dl>
<dd>Use <i>config-file</i> as the configuration file instead of the default, <i>/etc/lwresd.conf</i>. <code>-c</code> can not be used with <code>-C</code>.</dl>
<p> -C <i>config-file</i></p>
<dl>
<dd>Use <i>config-file</i> as the configuration file instead of the default, <i>/etc/resolv.conf</i>. <code>-C</code> can not be used with <code>-c</code>.</dl>
<p> -d <i>debug-level</i></p>
<dl>
<dd>Set the daemon&#8217;s debug level to <i>debug-level</i>. Debugging traces from <code>lwresd</code> become more verbose as the debug level increases.</dl>
<p> -f</p>
<dl>
<dd>Run the server in the foreground (i.e. do not daemonize).</dl>
<p> -g</p>
<dl>
<dd>Run the server in the foreground and force all logging to <i>stderr</i>.</dl>
<p> -i <i>pid-file</i></p>
<dl>
<dd>Use <i>pid-file</i> as the PID file instead of the default, <i>/var/run/lwresd/lwresd.pid</i>.</dl>
<p> -m <i>flag</i></p>
<dl>
<dd>Turn on memory usage debugging flags. Possible flags are <i>usage</i>, <i>trace</i>, <i>record</i>, <i>size</i>, and <i>mctx</i>. These correspond to the ISC_MEM_DEBUGXXXX flags described in <i>&lt;isc/mem.h&gt;</i>.</dl>
<p> -n <i>#cpus</i></p>
<dl>
<dd>Create <i>#cpus</i> worker threads to take advantage of multiple CPUs. If not specified, <code>lwresd</code> will try to determine the number of CPUs present and create one thread per CPU. If it is unable to determine the number of CPUs, a single worker thread will be created.</dl>
<p> -P <i>port</i></p>
<dl>
<dd>Listen for lightweight resolver queries on port <i>port</i>. If not specified, the default is port 921.</dl>
<p> -p <i>port</i></p>
<dl>
<dd>Send DNS lookups to port <i>port</i>. If not specified, the default is port 53. This provides a way of testing the lightweight resolver daemon with a name server that listens for queries on a non-standard port number.</dl>
<p> -s</p>
<dl>
<dd>Write memory usage statistics to <i>stdout</i> on exit.</p>
<dl>
<dd><code>Note:</code> This option is mainly of interest to BIND 9 developers and may be removed or changed in a future release.</dl>
</dl>
<p> -t <i>directory</i></p>
<dl>
<dd>Chroot to <i>directory</i> after processing the command line arguments, but before reading the configuration file.</p>
<dl>
<dd><code>Warning:</code> This option should be used in conjunction with the <code>-u</code> option, as chrooting a process running as root doesn&#8217;t enhance security on most systems; the way <code><a href="/docs/linux/man/2-chroot/">chroot</a>(2)</code> is defined allows a process with root privileges to escape a chroot jail.</dl>
</dl>
<p> -u <i>user</i></p>
<dl>
<dd>Setuid to <i>user</i> after completing privileged operations, such as creating sockets that listen on privileged ports.</dl>
<p> -v</p>
<dl>
<dd>Report the version number and exit.</dl>
<h2>Files</h2>
<p><i>/etc/resolv.conf</i></p>
<dl>
<dd>The default configuration file.</dl>
<p> <i>/var/run/lwresd.pid</i></p>
<dl>
<dd>The default process-id file.</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/8-named/">named</a></code>(8), <code><a href="/docs/linux/man/3-lwres/">lwres</a></code>(3), <code><a href="/docs/linux/man/5-resolver/">resolver</a></code>(5).</p>
<h2>Author</h2>
<p>Internet Systems Consortium</p>
<h2>Copyright</h2>
<p>Copyright &#169; 2004, 2005, 2007-2009 Internet Systems Consortium, Inc. (&quot;ISC&quot;)<br />
 Copyright &#169; 2000, 2001 Internet Software Consortium.</p>
