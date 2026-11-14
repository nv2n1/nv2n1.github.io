---
title: "snd_ctl_add_vmaster_hook(9)"
name: "snd_ctl_add_vmaster_hook"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_add_vmaster_hook/"
---

snd_ctl_add_vmaster_hook - Add a hook to a vmaster control

<h2>Synopsis</h2>

<pre><code>int snd_ctl_add_vmaster_hook(struct snd_kcontrol *kcontrol, void (*hook)(void *private_data, int), void *private_data);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>vmaster kctl element</dl>
 

 <i>hook</i>
<dl><dd>the hook function</dl>
 

 <i>private_data</i>
<dl><dd>the private_data pointer to be saved</dl>

<h2>Description</h2>

Adds the given hook to the vmaster control element so that it's called at each time when the value is changed.

<h2>Return</h2>

Zero.

<h2>Copyright</h2>


