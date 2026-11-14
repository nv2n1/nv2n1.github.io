---
title: "snd_soc_component_update_bits(9)"
name: "snd_soc_component_update_bits"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_update_bits/"
---

snd_soc_component_update_bits - Perform read/modify/write cycle

<h2>Synopsis</h2>

<pre><code>int snd_soc_component_update_bits(struct snd_soc_component *component, unsigned int reg, unsigned int mask, unsigned int val);</code></pre>

<h2>Arguments</h2>

<i>component</i>
<dl><dd><dd>Component to update</dl>
 

 <i>reg</i>
<dl><dd>Register to update</dl>
 

 <i>mask</i>
<dl><dd>Mask that specifies which bits to update</dl>
 

 <i>val</i>
<dl><dd>New value for the bits specified by mask</dl>

<h2>Return</h2>

1 if the operation was successful and the value of the register changed, 0 if the operation was successful, but the value did not change. Returns a negative error code otherwise.

<h2>Copyright</h2>


