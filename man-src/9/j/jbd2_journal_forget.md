---
title: "jbd2_journal_forget(9)"
name: "jbd2_journal_forget"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2_journal_forget/"
description: "jbd2_journal_forget – bforget for potentially-journaled buffers."
---

<p>jbd2_journal_forget &#8211; <code>bforget</code> for potentially-journaled buffers.</p>
<h2>Synopsis</h2>
<pre><code>int jbd2_journal_forget(handle_t *handle, struct buffer_head *bh);</code></pre>
<h2>Arguments</h2>
<p><i>handle</i></p>
<dl>
<dd>
<dd>transaction handle</dl>
<p> <i>bh</i></p>
<dl>
<dd>bh to &#8216;forget&#8217;</dl>
<h2>Description</h2>
<p>We can only do the bforget if there are no commits pending against the buffer. If the buffer is dirty in the current running transaction we can safely unlink it. </p>
<p> bh may not be a journalled buffer at all &#8211; it may be a non-JBD buffer which came off the hashtable. Check for this. </p>
<p> Decrements bh-&gt;b_count by one. </p>
<p> Allow this call even if the handle has aborted &#8212; it may be part of the caller&#8217;s cleanup after an abort.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
