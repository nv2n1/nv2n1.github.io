---
title: "nr_free_zone_pages(9)"
name: "nr_free_zone_pages"
section: "9"
letter: "n"
url: "/docs/linux/man/9-nr_free_zone_pages/"
description: "nr_free_zone_pages – count number of pages beyond high watermark"
---

<p>nr_free_zone_pages &#8211; count number of pages beyond high watermark</p>
<h2>Synopsis</h2>
<pre><code>unsigned long nr_free_zone_pages(int offset);</code></pre>
<h2>Arguments</h2>
<p><i>offset</i></p>
<dl>
<dd>
<dd>The zone index of the highest zone</dl>
<h2>Description</h2>
<p><code>nr_free_zone_pages</code> counts the number of counts pages which are beyond the high watermark within all zones at or below a given zone index. For each zone, the number of pages is calculated as: managed_pages &#8211; high_pages</p>
<h2>Copyright</h2>
