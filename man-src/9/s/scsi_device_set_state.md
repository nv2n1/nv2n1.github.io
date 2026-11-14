---
title: "scsi_device_set_state(9)"
name: "scsi_device_set_state"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_device_set_state/"
description: "scsi_device_set_state – Take the given device through the device state model."
---

<p>scsi_device_set_state &#8211; Take the given device through the device state model.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_device_set_state(struct scsi_device *sdev, enum scsi_device_state state);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device to change the state of.</dl>
<p> <i>state</i></p>
<dl>
<dd>state to change to.</dl>
<h2>Description</h2>
<p>Returns zero if unsuccessful or an error if the requested transition is illegal.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
