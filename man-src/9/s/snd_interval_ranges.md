---
title: "snd_interval_ranges(9)"
name: "snd_interval_ranges"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_interval_ranges/"
---

snd_interval_ranges - refine the interval value from the list of ranges

<h2>Synopsis</h2>

<pre><code>int snd_interval_ranges(struct snd_interval *i, unsigned int count, const struct snd_interval *ranges, unsigned int mask);</code></pre>

<h2>Arguments</h2>

<i>i</i>
<dl><dd><dd>the interval value to refine</dl>
 

 <i>count</i>
<dl><dd>the number of elements in the list of ranges</dl>
 

 <i>ranges</i>
<dl><dd>the ranges list</dl>
 

 <i>mask</i>
<dl><dd>the bit-mask to evaluate</dl>

<h2>Description</h2>

Refines the interval value from the list of ranges. When mask is non-zero, only the elements corresponding to bit 1 are evaluated.

<h2>Return</h2>

Positive if the value is changed, zero if it's not changed, or a negative error code.

<h2>Copyright</h2>


