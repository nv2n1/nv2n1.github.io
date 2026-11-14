---
title: "snd_device_disconnect(9)"
name: "snd_device_disconnect"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_device_disconnect/"
description: "snd_device_disconnect – disconnect the device"
---

<p>snd_device_disconnect &#8211; disconnect the device</p>
<h2>Synopsis</h2>
<pre><code>void snd_device_disconnect(struct snd_card *card, void *device_data);</code></pre>
<h2>Arguments</h2>
<p><i>card</i></p>
<dl>
<dd>
<dd>the card instance</dl>
<p> <i>device_data</i></p>
<dl>
<dd>the data pointer to disconnect</dl>
<h2>Description</h2>
<p>Turns the device into the disconnection state, invoking dev_disconnect callback, if the device was already registered. </p>
<p> Usually called from <code>snd_card_disconnect</code>.</p>
<h2>Return</h2>
<p>Zero if successful, or a negative error code on failure or if the device not found.</p>
<h2>Copyright</h2>
