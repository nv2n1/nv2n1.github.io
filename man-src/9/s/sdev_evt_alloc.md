---
title: "sdev_evt_alloc(9)"
name: "sdev_evt_alloc"
section: "9"
letter: "s"
url: "/docs/linux/man/9-sdev_evt_alloc/"
description: "sdev_evt_alloc – allocate a new scsi event"
---

<p>sdev_evt_alloc &#8211; allocate a new scsi event</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_event *sdev_evt_alloc(enum scsi_device_event evt_type, gfp_t gfpflags);</code></pre>
<h2>Arguments</h2>
<p><i>evt_type</i></p>
<dl>
<dd>
<dd>type of event to allocate</dl>
<p> <i>gfpflags</i></p>
<dl>
<dd>GFP flags for allocation</dl>
<h2>Description</h2>
<p>Allocates and returns a new scsi_event.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
