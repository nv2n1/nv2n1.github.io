---
title: "iscsi_scan_finished(9)"
name: "iscsi_scan_finished"
section: "9"
letter: "i"
url: "/docs/linux/man/9-iscsi_scan_finished/"
description: "iscsi_scan_finished – helper to report when running scans are done"
---

<p>iscsi_scan_finished &#8211; helper to report when running scans are done</p>
<h2>Synopsis</h2>
<pre><code>int iscsi_scan_finished(struct Scsi_Host *shost, unsigned long time);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>scsi host</dl>
<p> <i>time</i></p>
<dl>
<dd>scan run time</dl>
<h2>Description</h2>
<p>This function can be used by drives like qla4xxx to report to the scsi layer when the scans it kicked off at module load time are done.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
