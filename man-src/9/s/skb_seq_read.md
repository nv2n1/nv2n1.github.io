---
title: "skb_seq_read(9)"
name: "skb_seq_read"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_seq_read/"
description: "skb_seq_read – Sequentially read skb data"
---

<p>skb_seq_read &#8211; Sequentially read skb data</p>
<h2>Synopsis</h2>
<pre><code>unsigned int skb_seq_read(unsigned int consumed, const u8 **data, struct skb_seq_state *st);</code></pre>
<h2>Arguments</h2>
<p><i>consumed</i></p>
<dl>
<dd>
<dd>number of bytes consumed by the caller so far</dl>
<p> <i>data</i></p>
<dl>
<dd>destination pointer for data to be returned</dl>
<p> <i>st</i></p>
<dl>
<dd>state variable</dl>
<h2>Description</h2>
<p>Reads a block of skb data at <i>consumed</i> relative to the lower offset specified to <code>skb_prepare_seq_read</code>. Assigns the head of the data block to <i>data</i> and returns the length of the block or 0 if the end of the skb data or the upper offset has been reached. </p>
<p> The caller is not required to consume all of the data returned, i.e. <i>consumed</i> is typically set to the number of bytes already consumed and the next call to <code>skb_seq_read</code> will return the remaining part of the block. </p>
<p> Note 1: The size of each block of data returned can be arbitrary, this limitation is the cost for zerocopy sequential reads of potentially non linear data. </p>
<p> Note 2: Fragment lists within fragments are not implemented at the moment, state-&gt;root_skb could be replaced with a stack for this purpose.</p>
<h2>Copyright</h2>
