---
title: "master(8)"
name: "master"
section: "8"
letter: "m"
url: "/docs/linux/man/8-master/"
description: "master – Postfix master process"
---

<p>master &#8211; Postfix master process</p>
<h2>Synopsis</h2>
<pre><code>master</code> [<code>-Ddtvw</code>] [<code>-c </code><i>config_dir</i>] [<code>-e </code><i>exit_time</i>]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-master/">master</a></code>(8) daemon is the resident process that runs Postfix daemons on demand: daemons to send or receive messages via the network, daemons to deliver mail locally, etc. These daemons are created on demand up to a configurable maximum number per service. </p>
<p> Postfix daemons terminate voluntarily, either after being idle for a configurable amount of time, or after having serviced a configurable number of requests. Exceptions to this rule are the resident queue manager, address verification server, and the TLS session cache and pseudo-random number server. </p>
<p> The behavior of the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) daemon is controlled by the <code>master.cf</code> configuration file, as described in <code><a href="/docs/linux/man/5-master/">master</a></code>(5). </p>
<p> Options:</p>
<dl>
<dt><code>-c </code><i>config_dir</i></p>
<dd>Read the <code>main.cf</code> and <code>master.cf</code> configuration files in the named directory instead of the default configuration directory. This also overrides the configuration files for other Postfix daemon processes.</p>
<dt><code>-D</code></p>
<dd>After initialization, run a debugger on the master process. The debugging command is specified with the <code>debugger_command</code> in the <code>main.cf</code> global configuration file.</p>
<dt><code>-d</code></p>
<dd>Do not redirect stdin, stdout or stderr to /dev/null, and do not discard the controlling terminal. This must be used for debugging only.</p>
<dt><code>-e </code><i>exit_time</i></p>
<dd>Terminate the master process after <i>exit_time</i> seconds. Child processes terminate at their convenience.</p>
<dt><code>-t</code></p>
<dd>Test mode. Return a zero exit status when the <code>master.pid</code> lock file does not exist or when that file is not locked. This is evidence that the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) daemon is not running.</p>
<dt><code>-v</code></p>
<dd>Enable verbose logging for debugging purposes. This option is passed on to child processes. Multiple <code>-v</code> options make the software increasingly verbose.</p>
<dt><code>-w</code></p>
<dd>Wait in a dummy foreground process, while the real master daemon initializes in a background process. The dummy foreground process returns a zero exit status only if the master daemon initialization is successful, and if it completes in a reasonable amount of time. </p>
<p> This feature is available in Postfix 2.10 and later.</dl>
<p> Signals:</p>
<dl>
<dt><code>SIGHUP</code></p>
<dd>Upon receipt of a <code>HUP</code> signal (e.g., after &quot;<code>postfix reload</code>&quot;), the master process re-reads its configuration files. If a service has been removed from the <code>master.cf</code> file, its running processes are terminated immediately. Otherwise, running processes are allowed to terminate as soon as is convenient, so that changes in configuration settings affect only new service requests.</p>
<dt><code>SIGTERM</code></p>
<dd>Upon receipt of a <code>TERM</code> signal (e.g., after &quot;<code>postfix abort</code>&quot;), the master process passes the signal on to its child processes and terminates. This is useful for an emergency shutdown. Normally one would terminate only the master (&quot;<code>postfix stop</code>&quot;) and allow running processes to finish what they are doing.</dl>
<h2>Diagnostics</h2>
<p>Problems are reported to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). The exit status is non-zero in case of problems, including problems while initializing as a master daemon process in the background.</p>
<h2>Environment</h2>
<dl>
<dt><code>MAIL_DEBUG</code></p>
<dd>After initialization, start a debugger as specified with the <code>debugger_command</code> configuration parameter in the <code>main.cf</code> configuration file.</p>
<dt><code>MAIL_CONFIG</code></p>
<dd>Directory with Postfix configuration files.</dl>
<h2>Configuration Parameters</h2>
<p>Unlike most Postfix daemon processes, the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) server does not automatically pick up changes to <code>main.cf</code>. Changes to <code>master.cf</code> are never picked up automatically. Use the &quot;<code>postfix reload</code>&quot; command after a configuration change.</p>
<h2>Resource And Rate Controls</h2>
<dl>
<dt><code>default_process_limit (100)</code></p>
<dd>The default maximal number of Postfix child processes that provide a given service.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>service_throttle_time (60s)</code></p>
<dd>How long the Postfix <code><a href="/docs/linux/man/8-master/">master</a></code>(8) waits before forking a server that appears to be malfunctioning.</dl>
<p> Available in Postfix version 2.6 and later:</p>
<dl>
<dt><code>master_service_disable (empty)</code></p>
<dd>Selectively disable <code><a href="/docs/linux/man/8-master/">master</a></code>(8) listener ports by service type or by service name and type.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The directory with Postfix support programs and daemon programs.</p>
<dt><code>debugger_command (empty)</code></p>
<dd>The external command to execute when a Postfix daemon program is invoked with the -D option.</p>
<dt><code>inet_interfaces (all)</code></p>
<dd>The network interface addresses that this mail system receives mail on.</p>
<dt><code>inet_protocols (all)</code></p>
<dd>The Internet protocols Postfix will attempt to use when making or accepting connections.</p>
<dt><code>import_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The list of environment parameters that a Postfix process will import from a non-Postfix parent process.</p>
<dt><code>mail_owner (postfix)</code></p>
<dd>The UNIX system account that owns the Postfix queue and most Postfix daemon processes.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>Files</h2>
<p>To expand the directory names below into their actual values, use the command &quot;<code>postconf config_directory</code>&quot; etc. </p>
<pre>$config_directory/main.cf, global configuration file.
$config_directory/master.cf, master server configuration file.
$queue_directory/pid/master.pid, master lock file.
$data_directory/master.lock, master lock file.</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/8-verify/">verify</a>(8), address verification
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), master.cf configuration file syntax
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), main.cf configuration file syntax
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
