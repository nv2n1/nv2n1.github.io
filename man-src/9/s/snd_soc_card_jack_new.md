---
title: "snd_soc_card_jack_new(9)"
name: "snd_soc_card_jack_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_soc_card_jack_new/"
---

snd_soc_card_jack_new - Create a new jack

<h2>Synopsis</h2>

<pre><code>int snd_soc_card_jack_new(struct snd_soc_card *card, const char *id, int type, struct snd_soc_jack *jack, struct snd_soc_jack_pin *pins, unsigned int num_pins);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>ASoC card</dl>
 

 <i>id</i>
<dl><dd>an identifying string for this jack</dl>
 

 <i>type</i>
<dl><dd>a bitmask of enum snd_jack_type values that can be detected by this jack</dl>
 

 <i>jack</i>
<dl><dd>structure to use for the jack</dl>
 

 <i>pins</i>
<dl><dd>Array of jack pins to be added to the jack or NULL</dl>
 

 <i>num_pins</i>
<dl><dd>Number of elements in the <i>pins</i> array</dl>

<h2>Description</h2>

Creates a new jack object. 

 Returns zero if successful, or a negative error code on failure. On success jack will be initialised.

<h2>Copyright</h2>


