---
title: "snd_ctl_boolean_mono_info(9)"
name: "snd_ctl_boolean_mono_info"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_boolean_mono_info/"
---

snd_ctl_boolean_mono_info - Helper function for a standard boolean info callback with a mono channel

<h2>Synopsis</h2>

<pre><code>int snd_ctl_boolean_mono_info(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>the kcontrol instance</dl>
 

 <i>uinfo</i>
<dl><dd>info to store</dl>

<h2>Description</h2>

This is a function that can be used as info callback for a standard boolean control with a single mono channel.

<h2>Copyright</h2>


