---
title: "sdev_evt_send_simple(9)"
name: "sdev_evt_send_simple"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sdev_evt_send_simple/"
description: "sdev_evt_send_simple – send asserted event to uevent thread"
---

<p>sdev_evt_send_simple &#8211; send asserted event to uevent thread</p>
<h2>Synopsis</h2>
<pre><code>void sdev_evt_send_simple(struct scsi_device *sdev, enum scsi_device_event evt_type, gfp_t gfpflags);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi_device event occurred on</dl>
<p> <i>evt_type</i></p>
<dl>
<dd>type of event to send</dl>
<p> <i>gfpflags</i></p>
<dl>
<dd>GFP flags for allocation</dl>
<h2>Description</h2>
<p>Assert scsi device event asynchronously, given an event type.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
