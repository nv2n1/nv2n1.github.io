---
title: "scsi_eh_flush_done_q(9)"
name: "scsi_eh_flush_done_q"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_eh_flush_done_q/"
description: "scsi_eh_flush_done_q – finish processed commands or retry them."
---

<p>scsi_eh_flush_done_q &#8211; finish processed commands or retry them.</p>
<h2>Synopsis</h2>
<pre><code>void scsi_eh_flush_done_q(struct list_head *done_q);</code></pre>
<h2>Arguments</h2>
<p><i>done_q</i></p>
<dl>
<dd>
<dd>list_head of processed commands.</dl>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
