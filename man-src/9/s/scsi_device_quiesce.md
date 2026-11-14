---
title: "scsi_device_quiesce(9)"
name: "scsi_device_quiesce"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_quiesce/"
description: "scsi_device_quiesce – Block user issued commands."
---

<p>scsi_device_quiesce &#8211; Block user issued commands.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_device_quiesce(struct scsi_device *sdev);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device to quiesce.</dl>
<h2>Description</h2>
<p>This works by trying to transition to the SDEV_QUIESCE state (which must be a legal transition). When the device is in this state, only special requests will be accepted, all others will be deferred. Since special requests may also be requeued requests, a successful return doesn&#8217;t guarantee the device will be totally quiescent. </p>
<p> Must be called with user context, may sleep. </p>
<p> Returns zero if unsuccessful or an error if not.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
