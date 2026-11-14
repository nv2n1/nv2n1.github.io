---
title: "ocf_heartbeat_syslog-ng(7)"
name: "ocf_heartbeat_syslog-ng"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_syslog-ng/"
description: "ocf_heartbeat_syslog-ng – Syslog-ng resource agent"
---

<p>ocf_heartbeat_syslog-ng &#8211; Syslog-ng resource agent</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>syslog-ng</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script manages a syslog-ng instance as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>configfile</code></p>
<dl>
<dd>This parameter specifies a configuration file for a syslog-ng instance managed by this RA. (required, string, no default)</dl>
<p> <code>syslog_ng_binary</code></p>
<dl>
<dd>This parameter specifies syslog-ng&#8217;s executable file. (optional, string, default /sbin/syslog-ng)</dl>
<p> <code>start_opts</code></p>
<dl>
<dd>This parameter specifies startup options for a syslog-ng instance managed by this RA. When no value is given, no startup options is used. Don&#8217;t use option &#8216;-F&#8217;. It causes a stuck of a start action. (optional, string, no default)</dl>
<p> <code>kill_term_timeout</code></p>
<dl>
<dd>On a stop action, a normal stop method(pkill -TERM) is firstly used. And then the confirmation of its completion is waited for the specified seconds by this parameter. The default value is 10. (optional, integer, default 10)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 120s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 60s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60s. Suggested interval: 60s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a syslog-ng resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_syslog-ng ocf:heartbeat:syslog-ng \
params \
configfile=string \
op monitor depth=&quot;0&quot; timeout=&quot;60s&quot; interval=&quot;60s&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/syslog-ng_(resource_agent)">http://www.linux-ha.org/wiki/syslog-ng_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
