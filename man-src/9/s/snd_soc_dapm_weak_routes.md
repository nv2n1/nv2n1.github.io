---
title: "snd_soc_dapm_weak_routes(9)"
name: "snd_soc_dapm_weak_routes"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_weak_routes/"
---

snd_soc_dapm_weak_routes - Mark routes between DAPM widgets as weak

<h2>Synopsis</h2>

<pre><code>int snd_soc_dapm_weak_routes(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>DAPM context</dl>
 

 <i>route</i>
<dl><dd>audio routes</dl>
 

 <i>num</i>
<dl><dd>number of routes</dl>

<h2>Description</h2>

Mark existing routes matching those specified in the passed array as being weak, meaning that they are ignored for the purpose of power decisions. The main intended use case is for sidetone paths which couple audio between other independent paths if they are both active in order to make the combination work better at the user level but which aren't intended to be "used". 

 Note that CODEC drivers should not use this as sidetone type paths can frequently also be used as bypass paths.

<h2>Copyright</h2>


