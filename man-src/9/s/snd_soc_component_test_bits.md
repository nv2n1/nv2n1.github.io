---
title: "snd_soc_component_test_bits(9)"
name: "snd_soc_component_test_bits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_test_bits/"
---

snd_soc_component_test_bits - Test register for change

<h2>Synopsis</h2>

<pre><code>int snd_soc_component_test_bits(struct snd_soc_component *component, unsigned int reg, unsigned int mask, unsigned int value);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>component</dl>
 

 <i>reg</i>
<dl><dd>Register to test</dl>
 

 <i>mask</i>
<dl><dd>Mask that specifies which bits to test</dl>
 

 <i>value</i>
<dl><dd>Value to test against</dl>

<h2>Description</h2>

Tests a register with a new value and checks if the new value is different from the old value.

<h2>Return</h2>

1 for change, otherwise 0.

<h2>Copyright</h2>


