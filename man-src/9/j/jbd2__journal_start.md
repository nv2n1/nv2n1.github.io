---
title: "jbd2__journal_start(9)"
name: "jbd2__journal_start"
section: "9"
letter: "j"
url: "/docs/linux/man/9-jbd2__journal_start/"
description: "jbd2__journal_start – Obtain a new handle."
---

<p>jbd2__journal_start &#8211; Obtain a new handle.</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>handle_t * jbd2__journal_start(journal_t&nbsp;<wbr>*&nbsp;<wbr></code><i>journal</i><code>, int&nbsp;<wbr></code><i>nblocks</i><code>, int&nbsp;<wbr></code><i>rsv_blocks</i><code>, gfp_t&nbsp;<wbr></code><i>gfp_mask</i><code>, unsigned int&nbsp;<wbr></code><i>type</i><code>, unsigned int&nbsp;<wbr></code><i>line_no</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>journal</i></p>
<dl>
<dd>
<dd>Journal to start transaction on.</dl>
<p> <i>nblocks</i></p>
<dl>
<dd>number of block buffer we might modify</dl>
<p> <i>rsv_blocks</i></p>
<dl>
<dd>&#8212; undescribed &#8212;</dl>
<p> <i>gfp_mask</i></p>
<dl>
<dd>&#8212; undescribed &#8212;</dl>
<p> <i>type</i></p>
<dl>
<dd>&#8212; undescribed &#8212;</dl>
<p> <i>line_no</i></p>
<dl>
<dd>&#8212; undescribed &#8212;</dl>
<h2>Description</h2>
<p>We make sure that the transaction can guarantee at least nblocks of modified buffers in the log. We block until the log can guarantee that much space. Additionally, if rsv_blocks &gt; 0, we also create another handle with rsv_blocks reserved blocks in the journal. This handle is is stored in h_rsv_handle. It is not attached to any particular transaction and thus doesn&#8217;t block transaction commit. If the caller uses this reserved handle, it has to set h_rsv_handle to NULL as otherwise <code>jbd2_journal_stop</code> on the parent handle will dispose the reserved one. Reserved handle has to be converted to a normal handle using <code>jbd2_journal_start_reserved</code> before it can be used. </p>
<p> Return a pointer to a newly allocated handle, or an <code>ERR_PTR</code> value on failure.</p>
<h2>Authors</h2>
<p><code>Roger Gammans</code> &lt;rgammans [at] computer-surgery.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<p> <code>Stephen Tweedie</code> &lt;sct [at] redhat.com&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
