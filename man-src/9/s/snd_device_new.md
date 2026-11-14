---
title: "snd_device_new(9)"
name: "snd_device_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_device_new/"
---

snd_device_new - create an ALSA device component

<h2>Synopsis</h2>

<pre><code>int snd_device_new(struct snd_card *card, enum snd_device_type type, void *device_data, struct snd_device_ops *ops);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>type</i>
<dl><dd>the device type, SNDRV_DEV_XXX</dl>
 

 <i>device_data</i>
<dl><dd>the data pointer of this device</dl>
 

 <i>ops</i>
<dl><dd>the operator table</dl>

<h2>Description</h2>

Creates a new device component for the given data pointer. The device will be assigned to the card and managed together by the card. 

 The data pointer plays a role as the identifier, too, so the pointer address must be unique and unchanged.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


