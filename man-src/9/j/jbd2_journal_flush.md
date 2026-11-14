---
title: "jbd2_journal_flush(9)"
name: "jbd2_journal_flush"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_flush/"
description: "jbd2_journal_flush – Flush journal"
---

<p>jbd2_journal_flush &#8211; Flush journal</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_flush(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to act on.</dl>
<h2>Description</h2>
<p>Flush all data for a given journal to disk and empty the journal. Filesystems can use this when remounting readonly to ensure that recovery does not need to happen on remount.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
