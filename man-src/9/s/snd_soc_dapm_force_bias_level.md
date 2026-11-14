---
title: "snd_soc_dapm_force_bias_level(9)"
name: "snd_soc_dapm_force_bias_level"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_force_bias_level/"
description: "snd_soc_dapm_force_bias_level – Sets the DAPM bias level"
---

<p>snd_soc_dapm_force_bias_level &#8211; Sets the DAPM bias level</p>
<h2>Synopsis</h2>
<pre><code>int snd_soc_dapm_force_bias_level(struct snd_soc_dapm_context *dapm, enum snd_soc_bias_level level);</code></pre>
<h2>Arguments</h2>
<p><i>dapm</i></p>
<dl>
<dd>
<dd>The DAPM context for which to set the level</dl>
<p> <i>level</i></p>
<dl>
<dd>The level to set</dl>
<h2>Description</h2>
<p>Forces the DAPM bias level to a specific state. It will call the bias level callback of DAPM context with the specified level. This will even happen if the context is already at the same level. Furthermore it will not go through the normal bias level sequencing, meaning any intermediate states between the current and the target state will not be entered. </p>
<p> Note that the change in bias level is only temporary and the next time <code>snd_soc_dapm_sync</code> is called the state will be set to the level as determined by the DAPM core. The function is mainly intended to be used to used during probe or resume from suspend to power up the device so initialization can be done, before the DAPM core takes over.</p>
<h2>Copyright</h2>
