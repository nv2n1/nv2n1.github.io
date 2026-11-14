---
title: "scsi_finish_async_scan(9)"
name: "scsi_finish_async_scan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_finish_async_scan/"
description: "scsi_finish_async_scan – asynchronous scan has finished"
---

<p>scsi_finish_async_scan &#8211; asynchronous scan has finished</p>
<h2>Synopsis</h2>
<pre><code>void scsi_finish_async_scan(struct async_scan_data *data);</code></pre>
<h2>Arguments</h2>
<p><i>data</i></p>
<dl>
<dd>
<dd>cookie returned from earlier call to <code>scsi_prep_async_scan</code></dl>
<h2>Description</h2>
<p>All the devices currently attached to this host have been found. This function announces all the devices it has found to the rest of the system.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
