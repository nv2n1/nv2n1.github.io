---
title: "snd_power_wait(9)"
name: "snd_power_wait"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_power_wait/"
---

snd_power_wait - wait until the power-state is changed.

<h2>Synopsis</h2>

<pre><code>int snd_power_wait(struct snd_card *card, unsigned int power_state);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>soundcard structure</dl>
 

 <i>power_state</i>
<dl><dd>expected power state</dl>

<h2>Description</h2>

Waits until the power-state is changed.

<h2>Return</h2>

Zero if successful, or a negative error code.

<h2>Note</h2>

the power lock must be active before call.

<h2>Copyright</h2>


