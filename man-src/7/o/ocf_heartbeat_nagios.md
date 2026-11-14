---
title: "ocf_heartbeat_nagios(7)"
name: "ocf_heartbeat_nagios"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_nagios/"
description: "ocf_heartbeat_nagios – Nagios resource agent"
---

<p>ocf_heartbeat_nagios &#8211; Nagios resource agent</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nagios</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>OCF Resource script for Nagios 3.x or 4.x. It manages a Nagios instance as a HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>user</code></p>
<dl>
<dd>User running Nagios daemon (for file permissions) </p>
<p> (optional, string, default &quot;nagios&quot;)</dl>
<p> <code>group</code></p>
<dl>
<dd>Group running Nagios daemon (for file permissions) </p>
<p> (optional, string, default &quot;nagios&quot;)</dl>
<p> <code>binary</code></p>
<dl>
<dd>Location of the Nagios binary </p>
<p> (optional, string, default &quot;/usr/sbin/nagios&quot;)</dl>
<p> <code>config</code></p>
<dl>
<dd>Configuration file </p>
<p> (optional, string, default &quot;/etc/nagios/nagios.cfg&quot;)</dl>
<p> <code>log</code></p>
<dl>
<dd>Location of the Nagios log </p>
<p> (optional, string, default &quot;/var/log/nagios/nagios.log&quot;)</dl>
<p> <code>retention</code></p>
<dl>
<dd>Location of the Nagios retention file </p>
<p> (optional, string, default &quot;/var/log/nagios/retention.dat&quot;)</dl>
<p> <code>command</code></p>
<dl>
<dd>Location of the Nagios external command file </p>
<p> (optional, string, default &quot;/var/log/nagios/rw/nagios.cmd&quot;)</dl>
<p> <code>pid</code></p>
<dl>
<dd>Location of the Nagios pid/lock </p>
<p> (optional, string, default &quot;/var/run/nagios.pid&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 20.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 20.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a nagios resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_nagios ocf:heartbeat:nagios \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot; start-delay=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a nagios resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_nagios ocf:heartbeat:nagios \
 op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;10&quot; start-delay=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/nagios_(resource_agent)">http://www.linux-ha.org/wiki/nagios_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
