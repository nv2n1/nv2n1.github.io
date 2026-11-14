---
title: "get_gendisk(9)"
name: "get_gendisk"
section: "9"
letter: "g"
url: "/docs/linux/man/9-get_gendisk/"
---

get_gendisk - get partitioning information for a given device

<h2>Synopsis</h2>

<pre><code>struct gendisk *get_gendisk(dev_t devt, int *partno);</code></pre>

<h2>Arguments</h2>

<i>devt</i>
<dl><dd><dd>device to get partitioning information for</dl>
 

 <i>partno</i>
<dl><dd>returned partition index</dl>

<h2>Description</h2>

This function gets the structure containing partitioning information for the given device <i>devt</i>.

<h2>Copyright</h2>


