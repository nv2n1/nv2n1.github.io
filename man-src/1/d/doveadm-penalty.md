---
title: "doveadm-penalty(1)"
name: "doveadm-penalty"
section: "1"
letter: "d"
url: "/docs/linux/man/1-doveadm-penalty/"
description: "doveadm-penalty – Show current penalties"
---

<h2>NAME</h2>
<p> doveadm-penalty &#8211; Show current penalties</p>
<h2>SYNOPSIS</h2>
<p> <code>doveadm</code> [<code>-Dv</code>] <code>penalty</code> [<code>-a</code> <i>anvil_socket_path</i>] [<i>ip</i>[<code>/</code><i>mask</i>]]</p>
<h2>DESCRIPTION</h2>
<p> The <code>doveadm penalty</code> command can be used to see the current penalties. (Extend me!/explain it)</p>
<h2>OPTIONS</h2>
<p> Global <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) <i>options</i>:</p>
<dl>
<dt><code>-D</code></p>
<dd> Enables verbosity and debug messages.</p>
<dt><code>-v</code></p>
<dd> Enables verbosity, including progress counter.</dl>
<p> Command specific <i>options</i>:</p>
<dl>
<dt><code>-a&nbsp;<wbr></code><i>anvil_socket_path</i></p>
<dd> This option is used to specify an alternative socket. The option&#8217;s argument is either an absolute path to a local UNIX domain socket, or a hostname and port (<i>hostname</i>:<i>port</i>), in order to connect a remote host via a TCP socket. </p>
<p> By default <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) will use the socket <i>/var/run/dovecot/anvil</i>. The socket may be located in another directory, when the default <i>base_dir</i> setting was overridden in <i>/etc/dovecot/dovecot.conf</i>.</dl>
<h2>ARGUMENTS</h2>
<dl>
<dt><i>ip</i>[/<i>mask</i>]</p>
<dd> To reduce/filter the output supply an IP address or a network range in CIDR notation (ip/mask).</dl>
<h2>EXAMPLE</h2>
<p> Show current penalties </p>
<pre>
<code>doveadm penalty</code>
IP               penalty last_penalty        last_update
192.0.2.222            3 2010-06-15 15:19:27 15:19:27
192.0.2.53             3 2010-06-15 15:19:34 15:19:34
</pre>
<h2>REPORTING BUGS</h2>
<p> Report bugs, including <i>doveconf -n</i> output, to the Dovecot Mailing List &lt;dovecot [at] dovecot.org&gt;. Information about reporting bugs is available at: <a rel="nofollow" href="http://dovecot.org/bugreport.html">http://dovecot.org/bugreport.html</a></p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-doveadm/">doveadm</a></code>(1) </p>
<h2>Index</h2>
