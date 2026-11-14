---
title: "ocf_heartbeat_iscsilogicalunit(7)"
name: "ocf_heartbeat_iscsilogicalunit"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_iscsilogicalunit/"
description: "ocf_heartbeat_iSCSILogicalUnit – Manages iSCSI Logical Units (LUs)"
---

<p>ocf_heartbeat_iSCSILogicalUnit &#8211; Manages iSCSI Logical Units (LUs)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>iSCSILogicalUnit</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Manages iSCSI Logical Unit. An iSCSI Logical unit is a subdivision of an SCSI Target, exported via a daemon that speaks the iSCSI protocol.</p>
<h2>Supported Parameters</h2>
<p><code>implementation</code></p>
<dl>
<dd>The iSCSI target daemon implementation. Must be one of &quot;iet&quot;, &quot;tgt&quot;, &quot;lio&quot;, or &quot;lio-t&quot;. If unspecified, an implementation is selected based on the availability of management utilities, with &quot;iet&quot; being tried first, then &quot;tgt&quot;, then &quot;lio&quot;, then &quot;lio-t&quot;. </p>
<p> (optional, string, no default)</dl>
<p> <code>target_iqn</code></p>
<dl>
<dd>The iSCSI Qualified Name (IQN) that this Logical Unit belongs to. </p>
<p> (required, string, no default)</dl>
<p> <code>lun</code></p>
<dl>
<dd>The Logical Unit number (LUN) exposed to initiators. </p>
<p> (required, integer, no default)</dl>
<p> <code>path</code></p>
<dl>
<dd>The path to the block device exposed. Some implementations allow this to be a regular file, too. </p>
<p> (required, string, no default)</dl>
<p> <code>scsi_id</code></p>
<dl>
<dd>The SCSI ID to be configured for this Logical Unit. The default is the resource name, truncated to 24 bytes. </p>
<p> (unique, optional, string, default &quot;default&quot;)</dl>
<p> <code>scsi_sn</code></p>
<dl>
<dd>The SCSI serial number to be configured for this Logical Unit. The default is a hash of the resource name, truncated to 8 bytes. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>vendor_id</code></p>
<dl>
<dd>The SCSI vendor ID to be configured for this Logical Unit. </p>
<p> (optional, string, no default)</dl>
<p> <code>product_id</code></p>
<dl>
<dd>The SCSI product ID to be configured for this Logical Unit. </p>
<p> (optional, string, no default)</dl>
<p> <code>tgt_bstype</code></p>
<dl>
<dd>TGT specific backing store type. If you want to use aio, make sure your tgtadm is built against libaio. See <a href="/docs/linux/man/8-tgtadm/">tgtadm</a>(8). </p>
<p> (optional, string, no default)</dl>
<p> <code>tgt_bsoflags</code></p>
<dl>
<dd>TGT specific backing store open flags (direct|sync). See <a href="/docs/linux/man/8-tgtadm/">tgtadm</a>(8). </p>
<p> (optional, string, no default)</dl>
<p> <code>tgt_device_type</code></p>
<dl>
<dd>TGT specific device type. See <a href="/docs/linux/man/8-tgtadm/">tgtadm</a>(8). </p>
<p> (optional, string, no default)</dl>
<p> <code>additional_parameters</code></p>
<dl>
<dd>Additional LU parameters. A space-separated list of &quot;name=value&quot; pairs which will be passed through to the iSCSI daemon&#8217;s management interface. The supported parameters are implementation dependent. Neither the name nor the value may contain whitespace. </p>
<p> (optional, string, no default)</dl>
<p> <code>allowed_initiators</code></p>
<dl>
<dd>Allowed initiators. A space-separated list of initiators allowed to connect to this lun. Initiators may be listed in any syntax the target implementation allows. If this parameter is empty or not set, access to this lun will not be allowed from any initiator, if target is not in demo mode. </p>
<p> This parameter is only necessary when using LIO. </p>
<p> (optional, string, no default)</dl>
<p> <code>lio_iblock</code></p>
<dl>
<dd>LIO iblock device name, a number starting from 0. </p>
<p> Using distinct values here avoids a warning in LIO &quot;LEGACY: SHARED HBA&quot;; and it is necessary when using multiple LUNs started at the same time (eg. on node failover) to prevent a race condition in tcm_core on mkdir() in /sys/kernel/config/target/core/. </p>
<p> (optional, integer, default 0)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 10.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 10.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 10. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 10.</dl>
<h2>Example Crm Shell</h2>
<p>The following is an example configuration for a iSCSILogicalUnit resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_iSCSILogicalUnit ocf:heartbeat:iSCSILogicalUnit \
 params \
 target_iqn=<i>string</i> \
 lun=<i>integer</i> \
 path=<i>string</i> \
 op monitor timeout=&quot;10&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a iSCSILogicalUnit resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_iSCSILogicalUnit ocf:heartbeat:iSCSILogicalUnit \
 target_iqn=<i>string</i> \
 lun=<i>integer</i> \
 path=<i>string</i> \
 op monitor timeout=&quot;10&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/iSCSILogicalUnit_(resource_agent)">http://www.linux-ha.org/wiki/iSCSILogicalUnit_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
