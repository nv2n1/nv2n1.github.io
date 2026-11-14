---
title: "skb_pull(9)"
name: "skb_pull"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_pull/"
---

skb_pull - remove data from the start of a buffer

<h2>Synopsis</h2>

<pre><code>unsigned char *skb_pull(struct sk_buff *skb, unsigned int len);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>buffer to use</dl>
 

 <i>len</i>
<dl><dd>amount of data to remove</dl>

<h2>Description</h2>

This function removes data from the start of a buffer, returning the memory to the headroom. A pointer to the next data in the buffer is returned. Once the data has been pulled future pushes will overwrite the old data.

<h2>Copyright</h2>


