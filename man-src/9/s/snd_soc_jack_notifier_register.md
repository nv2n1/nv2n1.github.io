---
title: "snd_soc_jack_notifier_register(9)"
name: "snd_soc_jack_notifier_register"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_notifier_register/"
---

snd_soc_jack_notifier_register - Register a notifier for jack status

<h2>Synopsis</h2>

<pre><code>void snd_soc_jack_notifier_register(struct snd_soc_jack *jack, struct notifier_block *nb);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>ASoC jack</dl>
 

 <i>nb</i>
<dl><dd>Notifier block to register</dl>

<h2>Description</h2>

Register for notification of the current status of the jack. Note that it is not possible to report additional jack events in the callback from the notifier, this is intended to support applications such as enabling electrical detection only when a mechanical detection event has occurred.

<h2>Copyright</h2>


