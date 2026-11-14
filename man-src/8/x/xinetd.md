---
title: "xinetd(8)"
name: "xinetd"
section: "8"
letter: "x"
url: "/docs/linux/man/8-xinetd/"
description: "xinetd – the extended Internet services daemon"
---

<p>xinetd &#8211; the extended Internet services daemon</p>
<h2>Synopsis</h2>
<p><code>xinetd</code> [<i>options</i>]</p>
<h2>Description</h2>
<p><code>xinetd</code> performs the same function as <code>inetd</code>: it starts programs that provide Internet services. Instead of having such servers started at system initialization time, and be dormant until a connection request arrives, <code>xinetd</code> is the only daemon process started and it listens on all service ports for the services listed in its configuration file. When a request comes in, <code>xinetd</code> starts the appropriate server. Because of the way it operates, <code>xinetd</code> (as well as <code>inetd</code>) is also referred to as a super-server. </p>
<p> The services listed in <code>xinetd</code>&#8216;s configuration file can be separated into two groups. Services in the first group are called <i>multi-threaded</i> and they require the forking of a new server process for each new connection request. The new server then handles that connection. For such services, <code>xinetd</code> keeps listening for new requests so that it can spawn new servers. On the other hand, the second group includes services for which the service daemon is responsible for handling all new connection requests. Such services are called <i>single-threaded</i> and <code>xinetd</code> will stop handling new requests for them until the server dies. Services in this group are usually datagram-based. </p>
<p> So far, the only reason for the existence of a super-server was to conserve system resources by avoiding to fork a lot of processes which might be dormant for most of their lifetime. While fulfilling this function, <code>xinetd</code> takes advantage of the idea of a super-server to provide features such as access control and logging. Furthermore, <code>xinetd</code> is not limited to services listed in <i>/etc/services.</i> Therefore, anybody can use <code>xinetd</code> to start special-purpose servers. </p>
<p> BEWARE of xinetd reload termination handling. For services with type = INTERNAL, SIGTERM signal will be sent. For services without type = INTERNAL, SIGKILL signall will be sent. Take this into an account when dealing with proper handling of the SIGTERM and SIGKILL. It is important to be aware of this as your xinetd service could be killed on a xinetd reload.</p>
<h2>Options</h2>
<dl>
<dt><code>-d</code></p>
<dd>Enables debug mode. This produces a lot of debugging output, and it makes it possible to use a debugger on <code>xinetd</code>.</p>
<dt><code>-syslog</code><i> syslog_facility</i></p>
<dd>This option enables syslog logging of <code>xinetd</code>-produced messages using the specified syslog facility. The following facility names are supported: <i>daemon,</i> <i>auth,</i> <i>user,</i> <i>local[0-7]</i> (check <i><a href="/docs/linux/man/5-syslog-conf/">syslog.conf</a>(5)</i> for their meanings). This option is ineffective in debug mode since all relevant messages are sent to the terminal.</p>
<dt><code>-filelog</code><i> logfile</i></p>
<dd><code>xinetd</code>-produced messages will be placed in the specified file. Messages are always appended to the file. If the file does not exist, it will be created. This option is ineffective in debug mode since all relevant messages are sent to the terminal.</p>
<dt><code>-f</code><i> config_file</i></p>
<dd>Determines the file that <code>xinetd</code> uses for configuration. The default is <i>/etc/xinetd.conf</i>.</p>
<dt><code>-pidfile</code> pid_file</p>
<dd>The process ID is written to the file. This option is ineffective in debug mode.</p>
<dt><code>-dontfork</code></p>
<dd>Tells xinetd to stay in the foreground rather than detaching itself, to support being run from init or daemontools. This option automatically sets <code>-stayalive</code> (see below).</p>
<dt><code>-stayalive</code></p>
<dd>Tells xinetd to stay running even if no services are specified.</p>
<dt><code>-limit</code><i> proc_limit</i></p>
<dd>This option places a limit on the number of concurrently running processes that can be started by <code>xinetd.</code> Its purpose is to prevent process table overflows.</p>
<dt><code>-logprocs</code><i> limit</i></p>
<dd>This option places a limit on the number of concurrently running servers for remote userid acquisition.</p>
<dt><code>-version</code></p>
<dd>This option causes xinetd to print out its version information.</p>
<dt><code>-inetd_compat</code></p>
<dd>This option causes xinetd to read /etc/inetd.conf in addition to the standard xinetd config files. /etc/inetd.conf is read after the standard xinetd config files.</p>
<dt><code>-cc</code><i> interval</i></p>
<dd>This option instructs <code>xinetd</code> to perform periodic consistency checks on its internal state every <i>interval</i> seconds.</dl>
<p> The <i>syslog</i> and <i>filelog</i> options are mutually exclusive. If none is specified, the default is syslog using the <i>daemon</i> facility. You should not confuse <code>xinetd</code> messages with messages related to service logging. The latter are logged only if this is specified via the configuration file.</p>
<h2>Controlling Xinetd</h2>
<p><code>xinetd</code> performs certain actions when it receives certain signals. The actions associated with the specific signals can be redefined by editing <i>config.h</i> and recompiling.</p>
<dl>
<dt><code>SIGHUP</code></p>
<dd>causes a hard reconfiguration, which means that <code>xinetd</code> re-reads the configuration file and terminates the servers for services that are no longer available. Access control is performed again on running servers by checking the remote location, access times and server instances. If the number of server instances is lowered, some arbitrarily picked servers will be killed to satisfy the limit; this will happen <i>after</i> any servers are terminated because of failing the remote location or access time checks. Also, if the <code>INTERCEPT</code> flag was clear and is set, any running servers for that service will be terminated; <i>the purpose of this is to ensure that after a hard reconfiguration there will be no running servers that can accept packets from addresses that do not meet the access control criteria</i>.</p>
<dt><code>SIGQUIT</code></p>
<dd>causes program termination.</p>
<dt><code>SIGTERM</code></p>
<dd>terminates all running servers before terminating <code>xinetd</code>.</p>
<dt><code>SIGUSR1</code></p>
<dd>causes an internal state dump (the default dump file is <i>/var/run/xinetd.dump</i>; to change the filename, edit <i>config.h</i> and recompile).</p>
<dt><code>SIGIOT</code></p>
<dd>causes an internal consistency check to verify that the data structures used by the program have not been corrupted. When the check is completed <code>xinetd</code> will generate a message that says if the check was successful or not.</dl>
<p> On reconfiguration the log files are closed and reopened. This allows removal of old log files.</p>
<h2>Files</h2>
<dl>
<dt><code>/etc/xinetd.conf</code></p>
<dd>default configuration file</p>
<dt><code>/var/run/xinetd.dump</code></p>
<dd>default dump file</dl>
<h2>See Also</h2>
<p><i><a href="/docs/linux/man/8-inetd/">inetd</a>(8),</i> </p>
<p> <i><a href="/docs/linux/man/5-xinetd-conf/">xinetd.conf</a>(5),</i> </p>
<p> <i><a href="/docs/linux/man/5-xinetd-log/">xinetd.log</a>(5)</i> </p>
<p> <i><a rel="nofollow" href="http://cr.yp.to/daemontools.html">http://cr.yp.to/daemontools.html</a></i></p>
<h2>Author</h2>
<p>Panos Tsirigotis, CS Dept, University of Colorado, Boulder Rob Braun</p>
<h2>Pronunciation</h2>
<p>zy-net-d</p>
