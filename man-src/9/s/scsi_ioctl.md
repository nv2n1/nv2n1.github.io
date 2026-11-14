---
title: "scsi_ioctl(9)"
name: "scsi_ioctl"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_ioctl/"
description: "scsi_ioctl – Dispatch ioctl to scsi device"
---

<p>scsi_ioctl &#8211; Dispatch ioctl to scsi device</p>
<h2>Synopsis</h2>
<pre><code>int scsi_ioctl(struct scsi_device *sdev, int cmd, void __user *arg);</code></pre>
<h2>Arguments</h2>
<p><i>sdev</i></p>
<dl>
<dd>
<dd>scsi device receiving ioctl</dl>
<p> <i>cmd</i></p>
<dl>
<dd>which ioctl is it</dl>
<p> <i>arg</i></p>
<dl>
<dd>data associated with ioctl</dl>
<h2>Description</h2>
<p>The <code>scsi_ioctl</code> function differs from most ioctls in that it does not take a major/minor number as the dev field. Rather, it takes a pointer to a struct scsi_device.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
