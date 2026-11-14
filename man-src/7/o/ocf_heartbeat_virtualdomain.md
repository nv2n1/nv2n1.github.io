---
title: "ocf_heartbeat_virtualdomain(7)"
name: "ocf_heartbeat_virtualdomain"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_virtualdomain/"
description: "ocf_heartbeat_VirtualDomain – Manages virtual domains through the libvirt virtualization framework"
---

<p>ocf_heartbeat_VirtualDomain &#8211; Manages virtual domains through the libvirt virtualization framework</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>VirtualDomain</code> [start | stop | status | monitor | migrate_to | migrate_from | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource agent for a virtual domain (a.k.a. domU, virtual machine, virtual environment etc., depending on context) managed by libvirtd. </p>
<p> This resource agent may be configured for <i>native migration</i> if available in the cluster manager. For Pacemaker, the <i>allow-migrate=&quot;true&quot;</i> meta attribute enables native migration.</p>
<h2>Supported Parameters</h2>
<p><code>config</code></p>
<dl>
<dd>Absolute path to the libvirt configuration file, for this virtual domain. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>hypervisor</code></p>
<dl>
<dd>Hypervisor URI to connect to. See the libvirt documentation for details on supported URI formats. The default is system dependent. Determine the system&#8217;s default uri by running &#8216;virsh &#8211;quiet uri&#8217;. </p>
<p> (optional, string, no default)</dl>
<p> <code>force_stop</code></p>
<dl>
<dd>Always forcefully shut down (&quot;destroy&quot;) the domain on stop. The default behavior is to resort to a forceful shutdown only after a graceful shutdown attempt has failed. You should only set this to true if your virtual domain (or your virtualization backend) does not support graceful shutdown. </p>
<p> (optional, boolean, default 0)</dl>
<p> <code>migration_transport</code></p>
<dl>
<dd>Transport used to connect to the remote hypervisor while migrating. Please refer to the libvirt documentation for details on transports available. If this parameter is omitted, the resource will use libvirt&#8217;s default transport to connect to the remote hypervisor. </p>
<p> (optional, string, no default)</dl>
<p> <code>migration_downtime</code></p>
<dl>
<dd>Define max downtime during live migration in milliseconds </p>
<p> (optional, integer, default 0)</dl>
<p> <code>migration_speed</code></p>
<dl>
<dd>Define live migration speed per resource in MiB/s </p>
<p> (optional, integer, default 0)</dl>
<p> <code>migration_network_suffix</code></p>
<dl>
<dd>Use a dedicated migration network. The migration URI is composed by adding this parameters value to the end of the node name. If the node name happens to be an FQDN (as opposed to an unqualified host name), insert the suffix immediately prior to the first period (.) in the FQDN. At the moment Qemu/KVM and Xen migration via a dedicated network is supported. </p>
<p> Note: Be sure this composed host name is locally resolveable and the associated IP is reachable through the favored network. </p>
<p> See also the migrate_options parameter below. </p>
<p> (optional, string, no default)</dl>
<p> <code>migrate_options</code></p>
<dl>
<dd>Extra virsh options for the guest live migration. You can also specify here &#8211;migrateuri if the calculated migrate URI is unsuitable for your environment. If &#8211;migrateuri is set then migration_network_suffix and migrateport are effectively ignored. Use &quot;%n&quot; as the placeholder for the target node name. </p>
<p> Please refer to the libvirt documentation for details on guest migration. </p>
<p> (optional, string, no default)</dl>
<p> <code>monitor_scripts</code></p>
<dl>
<dd>To additionally monitor services within the virtual domain, add this parameter with a list of scripts to monitor. </p>
<p> Note: when monitor scripts are used, the start and migrate_from operations will complete only when all monitor scripts have completed successfully. Be sure to set the timeout of these operations to accommodate this delay. </p>
<p> (optional, string, no default)</dl>
<p> <code>autoset_utilization_cpu</code></p>
<dl>
<dd>If set true, the agent will detect the number of domainU&#8217;s vCPUs from virsh, and put it into the CPU utilization of the resource when the monitor is executed. </p>
<p> (optional, boolean, default true)</dl>
<p> <code>autoset_utilization_hv_memory</code></p>
<dl>
<dd>If set true, the agent will detect the number of *Max memory* from virsh, and put it into the hv_memory utilization of the resource when the monitor is executed. </p>
<p> (optional, boolean, default true)</dl>
<p> <code>migrateport</code></p>
<dl>
<dd>This port will be used in the qemu migrateuri. If unset, the port will be a random highport. </p>
<p> (optional, integer, no default)</dl>
<p> <code>snapshot</code></p>
<dl>
<dd>Path to the snapshot directory where the virtual machine image will be stored. When this parameter is set, the virtual machine&#8217;s RAM state will be saved to a file in the snapshot directory when stopped. If on start a state file is present for the domain, the domain will be restored to the same state it was in right before it stopped last. This option is incompatible with the &#8216;force_stop&#8217; option. </p>
<p> (optional, string, no default)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 90.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 90.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>migrate_from</code></p>
<dl>
<dd>Executes steps necessary for migrating the resource <i>away from</i> the node. Suggested minimum timeout: 60.</dl>
<p> <code>migrate_to</code></p>
<dl>
<dd>Executes steps necessary for migrating the resource <i>to</i> the node. Suggested minimum timeout: 120.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a VirtualDomain resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_VirtualDomain ocf:heartbeat:VirtualDomain \
 params \
 config=<i>string</i> \
 meta allow-migrate=&quot;true&quot; \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a VirtualDomain resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_VirtualDomain ocf:heartbeat:VirtualDomain \
 config=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/VirtualDomain_(resource_agent)">http://www.linux-ha.org/wiki/VirtualDomain_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
