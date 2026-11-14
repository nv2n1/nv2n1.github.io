---
title: "jbd2_journal_get_undo_access(9)"
name: "jbd2_journal_get_undo_access"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_get_undo_access/"
description: "jbd2_journal_get_undo_access – Notify intent to modify metadata with non-rewindable consequences"
---

<p>jbd2_journal_get_undo_access &#8211; Notify intent to modify metadata with non-rewindable consequences</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_get_undo_access(handle_t *handle, struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>transaction</dl>
<p> <i>bh</i></p>
<dl>
<dd>buffer to undo</dl>
<h2>Description</h2>
<p>Sometimes there is a need to distinguish between metadata which has been committed to disk and that which has not. The ext3fs code uses this for freeing and allocating space, we have to make sure that we do not reuse freed space until the deallocation has been committed, since if we overwrote that space we would make the delete un-rewindable in case of a crash. </p>
<p> To deal with that, jbd2_journal_get_undo_access requests write access to a buffer for parts of non-rewindable operations such as delete operations on the bitmaps. The journaling code must keep a copy of the buffer&#8217;s contents prior to the undo_access call until such time as we know that the buffer has definitely been committed to disk. </p>
<p> We never need to know which transaction the committed data is part of, buffers touched here are guaranteed to be dirtied later and so will be committed to a new transaction in due course, at which point we can discard the old committed data pointer. </p>
<p> Returns error number or 0 on success.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
