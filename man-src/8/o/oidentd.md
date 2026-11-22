---
title: "oidentd(8)"
name: "oidentd"
section: "8"
letter: "o"
url: "/docs/linux/man/8-oidentd/"
description: "oidentd – TCP/IP IDENT protocol server"
---

<p>oidentd &#8211; TCP/IP IDENT protocol server</p>
<h2>Synopsis</h2>
<p><code>oidentd [options]</code> <code>[ -dehiImoqSv ]</code><br/>
 <code>[ -a &lt;host&gt; ]</code><br/>
 <code>[ -c &lt;charset&gt; ]</code><br/>
 <code>[ -C &lt;config file&gt; ]</code><br/>
 <code>[ -f &lt;port&gt; ]</code><br/>
 <code>[ -p &lt;port&gt; ]</code><br/>
 <code>[ -P &lt;host&gt; ]</code><br/>
 <code>[ -o or &#8211;other=[&lt;OS string&gt;] ]</code><br/>
 <code>[ -t or &#8211;timeout=&lt;seconds&gt; ]</code><br/>
 <code>[ -g or &#8211;group=&lt;group|GID&gt; ]</code><br/>
 <code>[ -l or &#8211;limit=&lt;number&gt;]</code><br/>
 <code>[ -r or &#8211;reply=&lt;string&gt; ]</code><br/>
 <code>[ -u or &#8211;user=&lt;username|UID&gt; ]</code> </p>
<h2>Description</h2>
<p><code>oidentd</code> is a server that implements the TCP/IP standard IDENT user identification protocol as specified in the RFC 1413 document. <code>oidentd</code> operates by looking up specific TCP connections and returning the user name of the process owning the connection. </p>
<h2>Options</h2>
<dl>
<dt><code>-a or &#8211;address=&lt;address|hostname&gt;</code></dt>
<dd>Listen for connections on the specified address. The default is to listen for connections on all configured IP addresses. </dd>
<dt><code>-c or &#8211;charset=&lt;charset&gt;</code></dt>
<dd>Use the specified alternate charset. </dd>
<dt><code>-C or &#8211;config=&lt;config file&gt;</code></dt>
<dd>Use the specified file as the configuration file. The default location of the configuration file is <code>/etc/oidentd.conf</code>. </dd>
<dt><code>-d or &#8211;debug</code></dt>
<dd>Enable debugging. This causes debugging messages to be printed via syslog. This option can be useful when trying to track down the cause of failed lookups. </dd>
<dt><code>-e or &#8211;error</code></dt>
<dd>Return &quot;UNKNOWN-ERROR&quot; for all errors, so as not to divulge any unnecessary information to remote clients. </dd>
<dt><code>-f or &#8211;forward=[&lt;port&gt;]</code></dt>
<dd>When IP masquerading support is enabled, forward requests for machines that masquerade through us to those machines on the specified port. If a port is not given, oidentd will use the default port for the ident service (&quot;auth&quot; or port 113). If the forwarded request fails, <code>oidentd</code> will fall back to reading the <code>/etc/oidentd_masq.conf</code> file. In order for forwarding to work, the machine to which the connection is forwarded must also be running oidentd, and oidentd must be run with the -P switch specifying the host that is forwarding the connections. If the ident daemon on the host to which the connection is forwarded is capable of returning a fixed string for any lookup (for example, the ident server built in to the mIRC windows IRC client), it is not necessary to run oidentd on that host. </dd>
<dt><code>-g or &#8211;group=&lt;group|GID&gt;</code></dt>
<dd>Run with specified GID or group. </dd>
<dt><code>-i or &#8211;foreground</code></dt>
<dd>Run interactively, not as a daemon. This is useful when debugging, or when running from a service manager such as daemontools. </dd>
<dt><code>-I or &#8211;stdio</code></dt>
<dd>Service only a single client request then exit. The client is expected to be already connected via stdin and stdout. This mode is useful when running from listener utilities such as <code>inetd</code>(8), <code><a href="/docs/linux/man/8-xinetd/">xinetd</a></code>(8) or <code>tcpserver</code>(8). This option implies <code>-i</code> (run in foreground) also. </dd>
<dt><code>-l or &#8211;limit=&lt;number&gt;</code></dt>
<dd>Allow, at most, the specified number of open connections at once. </dd>
<dt><code>-m or &#8211;masq</code></dt>
<dd>Enable support for ident queries for masqueraded/NAT connections. See <code><a href="/docs/linux/man/5-oidentd_masq-conf/">oidentd_masq.conf</a></code>(5) for details on configuring support for masqueraded/NAT connections. </dd>
<dt><code>-o or &#8211;other=[&lt;string&gt;]</code></dt>
<dd>The string specified will be returned as the OS string by default for all successful ident lookups. If no argument is given, &quot;OTHER&quot; will be returned instead of the name of the operating system. Some requests may be interpreted as having failed by the client side (with ident in general, not just with <code>oidentd</code>), when some other string is returned instead of the actual name of the operating system. </dd>
<dt><code>-p or &#8211;port=&lt;port&gt;</code></dt>
<dd>Listen on the specified port. </dd>
<dt><code>-P or &#8211;proxy=&lt;host&gt;</code></dt>
<dd>The specified host acts as a proxy, forwarding connections to us. This option must be enabled when connections on the machine on which oidentd is running are masqueraded through another host and the host through which the connections are masqueraded forwards requests to us. </dd>
<dt><code>-q or &#8211;quiet</code></dt>
<dd>Quiet mode; do not log any status messages to syslog. </dd>
<dt><code>-S or &#8211;nosyslog</code></dt>
<dd>Log any status messages to stderr, not syslog. This is useful for debugging or integration with external loggers such as <code>multilog</code>(8). </dd>
<dt><code>-t or &#8211;timeout=&lt;seconds&gt;</code></dt>
<dd>Sets the number of seconds to wait for input from a client before closing the connection. </dd>
<dt><code>-u or &#8211;user=&lt;user|UID&gt;</code></dt>
<dd>Run with specified username or UID. </dd>
<dt><code>-U or &#8211;udb</code></dt>
<dd>Perform lookups in the UDB shared memory tables, both for connections originating on the local host and for masqueraded connections. When a match is found, it will be used instead of the values supplied by the operating system, for either masqueraded entries (with the -m flag) or normal TCP connections. Entries in the table which don&#8217;t match any local user will be returned verbatim. This allows oidentd to cooperate with other programs (e.g. RADIUS servers or proxies) to give valid replies for dynamic connections. </dd>
<dt><code>-r or &#8211;reply=&lt;string&gt;</code></dt>
<dd>Upon a failed lookup, the specified string will be returned to the client as if the lookup had succeeded. </dd>
<dt><code>-v or &#8211;version</code></dt>
<dd>Display version information and exit. </dd>
<dt><code>-h or &#8211;help</code></dt>
<dd>Display options and exit. </dd>
</dl>
<h2>Files</h2>
<dl>
<dt><code>/etc/oidentd.conf</code></dt>
<dd>The system-wide configuration file. </dd>
<dt><code>/etc/oidentd_masq.conf</code></dt>
<dd>The NAT/IP masquerading mappings. </dd>
<dt><code>$HOME/.oidentd.conf</code></dt>
<dd>Per-user configuration file. </dd>
</dl>
<h2>Author</h2>
<p>Ryan McCabe &lt;ryan [at] numb.org&gt;<br/>
 <a rel="nofollow" href="http://dev.ojnk.net">http://dev.ojnk.net</a></p>
<h2>Bugs</h2>
<p>Solaris lacks IPv6 support and NAT support. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/5-oidentd-conf/">oidentd.conf</a></code>(5) <code><a href="/docs/linux/man/5-oidentd_masq-conf/">oidentd_masq.conf</a></code>(5) </p>
