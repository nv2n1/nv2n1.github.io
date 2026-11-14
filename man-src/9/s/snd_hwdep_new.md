---
title: "snd_hwdep_new(9)"
name: "snd_hwdep_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_hwdep_new/"
---

snd_hwdep_new - create a new hwdep instance

<h2>Synopsis</h2>

<pre><code>int snd_hwdep_new(struct snd_card *card, char *id, int device, struct snd_hwdep **rhwdep);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>id</i>
<dl><dd>the id string</dl>
 

 <i>device</i>
<dl><dd>the device index (zero-based)</dl>
 

 <i>rhwdep</i>
<dl><dd>the pointer to store the new hwdep instance</dl>

<h2>Description</h2>

Creates a new hwdep instance with the given index on the card. The callbacks (hwdep-&gt;ops) must be set on the returned instance after this call manually by the caller.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


