---
title: "gnet_stats_start_copy(9)"
name: "gnet_stats_start_copy"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gnet_stats_start_copy/"
---

gnet_stats_start_copy - start dumping procedure in compatibility mode

<h2>Synopsis</h2>

<pre><code>int gnet_stats_start_copy(struct sk_buff *skb, int type, spinlock_t *lock, struct gnet_dump *d, int padattr);</code></pre>

<h2>Arguments</h2>

<i>skb</i>
<dl><dd><dd>socket buffer to put statistics TLVs into</dl>
 

 <i>type</i>
<dl><dd>TLV type for top level statistic TLV</dl>
 

 <i>lock</i>
<dl><dd>statistics lock</dl>
 

 <i>d</i>
<dl><dd>dumping handle</dl>
 

 <i>padattr</i>
<dl><dd>padding attribute</dl>

<h2>Description</h2>

Initializes the dumping handle, grabs the statistic lock and appends an empty TLV header to the socket buffer for use a container for all other statistic TLVS. 

 Returns 0 on success or -1 if the room in the socket buffer was not sufficient.

<h2>Copyright</h2>


