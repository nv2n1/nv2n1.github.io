---
title: "snd_soc_component_exit_regmap(9)"
name: "snd_soc_component_exit_regmap"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_component_exit_regmap/"
description: "snd_soc_component_exit_regmap – De-initialize regmap instance for the component"
---

<p>snd_soc_component_exit_regmap &#8211; De-initialize regmap instance for the component</p>
<h2>Synopsis</h2>
<pre><code>void snd_soc_component_exit_regmap(struct snd_soc_component *component);</code></pre>
<h2>Arguments</h2>
<p><i>component</i></p>
<dl>
<dd>
<dd>The component for which to de-initialize the regmap instance</dl>
<h2>Description</h2>
<p>Calls <code>regmap_exit</code> on the regmap instance associated to the component and removes the regmap instance from the component. </p>
<p> This function should only be used if <code>snd_soc_component_init_regmap</code> was used to initialize the regmap instance.</p>
<h2>Copyright</h2>
