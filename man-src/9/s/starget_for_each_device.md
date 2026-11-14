---
title: "starget_for_each_device(9)"
name: "starget_for_each_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-starget_for_each_device/"
description: "starget_for_each_device – helper to walk all devices of a target"
---

<p>starget_for_each_device &#8211; helper to walk all devices of a target</p>
<h2>Synopsis</h2>
<pre><code>void starget_for_each_device(struct scsi_target *starget, void *data, void (*fn)(struct scsi_device *, void *));</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>target whose devices we want to iterate over.</dl>
<p> <i>data</i></p>
<dl>
<dd>Opaque passed to each function call.</dl>
<p> <i>fn</i></p>
<dl>
<dd>Function to call on each device</dl>
<h2>Description</h2>
<p>This traverses over each device of <i>starget</i>. The devices have a reference that must be released by scsi_host_put when breaking out of the loop.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
