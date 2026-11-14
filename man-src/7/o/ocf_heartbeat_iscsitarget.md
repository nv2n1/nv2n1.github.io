---
title: "ocf_heartbeat_iscsitarget(7)"
name: "ocf_heartbeat_iscsitarget"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_iscsitarget/"
description: "ocf_heartbeat_iSCSITarget – iSCSI target export agent"
---

<p>ocf_heartbeat_iSCSITarget &#8211; iSCSI target export agent</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>iSCSITarget</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Manages iSCSI targets. An iSCSI target is a collection of SCSI Logical Units (LUs) exported via a daemon that speaks the iSCSI protocol.</p>
<h2>Supported Parameters</h2>
<p><code>implementation</code></p>
<dl>
<dd>The iSCSI target daemon implementation. Must be one of &quot;iet&quot;, &quot;tgt&quot;, &quot;lio&quot;, or &quot;lio-t&quot;. If unspecified, an implementation is selected based on the availability of management utilities, with &quot;iet&quot; being tried first, then &quot;tgt&quot;, then &quot;lio&quot;, then &quot;lio-t&quot;. </p>
<p> (optional, string, no default)</dl>
<p> <code>iqn</code></p>
<dl>
<dd>The target iSCSI Qualified Name (IQN). Should follow the conventional &quot;iqn.yyyy-mm.&lt;reversed domain name&gt;[:identifier]&quot; syntax. </p>
<p> (unique, required, string, no default)</dl>
<p> <code>tid</code></p>
<dl>
<dd>The iSCSI target ID. Required for tgt. </p>
<p> (unique, optional, integer, no default)</dl>
<p> <code>portals</code></p>
<dl>
<dd>iSCSI network portal addresses. Not supported by all implementations. If unset, the default is to create one portal that listens on . </p>
<p> (optional, string, default &quot;0.0.0.0:3260&quot;)</dl>
<p> <code>allowed_initiators</code></p>
<dl>
<dd>Allowed initiators. A space-separated list of initiators allowed to connect to this target. Initiators may be listed in any syntax the target implementation allows. If this parameter is empty or not set, access to this target will be allowed from any initiator. </p>
<p> (optional, string, no default)</dl>
<p> <code>incoming_username</code></p>
<dl>
<dd>A username used for incoming initiator authentication. If unspecified, allowed initiators will be able to log in without authentication. This is a unique parameter, as it not allowed to re-use a single username across multiple target instances. </p>
<p> (unique, optional, string, no default)</dl>
<p> <code>incoming_password</code></p>
<dl>
<dd>A password used for incoming initiator authentication. </p>
<p> (optional, string, no default)</dl>
<p> <code>additional_parameters</code></p>
<dl>
<dd>Additional target parameters. A space-separated list of &quot;name=value&quot; pairs which will be passed through to the iSCSI daemon&#8217;s management interface. The supported parameters are implementation dependent. Neither the name nor the value may contain whitespace. </p>
<p> (optional, string, no default)</dl>
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
<p>The following is an example configuration for a iSCSITarget resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<dl>
<dd>
<pre>primitive p_iSCSITarget ocf:heartbeat:iSCSITarget \
 params \
 iqn=<i>string</i> \
 op monitor timeout=&quot;10&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>Example Pcs</h2>
<p>The following is an example configuration for a iSCSITarget resource using <code><a href="/docs/linux/man/8-pcs/">pcs</a></code>(8) </p>
<dl>
<dd>
<pre>pcs resource create p_iSCSITarget ocf:heartbeat:iSCSITarget \
 iqn=<i>string</i> \
 op monitor timeout=&quot;10&quot; interval=&quot;10&quot; depth=&quot;0&quot; </pre>
</dl>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/iSCSITarget_(resource_agent)">http://www.linux-ha.org/wiki/iSCSITarget_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
