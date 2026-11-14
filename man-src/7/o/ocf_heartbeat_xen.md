---
title: "ocf_heartbeat_xen(7)"
name: "ocf_heartbeat_xen"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_xen/"
description: "ocf_heartbeat_Xen – Manages Xen unprivileged domains (DomUs)"
---

<p>ocf_heartbeat_Xen &#8211; Manages Xen unprivileged domains (DomUs)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>Xen</code> [start | stop | monitor | migrate_to | migrate_from | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource Agent for the Xen Hypervisor. Manages Xen virtual machine instances by mapping cluster resource start and stop, to Xen create and shutdown, respectively. A note on names We will try to extract the name from the config file (the xmfile attribute). If you use a simple assignment statement, then you should be fine. Otherwise, if there&#8217;s some python acrobacy involved such as dynamically assigning names depending on other variables, and we will try to detect this, then please set the name attribute. You should also do that if there is any chance of a pathological situation where a config file might be missing, for example if it resides on a shared storage. If all fails, we finally fall back to the instance id to preserve backward compatibility. Para-virtualized guests can also be migrated by enabling the meta_attribute allow-migrate.</p>
<h2>Supported Parameters</h2>
<p><code>xmfile</code></p>
<dl>
<dd>Absolute path to the Xen control file, for this virtual machine. (required, string, no default)</dl>
<p> <code>name</code></p>
<dl>
<dd>Name of the virtual machine. (optional, string, no default)</dl>
<p> <code>shutdown_timeout</code></p>
<dl>
<dd>The Xen agent will first try an orderly shutdown using xm shutdown. Should this not succeed within this timeout, the agent will escalate to xm destroy, forcibly killing the node. If this is not set, it will default to two-third of the stop action timeout. Setting this value to 0 forces an immediate destroy. (optional, string, no default)</dl>
<p> <code>allow_mem_management</code></p>
<dl>
<dd>This parameter enables dynamic adjustment of memory for start and stop actions used for Dom0 and the DomUs. The default is to not adjust memory dynamically. (optional, boolean, default 0)</dl>
<p> <code>node_ip_attribute</code></p>
<dl>
<dd>In case of a live migration, the system will default to using the IP address associated with the hostname via DNS or /etc/hosts. This parameter allows you to specify a node attribute that will be queried instead for the target node, overriding the IP address. This allows you to use a dedicated network for live migration traffic to a specific node. Warning: make very sure the IP address does point to the right node. Or else the live migration will end up somewhere else, greatly confusing the cluster and causing havoc. (optional, string, no default)</dl>
<p> <code>reserved_Dom0_memory</code></p>
<dl>
<dd>In case memory management is used, this parameter defines the minimum amount of memory to be reserved for the dom0. The default minimum memory is 512MB. (optional, string, default 512)</dl>
<p> <code>monitor_scripts</code></p>
<dl>
<dd>To additionally monitor services within the unprivileged domain, add this parameter with a list of scripts to monitor. (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 60.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 40.</dl>
<p> <code>migrate_from</code></p>
<dl>
<dd>Executes steps necessary for migrating the resource <i>away from</i> the node. Suggested minimum timeout: 120.</dl>
<p> <code>migrate_to</code></p>
<dl>
<dd>Executes steps necessary for migrating the resource <i>to</i> the node. Suggested minimum timeout: 120.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a Xen resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_Xen ocf:heartbeat:Xen \
params \
xmfile=string \
meta allow-migrate=&quot;true&quot; \
op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/Xen_(resource_agent)">http://www.linux-ha.org/wiki/Xen_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
