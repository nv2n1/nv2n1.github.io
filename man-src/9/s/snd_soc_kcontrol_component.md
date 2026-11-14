---
title: "snd_soc_kcontrol_component(9)"
name: "snd_soc_kcontrol_component"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_kcontrol_component/"
description: "snd_soc_kcontrol_component – Returns the component that registered the control"
---

<p>snd_soc_kcontrol_component &#8211; Returns the component that registered the control</p>
<h2>Synopsis</h2>
<pre><code>struct snd_soc_component *snd_soc_kcontrol_component(struct snd_kcontrol *kcontrol);</code></pre>
<h2>Arguments</h2>
<p><i>kcontrol</i></p>
<dl>
<dd>
<dd>The control for which to get the component</dl>
<h2>Note</h2>
<p>This function will work correctly if the control has been registered for a component. Either with <code>snd_soc_add_codec_controls</code> or <code>snd_soc_add_platform_controls</code> or via table based setup for either a CODEC, a platform or component driver. Otherwise the behavior is undefined.</p>
<h2>Copyright</h2>
