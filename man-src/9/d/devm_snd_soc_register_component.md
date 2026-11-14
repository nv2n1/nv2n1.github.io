---
title: "devm_snd_soc_register_component(9)"
name: "devm_snd_soc_register_component"
section: "9"
letter: "d"
url: "/docs/linux/man/9-devm_snd_soc_register_component/"
---

devm_snd_soc_register_component - resource managed component registration

<h2>Synopsis</h2>

<pre><code>int devm_snd_soc_register_component(struct device *dev, const struct snd_soc_component_driver *cmpnt_drv, struct snd_soc_dai_driver *dai_drv, int num_dai);</code></pre>

<h2>Arguments</h2>

<i>dev</i>
<dl><dd><dd>Device used to manage component</dl>
 

 <i>cmpnt_drv</i>
<dl><dd>Component driver</dl>
 

 <i>dai_drv</i>
<dl><dd>DAI driver</dl>
 

 <i>num_dai</i>
<dl><dd>Number of DAIs to register</dl>

<h2>Description</h2>

Register a component with automatic unregistration when the device is unregistered.

<h2>Copyright</h2>


