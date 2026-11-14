---
title: "scsi_complete_async_scans(9)"
name: "scsi_complete_async_scans"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_complete_async_scans/"
description: "scsi_complete_async_scans – Wait for asynchronous scans to complete"
---

<p>scsi_complete_async_scans &#8211; Wait for asynchronous scans to complete</p>
<h2>Synopsis</h2>
<pre><code>int scsi_complete_async_scans(void);</code></pre>
<h2>Arguments</h2>
<p><i>void</i></p>
<dl>
<dd>
<dd>no arguments</dl>
<h2>Description</h2>
<p>When this function returns, any host which started scanning before this function was called will have finished its scan. Hosts which started scanning after this function was called may or may not have finished.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
