---
title: "ocf_heartbeat_dummy(7)"
name: "ocf_heartbeat_dummy"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_dummy/"
description: "ocf_heartbeat_Dummy – Example stateless resource agent"
---

<p>ocf_heartbeat_Dummy &#8211; Example stateless resource agent</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Dummy</code> [start | stop | monitor | migrate_to | migrate_from | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This is a Dummy Resource Agent. It does absolutely nothing except keep track of whether its running or not. Its purpose in life is for testing and to serve as a template for RA writers. </p>
<p> NB: Please pay attention to the timeouts specified in the actions section below. They should be meaningful for the kind of resource the agent manages. They should be the minimum advised timeouts, but they shouldn&#8217;t/cannot cover _all_ possible resource instances. So, try to be neither overly generous nor too stingy, but moderate. The minimum timeouts should never be below 10 seconds. </p>
<p> This resource agent may be configured for <i>native migration</i> if available in the cluster manager. For Pacemaker, the <i>allow-migrate=&quot;true&quot;</i> meta attribute enables native migration.</p>
<h2>Supported Parameters</h2>
<p><code>state</code></p>
<dl>
<dd>Location to store the resource state in. </p>
<p> (unique, optional, string, default &quot;/var/run/resource-agents/Dummy-default.state&quot;)</dl>
<p> <code>fake</code></p>
<dl>
<dd>Fake attribute that can be changed to cause a reload </p>
<p> (optional, string, default &quot;dummy&quot;)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 10.</dl>
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 20.</dl>
<p> <code>migrate_to</code></p>
<dl>
<dd>Executes steps necessary for migrating the resource <i>to</i> the node. Suggested minimum timeout: 20.</dl>
<p> <code>migrate_from</code></p>
<dl>
<dd>Executes steps necessary for migrating the resource <i>away from</i> the node. Suggested minimum timeout: 20.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 20.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a Dummy resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_Dummy ocf:heartbeat:Dummy \
 meta allow-migrate=&quot;true&quot; \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a Dummy resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_Dummy ocf:heartbeat:Dummy \
 op monitor timeout=&quot;20&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Dummy_(resource_agent)">http://www.linux-ha.org/wiki/Dummy_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
