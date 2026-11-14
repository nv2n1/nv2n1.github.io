---
title: "jbd2_journal_get_write_access(9)"
name: "jbd2_journal_get_write_access"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_get_write_access/"
description: "jbd2_journal_get_write_access – notify intent to modify a buffer for metadata (not data) update."
---

<p>jbd2_journal_get_write_access &#8211; notify intent to modify a buffer for metadata (not data) update.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_get_write_access(handle_t *handle, struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>transaction to add buffer modifications to</dl>
<p> <i>bh</i></p>
<dl>
<dd>bh to be used for metadata writes</dl>
<h2>Description</h2>
<p>Returns an error code or 0 on success. </p>
<p> In full data journalling mode the buffer may be of type BJ_AsyncData, because we&#8217;re <code>write</code>ing a buffer which is also part of a shared mapping.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
