---
title: "dbus-run-session(1)"
name: "dbus-run-session"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-run-session/"
description: "dbus-run-session – start a process as a new D-Bus session"
---

<h2 class="name">NAME</h2>
<p> dbus-run-session &#8211; start a process as a new D-Bus session </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dbus-run-session</code> [&#8211;config-file&nbsp;<i>FILENAME</i>] [&#8211;dbus-daemon&nbsp;<i>BINARY</i>] [&#8211;] <i>PROGRAM</i> [<i>ARGUMENTS</i>&#8230;]</p>
<dt> <code>dbus-run-session</code> &#8211;help</p>
<dt> <code>dbus-run-session</code> &#8211;version</dl>
<h2>DESCRIPTION</h2>
<p> <code>dbus-run-session</code></p>
<dd>is used to start a session bus instance of <code>dbus-daemon</code> from a shell script, and start a specified program in that session. The <code>dbus-daemon</code> will run for as long as the program does, after which it will terminate. </p>
<p> One use is to run a shell with its own <code>dbus-daemon</code> in a text-mode or SSH session, and have the <code>dbus-daemon</code> terminate automatically on leaving the sub-shell, like this: </p>
<p> dbus-run-session &#8212; bash </p>
<p> or to replace the login shell altogether, by combining <code>dbus-run-session</code> with the <code>exec</code> builtin: </p>
<p> exec dbus-run-session &#8212; bash </p>
<p> Another use is to run regression tests and similar things in an isolated D-Bus session, to avoid either interfering with the &quot;real&quot; D-Bus session or relying on there already being a D-Bus session active, for instance: </p>
<p> dbus-run-session &#8212; make check </p>
<p> or (in <code><a href="/docs/linux/man/1-automake/">automake</a></code>(1)): </p>
<dl>
<dt>
<dd>
<pre>
  AM_TESTS_ENVIRONMENT = export MY_DEBUG=all;
  LOG_COMPILER = dbus-run-session
  AM_LOG_FLAGS = --
</pre>
</dl>
<h2>OPTIONS</h2>
<p> <code>&#8211;config-file=</code><i>FILENAME</i>, <code>&#8211;config-file</code> <i>FILENAME</i></p>
<dl>
<dt>
<dd> Pass <code>&#8211;config-file=</code><i>FILENAME</i> to the bus daemon, instead of passing it the <code>&#8211;session</code> argument. See <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1).</dl>
<p> <code>&#8211;dbus-daemon=</code><i>BINARY</i>, <code>&#8211;dbus-daemon</code> <i>BINARY</i></p>
<dl>
<dt>
<dd> Run <i>BINARY</i> as <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), instead of searching the <code>PATH</code> in the usual way for an executable called <code>dbus-daemon</code>.</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print usage information and exit.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version of dbus-run-session and exit.</dl>
<h2>EXIT STATUS</h2>
<p> <code>dbus-run-session</code> exits with the exit status of <i>PROGRAM</i>, 0 if the <code>&#8211;help</code> or <code>&#8211;version</code> options were used, 127 on an error within <code>dbus-run-session</code> itself, or 128+<i>n</i> if the <i>PROGRAM</i> was killed by signal <i>n</i>.</p>
<h2>ENVIRONMENT</h2>
<p> <code>PATH</code> is searched to find <i>PROGRAM</i>, and (if the &#8211;dbus-daemon option is not used or its argument does not contain a <code>/</code> character) to find <code>dbus-daemon</code>. </p>
<p> The session bus&#8217; address is made available to <i>PROGRAM</i> in the environment variable <code>DBUS_SESSION_BUS_ADDRESS</code>. </p>
<p> The variables <code>DBUS_SESSION_BUS_PID</code>, <code>DBUS_SESSION_BUS_WINDOWID</code>, <code>DBUS_STARTER_BUS_TYPE</code> and <code>DBUS_STARTER_ADDRESS</code> are removed from the environment, if present.</p>
<h2>BUGS</h2>
<p> Please send bug reports to the D-Bus mailing list or bug tracker, see m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[]</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/1-dbus-daemon/">dbus-daemon</a></code>(1), <code><a href="/docs/linux/man/1-dbus-launch/">dbus-launch</a></code>(1) </p>
<h2>Index</h2>
