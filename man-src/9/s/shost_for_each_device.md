---
title: "shost_for_each_device(9)"
name: "shost_for_each_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-shost_for_each_device/"
description: "shost_for_each_device – iterate over all devices of a host"
---

<p>shost_for_each_device &#8211; iterate over all devices of a host</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>shost_for_each_device(</code><i>sdev</i><code>, </code><i>shost</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>the struct scsi_device to use as a cursor</dl>
<p> <i>shost</i></p>
<dl>
<dd>the struct scsi_host to iterate over</dl>
<h2>Description</h2>
<p>Iterator that returns each device attached to <i>shost</i>. This loop takes a reference on each device and releases it at the end. If you break out of the loop, you must call scsi_device_put(sdev).</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
