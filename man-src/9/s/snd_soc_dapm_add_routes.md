---
title: "snd_soc_dapm_add_routes(9)"
name: "snd_soc_dapm_add_routes"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_add_routes/"
description: "snd_soc_dapm_add_routes – Add routes between DAPM widgets"
---

<p>snd_soc_dapm_add_routes &#8211; Add routes between DAPM widgets</p>
<h2>Synopsis</h2>
<pre><code>int snd_soc_dapm_add_routes(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num);</code></pre>
<h2>Arguments</h2>
<p><i>dapm</i></p>
<dl>
<dd>
<dd>DAPM context</dl>
<p> <i>route</i></p>
<dl>
<dd>audio routes</dl>
<p> <i>num</i></p>
<dl>
<dd>number of routes</dl>
<h2>Description</h2>
<p>Connects 2 dapm widgets together via a named audio path. The sink is the widget receiving the audio signal, whilst the source is the sender of the audio signal. </p>
<p> Returns 0 for success else error. On error all resources can be freed with a call to <code>snd_soc_card_free</code>.</p>
<h2>Copyright</h2>
