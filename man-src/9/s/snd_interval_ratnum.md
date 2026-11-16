---
title: "snd_interval_ratnum(9)"
name: "snd_interval_ratnum"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_interval_ratnum/"
---

snd_interval_ratnum - refine the interval value

<h2>Synopsis</h2>

<pre><code>int snd_interval_ratnum(struct snd_interval *i, unsigned int rats_count, const struct snd_ratnum *rats, unsigned int *nump, unsigned int *denp);</code></pre>

<h2>Arguments</h2>

<i>i</i>
<dl><dd></dd><dd>interval to refine</dd></dl>
 

 <i>rats_count</i>
<dl><dd>number of ratnum_t</dd></dl>
 

 <i>rats</i>
<dl><dd>ratnum_t array</dd></dl>
 

 <i>nump</i>
<dl><dd>pointer to store the resultant numerator</dd></dl>
 

 <i>denp</i>
<dl><dd>pointer to store the resultant denominator</dd></dl>

<h2>Return</h2>

Positive if the value is changed, zero if it's not changed, or a negative error code.

<h2>Copyright</h2>


