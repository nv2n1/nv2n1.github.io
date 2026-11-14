---
title: "snd_soc_limit_volume(9)"
name: "snd_soc_limit_volume"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_limit_volume/"
---

snd_soc_limit_volume - Set new limit to an existing volume control.

<h2>Synopsis</h2>

<pre><code>int snd_soc_limit_volume(struct snd_soc_card *card, const char *name, int max);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>where to look for the control</dl>
 

 <i>name</i>
<dl><dd>Name of the control</dl>
 

 <i>max</i>
<dl><dd>new maximum limit</dl>

<h2>Description</h2>

Return 0 for success, else error.

<h2>Copyright</h2>


