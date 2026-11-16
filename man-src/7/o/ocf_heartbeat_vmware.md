---
title: "ocf_heartbeat_vmware(7)"
name: "ocf_heartbeat_vmware"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_vmware/"
description: "ocf_heartbeat_vmware – Manages VMWare Server 2.0 virtual machines"
---

<p>ocf_heartbeat_vmware &#8211; Manages VMWare Server 2.0 virtual machines</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>vmware</code> [start | stop | monitor | meta-data]</dt></dl>
<h2>Description</h2>
<dd>OCF compliant script to control vmware server 2.0 virtual machines.</dd>
<h2>Supported Parameters</h2>
<p><code>vmxpath</code></p>
<dl>
<dd>VMX configuration file path (required, string, no default)</dd></dl>
<p> <code>vimshbin</code></p>
<dl>
<dd>vmware-vim-cmd executable path (optional, string, default /usr/bin/vmware-vim-cmd)</dd></dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 600.</dd></dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 600.</dd></dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 300.</dd></dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dd></dl>
<h2>Example</h2>
<p>The following is an example configuration for a vmware resource using the <code>crm</code>(8) shell: </p>
<pre><code>primitive example_vmware ocf:heartbeat:vmware \
params \
vmxpath=string \
op monitor timeout=&quot;30&quot; interval=&quot;300&quot; depth=&quot;0&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/vmware_(resource_agent)">http://www.linux-ha.org/wiki/vmware_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
