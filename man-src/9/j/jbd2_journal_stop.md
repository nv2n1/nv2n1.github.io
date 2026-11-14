---
title: "jbd2_journal_stop(9)"
name: "jbd2_journal_stop"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_stop/"
description: "jbd2_journal_stop – complete a transaction"
---

<p>jbd2_journal_stop &#8211; complete a transaction</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_stop(handle_t *handle);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>transaction to complete.</dl>
<h2>Description</h2>
<p>All done for a particular handle. </p>
<p> There is not much action needed here. We just return any remaining buffer credits to the transaction and remove the handle. The only complication is that we need to start a commit operation if the filesystem is marked for synchronous update. </p>
<p> jbd2_journal_stop itself will not usually return an error, but it may do so in unusual circumstances. In particular, expect it to return -EIO if a jbd2_journal_abort has been executed since the transaction began.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
