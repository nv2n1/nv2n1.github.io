---
title: "ocf_heartbeat_scsi2reservation(7)"
name: "ocf_heartbeat_scsi2reservation"
section: "7"
letter: "o"
url: "/docs/linux/man/7-ocf_heartbeat_scsi2reservation/"
description: "ocf_heartbeat_scsi2reservation – scsi-2 reservation"
---

<p>ocf_heartbeat_scsi2reservation &#8211; scsi-2 reservation</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>scsi2reservation</code> [start | stop | monitor | meta-data | validate-all]</dl>
<h2>Description</h2>
<dd>The scsi-2-reserve resource agent is a place holder for SCSI-2 reservation. A healthy instance of scsi-2-reserve resource, indicates the own of the specified SCSI device. This resource agent depends on the scsi_reserve from scsires package, which is Linux specific.</p>
<h2>Supported Parameters</h2>
<p><code>scsi_reserve</code></p>
<dl>
<dd>The scsi_reserve is a command from scsires package. It helps to issue SCSI-2 reservation on SCSI devices. (optional, string, default /usr/sbin/scsi_reserve)</dl>
<p> <code>sharedisk</code></p>
<dl>
<dd>The shared disk that can be reserved. (optional, string, default /dev/sdb)</dl>
<p> <code>start_loop</code></p>
<dl>
<dd>We are going to try several times before giving up. Start_loop indicates how many times we are going to re-try. (optional, string, default 10)</dl>
<h2>Supported Actions</h2>
<p>This resource agent supports the following actions (operations): </p>
<p> <code>start</code></p>
<dl>
<dd>Starts the resource. Suggested minimum timeout: 300.</dl>
<p> <code>stop</code></p>
<dl>
<dd>Stops the resource. Suggested minimum timeout: 100.</dl>
<p> <code>monitor</code></p>
<dl>
<dd>Performs a detailed status check. Suggested minimum timeout: 20. Suggested interval: 20.</dl>
<p> <code>meta-data</code></p>
<dl>
<dd>Retrieves resource agent metadata (internal use only). Suggested minimum timeout: 5.</dl>
<p> <code>validate-all</code></p>
<dl>
<dd>Performs a validation of the resource configuration. Suggested minimum timeout: 30.</dl>
<h2>Example</h2>
<p>The following is an example configuration for a scsi2reservation resource using the <code><a href="/docs/linux/man/8-crm/">crm</a></code>(8) shell: </p>
<pre><code>primitive example_scsi2reservation ocf:heartbeat:scsi2reservation \

op monitor depth=&quot;0&quot; timeout=&quot;20&quot; interval=&quot;20&quot;</code></pre>
<h2>See Also</h2>
<p>m[blue]<code><a rel="nofollow" href="http://www.linux-ha.org/wiki/scsi2reservation_(resource_agent)">http://www.linux-ha.org/wiki/scsi2reservation_(resource_agent)</a></code>m[]</p>
<h2>Author</h2>
<p><code>Linux-HA contributors (see the resource agent source for information about individual authors)</code></p>
