---
title: "ata_host_suspend(9)"
name: "ata_host_suspend"
section: "9"
letter: "a"
url: "/docs/linux/man/9-ata_host_suspend/"
description: "ata_host_suspend – suspend host"
---

<p>ata_host_suspend &#8211; suspend host</p>
<h2>Synopsis</h2>
<pre><code>int ata_host_suspend(struct ata_host *host, pm_message_t mesg);</code></pre>
<h2>Arguments</h2>
<p><i>host</i></p>
<dl>
<dd>
<dd>host to suspend</dl>
<p> <i>mesg</i></p>
<dl>
<dd>PM message</dl>
<h2>Description</h2>
<p>Suspend <i>host</i>. Actual operation is performed by port suspend.</p>
<h2>Author</h2>
<p><code>Jeff Garzik</code></p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
