---
title: "snd_jack_new(9)"
name: "snd_jack_new"
section: "9"
letter: "s"
url: "/docs/linux/man/9-snd_jack_new/"
---

snd_jack_new - Create a new jack

<h2>Synopsis</h2>

<pre><code>int snd_jack_new(struct snd_card *card, const char *id, int type, struct snd_jack **jjack, bool initial_kctl, bool phantom_jack);</code></pre>

<h2>Arguments</h2>

<i>card</i>
<dl><dd><dd>the card instance</dl>
 

 <i>id</i>
<dl><dd>an identifying string for this jack</dl>
 

 <i>type</i>
<dl><dd>a bitmask of enum snd_jack_type values that can be detected by this jack</dl>
 

 <i>jjack</i>
<dl><dd>Used to provide the allocated jack object to the caller.</dl>
 

 <i>initial_kctl</i>
<dl><dd>if true, create a kcontrol and add it to the jack list.</dl>
 

 <i>phantom_jack</i>
<dl><dd>Don't create a input device for phantom jacks.</dl>

<h2>Description</h2>

Creates a new jack object.

<h2>Return</h2>

Zero if successful, or a negative error code on failure. On success <i>jjack</i> will be initialised.

<h2>Copyright</h2>


