---
title: "jbd2_journal_force_commit(9)"
name: "jbd2_journal_force_commit"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_force_commit/"
description: "jbd2_journal_force_commit – force any uncommitted transactions"
---

<p>jbd2_journal_force_commit &#8211; force any uncommitted transactions</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_force_commit(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>journal to force</dl>
<h2>Description</h2>
<p>Caller want unconditional commit. We can only force the running transaction if we don&#8217;t have an active handle, otherwise, we will deadlock.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
