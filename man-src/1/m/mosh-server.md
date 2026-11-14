---
title: "mosh-server(1)"
name: "mosh-server"
section: "1"
letter: "m"
url: "/docs/linux/man/1-mosh-server/"
description: "mosh-server – server-side helper for mosh"
---

<h2 class="name">NAME</h2>
<p> mosh-server &#8211; server-side helper for mosh </p>
<h2>SYNOPSIS</h2>
<p> <code>mosh-server</code> new [-s] [-v] [-i <i>IP</i>] [-p <i>PORT</i>[:<i>PORT2</i>]] [-c <i>COLORS</i>] [&#8211; command&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> <code>mosh-server</code> is a helper program for the <code><a href="/docs/linux/man/1-mosh/">mosh</a>(1)</code> remote terminal application. </p>
<p> <code>mosh-server</code> binds to a high UDP port and chooses an encryption key to protect the session. It prints both on standard output, detaches from the terminal, and waits for the <code>mosh-client</code> to establish a connection. It will exit if no client has contacted it within 60 seconds. </p>
<p> By default, <code>mosh-server</code> binds to a port between 60000 and 61000 and executes the user&#8217;s login shell. </p>
<p> On platforms with <code>utempter</code>, <code>mosh-server</code> maintains an entry in the <code><a href="/docs/linux/man/5-utmp/">utmp</a>(5)</code> file to indicate its process ID, whether the session is connected, and the client&#8217;s current IP address. </p>
<p> <code>mosh-server</code> exits when the client terminates the connection. </p>
<h2>OPTIONS</h2>
<p> The argument &quot;new&quot; must be first on the command line to use command-line options. </p>
<dl>
<dt><code>-s</code></p>
<dd> bind to the local interface used for an incoming SSH connection, given in the <code>SSH_CONNECTION</code> environment variable (for multihomed hosts) </p>
<dt><code>-v</code></p>
<dd> Print some debugging information even after detaching. </p>
<dt><code>-i </code><i>IP</i></p>
<dd> IP address of the local interface to bind (for multihomed hosts) </p>
<dt><code>-p </code><i>PORT</i>[:<i>PORT2</i>]</p>
<dd> UDP port number or port-range to bind </p>
<dt><code>-c </code><i>COLORS</i></p>
<dd> Number of colors to advertise to applications through TERM (e.g. 8, 256) </p>
<dt><code>-l </code><i>NAME=VALUE</i></p>
<dd> Locale-related environment variable to try as part of a fallback environment, if the startup environment does not specify a character set of UTF-8. </p>
</dl>
<h2>ENVIRONMENT VARIABLES</h2>
<p> These variables allow server-side configuration of Mosh&#8217;s behavior. They may be set by administrators in system login/rc files, /etc/login.conf, or similar mechanisms, or users in their shell&#8217;s login/rc files. <code>mosh-server</code> passes these variables to the login session and shell that it starts, but changing them there will have no effect. </p>
<dl>
<dt><code>MOSH_SERVER_NETWORK_TMOUT</code></p>
<dd> If this variable is set to a positive integer number, it specifies how long (in seconds) <code>mosh-server</code> will wait to receive an update from the client before exiting. Since mosh is very useful for mobile clients with intermittent operation and connectivity, we suggest setting this variable to a high value, such as 604800 (one week) or 2592000 (30 days). Otherwise, <code>mosh-server</code> will wait indefinitely for a client to reappear. This variable is somewhat similar to the <code>TMOUT</code> variable found in many Bourne shells. However, it is not a login-session inactivity timeout; it only applies to network connectivity. </p>
<dt><code>MOSH_SERVER_SIGNAL_TMOUT</code></p>
<dd> If this variable is set to a positive integer number, it specifies how long (in seconds) <code>mosh-server</code> will ignore SIGUSR1 while waiting to receive an update from the client. Otherwise, <code>SIGUSR1</code> will always terminate <code>mosh-server</code>. Users and administrators may implement scripts to clean up disconnected Mosh sessions. With this variable set, a user or administrator can issue </p>
<pre>
$ pkill -SIGUSR1 mosh-server
</pre>
<p> to kill disconnected sessions without killing connected login sessions. </p>
</dl>
<h2>EXAMPLE</h2>
<pre><code>
$ mosh - server MOSH CONNECT 60001 UAkFedSsVJs2LfMeKyQB5g mosh - server(mosh 1.1)[...](copyright notice omitted)[mosh - server detached, pid = 20443]
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-mosh/">mosh</a></code>(1), <code><a href="/docs/linux/man/1-mosh-client/">mosh-client</a></code>(1). </p>
<p> Project home page: <i><a rel="nofollow" href="http://mosh.mit.edu">http://mosh.mit.edu</a></i> </p>
<h2>AUTHOR</h2>
<p> mosh was written by Keith Winstein &lt;mosh-devel [at] mit.edu&gt;.</p>
<h2>BUGS</h2>
<p> Please report bugs to <i>mosh-devel [at] mit.edu</i>. Users may also subscribe to the <i>mosh-users [at] mit.edu</i> mailing list, at<br />
 <i><a rel="nofollow" href="http://mailman.mit.edu/mailman/listinfo/mosh-users">http://mailman.mit.edu/mailman/listinfo/mosh-users</a></i> </p>
<h2>Index</h2>
