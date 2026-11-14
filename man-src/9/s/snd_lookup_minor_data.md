---
title: "snd_lookup_minor_data(9)"
name: "snd_lookup_minor_data"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_lookup_minor_data/"
description: "snd_lookup_minor_data – get user data of a registered device"
---

<p>snd_lookup_minor_data &#8211; get user data of a registered device</p>
<h2>Synopsis</h2>
<pre><code>void *snd_lookup_minor_data(unsigned int minor, int type);</code></pre>
<h2>Arguments</h2>
<p><i>minor</i></p>
<dl>
<dd>
<dd>the minor number</dl>
<p> <i>type</i></p>
<dl>
<dd>device type (SNDRV_DEVICE_TYPE_XXX)</dl>
<h2>Description</h2>
<p>Checks that a minor device with the specified type is registered, and returns its user data pointer. </p>
<p> This function increments the reference counter of the card instance if an associated instance with the given minor number and type is found. The caller must call <code>snd_card_unref</code> appropriately later.</p>
<h2>Return</h2>
<p>The user data pointer if the specified device is found. <code>NULL</code> otherwise.</p>
<h2>Copyright</h2>
