---
title: "part_round_stats(9)"
name: "part_round_stats"
section: "9"
letter: "p"
url: "/docs/linux/man/9-part_round_stats/"
---

part_round_stats - Round off the performance stats on a struct disk_stats.

<h2>Synopsis</h2>

<pre><code>void part_round_stats(int cpu, struct hd_struct *part);</code></pre>

<h2>Arguments</h2>

<i>cpu</i>
<dl><dd><dd>cpu number for stats access</dl>
 

 <i>part</i>
<dl><dd>target partition</dl>

<h2>Description</h2>

The average IO queue length and utilisation statistics are maintained by observing the current state of the queue length and the amount of time it has been in this state for. 

 Normally, that accounting is done on IO completion, but that can result in more than a second's worth of IO being accounted for within any one second, leading to &gt;100% utilisation. To deal with that, we call this function to do a round-off before returning the results when reading /proc/diskstats. This accounts immediately for all queue usage up to the current jiffies and restarts the counters again.

<h2>Copyright</h2>


