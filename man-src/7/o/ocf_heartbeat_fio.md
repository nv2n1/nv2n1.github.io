---
title: "ocf_heartbeat_fio(7)"
name: "ocf_heartbeat_fio"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_fio/"
description: "ocf_heartbeat_fio – fio IO load generator"
---

<p>ocf_heartbeat_fio &#8211; fio IO load generator</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>fio</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>fio is a generic I/O load generator. This RA allows start/stop of fio instances to simulate load on a cluster without configuring complex services.</p>
<h2>Supported Parameters</h2>
<p><code>args</code></p>
<dl>
<dd>Arguments to the fio client. Minimally, this should be a (list of) job descriptions to run. (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 60.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 60. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a fio resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_fio ocf:heartbeat:fio \

op monitor timeout=&quot;60&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/fio_(resource_agent)">http://www.linux-ha.org/wiki/fio_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
