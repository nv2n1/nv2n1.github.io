---
title: "qmqpd(8)"
name: "qmqpd"
section: "8"
letter: "q"
url: "/docs/linux/man/8-qmqpd/"
description: "qmqpd – Postfix QMQP server"
---

<p>qmqpd &#8211; Postfix QMQP server</p>
<h2>Synopsis</h2>
<pre><code>qmqpd</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The Postfix QMQP server receives one message per connection. Each message is piped through the <code><a href="/docs/linux/man/8-cleanup/">cleanup</a></code>(8) daemon, and is placed into the <code>incoming</code> queue as one single queue file. The program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> The QMQP server implements one access policy: only explicitly authorized client hosts are allowed to use the service.</p>
<h2>Security</h2>
<p>The QMQP server is moderately security-sensitive. It talks to QMQP clients and to DNS servers on the network. The QMQP server can be run chrooted at fixed low privilege.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>The QMQP protocol provides only one server reply per message delivery. It is therefore not possible to reject individual recipients. </p>
<p> The QMQP protocol requires the server to receive the entire message before replying. If a message is malformed, or if any netstring component is longer than acceptable, Postfix replies immediately and closes the connection. It is left up to the client to handle the situation.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-qmqpd/">qmqpd</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Content Inspection Controls</h2>
<dl>
<dt><code>content_filter (empty)</code></p>
<dd>After the message is queued, send the entire message to the specified <i>transport:destination</i>.</p>
<dt><code>receive_override_options (empty)</code></p>
<dd>Enable or disable recipient validation, built-in content filtering, or address mapping.</dl>
<h2>Resource And Rate Controls</h2>
<dl>
<dt><code>line_length_limit (2048)</code></p>
<dd>Upon input, long lines are chopped up into pieces of at most this length; upon delivery, long lines are reconstructed.</p>
<dt><code>hopcount_limit (50)</code></p>
<dd>The maximal number of Received: message headers that is allowed in the primary message headers.</p>
<dt><code>message_size_limit (10240000)</code></p>
<dd>The maximal size in bytes of a message, including envelope information.</p>
<dt><code>qmqpd_timeout (300s)</code></p>
<dd>The time limit for sending or receiving information over the network.</dl>
<h2>Trouble Shooting Controls</h2>
<dl>
<dt><code>debug_peer_level (2)</code></p>
<dd>The increment in verbose logging level when a remote client or server matches a pattern in the debug_peer_list parameter.</p>
<dt><code>debug_peer_list (empty)</code></p>
<dd>Optional list of remote client or server hostname or network address patterns that cause the verbose logging level to increase by the amount specified in $debug_peer_level.</p>
<dt><code>soft_bounce (no)</code></p>
<dd>Safety net to keep mail queued that would otherwise be returned to the sender.</dl>
<h2>Tarpit Controls</h2>
<dl>
<dt><code>qmqpd_error_delay (1s)</code></p>
<dd>How long the Postfix QMQP server will pause before sending a negative reply to the remote QMQP client.</dl>
<h2>Miscellaneous Controls</h2>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>qmqpd_authorized_clients (empty)</code></p>
<dd>What remote QMQP clients are allowed to connect to the Postfix QMQP server port.</p>
<dt><code>queue_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The location of the Postfix top-level queue directory.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</p>
<dt><code>verp_delimiter_filter (-=+)</code></p>
<dd>The characters Postfix accepts as VERP delimiter characters on the Postfix <code><a href="/docs/linux/man/1-sendmail/">sendmail</a></code>(1) command line and in SMTP commands.</dl>
<p> Available in Postfix version 2.5 and later:</p>
<dl>
<dt><code>qmqpd_client_port_logging (no)</code></p>
<dd>Enable logging of the remote QMQP client port in addition to the hostname and IP address.</dl>
<h2>See Also</h2>
<pre><a rel="nofollow" href="http://cr.yp.to/proto/qmqp.html,">http://cr.yp.to/proto/qmqp.html,</a> QMQP protocol
<a href="//www.systutorials.com/docs/linux/man/8-cleanup/">cleanup</a>(8), message canonicalization
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>QMQP_README, Postfix ezmlm-idx howto.</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>The qmqpd service was introduced with Postfix version 1.1.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
