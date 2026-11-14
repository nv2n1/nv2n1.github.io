---
title: "ocf_heartbeat_nfsnotify(7)"
name: "ocf_heartbeat_nfsnotify"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_nfsnotify/"
description: "ocf_heartbeat_nfsnotify – sm-notify reboot notifications"
---

<p>ocf_heartbeat_nfsnotify &#8211; sm-notify reboot notifications</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>nfsnotify</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This agent sends NFSv3 reboot notifications to clients which informs clients to reclaim locks.</p>
<h2>Supported Parameters</h2>
<p><code>source_host</code></p>
<dl>
<dd>Comma separated list of floating IP addresses or host names that clients use to access the nfs service. This will be used to set the source address and mon_name of the SN_NOTIFY reboot notifications. </p>
<p> (optional, string, no default)</dl>
<p> <code>notify_args</code></p>
<dl>
<dd>Additional arguments to send to the sm-notify command. By default this agent will always set sm-notify&#8217;s &#8216;-f&#8217; option. When the source_host option is set, the &#8216;-v&#8217; option will be used automatically to set the proper source address. Any additional sm-notify arguments set with this option will be used in addition to the previous default arguments. </p>
<p> (optional, string, default &quot;false&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 90.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 90.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 90. Suggested interval: 30.</dl>
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 90.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a nfsnotify resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_nfsnotify ocf:heartbeat:nfsnotify \
 op monitor timeout=&quot;90&quot; interval=&quot;30&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a nfsnotify resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_nfsnotify ocf:heartbeat:nfsnotify \
 op monitor timeout=&quot;90&quot; interval=&quot;30&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/nfsnotify_(resource_agent)">http://www.linux-ha.org/wiki/nfsnotify_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
