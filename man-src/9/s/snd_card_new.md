---
title: "snd_card_new(9)"
name: "snd_card_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_card_new/"
---

snd_card_new - create and initialize a soundcard structure

<h2>Synopsis</h2>

<pre><code>int snd_card_new(struct device *parent, int idx, const char *xid, struct module *module, int extra_size, struct snd_card **card_ret);</code></pre>

<h2>Arguments</h2>

<i>parent</i>
<dl><dd><dd>the parent device object</dl>
 

 <i>idx</i>
<dl><dd>card index (address) [0 ... (SNDRV_CARDS-1)]</dl>
 

 <i>xid</i>
<dl><dd>card identification (ASCII string)</dl>
 

 <i>module</i>
<dl><dd>top level module for locking</dl>
 

 <i>extra_size</i>
<dl><dd>allocate this extra size after the main soundcard structure</dl>
 

 <i>card_ret</i>
<dl><dd>the pointer to store the created card instance</dl>

<h2>Description</h2>

Creates and initializes a soundcard structure. 

 The function allocates snd_card instance via kzalloc with the given space for the driver to use freely. The allocated struct is stored in the given card_ret pointer.

<h2>Return</h2>

Zero if successful or a negative error code.

<h2>Copyright</h2>


