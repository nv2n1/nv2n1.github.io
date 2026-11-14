---
title: "ocf_heartbeat_delay(7)"
name: "ocf_heartbeat_delay"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_delay/"
description: "ocf_heartbeat_Delay – Waits for a defined timespan"
---

<p>ocf_heartbeat_Delay &#8211; Waits for a defined timespan</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Delay</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script is a test resource for introducing delay.</p>
<h2>Supported Parameters</h2>
<p><code>startdelay</code></p>
<dl>
<dd>How long in seconds to delay on start operation. </p>
<p> (optional, integer, default 30)</dl>
<p> <code>stopdelay</code></p>
<dl>
<dd>How long in seconds to delay on stop operation. Defaults to &quot;startdelay&quot; if unspecified. </p>
<p> (optional, integer, default 30)</dl>
<p> <code>mondelay</code></p>
<dl>
<dd>How long in seconds to delay on monitor operation. Defaults to &quot;startdelay&quot; if unspecified. </p>
<p> (optional, integer, default 30)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 30.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 30.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a Delay resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_Delay ocf:heartbeat:Delay \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a Delay resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_Delay ocf:heartbeat:Delay \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Delay_(resource_agent)">http://www.linux-ha.org/wiki/Delay_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
