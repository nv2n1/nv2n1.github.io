---
title: "snd_ac97_set_rate(9)"
name: "snd_ac97_set_rate"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_ac97_set_rate/"
---

snd_ac97_set_rate - change the rate of the given input/output.

<h2>Synopsis</h2>

<pre><code>int snd_ac97_set_rate(struct snd_ac97 *ac97, int reg, unsigned int rate);</code></pre>

<h2>Arguments</h2>

<i>ac97</i>
<dl><dd><dd>the ac97 instance</dl>
 

 <i>reg</i>
<dl><dd>the register to change</dl>
 

 <i>rate</i>
<dl><dd>the sample rate to set</dl>

<h2>Description</h2>

Changes the rate of the given input/output on the codec. If the codec doesn't support VAR, the rate must be 48000 (except for SPDIF). 

 The valid registers are AC97_PMC_MIC_ADC_RATE, AC97_PCM_FRONT_DAC_RATE, AC97_PCM_LR_ADC_RATE. AC97_PCM_SURR_DAC_RATE and AC97_PCM_LFE_DAC_RATE are accepted if the codec supports them. AC97_SPDIF is accepted as a pseudo register to modify the SPDIF status bits.

<h2>Return</h2>

Zero if successful, or a negative error code on failure.

<h2>Copyright</h2>


