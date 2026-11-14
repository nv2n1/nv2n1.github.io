---
title: "jbd2_journal_load(9)"
name: "jbd2_journal_load"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_load/"
description: "jbd2_journal_load – Read journal from disk."
---

<p>jbd2_journal_load &#8211; Read journal from disk.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_load(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to act on.</dl>
<h2>Description</h2>
<p>Given a journal_t structure which tells us which disk blocks contain a journal, read the journal from disk to initialise the in-memory structures.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
