---
title: "scsi_prep_async_scan(9)"
name: "scsi_prep_async_scan"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_prep_async_scan/"
description: "scsi_prep_async_scan – prepare for an async scan"
---

<p>scsi_prep_async_scan &#8211; prepare for an async scan</p>
<h2>Synopsis</h2>
<pre><code>struct async_scan_data *scsi_prep_async_scan(struct Scsi_Host *shost);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>the host which will be scanned</dl>
<h2>Return</h2>
<p>a cookie to be passed to <code>scsi_finish_async_scan</code> </p>
<p> Tells the midlayer this host is going to do an asynchronous scan. It reserves the host&#8217;s position in the scanning list and ensures that other asynchronous scans started after this one won&#8217;t affect the ordering of the discovered devices.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
