---
title: "doveadm-who(1)"
name: "doveadm-who"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-who/"
description: "doveadm-who – Show who is logged in to the Dovecot server"
---

<h2>NAME</h2>
<p> doveadm-who &#8211; Show who is logged in to the Dovecot server</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] [<code>-f</code> <i>formatter</i>] <code>who&nbsp;<wbr></code>[<code>-1</code>] [<code>-a</code> <i>anvil_socket_path</i>] [<i>user</i>] [<i>ip</i>[<code>/</code><i>mask</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>who</code> command is used to show which users from which hosts are currently connected to which service.</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-f&nbsp;<wbr></code><i>formatter</i></p>
<dd> Specifies the <i>formatter</i> for formatting the output. Supported formatters are:</p>
<dl>
<dt>
<dd>
<dl>
<dt><code>flow</code></p>
<dd> prints each line with <i>key</i><code>=</code><i>value</i> pairs.</p>
<dt><code>pager</code></p>
<dd> prints each <i>key</i>:&nbsp;<wbr><i>value</i> pair on its own line and separates records with form feed character (<code>^L</code>).</p>
<dt><code>tab</code></p>
<dd> prints a table header followed by tab separated value lines.</p>
<dt><code>table</code></p>
<dd> prints a table header followed by adjusted value lines.</dl>
</dl>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> This command uses by default the output formatter <code>table</code>. </p>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-1</code></p>
<dd> Print one line per user and connection. Otherwise the connections are grouped by the username.</p>
<dt><code>-a&nbsp;<wbr></code><i>anvil_socket_path</i></p>
<dd> This option is used to specify an alternative socket. The option&#8217;s argument is either an absolute path to a local UNIX domain socket, or a hostname and port (<i>hostname</i>:<i>port</i>), in order to connect a remote host via a TCP socket. </p>
<p> By default <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will use the socket <i>/var/run/dovecot/anvil</i>. The socket may be located in another directory, when the default <i>base_dir</i> setting was overridden in <i>/etc/dovecot/dovecot.conf</i>.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>ip</i>[<code>/</code><i>mask</i>]</p>
<dd> Specify an <i>ip</i> address or network range, in CIDR notation, to reduce the result to matching connections.</p>
<dt><i>user</i></p>
<dd> List only users, whose name match <i>user</i>. It&#8217;s also possible to use wildcards in the <i>user</i> name.</dl>
<h2>EXAMPLE</h2>
<p> Show authenticated sessions, filtered by the client&#8217;s IP address. </p>
<pre>
<code>doveadm who ::1</code>
username                       # proto (pids)        (ips)
jane                           2 imap  (30155 30412) (::1)
<code>doveadm who 192.0.2.0/24</code>
username                        # proto (pids)  (ips)
john [at] example.com                1 imap  (30257) (192.0.2.34)
</pre>
<p> Show authenticated sessions, filtered by username. </p>
<pre>
<code>doveadm who pvo</code>
username         # proto (pids)                    (ips)
pvo              1 sieve (30343)                   (fd95:4eed:38ba::25)
pvo              4 imap  (25693 25686 25679 25669) (fd95:4eed:38ba::25)
<code>doveadm who ja*</code>
username                    # proto (pids)        (ips)
james                       1 imap  (30091)       (127.0.0.1)
jane                        2 imap  (30155 30412) (::1)
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1), <code><a href="/docs/linux/man/1-doveadm-kick/">doveadm-kick</a></code>(1) </p>
<h2>Index</h2>
