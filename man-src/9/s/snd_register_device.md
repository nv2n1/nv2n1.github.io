---
title: "snd_register_device(9)"
name: "snd_register_device"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_register_device/"
description: "snd_register_device – Register the ALSA device file for the card"
---

<p>snd_register_device &#8211; Register the ALSA device file for the card</p>
<h2>Synopsis</h2>
<pre><code>int snd_register_device(int type, struct snd_card *card, int dev, const struct file_operations *f_ops, void *private_data, struct device *device);</code></pre>
<h2>Arguments</h2>
<p><i>type</i></p>
<dl>
<dd>
<dd>the device type, SNDRV_DEVICE_TYPE_XXX</dl>
<p> <i>card</i></p>
<dl>
<dd>the card instance</dl>
<p> <i>dev</i></p>
<dl>
<dd>the device index</dl>
<p> <i>f_ops</i></p>
<dl>
<dd>the file operations</dl>
<p> <i>private_data</i></p>
<dl>
<dd>user pointer for f_ops-&gt;<code>open</code></dl>
<p> <i>device</i></p>
<dl>
<dd>the device to register</dl>
<h2>Description</h2>
<p>Registers an ALSA device file for the given card. The operators have to be set in reg parameter.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure.</p>
<h2>Copyright</h2>
