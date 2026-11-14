---
title: "scsi_target_reap(9)"
name: "scsi_target_reap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_target_reap/"
description: "scsi_target_reap – check to see if target is in use and destroy if not"
---

<p>scsi_target_reap &#8211; check to see if target is in use and destroy if not</p>
<h2>Synopsis</h2>
<pre><code>void scsi_target_reap(struct scsi_target *starget);</code></pre>
<h2>Arguments</h2>
<p><i>starget</i></p>
<dl>
<dd>
<dd>target to be checked</dl>
<h2>Description</h2>
<p>This is used after removing a LUN or doing a last put of the target it checks atomically that nothing is using the target and removes it if so.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
