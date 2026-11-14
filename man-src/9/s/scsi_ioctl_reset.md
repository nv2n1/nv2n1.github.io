---
title: "scsi_ioctl_reset(9)"
name: "scsi_ioctl_reset"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_ioctl_reset/"
description: "scsi_ioctl_reset –"
---

<p>scsi_ioctl_reset &#8211;</p>
<h2>Synopsis</h2>
<pre><code>int scsi_ioctl_reset(struct scsi_device *dev, int __user *arg);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>scsi_device to operate on</dl>
<p> <i>arg</i></p>
<dl>
<dd>reset type (see sg.h)</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
