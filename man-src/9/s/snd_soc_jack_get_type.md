---
title: "snd_soc_jack_get_type(9)"
name: "snd_soc_jack_get_type"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_jack_get_type/"
---

snd_soc_jack_get_type - Based on the mic bias value, this function returns the type of jack from the zones declared in the jack type

<h2>Synopsis</h2>

<pre><code>int snd_soc_jack_get_type(struct snd_soc_jack *jack, int micbias_voltage);</code></pre>

<h2>Arguments</h2>

<i>jack</i>
<dl><dd><dd>ASoC jack</dl>
 

 <i>micbias_voltage</i>
<dl><dd>mic bias voltage at adc channel when jack is plugged in</dl>

<h2>Description</h2>

Based on the mic bias value passed, this function helps identify the type of jack from the already declared jack zones

<h2>Copyright</h2>


