---
title: "skb_cow_data(9)"
name: "skb_cow_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-skb_cow_data/"
---

skb_cow_data - Check that a socket buffer's data buffers are writable

<h2>Synopsis</h2>

<pre><code>int skb_cow_data(struct sk_buff *skb, int tailbits, struct sk_buff **trailer);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>The socket buffer to check.</dl>
 

 <i>tailbits</i>
<dl><dd>Amount of trailing space to be added</dl>
 

 <i>trailer</i>
<dl><dd>Returned pointer to the skb where the <i>tailbits</i> space begins</dl>

<h2>Description</h2>

Make sure that the data buffers attached to a socket buffer are writable. If they are not, private copies are made of the data buffers and the socket buffer is set to use these instead. 

 If <i>tailbits</i> is given, make sure that there is space to write <i>tailbits</i> bytes of data beyond current end of socket buffer. <i>trailer</i> will be set to point to the skb in which this space begins. 

 The number of scatterlist elements required to completely map the COW'd and extended socket buffer will be returned.

<h2>Copyright</h2>


