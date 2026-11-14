---
title: "scsi_change_queue_depth(9)"
name: "scsi_change_queue_depth"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_change_queue_depth/"
description: "scsi_change_queue_depth – change a device’s queue depth"
---

<p>scsi_change_queue_depth &#8211; change a device&#8217;s queue depth</p>
<h2>Synopsis</h2>
<pre><code>int scsi_change_queue_depth(struct scsi_device *sdev, int depth);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>SCSI Device in question</dl>
<p> <i>depth</i></p>
<dl>
<dd>number of commands allowed to be queued to the driver</dl>
<h2>Description</h2>
<p>Sets the device queue depth and returns the new value.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
