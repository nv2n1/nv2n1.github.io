---
title: "systemd-activate(8)"
name: "systemd-activate"
section: "8"
letter: "s"
url: "/docs/linux/man/8-systemd-activate/"
description: "systemd-activate – Test socket activation of daemons"
---

<p>systemd-activate &#8211; Test socket activation of daemons</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>/usr/lib/systemd/systemd-activate</code> [OPTIONS&#8230;] <i>daemon</i> [OPTIONS&#8230;]</dl>
<h2>Description</h2>
<p><code>systemd-activate</code></p>
<dd>can be used to launch a socket activated daemon from the command line for testing purposes. It can also be used to launch single instances of the daemon per connection (inetd-style). </p>
<p> The daemon to launch and its options should be specifed after options intended for <code>systemd-activate</code>. </p>
<p> If the <code>-a</code> option is given, file descriptor of the connection will be used as the standard input and output of the launched process. Otherwise, standard input and output will be inherited, and sockets will be passed through file descriptors 3 and higher. Sockets passed through <i>$LISTEN_FDS</i> to <code>systemd-activate</code> will be passed through to the dameon, in the original positions. Other sockets specified with <code>&#8211;listen</code> will use consecutive descriptors.</p>
<h2>Options</h2>
<p><code>-l </code><i>address</i>, <code>&#8211;listen=</code><i>address</i></p>
<dl>
<dd>Listen on this <i>address</i>. Takes a string like &quot;2000&quot; or &quot;127.0.0.1:2001&quot;.</dl>
<p> <code>-a</code>, <code>&#8211;accept</code></p>
<dl>
<dd>Launch a separate instance of daemon per connection and pass the connection socket as standard input and standard output.</dl>
<p> <code>-E </code><i>VAR</i><code>[=</code><i>VALUE</i>], <code>&#8211;setenv=</code><i>VAR</i><code>[=</code><i>VALUE</i>]</p>
<dl>
<dd>Add this variable to the environment of the launched process. If <i>VAR</i> is followed by &quot;=&quot;, assume that it is a variable-value pair. Otherwise, obtain the value from the environment of <code>systemd-activate</code> itself.</dl>
<p> <code>-h</code>, <code>&#8211;help</code></p>
<dl>
<dd>Print a short help text and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dd>Print a short version string and exit.</dl>
<h2>Environment Variables</h2>
<p><i>$LISTEN_FDS</i>, <i>$LISTEN_PID</i></p>
<dl>
<dd>See <code><a href="/docs/linux/man/3-sd_listen_fds/">sd_listen_fds</a></code>(3).</dl>
<p> <i>$SYSTEMD_LOG_TARGET</i>, <i>$SYSTEMD_LOG_LEVEL</i>, <i>$SYSTEMD_LOG_COLOR</i>, <i>$SYSTEMD_LOG_LOCATION</i></p>
<dl>
<dd>Same as in <code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1).</dl>
<h2>Examples</h2>
<p><code>Example 1. Run an echo server on port 2000</code> </p>
<dl>
<dd>
<pre>$ /usr/lib/systemd/systemd-activate -l 2000 -a cat</pre>
</dl>
<p> <code>Example 2. Run a socket activated instance of <a href="/docs/linux/man/8-systemd-journal-gatewayd/">systemd-journal-gatewayd</a>(8)</code> </p>
<dl>
<dd>
<pre>$ /usr/lib/systemd/systemd-activate -l 19531 /usr/lib/systemd/systemd-journal-gatewayd</pre>
</dl>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/1-systemd/">systemd</a></code>(1), <code><a href="/docs/linux/man/5-systemd-socket/">systemd.socket</a></code>(5), <code><a href="/docs/linux/man/5-systemd-service/">systemd.service</a></code>(5), <code><a href="/docs/linux/man/1-cat/">cat</a></code>(1) </p>
