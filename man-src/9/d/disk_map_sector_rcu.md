---
title: "disk_map_sector_rcu(9)"
name: "disk_map_sector_rcu"
section: "9"
letter: "d"
url: "/docs/linux/man/9-disk_map_sector_rcu/"
---

disk_map_sector_rcu - map sector to partition

<h2>Synopsis</h2>

<pre><code>struct hd_struct *disk_map_sector_rcu(struct gendisk *disk, sector_t sector);</code></pre>

<h2>Arguments</h2>

<i>disk</i>
<dl><dd><dd>gendisk of interest</dl>
 

 <i>sector</i>
<dl><dd>sector to map</dl>

<h2>Description</h2>

Find out which partition <i>sector</i> maps to on <i>disk</i>. This is primarily used for stats accounting.

<h2>Context</h2>

RCU read locked. The returned partition pointer is valid only while preemption is disabled.

<h2>Return</h2>

Found partition on success, part0 is returned if no partition matches

<h2>Copyright</h2>


