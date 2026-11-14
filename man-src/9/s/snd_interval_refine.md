---
title: "snd_interval_refine(9)"
name: "snd_interval_refine"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_interval_refine/"
---

snd_interval_refine - refine the interval value of configurator

<h2>Synopsis</h2>

<pre><code>int snd_interval_refine(struct snd_interval *i, const struct snd_interval *v);</code></pre>

<h2>Arguments</h2>

<i>i</i>
<dl><dd><dd>the interval value to refine</dl>
 

 <i>v</i>
<dl><dd>the interval value to refer to</dl>

<h2>Description</h2>

Refines the interval value with the reference value. The interval is changed to the range satisfying both intervals. The interval status (min, max, integer, etc.) are evaluated.

<h2>Return</h2>

Positive if the value is changed, zero if it's not changed, or a negative error code.

<h2>Copyright</h2>


