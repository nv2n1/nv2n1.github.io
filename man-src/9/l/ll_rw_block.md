---
title: "ll_rw_block(9)"
name: "ll_rw_block"
section: "9"
letter: "l"
url: "/docs/linux/man/9-ll_rw_block/"
description: "ll_rw_block – level access to block devices (DEPRECATED)"
---

<p>ll_rw_block &#8211; level access to block devices (DEPRECATED)</p>
<h2>Synopsis</h2>
<pre><code>void ll_rw_block(int op, int op_flags, int nr, struct buffer_head *bhs[]);</code></pre>
<h2>Arguments</h2>
<p><i>op</i></p>
<dl>
<dd>
<dd>whether to <code>READ</code> or <code>WRITE</code></dl>
<p> <i>op_flags</i></p>
<dl>
<dd>rq_flag_bits</dl>
<p> <i>nr</i></p>
<dl>
<dd>number of struct buffer_heads in the array</dl>
<p> <i>bhs[]</i></p>
<dl>
<dd>array of pointers to struct buffer_head</dl>
<h2>Description</h2>
<p><code>ll_rw_block</code> takes an array of pointers to struct buffer_heads, and requests an I/O operation on them, either a <code>REQ_OP_READ</code> or a <code>REQ_OP_WRITE</code>. <i>op_flags</i> contains flags modifying the detailed I/O behavior, most notably <code>REQ_RAHEAD</code>. </p>
<p> This function drops any buffer that it cannot get a lock on (with the BH_Lock state bit), any buffer that appears to be clean when doing a write request, and any buffer that appears to be up-to-date when doing read request. Further it marks as clean buffers that are processed for writing (the buffer cache won&#8217;t assume that they are actually clean until the buffer gets unlocked). </p>
<p> ll_rw_block sets b_end_io to simple completion handler that marks the buffer up-to-date (if appropriate), unlocks the buffer and wakes any waiters. </p>
<p> All of the buffers must be for the same device, and must also be a multiple of the current approved size for the device.</p>
<h2>Copyright</h2>
