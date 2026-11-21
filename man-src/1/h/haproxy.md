---

title: "haproxy(1)"
name: "haproxy"
section: "1"
letter: "h"
url: "/docs/linux/man/1-haproxy/"
description: "HAProxy – fast and reliable http reverse proxy and load balancer"
---

<p> HAProxy &#8211; fast and reliable http reverse proxy and load balancer</p>
<h2>SYNOPSIS</h2>
<p> haproxy -f &lt;configuration file&gt; [-L&nbsp;<wbr>&lt;name&gt;] [-n maxconn] [-N maxconn] [-C&nbsp;<wbr>&lt;dir&gt;] [-v|-vv] [-d] [-D] [-q] [-V] [-c] [-p&nbsp;<wbr>&lt;pidfile&gt;] [-dk] [-ds] [-de] [-dp] [-db] [-dM[&lt;byte&gt;]] [-m&nbsp;<wbr>&lt;megs&gt;] [{-sf|-st}&nbsp;<wbr>pidlist&#8230;] </p>
<h2>DESCRIPTION</h2>
<p> HAProxy is a TCP/HTTP reverse proxy which is particularly suited for high availability environments. Indeed, it can:<br />
&nbsp;<wbr>&#8211; route HTTP requests depending on statically assigned cookies&nbsp;<wbr>;<br />
&nbsp;<wbr>&#8211; spread the load among several servers while assuring server<br />
persistence through the use of HTTP cookies&nbsp;<wbr>;<br />
&nbsp;<wbr>&#8211; switch to backup servers in the event a main one fails&nbsp;<wbr>;<br />
&nbsp;<wbr>&#8211; accept connections to special ports dedicated to service<br />
monitoring&nbsp;<wbr>;<br />
&nbsp;<wbr>&#8211; stop accepting connections without breaking existing ones&nbsp;<wbr>;<br />
&nbsp;<wbr>&#8211; add/modify/delete HTTP headers both ways&nbsp;<wbr>;<br />
&nbsp;<wbr>&#8211; block requests matching a particular pattern&nbsp;<wbr>;<br />
&nbsp;<wbr>&#8211; hold clients to the right application server depending on<br />
application cookies<br />
&nbsp;<wbr>&#8211; report detailed status as HTML pages to authenticated users from an<br />
URI intercepted from the application. </p>
<p> It needs very little resource. Its event-driven architecture allows it to easily handle thousands of simultaneous connections on hundreds of instances without risking the system&#8217;s stability. </p>
<h2>OPTIONS</h2>
<dl>
<dt><code>-f &lt;configuration file&gt;</code></dt>
<dd> Specify configuration file path. </dd>
<dt><code>-L &lt;name&gt;</code></dt>
<dd> Set the local instance&#8217;s peer name. Peers are defined in the <code>peers</code> configuration section and used for syncing stick tables between different instances. If this option is not specified, the local hostname is used as peer name. </dd>
<dt><code>-n &lt;maxconn&gt;</code></dt>
<dd> Set the high limit for the total number of simultaneous connections. </dd>
<dt><code>-N &lt;maxconn&gt;</code></dt>
<dd> Set the high limit for the per-listener number of simultaneous connections. </dd>
<dt><code>-C &lt;dir&gt;</code></dt>
<dd> Change directory to &lt;<i>dir</i>&gt; before loading any files. </dd>
<dt><code>-v</code></dt>
<dd> Display HAProxy&#8217;s version. </dd>
<dt><code>-vv</code></dt>
<dd> Display HAProxy&#8217;s version and all build options. </dd>
<dt><code>-d</code></dt>
<dd> Start in foreground with debugging mode enabled. When the proxy runs in this mode, it dumps every connections, disconnections, timestamps, and HTTP headers to stdout. This should NEVER be used in an init script since it will prevent the system from starting up. </dd>
<dt><code>-D</code></dt>
<dd> Start in daemon mode. </dd>
<dt><code>-Ds</code></dt>
<dd> Start in systemd daemon mode, keeping a process in foreground. </dd>
<dt><code>-q</code></dt>
<dd> Disable messages on output. </dd>
<dt><code>-V</code></dt>
<dd> Displays messages on output even when -q or &#8216;quiet&#8217; are specified. Some information about pollers and config file are displayed during startup. </dd>
<dt><code>-c</code></dt>
<dd> Only checks config file and exits with code 0 if no error was found, or exits with code 1 if a syntax error was found. </dd>
<dt><code>-p &lt;pidfile&gt;</code></dt>
<dd> Ask the process to write down each of its children&#8217;s pids to this file in daemon mode. </dd>
<dt><code>-dk</code></dt>
<dd> Disable use of <code>kqueue</code>(2). <code>kqueue</code>(2) is available only on BSD systems. </dd>
<dt><code>-ds</code></dt>
<dd> Disable use of speculative <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) is available only on Linux 2.6 and some custom Linux 2.4 systems. </dd>
<dt><code>-de</code></dt>
<dd> Disable use of <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7). <code><a href="/docs/linux/man/7-epoll/">epoll</a></code>(7) is available only on Linux 2.6 and some custom Linux 2.4 systems. </dd>
<dt><code>-dp</code></dt>
<dd> Disables use of <code><a href="/docs/linux/man/2-poll/">poll</a></code>(2). <code><a href="/docs/linux/man/2-select/">select</a></code>(2) might be used instead. </dd>
<dt><code>-dS</code></dt>
<dd> Disables use of <code><a href="/docs/linux/man/2-splice/">splice</a></code>(2), which is broken on older kernels. </dd>
<dt><code>-db</code></dt>
<dd> Disables background mode (stays in foreground, useful for debugging). For debugging, the &#8216;-db&#8217; option is very useful as it temporarily disables daemon mode and multi-process mode. The service can then be stopped by simply pressing Ctrl-C, without having to edit the config nor run full debug. </dd>
<dt><code>-dM[&lt;byte&gt;]</code></dt>
<dd> Initializes all allocated memory areas with the given &lt;<i>byte</i>&gt;. This makes it easier to detect bugs resulting from uninitialized memory accesses, at the expense of touching all allocated memory once. If &lt;<i>byte</i>&gt; is not specified, it defaults to 0x50 (ASCII &#8216;P&#8217;). </dd>
<dt><code>-m &lt;megs&gt;</code></dt>
<dd> Enforce a memory usage limit to a maximum of &lt;megs&gt; megabytes. </dd>
<dt><code>-sf &lt;pidlist&gt;</code></dt>
<dd> Send FINISH signal to the pids in pidlist after startup. The processes which receive this signal will wait for all sessions to finish before exiting. This option must be specified last, followed by any number of PIDs. Technically speaking, <code>SIGTTOU</code> and <code>SIGUSR1</code> are sent. </dd>
<dt><code>-st &lt;pidlist&gt;</code></dt>
<dd> Send TERMINATE signal to the pids in pidlist after startup. The processes which receive this signal will wait immediately terminate, closing all active sessions. This option must be specified last, followed by any number of PIDs. Technically speaking, <code>SIGTTOU</code> and <code>SIGTERM</code> are sent. </dd>
</dl>
<h2>LOGGING</h2>
<p> Since HAProxy can run inside a chroot, it cannot reliably access /dev/log. For this reason, it uses the UDP protocol to send its logs to the server, even if it is the local server. People who experience trouble receiving logs should ensure that their syslog daemon listens to the UDP socket. Several Linux distributions which ship with syslogd from the sysklogd package have UDP disabled by default. The <code>-r</code> option must be passed to the daemon in order to enable UDP. </p>
<h2>SIGNALS</h2>
<p> Some signals have a special meaning for the haproxy daemon. Generally, they are used between daemons and need not be used by the administrator.</p>
<dl>
<dt>&#8211; <code>SIGUSR1</code></dt>
<dd> Tells the daemon to stop all proxies and exit once all sessions are closed. It is often referred to as the &quot;soft-stop&quot; signal.</dd>
<dt>&#8211; <code>SIGTTOU</code></dt>
<dd> Tells the daemon to stop listening to all sockets. Used internally by <code>-sf</code> and <code>-st</code>.</dd>
<dt>&#8211; <code>SIGTTIN</code></dt>
<dd> Tells the daemon to restart listening to all sockets after a <code>SIGTTOU</code>. Used internally when there was a problem during hot reconfiguration.</dd>
<dt>&#8211; <code>SIGINT</code> and <code>SIGTERM</code></dt>
<dd> Both signals can be used to quickly stop the daemon.</dd>
<dt>&#8211; <code>SIGHUP</code></dt>
<dd> Dumps the status of all proxies and servers into the logs. Mostly used for trouble-shooting purposes.</dd>
<dt>&#8211; <code>SIGQUIT</code></dt>
<dd> Dumps information about memory pools on stderr. Mostly used for debugging purposes.</dd>
<dt>&#8211; <code>SIGPIPE</code></dt>
<dd> This signal is intercepted and ignored on systems without <code>MSG_NOSIGNAL</code>. </dd>
</dl>
<h2>SEE ALSO</h2>
<p> A much better documentation can be found in configuration.txt. On Debian systems, you can find this file in /usr/share/doc/haproxy/configuration.txt.gz. </p>
<h2>AUTHOR</h2>
<p> HAProxy was written by Willy Tarreau. This man page was written by Arnaud Cornet and Willy Tarreau. </p>
