---
title: "ocf_heartbeat_portblock(7)"
name: "ocf_heartbeat_portblock"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_portblock/"
description: "ocf_heartbeat_portblock – Block and unblocks access to TCP and UDP ports"
---

<p>ocf_heartbeat_portblock &#8211; Block and unblocks access to TCP and UDP ports</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>portblock</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for portblock. It is used to temporarily block ports using iptables. In addition, it may allow for faster TCP reconnects for clients on failover. Use that if there are long lived TCP connections to an HA service. This feature is enabled by setting the tickle_dir parameter and only in concert with action set to unblock. Note that the tickle ACK function is new as of version 3.0.2 and hasn&#8217;t yet seen widespread use.</p>
<h2>Supported Parameters</h2>
<p><code>protocol</code></p>
<dl>
<dd>The protocol used to be blocked/unblocked. </p>
<p> (required, string, no default)</dl>
<p> <code>portno</code></p>
<dl>
<dd>The port number used to be blocked/unblocked. </p>
<p> (required, string, no default)</dl>
<p> <code>action</code></p>
<dl>
<dd>The action (block/unblock) to be done on the protocol::portno. </p>
<p> (required, string, no default)</dl>
<p> <code>reset_local_on_unblock_stop</code></p>
<dl>
<dd>If for some reason the long lived server side TCP sessions won&#8217;t be cleaned up by a reconfiguration/flush/stop of whatever services this portblock protects, they would linger in the connection table, even after the IP is gone and services have been switched over to an other node. </p>
<p> An example would be the default NFS kernel server. </p>
<p> These &quot;known&quot; connections may seriously confuse and delay a later switchback. </p>
<p> Enabling this option will cause this agent to try to get rid of these connections by injecting a temporary iptables rule to TCP-reset outgoing packets from the blocked ports, and additionally tickle them locally, just before it starts to DROP incoming packets on &quot;unblock stop&quot;. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>ip</code></p>
<dl>
<dd>The IP address used to be blocked/unblocked. </p>
<p> (optional, string, default &quot;0.0.0.0/0&quot;)</dl>
<p> <code>tickle_dir</code></p>
<dl>
<dd>The shared or local directory (_must_ be absolute path) which stores the established TCP connections. </p>
<p> (optional, string, no default)</dl>
<p> <code>sync_script</code></p>
<dl>
<dd>If the tickle_dir is a local directory, then the TCP connection state file has to be replicated to other nodes in the cluster. It can be csync2 (default), some wrapper of rsync, or whatever. It takes the file name as a single argument. For csync2, set it to &quot;csync2 -xv&quot;. </p>
<p> (optional, string, no default)</dl>
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
<dd>Performs a status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a portblock resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_portblock ocf:heartbeat:portblock \
 params \
 protocol=<i>string</i> \
 portno=<i>string</i> \
 action=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a portblock resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_portblock ocf:heartbeat:portblock \
 protocol=<i>string</i> \
 portno=<i>string</i> \
 action=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/portblock_(resource_agent)">http://www.linux-ha.org/wiki/portblock_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
