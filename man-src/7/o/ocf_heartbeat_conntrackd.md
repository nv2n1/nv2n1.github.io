---
title: "ocf_heartbeat_conntrackd(7)"
name: "ocf_heartbeat_conntrackd"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_conntrackd/"
description: "ocf_heartbeat_conntrackd – This resource agent manages conntrackd"
---

<p>ocf_heartbeat_conntrackd &#8211; This resource agent manages conntrackd</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>conntrackd</code> [start | stop | monitor | promote | demote | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Master/Slave OCF Resource Agent for conntrackd</p>
<h2>Supported Parameters</h2>
<p><code>binary</code></p>
<dl>
<dd>Name of the conntrackd executable. If conntrackd is installed and available in the default PATH, it is sufficient to configure the name of the binary For example &quot;my-conntrackd-binary-version-0.9.14&quot; If conntrackd is installed somewhere else, you may also give a full path For example &quot;/packages/conntrackd-0.9.14/sbin/conntrackd&quot; </p>
<p> (optional, string, default &quot;conntrackd&quot;)</dl>
<p> <code>config</code></p>
<dl>
<dd>Full path to the conntrackd.conf file. For example &quot;/packages/conntrackd-0.9.14/etc/conntrackd/conntrackd.conf&quot; </p>
<p> (optional, string, default &quot;/etc/conntrackd/conntrackd.conf&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 30.</dl>
<p> <code>promote</code></p>
<dl>
<dd>Promotes the resource to the Master role. Suggested minimum timeout: 30.</dl>
<p> <code>demote</code></p>
<dl>
<dd>Demotes the resource to the Slave role. Suggested minimum timeout: 30.</dl>
<p> <code>notify</code></p>
<dl>
<dd>Suggested minimum timeout: 30.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 30.</dl>
<p> <code>monitor (Slave role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 20.</dl>
<p> <code>monitor (Master role)</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 30.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a conntrackd resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_conntrackd ocf:heartbeat:conntrackd \
 op monitor timeout=&quot;20&quot; interval=&quot;20&quot; role=&quot;Slave&quot; \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; role=&quot;Master&quot; </pre>
</dl>
<dl>
<dd>
<pre>ms ms_conntrackd p_conntrackd \
 meta notify=&quot;true&quot; interleave=&quot;true&quot;</pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a conntrackd resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_conntrackd ocf:heartbeat:conntrackd \
 op monitor timeout=&quot;20&quot; interval=&quot;20&quot; role=&quot;Slave&quot; \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; role=&quot;Master&quot; --master</pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/conntrackd_(resource_agent)">http://www.linux-ha.org/wiki/conntrackd_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
