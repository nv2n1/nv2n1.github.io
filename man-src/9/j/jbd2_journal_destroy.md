---
title: "jbd2_journal_destroy(9)"
name: "jbd2_journal_destroy"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_destroy/"
description: "jbd2_journal_destroy – Release a journal_t structure."
---

<p>jbd2_journal_destroy &#8211; Release a journal_t structure.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_destroy(journal_t *journal);</code></pre>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to act on.</dl>
<h2>Description</h2>
<p>Release a journal_t structure once it is no longer in use by the journaled object. Return &lt;0 if we couldn&#8217;t clean up the journal.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
