---
title: "snd_soc_component_update_bits_async(9)"
name: "snd_soc_component_update_bits_async"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_update_bits_async/"
description: "snd_soc_component_update_bits_async – Perform asynchronous read/modify/write cycle"
---

<p>snd_soc_component_update_bits_async &#8211; Perform asynchronous read/modify/write cycle</p>
<h2>Synopsis</h2>
<pre><code>int snd_soc_component_update_bits_async(struct snd_soc_component *component, unsigned int reg, unsigned int mask, unsigned int val);</code></pre>
<h2>Arguments</h2>
<p><i>component</i></p>
<dl>
<dd>
<dd>Component to update</dl>
<p> <i>reg</i></p>
<dl>
<dd>Register to update</dl>
<p> <i>mask</i></p>
<dl>
<dd>Mask that specifies which bits to update</dl>
<p> <i>val</i></p>
<dl>
<dd>New value for the bits specified by mask</dl>
<h2>Description</h2>
<p>This function is similar to <code>snd_soc_component_update_bits</code>, but the update operation is scheduled asynchronously. This means it may not be completed when the function returns. To make sure that all scheduled updates have been completed <code>snd_soc_component_async_complete</code> must be called.</p>
<h2>Return</h2>
<p>1 if the operation was successful and the value of the register changed, 0 if the operation was successful, but the value did not change. Returns a negative error code otherwise.</p>
<h2>Copyright</h2>
