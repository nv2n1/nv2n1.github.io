---
title: "jbd2_journal_errno(9)"
name: "jbd2_journal_errno"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_errno/"
description: "jbd2_journal_errno – returns the journal’s error state."
---

<p>jbd2_journal_errno &#8211; returns the journal&#8217;s error state.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_errno(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>journal to examine.</dl>
<h2>Description</h2>
<p>This is the errno number set with <code>jbd2_journal_abort</code>, the last time the journal was mounted &#8211; if the journal was stopped without calling abort this will be 0. </p>
<p> If the journal has been aborted on this mount time -EROFS will be returned.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
