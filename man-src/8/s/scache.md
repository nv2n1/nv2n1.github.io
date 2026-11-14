---
title: "scache(8)"
name: "scache"
section: "8"
letter: "s"
url: "/docs/linux/man/8-scache/"
description: "scache – Postfix shared connection cache server"
---

<p>scache &#8211; Postfix shared connection cache server</p>
<h2>Synopsis</h2>
<pre><code>scache</code> [generic Postfix daemon options]</pre>
<h2>Description</h2>
<p>The <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server maintains a shared multi-connection cache. This information can be used by, for example, Postfix SMTP clients or other Postfix delivery agents. </p>
<p> The connection cache is organized into logical destination names, physical endpoint names, and connections. </p>
<p> As a specific example, logical SMTP destinations specify (transport, domain, port), and physical SMTP endpoints specify (transport, IP address, port). An SMTP connection may be saved after a successful mail transaction. </p>
<p> In the general case, one logical destination may refer to zero or more physical endpoints, one physical endpoint may be referenced by zero or more logical destinations, and one endpoint may refer to zero or more connections. </p>
<p> The exact syntax of a logical destination or endpoint name is application dependent; the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server does not care. A connection is stored as a file descriptor together with application-dependent information that is needed to re-activate a connection object. Again, the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server is completely unaware of the details of that information. </p>
<p> All information is stored with a finite time to live (ttl). The connection cache daemon terminates when no client is connected for <code>max_idle</code> time units. </p>
<p> This server implements the following requests:</p>
<dl>
<dt><code>save_endp</code><i> ttl endpoint endpoint_properties file_descriptor</i></p>
<dd>Save the specified file descriptor and connection property data under the specified endpoint name. The endpoint properties are used by the client to re-activate a passivated connection object.</p>
<dt><code>find_endp</code><i> endpoint</i></p>
<dd>Look up cached properties and a cached file descriptor for the specified endpoint.</p>
<dt><code>save_dest</code><i> ttl destination destination_properties endpoint</i></p>
<dd>Save the binding between a logical destination and an endpoint under the destination name, together with destination specific connection properties. The destination properties are used by the client to re-activate a passivated connection object.</p>
<dt><code>find_dest</code><i> destination</i></p>
<dd>Look up cached destination properties, cached endpoint properties, and a cached file descriptor for the specified logical destination.</dl>
<h2>Security</h2>
<p>The <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server is not security-sensitive. It does not talk to the network, and it does not talk to local users. The <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server can run chrooted at fixed low privilege. </p>
<p> The <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server is not a trusted process. It must not be used to store information that is security sensitive.</p>
<h2>Diagnostics</h2>
<p>Problems and transactions are logged to <code><a href="/docs/linux/man/8-syslogd/">syslogd</a></code>(8).</p>
<h2>Bugs</h2>
<p>The session cache cannot be shared among multiple machines. </p>
<p> When a connection expires from the cache, it is closed without the appropriate protocol specific handshake.</p>
<h2>Configuration Parameters</h2>
<p>Changes to <code>main.cf</code> are picked up automatically as <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) processes run for only a limited amount of time. Use the command &quot;<code>postfix reload</code>&quot; to speed up a change. </p>
<p> The text below provides only a parameter summary. See <code><a href="/docs/linux/man/5-postconf/">postconf</a></code>(5) for more details including examples.</p>
<h2>Resource Controls</h2>
<dl>
<dt><code>connection_cache_ttl_limit (2s)</code></p>
<dd>The maximal time-to-live value that the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) connection cache server allows.</p>
<dt><code>connection_cache_status_update_time (600s)</code></p>
<dd>How frequently the <code><a href="/docs/linux/man/8-scache/">scache</a></code>(8) server logs usage statistics with connection cache hit and miss rates for logical destinations and for physical endpoints.</dl>
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
<dt><code>process_id (read-only)</code></p>
<dd>The process ID of a Postfix command or daemon process.</p>
<dt><code>process_name (read-only)</code></p>
<dd>The process name of a Postfix command or daemon process.</p>
<dt><code>syslog_facility (mail)</code></p>
<dd>The syslog facility of Postfix logging.</p>
<dt><code>syslog_name (see &#8216;postconf -d&#8217; output)</code></p>
<dd>The mail system name that is prepended to the process name in syslog records, so that &quot;smtpd&quot; becomes, for example, &quot;postfix/smtpd&quot;.</dl>
<h2>See Also</h2>
<pre><a href="//www.systutorials.com/docs/linux/man/8-smtp/">smtp</a>(8), SMTP client
<a href="//www.systutorials.com/docs/linux/man/5-postconf/">postconf</a>(5), configuration parameters
<a href="//www.systutorials.com/docs/linux/man/8-master/">master</a>(8), process manager
<a href="//www.systutorials.com/docs/linux/man/8-syslogd/">syslogd</a>(8), system logging</pre>
<h2>Readme Files</h2>
<p>Use &quot;<code>postconf readme_directory</code>&quot; or &quot;<code>postconf html_directory</code>&quot; to locate this information. </p>
<pre>CONNECTION_CACHE_README, Postfix connection cache</pre>
<h2>License</h2>
<p>The Secure Mailer license must be distributed with this software.</p>
<h2>History</h2>
<pre>This service was introduced with Postfix version 2.2.</pre>
<h2>Author(S)</h2>
<pre>Wietse Venema
IBM T.J. Watson Research
P.O. Box 704
Yorktown Heights, NY 10598, USA</pre>
