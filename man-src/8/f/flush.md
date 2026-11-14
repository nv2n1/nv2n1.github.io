---
title: "flush(8)"
name: "flush"
section: "8"
letter: "f"
url: "/docs/linux/man/8-flush/"
description: "flush – Postfix fast flush server"
---

<p>flush &#8211; Postfix fast flush server</p>
<h2>Synopsis</h2>
<pre><code>flush</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) server maintains a record of deferred mail by destination. This information is used to improve the performance of the SMTP <code>ETRN</code> request, and of its command-line equivalent, &quot;<code>sendmail -qR</code>&quot; or &quot;<code>postqueue -f</code>&quot;. This program expects to be run from the <code><a href="/docs/linux/man/8-master/">master</a></code>(8) process manager. </p>
<p> The record is implemented as a per-destination logfile with as contents the queue IDs of deferred mail. A logfile is append-only, and is truncated when delivery is requested for the corresponding destination. A destination is the part on the right-hand side of the right-most <code>@</code> in an email address. </p>
<p> Per-destination logfiles of deferred mail are maintained only for eligible destinations. The list of eligible destinations is specified with the <code>fast_flush_domains</code> configuration parameter, which defaults to <code>$relay_domains</code>. </p>
<p> This server implements the following requests:</p>
<dl>
<dt><code>add</code><i> sitename queueid</i></p>
<dd>Inform the <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) server that the message with the specified queue ID is queued for the specified destination.</p>
<dt><code>send_site</code><i> sitename</i></p>
<dd>Request delivery of mail that is queued for the specified destination.</p>
<dt><code>send_file</code><i> queueid</i></p>
<dd>Request delivery of the specified deferred message.</p>
<dt><code>refresh</code></p>
<dd>Refresh non-empty per-destination logfiles that were not read in <code>$fast_flush_refresh_time</code> hours, by simulating send requests (see above) for the corresponding destinations. </p>
<p> Delete empty per-destination logfiles that were not updated in <code>$fast_flush_purge_time</code> days. </p>
<p> This request completes in the background.</p>
<dt><code>purge</code></p>
<dd>Do a <code>refresh</code> for all per-destination logfiles.</dl>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) server is not security-sensitive. It does not talk to the network, and it does not talk to local users. The fast flush server can run chrooted at fixed low privilege.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>Fast flush logfiles are truncated only after a &quot;send&quot; request, not when mail is actually delivered, and therefore can accumulate outdated or redundant data. In order to maintain sanity, &quot;refresh&quot; must be executed periodically. This can be automated with a suitable wakeup timer setting in the <code>master.cf</code> configuration file. </p>
<p> Upon receipt of a request to deliver mail for an eligible destination, the <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) server requests delivery of all messages that are listed in that destination&#8217;s logfile, regardless of the recipients of those messages. This is not an issue for mail that is sent to a <code>relay_domains</code> destination because such mail typically only has recipients in one domain.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically as <code><a href="/docs/linux/man/8-flush/">flush</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>config_directory (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The default location of the Postfix main.cf and master.cf configuration files.</p>
<dt><code>daemon_timeout (18000s)</code></p>
<dd>How much time a Postfix daemon process may take to handle a request before it is terminated by a built-in watchdog timer.</p>
<dt><code>fast_flush_domains ($relay_domains)</code></p>
<dd>Optional list of destinations that are eligible for per-destination logfiles with mail that is queued to those destinations.</p>
<dt><code>fast_flush_refresh_time (12h)</code></p>
<dd>The time after which a non-empty but unread per-destination &quot;fast flush&quot; logfile needs to be refreshed.</p>
<dt><code>fast_flush_purge_time (7d)</code></p>
<dd>The time after which an empty per-destination &quot;fast flush&quot; logfile is deleted.</p>
<dt><code>ipc_timeout (3600s)</code></p>
<dd>The time limit for sending or receiving information over an internal communication channel.</p>
<dt><code>max_idle (100s)</code></p>
<dd>The maximum amount of time that an idle Postfix daemon process waits for an incoming connection before terminating voluntarily.</p>
<dt><code>max_use (100)</code></p>
<dd>The maximal number of incoming connections that a Postfix daemon process will service before terminating voluntarily.</p>
<dt><code>parent_domain_matches_subdomains (see &#8216;postconf -d&#8217; output)</code></p>
<dd>What Postfix features match subdomains of &quot;domain.tld&quot; automatically, instead of requiring an explicit &quot;.domain.tld&quot; pattern.</p>
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
<pre>/var/spool/postfix/flush, &quot;fast flush&quot; logfiles.</pre>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), SMTP server
<a href="//www.systutorials.com/docs/linux/man/8-qmgr/">qmgr</a>(8), queue manager
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>ETRN_README, Postfix ETRN howto</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<pre>This service was introduced with Postfix version 1.0.</pre>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
