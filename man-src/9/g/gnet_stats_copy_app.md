---
title: "gnet_stats_copy_app(9)"
name: "gnet_stats_copy_app"
section: "9"
letter: "g"
url: "/docs/linux/man/9-gnet_stats_copy_app/"
description: "gnet_stats_copy_app – copy application specific statistics into statistics TLV"
---

<p>gnet_stats_copy_app &#8211; copy application specific statistics into statistics TLV</p>
<h2>Synopsis</h2>
<pre><code>int gnet_stats_copy_app(struct gnet_dump *d, void *st, int len);</code></pre>
<h2>Arguments</h2>
<p><i>d</i></p>
<dl>
<dd>
<dd>dumping handle</dl>
<p> <i>st</i></p>
<dl>
<dd>application specific statistics data</dl>
<p> <i>len</i></p>
<dl>
<dd>length of data</dl>
<h2>Description</h2>
<p>Appends the application specific statistics to the top level TLV created by <code>gnet_stats_start_copy</code> and remembers the data for XSTATS if the dumping handle is in backward compatibility mode. </p>
<p> Returns 0 on success or -1 with the statistic lock released if the room in the socket buffer was not sufficient.</p>
<h2>Copyright</h2>
