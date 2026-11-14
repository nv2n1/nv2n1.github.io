---
title: "jbd2_journal_ack_err(9)"
name: "jbd2_journal_ack_err"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_ack_err/"
description: "jbd2_journal_ack_err – Ack journal err."
---

<p>jbd2_journal_ack_err &#8211; Ack journal err.</p>
<h2>Synopsis</h2>
<pre><code>void jbd2_journal_ack_err(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>journal to act on.</dl>
<h2>Description</h2>
<p>An error must be cleared or acked to take a FS out of readonly mode.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
