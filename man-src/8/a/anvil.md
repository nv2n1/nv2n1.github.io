---
title: "anvil(8)"
name: "anvil"
section: "8"
letter: "a"
url: "/docs/linux/man/8-anvil/"
description: "anvil – Postfix session count and request rate control"
---

<p>anvil &#8211; Postfix session count and request rate control</p>
<h2>Synopsis</h2>
<pre><code>anvil</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The Postfix <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server maintains statistics about client connection counts or client request rates. This information can be used to defend against clients that hammer a server with either too many simultaneous sessions, or with too many successive requests within a configurable time interval. This server is designed to run under control by the Postfix <code><a href="/docs/linux/man/8-master/">master</a></code>(8) server. </p>
<p> In the following text, <code>ident</code> specifies a (service, client) combination. The exact syntax of that information is application-dependent; the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server does not care.</p>
<h2>Connection Count/Rate Control</h2>
<p>To register a new connection send the following request to the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server: </p>
<pre> <code>request=connect</code>
 <code>ident=</code><i>string</i></pre>
<p>The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server answers with the number of simultaneous connections and the number of connections per unit time for the (service, client) combination specified with <code>ident</code>: </p>
<pre> <code>status=0</code>
 <code>count=</code><i>number</i>
 <code>rate=</code><i>number</i></pre>
<p>To register a disconnect event send the following request to the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server: </p>
<pre> <code>request=disconnect</code>
 <code>ident=</code><i>string</i></pre>
<p>The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server replies with: </p>
<pre> <code>status=0</code></pre>
<h2>Message Rate Control</h2>
<p>To register a message delivery request send the following request to the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server: </p>
<pre> <code>request=message</code>
 <code>ident=</code><i>string</i></pre>
<p>The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server answers with the number of message delivery requests per unit time for the (service, client) combination specified with <code>ident</code>: </p>
<pre> <code>status=0</code>
 <code>rate=</code><i>number</i></pre>
<h2>Recipient Rate Control</h2>
<p>To register a recipient request send the following request to the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server: </p>
<pre> <code>request=recipient</code>
 <code>ident=</code><i>string</i></pre>
<p>The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server answers with the number of recipient addresses per unit time for the (service, client) combination specified with <code>ident</code>: </p>
<pre> <code>status=0</code>
 <code>rate=</code><i>number</i></pre>
<h2>Tls Session Negotiation Rate Control</h2>
<p>The features described in this section are available with Postfix 2.3 and later. </p>
<p> To register a request for a new (i.e. not cached) TLS session send the following request to the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server: </p>
<pre> <code>request=newtls</code>
 <code>ident=</code><i>string</i></pre>
<p>The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server answers with the number of new TLS session requests per unit time for the (service, client) combination specified with <code>ident</code>: </p>
<pre> <code>status=0</code>
 <code>rate=</code><i>number</i></pre>
<p>To retrieve new TLS session request rate information without updating the counter information, send: </p>
<pre> <code>request=newtls_report</code>
 <code>ident=</code><i>string</i></pre>
<p>The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server answers with the number of new TLS session requests per unit time for the (service, client) combination specified with <code>ident</code>: </p>
<pre> <code>status=0</code>
 <code>rate=</code><i>number</i></pre>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server does not talk to the network or to local users, and can run chrooted at fixed low privilege. </p>
<p> The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server maintains an in-memory table with information about recent clients requests. No persistent state is kept because standard system library routines are not sufficiently robust for update-intensive applications. </p>
<p> Although the in-memory state is kept only temporarily, this may require a lot of memory on systems that handle connections from many remote clients. To reduce memory usage, reduce the time unit over which state is kept.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8). </p>
<p> Upon exit, and every <code>anvil_status_update_time</code> seconds, the server logs the maximal count and rate values measured, together with (service, client) information and the time of day associated with those events. In order to avoid unnecessary overhead, no measurements are done for activity that isn&#8217;t concurrency limited or rate limited.</p>
<h2>Bugs</h2>
<p>Systems behind network address translating routers or proxies appear to have the same client address and can run into connection count and/or rate limits falsely. </p>
<p> In this preliminary implementation, a count (or rate) limited server process can have only one remote client at a time. If a server process reports multiple simultaneous clients, state is kept only for the last reported client. </p>
<p> The <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server automatically discards client request information after it expires. To prevent the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) server from discarding client request rate information too early or too late, a rate limited service should always register connect/disconnect events even when it does not explicitly limit them.</p>
<h2>Configuration Parameters</h2>
<p>On low-traffic mail systems, changes to <code>main.cf</code> are picked up automatically as <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) processes run for only a limited amount of time. On other mail systems, use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<dl>
<dt><code>anvil_rate_time_unit (60s)</code></p>
<dd>The time unit over which client connection rates and other rates are calculated.</p>
<dt><code>anvil_status_update_time (600s)</code></p>
<dd>How frequently the <code><a href="/docs/linux/man/8-anvil/">anvil</a></code>(8) connection and rate limiting server logs peak usage information.</p>
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
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-smtpd/">smtpd</a>(8), Postfix SMTP server
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/5-master/">master</a>(5), generic daemon options</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>TUNING_README, performance tuning</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<p>The anvil service is available in Postfix 2.2 and later.</p>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
