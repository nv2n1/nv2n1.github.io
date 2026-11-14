---
title: "gnet_stats_finish_copy(9)"
name: "gnet_stats_finish_copy"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gnet_stats_finish_copy/"
description: "gnet_stats_finish_copy – finish dumping procedure"
---

<p>gnet_stats_finish_copy &#8211; finish dumping procedure</p>
<h2>Synopsis</h2>
<pre><code>int gnet_stats_finish_copy(struct gnet_dump *d);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>dumping handle</dl>
<h2>Description</h2>
<p>Corrects the length of the top level TLV to include all TLVs added by <code>gnet_stats_copy_XXX</code> calls. Adds the backward compatibility TLVs if <code>gnet_stats_start_copy_compat</code> was used and releases the statistics lock. </p>
<p> Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.</p>
<h2>Copyright</h2>
