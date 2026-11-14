---
title: "master(5)"
name: "master"
section: "5"
letter: "m"
url: "/docs/linux/man/5-master/"
description: "master – Postfix master process configuration file format"
---

<p>master &#8211; Postfix master process configuration file format</p>
<h2>Description</h2>
<p>The Postfix mail system is implemented by small number of (mostly) client commands that are invoked by users, and by a larger number of services that run in the background. </p>
<p> Postfix services are implemented by daemon processes. These run in the background under control of the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process. The master.cf configuration file defines how a client program connects to a service, and what daemon program runs when a service is requested. Most daemon processes are short-lived and terminate voluntarily after serving <code>max_use</code> clients, or after inactivity for <code>max_idle</code> or more units of time. </p>
<p> All daemons specified here must speak a Postfix-internal protocol. In order to execute non-Postfix software use the <code><a href="/docs/linux/man/8-local/">local</a></code>(8), <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8) or <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8) services, or run the server under control by <code><a href="/docs/linux/man/8-inetd/">inetd</a></code>(8) or equivalent. </p>
<p> After changing master.cf you must execute &quot;<code>postfix reload</code>&quot; to reload the configuration.</p>
<h2>Syntax</h2>
<p>The general format of the master.cf file is as follows:</p>
<dl>
<dt>&bull;</p>
<dd>Empty lines and whitespace-only lines are ignored, as are lines whose first non-whitespace character is a `#&#8217;.</p>
<dt>&bull;</p>
<dd>A logical line starts with non-whitespace text. A line that starts with whitespace continues a logical line.</p>
<dt>&bull;</p>
<dd>Each logical line defines a single Postfix service. Each service is identified by its name and type as described below. When multiple lines specify the same service name and type, only the last one is remembered. Otherwise, the order of master.cf service definitions does not matter.</dl>
<p> Each logical line consists of eight fields separated by whitespace. These are described below in the order as they appear in the master.cf file. </p>
<p> Where applicable a field of &quot;-&quot; requests that the built-in default value be used. For boolean fields specify &quot;y&quot; or &quot;n&quot; to override the default value.</p>
<dl>
<dt><code>Service name</code></p>
<dd>The service name syntax depends on the service type as described next.</p>
<dt><code>Service type</code></p>
<dd>Specify one of the following service types:</p>
<dl>
<dd>
<dl>
<dt><code>inet</code></p>
<dd>The service listens on a TCP/IP socket and is accessible via the network. </p>
<p> The service name is specified as <i>host:port</i>, denoting the host and port on which new connections should be accepted. The host part (and colon) may be omitted. Either host or port may be given in symbolic form (see <code><a href="/docs/linux/man/5-hosts/">hosts</a></code>(5) or <code><a href="/docs/linux/man/5-services/">services</a></code>(5)) or in numeric form (IP address or port number). Host information may be enclosed inside &quot;[]&quot;; this form is necessary only with IPv6 addresses. </p>
<p> Examples: a service named <code>127.0.0.1:smtp</code> or <code>::1:smtp</code> receives mail via the loopback interface only; and a service named <code>10025</code> accepts connections on TCP port 10025 via all interfaces configured with the <code>inet_interfaces</code> parameter. </p>
<p> Note: with Postfix version 2.2 and later specify &quot;<code>inet_interfaces = loopback-only</code>&quot; in main.cf, instead of hard-coding loopback IP address information in master.cf or in main.cf.</p>
<dt><code>unix</code></p>
<dd>The service listens on a UNIX-domain stream socket and is accessible for local clients only. </p>
<p> The service name is a pathname relative to the Postfix queue directory (pathname controlled with the <code>queue_directory</code> configuration parameter in main.cf). </p>
<p> On Solaris 8 and earlier systems the <code>unix</code> type is implemented with streams sockets.</p>
<dt><code>unix-dgram</code></p>
<dd>The service listens on a UNIX-domain datagram socket and is accessible for local clients only. </p>
<p> The service name is a pathname relative to the Postfix queue directory (pathname controlled with the <code>queue_directory</code> configuration parameter in main.cf).</p>
<dt><code>fifo</code> (obsolete)</p>
<dd>The service listens on a FIFO (named pipe) and is accessible for local clients only. </p>
<p> The service name is a pathname relative to the Postfix queue directory (pathname controlled with the <code>queue_directory</code> configuration parameter in main.cf).</p>
<dt><code>pass</code></p>
<dd>The service listens on a UNIX-domain stream socket, and is accessible to local clients only. It receives one open connection (file descriptor passing) per connection request. </p>
<p> The service name is a pathname relative to the Postfix queue directory (pathname controlled with the <code>queue_directory</code> configuration parameter in main.cf). </p>
<p> On Solaris 8 and earlier systems the <code>pass</code> type is implemented with streams sockets. </p>
<p> This feature is available as of Postfix version 2.5.</dl>
</dl>
<dt><code>Private (default: y)</code></p>
<dd>Whether or not access is restricted to the mail system. Internet (type <code>inet</code>) services can&#8217;t be private.</p>
<dt><code>Unprivileged (default: y)</code></p>
<dd>Whether the service runs with root privileges or as the owner of the Postfix system (the owner name is controlled by the <code>mail_owner</code> configuration variable in the main.cf file). </p>
<p> The <code><a href="/docs/linux/man/8-local/">local</a></code>(8), <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8), <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8), and <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) daemons require privileges.</p>
<dt><code>Chroot (default: Postfix &gt;= 3.0: n, Postfix &lt;3.0: y)</code></p>
<dd>Whether or not the service runs chrooted to the mail queue directory (pathname is controlled by the <code>queue_directory</code> configuration variable in the main.cf file). </p>
<p> Chroot should not be used with the <code><a href="/docs/linux/man/8-local/">local</a></code>(8), <code><a href="/docs/linux/man/8-pipe/">pipe</a></code>(8), <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8), and <code><a href="/docs/linux/man/8-virtual/">virtual</a></code>(8) daemons. Although the <code><a href="/docs/linux/man/8-proxymap/">proxymap</a></code>(8) server can run chrooted, doing so defeats most of the purpose of having that service in the first place. </p>
<p> The files in the examples/chroot-setup subdirectory of the Postfix source show how to set up a Postfix chroot environment on a variety of systems. See also BASIC_CONFIGURATION_README for issues related to running daemons chrooted.</p>
<dt><code>Wake up time (default: 0)</code></p>
<dd>Automatically wake up the named service after the specified number of seconds. The wake up is implemented by connecting to the service and sending a wake up request. A ? at the end of the wake-up time field requests that no wake up events be sent before the first time a service is used. Specify 0 for no automatic wake up. </p>
<p> The <code><a href="/docs/linux/man/8-pickup/">pickup</a></code>(8), <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8) and <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) daemons require a wake up timer.</p>
<dt><code>Process limit (default: $default_process_limit)</code></p>
<dd>The maximum number of processes that may execute this service simultaneously. Specify 0 for no process count limit. </p>
<p> NOTE: Some Postfix services must be configured as a single-process service (for example, <code><a href="/docs/linux/man/8-qmgr/">qmgr</a></code>(8)) and some services must be configured with no process limit (for example, <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8)). These limits must not be changed.</p>
<dt><code>Command name + arguments</code></p>
<dd>The command to be executed. Characters that are special to the shell such as &quot;&gt;&quot; or &quot;|&quot; have no special meaning here, and quotes cannot be used to protect arguments containing whitespace. To protect whitespace, use &quot;{&quot; and &quot;}&quot; as described below. </p>
<p> The command name is relative to the Postfix daemon directory (pathname is controlled by the <code>daemon_directory</code> configuration variable). </p>
<p> The command argument syntax for specific commands is specified in the respective daemon manual page. </p>
<p> The following command-line options have the same effect for all daemon programs:</p>
<dl>
<dd>
<dl>
<dt><code>-D</code></p>
<dd>Run the daemon under control by the command specified with the <code>debugger_command</code> variable in the main.cf configuration file. See DEBUG_README for hints and tips.</p>
<dt><code>-o { </code><i>name</i> = <i>value</i><code> }</code> (long form, Postfix &gt;= 3.0)</p>
<dd>
<dt><code>-o </code><i>name</i>=<i>value</i> (short form)</p>
<dd>Override the named main.cf configuration parameter. The parameter value can refer to other parameters as <i>$name</i> etc., just like in main.cf. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for syntax. </p>
<p> NOTE 1: With the &quot;long form&quot; shown above, whitespace after &quot;{&quot;, around &quot;=&quot;, and before &quot;}&quot; is ignored, and whitespace within the parameter value is preserved. </p>
<p> NOTE 2: with the &quot;short form&quot; shown above, do not specify whitespace around the &quot;=&quot; or in parameter values. To specify a parameter value that contains whitespace, use the long form described above, or use commas instead of spaces, or specify the value in main.cf. Example: </p>
<pre>/etc/postfix/master.cf:
 submission inet .... smtpd
 -o smtpd_xxx_yyy=$submission_xxx_yyy
/etc/postfix/main.cf
 submission_xxx_yyy = text with whitespace...</pre>
<p>NOTE 3: Over-zealous use of parameter overrides makes the Postfix configuration hard to understand and maintain. At a certain point, it might be easier to configure multiple instances of Postfix, instead of configuring multiple personalities via master.cf.</p>
<dt><code>-v</code></p>
<dd>Increase the verbose logging level. Specify multiple <code>-v</code> options to make a Postfix daemon process increasingly verbose.</p>
<dt>Other command-line arguments</p>
<dd>Specify &quot;{&quot; and &quot;}&quot; around command arguments that contain whitespace (Postfix 3.0 and later). Whitespace after &quot;{&quot; and before &quot;}&quot; is ignored.</dl>
</dl>
</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>BASIC_CONFIGURATION_README, basic configuration
DEBUG_README, Postfix debugging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Initial version by
Magnus Baeck
Lund Institute of Technology
Sweden
Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA
Wietse Venema
Google, Inc.
111 8th Avenue
New York, NY 10011, USA</pre>
