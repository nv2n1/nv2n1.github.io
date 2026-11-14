---
title: "sdev_evt_send(9)"
name: "sdev_evt_send"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sdev_evt_send/"
description: "sdev_evt_send – send asserted event to uevent thread"
---

<p>sdev_evt_send &#8211; send asserted event to uevent thread</p>
<h2>Synopsis</h2>
<pre><code>void sdev_evt_send(struct scsi_device *sdev, struct scsi_event *evt);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi_device event occurred on</dl>
<p> <i>evt</i></p>
<dl>
<dd>event to send</dl>
<h2>Description</h2>
<p>Assert scsi device event asynchronously.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
