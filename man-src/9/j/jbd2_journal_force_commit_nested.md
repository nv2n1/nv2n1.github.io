---
title: "jbd2_journal_force_commit_nested(9)"
name: "jbd2_journal_force_commit_nested"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_force_commit_nested/"
description: "jbd2_journal_force_commit_nested –"
---

<p>jbd2_journal_force_commit_nested &#8211;</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_force_commit_nested(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>journal to force Returns true if progress was made.</dl>
<h2>Description</h2>
<p>transaction. This is used for forcing out undo-protected data which contains bitmaps, when the fs is running out of space.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
