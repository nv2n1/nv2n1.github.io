---
title: "scsi_init_devinfo(9)"
name: "scsi_init_devinfo"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_init_devinfo/"
description: "scsi_init_devinfo – set up the dynamic device list."
---

<p>scsi_init_devinfo &#8211; set up the dynamic device list.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_init_devinfo(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>Add command line entries from scsi_dev_flags, then add scsi_static_device_list entries to the scsi device info list.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
