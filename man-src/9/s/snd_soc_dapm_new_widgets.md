---
title: "snd_soc_dapm_new_widgets(9)"
name: "snd_soc_dapm_new_widgets"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_new_widgets/"
---

snd_soc_dapm_new_widgets - add new dapm widgets

<h2>Synopsis</h2>

<pre><code>int snd_soc_dapm_new_widgets(struct snd_soc_card *card);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>card to be checked for new dapm widgets</dl>

<h2>Description</h2>

Checks the codec for any new dapm widgets and creates them if found. 

 Returns 0 for success.

<h2>Copyright</h2>


