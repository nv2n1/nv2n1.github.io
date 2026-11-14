---
title: "gnet_stats_start_copy_compat(9)"
name: "gnet_stats_start_copy_compat"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gnet_stats_start_copy_compat/"
description: "gnet_stats_start_copy_compat – start dumping procedure in compatibility mode"
---

<p>gnet_stats_start_copy_compat &#8211; start dumping procedure in compatibility mode</p>
<h2>Synopsis</h2>
<pre><code>int gnet_stats_start_copy_compat(struct sk_buff *skb, int type, int tc_stats_type, int xstats_type, spinlock_t *lock, struct gnet_dump *d, int padattr);</code></pre>
<h2>Arguments</h2>
<p><i>skb</i></p>
<dl>
<dd>
<dd>socket buffer to put statistics TLVs into</dl>
<p> <i>type</i></p>
<dl>
<dd>TLV type for top level statistic TLV</dl>
<p> <i>tc_stats_type</i></p>
<dl>
<dd>TLV type for backward compatibility struct tc_stats TLV</dl>
<p> <i>xstats_type</i></p>
<dl>
<dd>TLV type for backward compatibility xstats TLV</dl>
<p> <i>lock</i></p>
<dl>
<dd>statistics lock</dl>
<p> <i>d</i></p>
<dl>
<dd>dumping handle</dl>
<p> <i>padattr</i></p>
<dl>
<dd>padding attribute</dl>
<h2>Description</h2>
<p>Initializes the dumping handle, grabs the statistic lock and appends an empty TLV header to the socket buffer for use a container for all other statistic TLVS. </p>
<p> The dumping handle is marked to be in backward compatibility mode telling all <code>gnet_stats_copy_XXX</code> functions to fill a local copy of struct tc_stats. </p>
<p> Returns 0 on success or -1 if the room in the socket buffer was not sufficient.</p>
<h2>Copyright</h2>
