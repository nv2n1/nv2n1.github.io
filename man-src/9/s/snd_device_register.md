---
title: "snd_device_register(9)"
name: "snd_device_register"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_device_register/"
description: "snd_device_register – register the device"
---

<p>snd_device_register &#8211; register the device</p>
<h2>Synopsis</h2>
<pre><code>int snd_device_register(struct snd_card *card, void *device_data);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>device_data</i></p>
<dl>
<dd>the data pointer to register</dl>
<h2>Description</h2>
<p>Registers the device which was already created via <code>snd_device_new</code>. Usually this is called from <code>snd_card_register</code>, but it can be called later if any new devices are created after invocation of <code>snd_card_register</code>.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure or if the device not found.</p>
<h2>Copyright</h2>
