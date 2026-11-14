---
title: "ocf_heartbeat_linuxscsi(7)"
name: "ocf_heartbeat_linuxscsi"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_linuxscsi/"
description: "ocf_heartbeat_LinuxSCSI – Enables and disables SCSI devices through the kernel SCSI hot-plug subsystem (deprecated)"
---

<p>ocf_heartbeat_LinuxSCSI &#8211; Enables and disables SCSI devices through the kernel SCSI hot-plug subsystem (deprecated)</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>LinuxSCSI</code> [start | stop | status | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>Deprecation warning: This agent makes use of Linux SCSI hot-plug functionality which has been superseded by SCSI reservations. It is deprecated and may be removed from a future release. See the scsi2reservation and sfex agents for alternatives. &#8212; This is a resource agent for LinuxSCSI. It manages the availability of a SCSI device from the point of view of the linux kernel. It make Linux believe the device has gone away, and it can make it come back again.</p>
<h2>Supported Parameters</h2>
<p><code>scsi</code></p>
<dl>
<dd>The SCSI instance to be managed. (required, string, no default)</dl>
<p> <code>ignore_deprecation</code></p>
<dl>
<dd>If set to true, suppresses the deprecation warning for this agent. (optional, boolean, default false)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 20s.</dl>
<p> <code>methods</code></p>
<dl>
<dd>Suggested minimum timeout: 5.</dl>
<p> <code>status</code></p>
<dl>
<dd>Performs a status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20s. Suggested interval: 10.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 5.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a LinuxSCSI resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_LinuxSCSI ocf:heartbeat:LinuxSCSI \
params \
scsi=string \
op monitor depth=&quot;0&quot; timeout=&quot;20s&quot; interval=&quot;10&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/LinuxSCSI_(resource_agent)">http://www.linux-ha.org/wiki/LinuxSCSI_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
