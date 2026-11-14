---
title: "typedef_journal_t(9)"
name: "typedef_journal_t"
section: "9"
letter: "t"
url: "/docs/linux/man/9-typedef_journal_t/"
description: "typedef_journal_t – The journal_t maintains all of the journaling state information for a single filesystem."
---

<p>typedef_journal_t &#8211; The journal_t maintains all of the journaling state information for a single filesystem.</p>
<h2>Synopsis</h2>
<pre>typedef journal_t;</pre>
<h2>Description</h2>
<p>journal_t is linked to from the fs superblock structure. </p>
<p> We use the journal_t to keep track of all outstanding transaction activity on the filesystem, and to manage the state of the log writing process. </p>
<p> This is an opaque datatype.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
