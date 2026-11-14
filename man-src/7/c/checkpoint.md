---
title: "checkpoint(7)"
name: "checkpoint"
section: "7"
letter: "c"
url: "/docs/linux/man/7-checkpoint/"
description: "CHECKPOINT – force a transaction log checkpoint"
---

<p>CHECKPOINT &#8211; force a transaction log checkpoint </p>
<h2>Synopsis</h2>
<pre>CHECKPOINT</pre>
<h2>Description</h2>
<p>Write-Ahead Logging (WAL) puts a checkpoint in the transaction log every so often. (To adjust the automatic checkpoint interval, see the run-time configuration options checkpoint_segments and checkpoint_timeout.) The <code>CHECKPOINT</code> command forces an immediate checkpoint when the command is issued, without waiting for a scheduled checkpoint. </p>
<p> A checkpoint is a point in the transaction log sequence at which all data files have been updated to reflect the information in the log. All data files will be flushed to disk. Refer to in the documentation for more information about the WAL system. </p>
<p> Only superusers can call <code>CHECKPOINT</code>. The command is not intended for use during normal operation.</p>
<h2>Compatibility</h2>
<p>The <code>CHECKPOINT</code> command is a PostgreSQL language extension.</p>
