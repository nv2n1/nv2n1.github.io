---
title: "snd_ctl_boolean_stereo_info(9)"
name: "snd_ctl_boolean_stereo_info"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ctl_boolean_stereo_info/"
---

snd_ctl_boolean_stereo_info - Helper function for a standard boolean info callback with stereo two channels

<h2>Synopsis</h2>

<pre><code>int snd_ctl_boolean_stereo_info(struct snd_kcontrol *kcontrol, struct snd_ctl_elem_info *uinfo);</code></pre>

<h2>Arguments</h2>

<i>kcontrol</i>
<dl><dd><dd>the kcontrol instance</dl>
 

 <i>uinfo</i>
<dl><dd>info to store</dl>

<h2>Description</h2>

This is a function that can be used as info callback for a standard boolean control with stereo two channels.

<h2>Copyright</h2>


