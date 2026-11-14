---
title: "snd_interval_list(9)"
name: "snd_interval_list"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_interval_list/"
---

snd_interval_list - refine the interval value from the list

<h2>Synopsis</h2>

<pre><code>int snd_interval_list(struct snd_interval *i, unsigned int count, const unsigned int *list, unsigned int mask);</code></pre>

<h2>Arguments</h2>

<i>i</i>
<dl><dd><dd>the interval value to refine</dl>
 

 <i>count</i>
<dl><dd>the number of elements in the list</dl>
 

 <i>list</i>
<dl><dd>the value list</dl>
 

 <i>mask</i>
<dl><dd>the bit-mask to evaluate</dl>

<h2>Description</h2>

Refines the interval value from the list. When mask is non-zero, only the elements corresponding to bit 1 are evaluated.

<h2>Return</h2>

Positive if the value is changed, zero if it's not changed, or a negative error code.

<h2>Copyright</h2>


