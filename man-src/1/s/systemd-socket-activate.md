---
title: "systemd-socket-activate(1)"
name: "systemd-socket-activate"
section: "1"
letter: "s"
url: "/docs/linux/man/1-systemd-socket-activate/"
description: "systemd-socket-activate – Test socket activation of daemons"
---

<h2 class="name">NAME</h2>
<p> systemd-socket-activate &#8211; Test socket activation of daemons </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>systemd-socket-activate</code> [OPTIONS&#8230;] <i>daemon</i> [OPTIONS&#8230;]</dl>
<h2>DESCRIPTION</h2>
<p> <code>systemd-socket-activate</code></p>
<dd>may be used to launch a socket-activated service program from the command line for testing purposes. It may also be used to launch individual instances of the service program per connection. </p>
<p> The daemon to launch and its options should be specified after options intended for <code>systemd-socket-activate</code>. </p>
<p> If the <code>&#8211;inetd</code> option is given, the socket file descriptor will be used as the standard input and output of the launched process. Otherwise, standard input and output will be inherited, and sockets will be passed through file descriptors 3 and higher. Sockets passed through <i>$LISTEN_FDS</i> to <code>systemd-socket-activate</code> will be passed through to the daemon, in the original positions. Other sockets specified with <code>&#8211;listen=</code> will use consecutive descriptors. By default, <code>systemd-socket-activate</code> listens on a stream socket, use <code>&#8211;datagram</code> and <code>&#8211;seqpacket</code> to listen on datagram or sequential packet sockets instead (see below).</p>
<h2>OPTIONS</h2>
<p> <code>-l </code><i>address</i>, <code>&#8211;listen=</code><i>address</i></p>
<dl>
<dt>
<dd> Listen on this <i>address</i>. Takes a string like &quot;2000&quot; or &quot;127.0.0.1:2001&quot;.</dl>
<p> <code>-a</code>, <code>&#8211;accept</code></p>
<dl>
<dt>
<dd> Launch an instance of the service program for each connection and pass the connection socket.</dl>
<p> <code>-d</code>, <code>&#8211;datagram</code></p>
<dl>
<dt>
<dd> Listen on a datagram socket (<code>SOCK_DGRAM</code>), instead of a stream socket (<code>SOCK_STREAM</code>). May not be combined with <code>&#8211;seqpacket</code>.</dl>
<p> <code>&#8211;seqpacket</code></p>
<dl>
<dt>
<dd> Listen on a sequential packet socket (<code>SOCK_SEQPACKET</code>), instead of a stream socket (<code>SOCK_STREAM</code>). May not be combined with <code>&#8211;datagram</code>.</dl>
<p> <code>&#8211;inetd</code></p>
<dl>
<dt>
<dd> Use the inetd protocol for passing file descriptors, i.e. as standard input and standard output, instead of the new-style protocol for passing file descriptors using <i>$LISTEN_FDS</i> (see above).</dl>
<p> <code>-E </code><i>VAR</i><code>[=</code><i>VALUE</i>], <code>&#8211;setenv=</code><i>VAR</i><code>[=</code><i>VALUE</i>]</p>
<dl>
<dt>
<dd> Add this variable to the environment of the launched process. If <i>VAR</i> is followed by &quot;=&quot;, assume that it is a variable-value pair. Otherwise, obtain the value from the environment of <code>systemd-socket-activate</code> itself.</dl>
<p> <code>&#8211;fdname=</code><i>NAME</i>[:<i>NAME</i>&#8230;]</p>
<dl>
<dt>
<dd> Specify names for the file descriptors passed. This is equivalent to setting <i>FileDescriptorName=</i> in socket unit files, and enables use of <code><a href="/docs/linux/man/3-sd_listen_fds_with_names/">sd_listen_fds_with_names</a></code>(3). Multiple entries may be specifies using separate options or by separating names with colons (&quot;:&quot;) in one option. In case more names are given than descriptors, superfluous ones will be ignored. In case less names are given than descriptors, the remaining file descriptors will be unnamed.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print a short version string and exit.</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> <i>$LISTEN_FDS</i>, <i>$LISTEN_PID</i>, <i>$LISTEN_FDNAMES</i></p>
<dl>
<dt>
<dd> See <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3).</dl>
<p> <i>$SYSTEMD_LOG_TARGET</i>, <i>$SYSTEMD_LOG_LEVEL</i>, <i>$SYSTEMD_LOG_TIME</i>, <i>$SYSTEMD_LOG_COLOR</i>, <i>$SYSTEMD_LOG_LOCATION</i></p>
<dl>
<dt>
<dd> Same as in <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</dl>
<h2>EXAMPLES</h2>
<p> <code>Example 1. Run an echo server on port 2000</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-socket-activate -l 2000 --inetd -a cat
</pre>
</dl>
<p> <code>Example 2. Run a socket-activated instance of <a href="/docs/linux/man/8-systemd-journal-gatewayd/">systemd-journal-gatewayd</a>(8)</code> </p>
<dl>
<dt>
<dd>
<pre>
$ systemd-socket-activate -l 19531 /lib/systemd/systemd-journal-gatewayd
</pre>
</dl>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/1-systemd-run/">systemd-run</a></code>(1), <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3), <code><a href="/docs/linux/man/3-sd_listen_fds_with_names/">sd_listen_fds_with_names</a></code>(3), <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) </p>
<h2>Index</h2>
