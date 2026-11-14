---
title: "ocf_heartbeat_lvm(7)"
name: "ocf_heartbeat_lvm"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_lvm/"
description: "ocf_heartbeat_LVM – Controls the availability of an LVM Volume Group"
---

<p>ocf_heartbeat_LVM &#8211; Controls the availability of an LVM Volume Group</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>LVM</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Resource script for LVM. It manages an Linux Volume Manager volume (LVM) as an HA resource.</p>
<h2>Supported Parameters</h2>
<p><code>volgrpname</code></p>
<dl>
<dd>The name of volume group. </p>
<p> (required, string, no default)</dl>
<p> <code>exclusive</code></p>
<dl>
<dd>If set, the volume group will be activated exclusively. This option works one of two ways. If the volume group has the cluster attribute set, then the volume group will be activated exclusively using clvmd across the cluster. If the cluster attribute is not set, the volume group will be activated exclusively through the use of the volume_list filter in lvm.conf. In the filter scenario, the LVM agent verifies that pacemaker&#8217;s configuration will result in the volume group only being active on a single node in the cluster and that the local node&#8217;s volume_list filter will prevent the volume group from activating outside of the resource agent. On activation this agent claims the volume group through the use of a unique tag, and then overrides the volume_list field in a way that allows the volume group to be activated only by the agent. To use exclusive activation without clvmd, the volume_list in lvm.conf must be initialized. If volume groups exist locally that are not controlled by the cluster, such as the root volume group, make sure those volume groups are listed in the volume_list so they will be allowed to activate on bootup. </p>
<p> (optional, boolean, default false)</dl>
<p> <code>tag</code></p>
<dl>
<dd>If &quot;exclusive&quot; is set on a non clustered volume group, this overrides the tag to be used. </p>
<p> (optional, string, default &quot;pacemaker&quot;)</dl>
<p> <code>partial_activation</code></p>
<dl>
<dd>If set, the volume group will be activated even only partial of the physical volumes available. It helps to set to true, when you are using mirroring logical volumes. </p>
<p> (optional, string, default &quot;false&quot;)</dl>
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
<dd>Performs a status check. Suggested minimum timeout: 30.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 30. Suggested interval: 10.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a LVM resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_LVM ocf:heartbeat:LVM \
 params \
 volgrpname=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a LVM resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_LVM ocf:heartbeat:LVM \
 volgrpname=<i>string</i> \
 op monitor depth=&quot;0&quot; timeout=&quot;30&quot; interval=&quot;10&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/LVM_(resource_agent)">http://www.linux-ha.org/wiki/LVM_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
