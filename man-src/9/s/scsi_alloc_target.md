---
title: "scsi_alloc_target(9)"
name: "scsi_alloc_target"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_alloc_target/"
description: "scsi_alloc_target – allocate a new or find an existing target"
---

<p>scsi_alloc_target &#8211; allocate a new or find an existing target</p>
<h2>Synopsis</h2>
<pre><code>struct scsi_target *scsi_alloc_target(struct device *parent, int channel, uint id);</code></pre>
<h2>Arguments</h2>
<p><i>parent</i></p>
<dl>
<dd>
<dd>parent of the target (need not be a scsi host)</dl>
<p> <i>channel</i></p>
<dl>
<dd>target channel number (zero if no channels)</dl>
<p> <i>id</i></p>
<dl>
<dd>target id number</dl>
<h2>Description</h2>
<p>Return an existing target if one exists, provided it hasn&#8217;t already gone into STARGET_DEL state, otherwise allocate a new target. </p>
<p> The target is returned with an incremented reference, so the caller is responsible for both reaping and doing a last put</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
