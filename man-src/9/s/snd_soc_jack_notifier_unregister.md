---
title: "snd_soc_jack_notifier_unregister(9)"
name: "snd_soc_jack_notifier_unregister"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_notifier_unregister/"
---

snd_soc_jack_notifier_unregister - Unregister a notifier for jack status

<h2>Synopsis</h2>

<pre><code>void snd_soc_jack_notifier_unregister(struct snd_soc_jack *jack, struct notifier_block *nb);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>ASoC jack</dl>
 

 <i>nb</i>
<dl><dd>Notifier block to unregister</dl>

<h2>Description</h2>

Stop notifying for status changes.

<h2>Copyright</h2>


