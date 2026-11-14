---
title: "scsi_queue_work(9)"
name: "scsi_queue_work"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_queue_work/"
description: "scsi_queue_work – Queue work to the Scsi_Host workqueue."
---

<p>scsi_queue_work &#8211; Queue work to the Scsi_Host workqueue.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_queue_work(struct Scsi_Host *shost, struct work_struct *work);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>Pointer to Scsi_Host.</dl>
<p> <i>work</i></p>
<dl>
<dd>Work to queue for execution.</dl>
<h2>Description</h2>
<p>Return value: 1 &#8211; work queued for execution 0 &#8211; work is already queued -EINVAL &#8211; work queue doesn&#8217;t exist</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
