---
title: "dbus-launch(1)"
name: "dbus-launch"
section: "1"
letter: "d"
url: "/docs/linux/man/1-dbus-launch/"
description: "dbus-launch – Utility to start a message bus from a shell script"
---

<h2 class="name">NAME</h2>
<p> dbus-launch &#8211; Utility to start a message bus from a shell script </p>
<h2>SYNOPSIS</h2>
<dl>
<dt> <code>dbus-launch</code> [&#8211;version] [&#8211;help] [&#8211;sh-syntax] [&#8211;csh-syntax] [&#8211;auto-syntax] [&#8211;binary-syntax] [&#8211;close-stderr] [&#8211;exit-with-session] [&#8211;exit-with-x11] [&#8211;autolaunch=<i>MACHINEID</i>] [&#8211;config-file=<i>FILENAME</i>] [<i>PROGRAM</i>] [<i>ARGS</i>&#8230;]</p>
<dd>
</dl>
<h2>DESCRIPTION</h2>
<dd>The <code>dbus-launch</code> command is used to start a session bus instance of <i>dbus-daemon</i> from a shell script. It would normally be called from a user&#8217;s login scripts. Unlike the daemon itself, <code>dbus-launch</code> exits, so backticks or the $() construct can be used to read information from <code>dbus-launch</code>. </p>
<p> With no arguments, <code>dbus-launch</code> will launch a session bus instance and print the address and PID of that instance to standard output. </p>
<p> You may specify a program to be run; in this case, <code>dbus-launch</code> will launch a session bus instance, set the appropriate environment variables so the specified program can find the bus, and then execute the specified program, with the specified arguments. See below for examples. </p>
<p> If you launch a program, <code>dbus-launch</code> will not print the information about the new bus to standard output. </p>
<p> When <code>dbus-launch</code> prints bus information to standard output, by default it is in a simple key-value pairs format. However, you may request several alternate syntaxes using the &#8211;sh-syntax, &#8211;csh-syntax, &#8211;binary-syntax, or &#8211;auto-syntax options. Several of these cause <code>dbus-launch</code> to emit shell code to set up the environment. </p>
<p> With the &#8211;auto-syntax option, <code>dbus-launch</code> looks at the value of the SHELL environment variable to determine which shell syntax should be used. If SHELL ends in &quot;csh&quot;, then csh-compatible code is emitted; otherwise Bourne shell code is emitted. Instead of passing &#8211;auto-syntax, you may explicitly specify a particular one by using &#8211;sh-syntax for Bourne syntax, or &#8211;csh-syntax for csh syntax. In scripts, it&#8217;s more robust to avoid &#8211;auto-syntax and you hopefully know which shell your script is written in. </p>
<p> See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] for more information about D-Bus. See also the man page for <i>dbus-daemon</i>.</p>
<h2>EXAMPLES</h2>
<p> Distributions running <code>dbus-launch</code> as part of a standard X session should run <code>dbus-launch &#8211;exit-with-session</code> after the X server has started and become available, as a wrapper around the &quot;main&quot; X client (typically a session manager or window manager), as in these examples: </p>
<p> <code>dbus-launch &#8211;exit-with-session gnome-session</code> </p>
<p> <code>dbus-launch &#8211;exit-with-session openbox</code> </p>
<p> <code>dbus-launch &#8211;exit-with-session ~/.xsession</code> </p>
<p> If your distribution does not do this, you can achieve similar results by running your session or window manager in the same way in a script run by your X session, such as ~/.xsession, ~/.xinitrc or ~/.Xclients. </p>
<p> To start a D-Bus session within a text-mode session, do not use <code>dbus-launch</code>. Instead, see <code><a href="/docs/linux/man/1-dbus-run-session/">dbus-run-session</a></code>(1). </p>
<dl>
<dt>
<dd>
<pre><code>
  ## test for an existing bus daemon, just to be safe
  if test -z "$DBUS_SESSION_BUS_ADDRESS" ;
  then##if not found, launch a new one
                              eval `dbus -
                          launch-- sh - syntax` echo "D-Bus per-session daemon address is: $DBUS_SESSION_BUS_ADDRESS" fi
</code></pre>
</dl>
<p> Note that in this case, dbus-launch will exit, and dbus-daemon will not be terminated automatically on logout.</p>
<h2>AUTOMATIC LAUNCHING</h2>
<p> If DBUS_SESSION_BUS_ADDRESS is not set for a process that tries to use D-Bus, by default the process will attempt to invoke dbus-launch with the &#8211;autolaunch option to start up a new session bus or find the existing bus address on the X display or in a file in ~/.dbus/session-bus/ </p>
<p> Whenever an autolaunch occurs, the application that had to start a new bus will be in its own little world; it can effectively end up starting a whole new session if it tries to use a lot of bus services. This can be suboptimal or even totally broken, depending on the app and what it tries to do. </p>
<p> There are two common reasons for autolaunch. One is ssh to a remote machine. The ideal fix for that would be forwarding of DBUS_SESSION_BUS_ADDRESS in the same way that DISPLAY is forwarded. In the meantime, you can edit the session.conf config file to have your session bus listen on TCP, and manually set DBUS_SESSION_BUS_ADDRESS, if you like. </p>
<p> The second common reason for autolaunch is an su to another user, and display of X applications running as the second user on the display belonging to the first user. Perhaps the ideal fix in this case would be to allow the second user to connect to the session bus of the first user, just as they can connect to the first user&#8217;s display. However, a mechanism for that has not been coded. </p>
<p> You can always avoid autolaunch by manually setting DBUS_SESSION_BUS_ADDRESS. Autolaunch happens because the default address if none is set is &quot;autolaunch:&quot;, so if any other address is set there will be no autolaunch. You can however include autolaunch in an explicit session bus address as a fallback, for example DBUS_SESSION_BUS_ADDRESS=&quot;something:,autolaunch:&quot; &#8211; in that case if the first address doesn&#8217;t work, processes will autolaunch. (The bus address variable contains a comma-separated list of addresses to try.) </p>
<p> The &#8211;autolaunch option is considered an internal implementation detail of libdbus, and in fact there are plans to change it. There&#8217;s no real reason to use it outside of the libdbus implementation anyhow.</p>
<h2>OPTIONS</h2>
<p> The following options are supported: </p>
<p> <code>&#8211;auto-syntax</code></p>
<dl>
<dt>
<dd> Choose &#8211;csh-syntax or &#8211;sh-syntax based on the SHELL environment variable.</dl>
<p> <code>&#8211;binary-syntax</code></p>
<dl>
<dt>
<dd> Write to stdout a nul-terminated bus address, then the bus PID as a binary integer of size sizeof(pid_t), then the bus X window ID as a binary integer of size sizeof(long). Integers are in the machine&#8217;s byte order, not network byte order or any other canonical byte order.</dl>
<p> <code>&#8211;close-stderr</code></p>
<dl>
<dt>
<dd> Close the standard error output stream before starting the D-Bus daemon. This is useful if you want to capture dbus-launch error messages but you don&#8217;t want dbus-daemon to keep the stream open to your application.</dl>
<p> <code>&#8211;config-file=FILENAME</code></p>
<dl>
<dt>
<dd> Pass &#8211;config-file=FILENAME to the bus daemon, instead of passing it the &#8211;session argument. See the man page for dbus-daemon</dl>
<p> <code>&#8211;csh-syntax</code></p>
<dl>
<dt>
<dd> Emit csh compatible code to set up environment variables.</dl>
<p> <code>&#8211;exit-with-x11</code></p>
<dl>
<dt>
<dd> If this option is provided, a persistent &quot;babysitter&quot; process will be created, and will connect to the X server. If it cannot do so, launching fails. If the &quot;babysitter&quot; process loses its X connection, it kills the message bus daemon, disconnecting all of its clients (which should exit in response). This avoids having leftover daemon processes from a user X session, after the X session has ended.</dl>
<p> <code>&#8211;exit-with-session</code></p>
<dl>
<dt>
<dd> If this option is provided, a persistent &quot;babysitter&quot; process will be created, as if for &#8211;exit-with-x11. If it cannot connect to the X server, it will monitor the terminal from which dbus-launch was started instead, and if it gets a HUP on stdin, the message bus daemon will be killed. This option is not recommended, since it will consume input from the terminal where it was started; it is mainly provided for backwards compatibility.</dl>
<p> <code>&#8211;autolaunch=MACHINEID</code></p>
<dl>
<dt>
<dd> This option implies that <code>dbus-launch</code> should scan for a previously-started session and reuse the values found there. If no session is found, it will start a new session. The &#8211;exit-with-session option is implied if &#8211;autolaunch is given. This option is for the exclusive use of libdbus, you do not want to use it manually. It may change in the future.</dl>
<p> <code>&#8211;sh-syntax</code></p>
<dl>
<dt>
<dd> Emit Bourne-shell compatible code to set up environment variables.</dl>
<p> <code>&#8211;version</code></p>
<dl>
<dt>
<dd> Print the version of dbus-launch</dl>
<p> <code>&#8211;help</code></p>
<dl>
<dt>
<dd> Print the help info of dbus-launch</dl>
<h2>NOTES</h2>
<p> If you run <code>dbus-launch myapp</code> (with any other options), dbus-daemon will <i>not</i> exit when <code>myapp</code> terminates: this is because <code>myapp</code> is assumed to be part of a larger session, rather than a session in its own right.</p>
<h2>AUTHOR</h2>
<p> See m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/doc/AUTHORS">http://www.freedesktop.org/software/dbus/doc/AUTHORS</a></code>m[]</p>
<h2>BUGS</h2>
<p> Please send bug reports to the D-Bus mailing list or bug tracker, see m[blue]<code><a rel="nofollow" href="http://www.freedesktop.org/software/dbus/">http://www.freedesktop.org/software/dbus/</a></code>m[] </p>
<h2>Index</h2>
