---
title: "snd_soc_dapm_del_routes(9)"
name: "snd_soc_dapm_del_routes"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_dapm_del_routes/"
---

snd_soc_dapm_del_routes - Remove routes between DAPM widgets

<h2>Synopsis</h2>

<pre><code>int snd_soc_dapm_del_routes(struct snd_soc_dapm_context *dapm, const struct snd_soc_dapm_route *route, int num);</code></pre>

<h2>Arguments</h2>

<i>dapm</i>
<dl><dd><dd>DAPM context</dl>
 

 <i>route</i>
<dl><dd>audio routes</dl>
 

 <i>num</i>
<dl><dd>number of routes</dl>

<h2>Description</h2>

Removes routes from the DAPM context.

<h2>Copyright</h2>


