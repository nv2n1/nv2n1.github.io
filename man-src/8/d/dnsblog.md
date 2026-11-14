---
title: "dnsblog(8)"
name: "dnsblog"
section: "8"
letter: "d"
url: "/docs/linux/man/8-dnsblog/"
description: "dnsblog – Postfix DNS white/blacklist logger"
---

<p>dnsblog &#8211; Postfix DNS white/blacklist logger</p>
<h2>Synopsis</h2>
<pre><code>dnsblog</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-dnsblog/">dnsblog</a></code>(8) server implements an ad-hoc DNS white/blacklist lookup service. This may eventually be replaced by an UDP client that is built directly into the <code><a href="/docs/linux/man/8-postscreen/">postscreen</a></code>(8) server.</p>
<h2>Protocol</h2>
<p>With each connection, the <code><a href="/docs/linux/man/8-dnsblog/">dnsblog</a></code>(8) server receives a DNS white/blacklist domain name, IP address, and an ID. If the address is listed under the DNS white/blacklist, the <code><a href="/docs/linux/man/8-dnsblog/">dnsblog</a></code>(8) server logs the match and replies with the query arguments plus an address list with the resulting IP addresses separated by whitespace. Otherwise it replies with the query arguments plus an empty address list. Finally, The <code><a href="/docs/linux/man/8-dnsblog/">dnsblog</a></code>(8) server closes the connection.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically, as <code><a href="/docs/linux/man/8-dnsblog/">dnsblog</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>postscreen_dnsbl_sites (empty)</code></p>
<dd>Optional list of DNS white/blacklist domains, filters and weight factors.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
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
<pre><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), Postfix SMTP server
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-syslogd/">syslogd</a>(5), system logging</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>This service was introduced with Postfix version 2.8.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
