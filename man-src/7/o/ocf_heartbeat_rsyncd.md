---
title: "ocf_heartbeat_rsyncd(7)"
name: "ocf_heartbeat_rsyncd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_rsyncd/"
description: "ocf_heartbeat_rsyncd – Manages an rsync daemon"
---

<p>ocf_heartbeat_rsyncd &#8211; Manages an rsync daemon</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>rsyncd</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script manages rsync daemon</p>
<h2>Supported Parameters</h2>
<p><code>binpath</code></p>
<dl>
<dd>The rsync binary path. For example, &quot;/usr/bin/rsync&quot; </p>
<p> (optional, string, default &quot;rsync&quot;)</dl>
<p> <code>conffile</code></p>
<dl>
<dd>The rsync daemon configuration file name with full path. For example, &quot;/etc/rsyncd.conf&quot; </p>
<p> (optional, string, default &quot;/etc/rsyncd.conf&quot;)</dl>
<p> <code>bwlimit</code></p>
<dl>
<dd>This option allows you to specify a maximum transfer rate in kilobytes per second. This option is most effective when using rsync with large files (several megabytes and up). Due to the nature of rsync transfers, blocks of data are sent, then if rsync determines the transfer was too fast, it will wait before sending the next data block. The result is an average transfer rate equaling the specified limit. A value of zero specifies no limit. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 60s.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20s.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5s.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a rsyncd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_rsyncd ocf:heartbeat:rsyncd \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a rsyncd resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_rsyncd ocf:heartbeat:rsyncd \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/rsyncd_(resource_agent)">http://www.linux-ha.org/wiki/rsyncd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
