---
title: "jbd2_journal_lock_updates(9)"
name: "jbd2_journal_lock_updates"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_lock_updates/"
description: "jbd2_journal_lock_updates – establish a transaction barrier."
---

<p>jbd2_journal_lock_updates &#8211; establish a transaction barrier.</p>
<h2>Synopsis</h2>
<pre><code>void jbd2_journal_lock_updates(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to establish a barrier on.</dl>
<h2>Description</h2>
<p>This locks out any further updates from being started, and blocks until all existing updates have completed, returning only once the journal is in a quiescent state with no updates running. </p>
<p> The journal lock should not be held on entry.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
