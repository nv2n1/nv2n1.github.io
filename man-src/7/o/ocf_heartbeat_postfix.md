---
title: "ocf_heartbeat_postfix(7)"
name: "ocf_heartbeat_postfix"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_postfix/"
description: "ocf_heartbeat_postfix – Manages a highly available Postfix mail server instance"
---

<p>ocf_heartbeat_postfix &#8211; Manages a highly available Postfix mail server instance</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>postfix</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>This script manages Postfix as an OCF resource in a high-availability setup.</p>
<h2>Supported Parameters</h2>
<p><code>binary</code></p>
<dl>
<dd>Full path to the Postfix binary. For example, &quot;/usr/sbin/postfix&quot;. </p>
<p> (optional, string, default &quot;/usr/sbin/postfix&quot;)</dl>
<p> <code>config_dir</code></p>
<dl>
<dd>Full path to a Postfix configuration directory. For example, &quot;/etc/postfix&quot;. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>parameters</code></p>
<dl>
<dd>The Postfix daemon may be called with additional parameters. Specify any of them here. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>reload</code></p>
<dl>
<dd>Suggested minimum timeout: 20s.</dl>
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
<p>The following is an example configuration for a postfix resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_postfix ocf:heartbeat:postfix \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a postfix resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_postfix ocf:heartbeat:postfix \
 op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;60s&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/postfix_(resource_agent)">http://www.linux-ha.org/wiki/postfix_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
