---
title: "jbd2_journal_update_sb_errno(9)"
name: "jbd2_journal_update_sb_errno"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_update_sb_errno/"
description: "jbd2_journal_update_sb_errno – Update error in the journal."
---

<p>jbd2_journal_update_sb_errno &#8211; Update error in the journal.</p>
<h2>Synopsis</h2>
<pre><code>void jbd2_journal_update_sb_errno(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>The journal to update.</dl>
<h2>Description</h2>
<p>Update a journal&#8217;s errno. Write updated superblock to disk waiting for IO to complete.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
