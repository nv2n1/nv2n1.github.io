---
title: "scsi_eh_finish_cmd(9)"
name: "scsi_eh_finish_cmd"
section: "9"
letter: "s"
url: "/docs/linux/man/9-scsi_eh_finish_cmd/"
description: "scsi_eh_finish_cmd – Handle a cmd that eh is finished with."
---

<p>scsi_eh_finish_cmd &#8211; Handle a cmd that eh is finished with.</p>
<h2>Synopsis</h2>
<pre><code>void scsi_eh_finish_cmd(struct scsi_cmnd *scmd, struct list_head *done_q);</code></pre>
<h2>Arguments</h2>
<p><i>scmd</i></p>
<dl>
<dd>
<dd>Original SCSI cmd that eh has finished.</dl>
<p> <i>done_q</i></p>
<dl>
<dd>Queue for processed commands.</dl>
<h2>Notes</h2>
<p>We don&#8217;t want to use the normal command completion while we are are still handling errors &#8211; it may cause other commands to be queued, and that would disturb what we are doing. Thus we really want to keep a list of pending commands for final completion, and once we are ready to leave error handling we handle completion for real.</p>
<h2>Authors</h2>
<p><code>James Bottomley</code> &lt;James.Bottomley [at] hansenpartnership.com&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Rob Landley</code> &lt;rob [at] landley.net&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
