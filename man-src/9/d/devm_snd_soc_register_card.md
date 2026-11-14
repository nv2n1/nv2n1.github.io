---
title: "devm_snd_soc_register_card(9)"
name: "devm_snd_soc_register_card"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_snd_soc_register_card/"
---

devm_snd_soc_register_card - resource managed card registration

<h2>Synopsis</h2>

<pre><code>int devm_snd_soc_register_card(struct device *dev, struct snd_soc_card *card);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Device used to manage card</dl>
 

 <i>card</i>
<dl><dd>Card to register</dl>

<h2>Description</h2>

Register a card with automatic unregistration when the device is unregistered.

<h2>Copyright</h2>


