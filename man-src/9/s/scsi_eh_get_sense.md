---
title: "scsi_eh_get_sense(9)"
name: "scsi_eh_get_sense"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_eh_get_sense/"
description: "scsi_eh_get_sense – Get device sense data."
---

<p>scsi_eh_get_sense &#8211; Get device sense data.</p>
<h2>Synopsis</h2>
<pre><code>int scsi_eh_get_sense(struct list_head *work_q, struct list_head *done_q);</code></pre>
<h2>Arguments</h2>
<p><i>work_q</i></p>
<dl>
<dd>
<dd>Queue of commands to process.</dl>
<p> <i>done_q</i></p>
<dl>
<dd>Queue of processed commands.</dl>
<h2>Description</h2>
<p>See if we need to request sense information. if so, then get it now, so we have a better idea of what to do.</p>
<h2>Notes</h2>
<p>This has the unfortunate side effect that if a shost adapter does not automatically request sense information, we end up shutting it down before we request it. </p>
<p> All drivers should request sense information internally these days, so for now all I have to say is tough noogies if you end up in here. </p>
<p> XXX: Long term this code should go away, but that needs an audit of all LLDDs first.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
