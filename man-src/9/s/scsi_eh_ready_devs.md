---
title: "scsi_eh_ready_devs(9)"
name: "scsi_eh_ready_devs"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_eh_ready_devs/"
description: "scsi_eh_ready_devs – check device ready state and recover if not."
---

<p>scsi_eh_ready_devs &#8211; check device ready state and recover if not.</p>
<h2>Synopsis</h2>
<pre><code>void scsi_eh_ready_devs(struct Scsi_Host *shost, struct list_head *work_q, struct list_head *done_q);</code></pre>
<h2>Arguments</h2>
<p><i>shost</i></p>
<dl>
<dd>
<dd>host to be recovered.</dl>
<p> <i>work_q</i></p>
<dl>
<dd>list_head for pending commands.</dl>
<p> <i>done_q</i></p>
<dl>
<dd>list_head for processed commands.</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
