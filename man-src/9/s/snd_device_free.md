---
title: "snd_device_free(9)"
name: "snd_device_free"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_device_free/"
---

snd_device_free - release the device from the card

<h2>Synopsis</h2>

<pre><code>void snd_device_free(struct snd_card *card, void *device_data);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>device_data</i>
<dl><dd>the data pointer to release</dl>

<h2>Description</h2>

Removes the device from the list on the card and invokes the callbacks, dev_disconnect and dev_free, corresponding to the state. Then release the device.

<h2>Copyright</h2>


