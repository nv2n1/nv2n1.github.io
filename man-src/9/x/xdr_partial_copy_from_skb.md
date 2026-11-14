---
title: "xdr_partial_copy_from_skb(9)"
name: "xdr_partial_copy_from_skb"
section: "9"
letter: "x"
url: "/docs/linux/man/9-xdr_partial_copy_from_skb/"
description: "xdr_partial_copy_from_skb – copy data out of an skb"
---

<p>xdr_partial_copy_from_skb &#8211; copy data out of an skb</p>
<h2>Synopsis</h2>
<dl>
<dt> <code>ssize_t xdr_partial_copy_from_skb(struct xdr_buf&nbsp;<wbr>*&nbsp;<wbr></code><i>xdr</i><code>, unsigned int&nbsp;<wbr></code><i>base</i><code>, struct xdr_skb_reader&nbsp;<wbr>*&nbsp;<wbr></code><i>desc</i><code>, xdr_skb_read_actor&nbsp;<wbr></code><i>copy_actor</i><code>);</code></dl>
<h2>Arguments</h2>
<p><i>xdr</i></p>
<dl>
<dd>
<dd>target XDR buffer</dl>
<p> <i>base</i></p>
<dl>
<dd>starting offset</dl>
<p> <i>desc</i></p>
<dl>
<dd>sk_buff copy helper</dl>
<p> <i>copy_actor</i></p>
<dl>
<dd>virtual method for copying data</dl>
<h2>Copyright</h2>
