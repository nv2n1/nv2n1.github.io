---
title: "gnet_stats_copy_basic(9)"
name: "gnet_stats_copy_basic"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gnet_stats_copy_basic/"
description: "gnet_stats_copy_basic – copy basic statistics into statistic TLV"
---

<p>gnet_stats_copy_basic &#8211; copy basic statistics into statistic TLV</p>
<h2>Synopsis</h2>
<pre><code>int gnet_stats_copy_basic(const seqcount_t *running, struct gnet_dump *d, struct gnet_stats_basic_cpu __percpu *cpu, struct gnet_stats_basic_packed *b);</code></pre>
<h2>Arguments</h2>
<p><i>running</i></p>
<dl>
<dd>
<dd>seqcount_t pointer</dl>
<p> <i>d</i></p>
<dl>
<dd>dumping handle</dl>
<p> <i>cpu</i></p>
<dl>
<dd>copy statistic per cpu</dl>
<p> <i>b</i></p>
<dl>
<dd>basic statistics</dl>
<h2>Description</h2>
<p>Appends the basic statistics to the top level TLV created by <code>gnet_stats_start_copy</code>. </p>
<p> Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.</p>
<h2>Copyright</h2>
