---
title: "spawn(8)"
name: "spawn"
section: "8"
letter: "s"
url: "/docs/linux/man/8-spawn/"
description: "spawn – Postfix external command spawner"
---

<p>spawn &#8211; Postfix external command spawner</p>
<h2>Synopsis</h2>
<pre><code>spawn</code> [generic Postfix daemon options] command_attributes...</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8) daemon provides the Postfix equivalent of <code>inetd</code>. It listens on a port as specified in the Postfix <code>master.cf</code> file and spawns an external command whenever a connection is established. The connection can be made over local IPC (such as UNIX-domain sockets) or over non-local IPC (such as TCP sockets). The command&#8217;s standard input, output and error streams are connected directly to the communication endpoint. </p>
<p> This daemon expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager.</p>
<h2>Command Attribute Syntax</h2>
<p>The external command attributes are given in the <code>master.cf</code> file at the end of a service definition. The syntax is as follows:</p>
<dl>
<dt><code>user</code>=<i>username</i> (required)</p>
<dd>
<dt><code>user</code>=<i>username</i>:<i>groupname</i></p>
<dd>The external command is executed with the rights of the specified <i>username</i>. The software refuses to execute commands with root privileges, or with the privileges of the mail system owner. If <i>groupname</i> is specified, the corresponding group ID is used instead of the group ID of <i>username</i>.</p>
<dt><code>argv</code>=<i>command</i>&#8230; (required)</p>
<dd>The command to be executed. This must be specified as the last command attribute. The command is executed directly, i.e. without interpretation of shell meta characters by a shell command interpreter.</dl>
<h2>Bugs</h2>
<p>In order to enforce standard Postfix process resource controls, the <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8) daemon runs only one external command at a time. As such, it presents a noticeable overhead by wasting precious process resources. The <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8) daemon is expected to be replaced by a more structural solution.</p>
<h2>Diagnostics</h2>
<p>The <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8) daemon reports abnormal child exits. Problems are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Security</h2>
<p>This program needs root privilege in order to execute external commands as the specified user. It is therefore security sensitive. However the <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8) daemon does not talk to the external command and thus is not vulnerable to data-driven attacks.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically as <code><a href="/docs/linux/man/8-spawn/">spawn</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples. </p>
<p> In the text below, <i>transport</i> is the first field of the entry in the <code>master.cf</code> file.</p>
<h2>Resource And Rate Control</h2>
<dl>
<dt><i>transport</i><code>_time_limit ($command_time_limit)</code></p>
<dd>The amount of time the command is allowed to run before it is terminated. </p>
<p> Postfix 2.4 and later support a suffix that specifies the time unit: s (seconds), m (minutes), h (hours), d (days), w (weeks). The default time unit is seconds.</dl>
<h2>Miscellaneous</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>export_environment (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The list of environment variables that a Postfix process will export to non-Postfix processes.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>mail_owner (postfix)</code></p>
<dd>The UNIX system account that owns the Postfix queue and most Postfix daemon processes.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
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
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
