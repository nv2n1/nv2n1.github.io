---
title: "ocf_heartbeat_named(7)"
name: "ocf_heartbeat_named"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_named/"
description: "ocf_heartbeat_named – Manages a named server"
---

<p>ocf_heartbeat_named &#8211; Manages a named server</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>named</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for named (Bind) server. It manages named as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>named</code></p>
<dl>
<dd>Path to the named command. </p>
<p> (optional, string, default &quot;/usr/sbin/named&quot;)</dl>
<p> <code>rndc</code></p>
<dl>
<dd>Path to the rndc command. </p>
<p> (optional, string, default &quot;/usr/sbin/rndc&quot;)</dl>
<p> <code>host</code></p>
<dl>
<dd>Path to the host command. </p>
<p> (optional, string, default &quot;/usr/bin/host&quot;)</dl>
<p> <code>named_user</code></p>
<dl>
<dd>User that should own named process. </p>
<p> (optional, string, default &quot;named&quot;)</dl>
<p> <code>named_config</code></p>
<dl>
<dd>Configuration file for named. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>named_pidfile</code></p>
<dl>
<dd>PIDFILE file for named. </p>
<p> (unique, optional, string, default &quot;/var/run/named/named.pid&quot;)</dl>
<p> <code>named_rootdir</code></p>
<dl>
<dd>Directory that named should use for chroot if any. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>named_options</code></p>
<dl>
<dd>Options for named process if any. </p>
<p> (optional, string, no default)</dl>
<p> <code>named_keytab_file</code></p>
<dl>
<dd>named service keytab file (for GSS-TSIG). </p>
<p> (optional, string, no default)</dl>
<p> <code>monitor_request</code></p>
<dl>
<dd>Request that shall be sent to named for monitoring. Usually an A record in DNS. </p>
<p> (optional, string, default &quot;localhost&quot;)</dl>
<p> <code>monitor_response</code></p>
<dl>
<dd>Expected response from named server. </p>
<p> (optional, string, default &quot;127.0.0.1&quot;)</dl>
<p> <code>monitor_ip</code></p>
<dl>
<dd>IP Address where named listens. </p>
<p> (optional, string, default &quot;127.0.0.1&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 60.</dl>
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 60.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 30.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a named resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_named ocf:heartbeat:named \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a named resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_named ocf:heartbeat:named \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;30&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/named_(resource_agent)">http://www.linux-ha.org/wiki/named_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
