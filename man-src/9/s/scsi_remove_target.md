---
title: "scsi_remove_target(9)"
name: "scsi_remove_target"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_remove_target/"
description: "scsi_remove_target – try to remove a target and all its devices"
---

<p>scsi_remove_target &#8211; try to remove a target and all its devices</p>
<h2>Synopsis</h2>
<pre><code>void scsi_remove_target(struct device *dev);</code></pre>
<h2>Arguments</h2>
<p><i>dev</i></p>
<dl>
<dd>
<dd>generic starget or parent of generic stargets to be removed</dl>
<h2>Note</h2>
<p>This is slightly racy. It is possible that if the user requests the addition of another device then the target won&#8217;t be removed.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
