---
title: "jbd2_journal_dirty_metadata(9)"
name: "jbd2_journal_dirty_metadata"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_dirty_metadata/"
description: "jbd2_journal_dirty_metadata – mark a buffer as containing dirty metadata"
---

<p>jbd2_journal_dirty_metadata &#8211; mark a buffer as containing dirty metadata</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_dirty_metadata(handle_t *handle, struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>transaction to add buffer to.</dl>
<p> <i>bh</i></p>
<dl>
<dd>buffer to mark</dl>
<h2>Description</h2>
<p>mark dirty metadata which needs to be journaled as part of the current transaction. </p>
<p> The buffer must have previously had <code>jbd2_journal_get_write_access</code> called so that it has a valid journal_head attached to the buffer head. </p>
<p> The buffer is placed on the transaction&#8217;s metadata list and is marked as belonging to the transaction. </p>
<p> Returns error number or 0 on success. </p>
<p> Special care needs to be taken if the buffer already belongs to the current committing transaction (in which case we should have frozen data present for that commit). In that case, we don&#8217;t relink the buffer: that only gets done when the old transaction finally completes its commit.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
