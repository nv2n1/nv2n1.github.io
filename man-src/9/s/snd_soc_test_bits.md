---
title: "snd_soc_test_bits(9)"
name: "snd_soc_test_bits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_test_bits/"
---

snd_soc_test_bits - test register for change

<h2>Synopsis</h2>

<pre><code>int snd_soc_test_bits(struct snd_soc_codec *codec, unsigned int reg, unsigned int mask, unsigned int value);</code></pre>

<h2>Arguments</h2>

<i>codec</i>
<dl><dd><dd>audio codec</dl>
 

 <i>reg</i>
<dl><dd>codec register</dl>
 

 <i>mask</i>
<dl><dd>register mask</dl>
 

 <i>value</i>
<dl><dd>new value</dl>

<h2>Description</h2>

Tests a register with a new value and checks if the new value is different from the old value. 

 Returns 1 for change else 0.

<h2>Copyright</h2>


