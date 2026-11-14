---
title: "jbd2_journal_unlock_updates(9)"
name: "jbd2_journal_unlock_updates"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_unlock_updates/"
description: "jbd2_journal_unlock_updates – release barrier"
---

<p>jbd2_journal_unlock_updates &#8211; release barrier</p>
<h2>Synopsis</h2>
<pre><code>void jbd2_journal_unlock_updates(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to release the barrier on.</dl>
<h2>Description</h2>
<p>Release a transaction barrier obtained with <code>jbd2_journal_lock_updates</code>. </p>
<p> Should be called without the journal lock held.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
