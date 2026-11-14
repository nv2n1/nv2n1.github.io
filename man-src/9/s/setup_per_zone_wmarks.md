---
title: "setup_per_zone_wmarks(9)"
name: "setup_per_zone_wmarks"
section: "9"
letter: "s"
url: "/docs/linux/man/9-setup_per_zone_wmarks/"
---

setup_per_zone_wmarks - called when min_free_kbytes changes or when memory is hot-{added|removed}

<h2>Synopsis</h2>

<pre><code>void setup_per_zone_wmarks(void);</code></pre>

<h2>Arguments</h2>

<i>void</i>
<dl><dd><dd>no arguments</dl>

<h2>Description</h2>

Ensures that the watermark[min,low,high] values for each zone are set correctly with respect to min_free_kbytes.

<h2>Copyright</h2>


