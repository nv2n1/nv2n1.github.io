---
title: "ocf_heartbeat_xinetd(7)"
name: "ocf_heartbeat_xinetd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_xinetd/"
description: "ocf_heartbeat_Xinetd – Manages a service of Xinetd"
---

<p>ocf_heartbeat_Xinetd &#8211; Manages a service of Xinetd</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Xinetd</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for Xinetd. It starts/stops services managed by xinetd by enabling or disabling them in the configuration file. </p>
<p> The xinetd daemon itself must be running: we are not going to start or stop it ourselves. </p>
<p> All services should have a line saying either &quot;disable=yes&quot; or &quot;disable=no&quot;. The script just changes those settings before reloading xinetd. </p>
<p> Important: in case the services managed by the cluster are the only ones enabled, you should specify the -stayalive option for xinetd or it will exit on Heartbeat stop. Alternatively, you may enable some internal service such as echo.</p>
<h2>Supported Parameters</h2>
<p><code>service</code></p>
<dl>
<dd>The name of the service managed by xinetd. </p>
<p> (required, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>restart</code></p>
<dl>
<dd>Suggested minimum timeout: 20s.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a Xinetd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_Xinetd ocf:heartbeat:Xinetd \
 params \
 service=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a Xinetd resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_Xinetd ocf:heartbeat:Xinetd \
 service=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;10&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Xinetd_(resource_agent)">http://www.linux-ha.org/wiki/Xinetd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
