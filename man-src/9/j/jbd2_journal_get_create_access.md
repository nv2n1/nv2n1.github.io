---
title: "jbd2_journal_get_create_access(9)"
name: "jbd2_journal_get_create_access"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_get_create_access/"
description: "jbd2_journal_get_create_access – notify intent to use newly created bh"
---

<p>jbd2_journal_get_create_access &#8211; notify intent to use newly created bh</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_get_create_access(handle_t *handle, struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>transaction to new buffer to</dl>
<p> <i>bh</i></p>
<dl>
<dd>new buffer.</dl>
<h2>Description</h2>
<p>Call this if you create a new bh.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
