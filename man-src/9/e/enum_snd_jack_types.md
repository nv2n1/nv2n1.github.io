---
title: "enum_snd_jack_types(9)"
name: "enum_snd_jack_types"
section: "9"
letter: "e"
url: "/docs/linux/man/9-enum_snd_jack_types/"
---

enum_snd_jack_types - Jack types which can be reported

<h2>Synopsis</h2>

<pre>enum snd_jack_types {
 SND_JACK_HEADPHONE,
 SND_JACK_MICROPHONE,
 SND_JACK_HEADSET,
 SND_JACK_LINEOUT,
 SND_JACK_MECHANICAL,
 SND_JACK_VIDEOOUT,
 SND_JACK_AVOUT,
 SND_JACK_LINEIN,
 SND_JACK_BTN_0,
 SND_JACK_BTN_1,
 SND_JACK_BTN_2,
 SND_JACK_BTN_3,
 SND_JACK_BTN_4,
 SND_JACK_BTN_5
}; </pre>

<h2>Constants</h2>

SND_JACK_HEADPHONE
<dl><dd>Headphone</dl>
 

 SND_JACK_MICROPHONE
<dl><dd>Microphone</dl>
 

 SND_JACK_HEADSET
<dl><dd>Headset</dl>
 

 SND_JACK_LINEOUT
<dl><dd>Line out</dl>
 

 SND_JACK_MECHANICAL
<dl><dd>Mechanical switch</dl>
 

 SND_JACK_VIDEOOUT
<dl><dd>Video out</dl>
 

 SND_JACK_AVOUT
<dl><dd>AV (Audio Video) out</dl>
 

 SND_JACK_LINEIN
<dl><dd>Line in</dl>
 

 SND_JACK_BTN_0
<dl><dd>Button 0</dl>
 

 SND_JACK_BTN_1
<dl><dd>Button 1</dl>
 

 SND_JACK_BTN_2
<dl><dd>Button 2</dl>
 

 SND_JACK_BTN_3
<dl><dd>Button 3</dl>
 

 SND_JACK_BTN_4
<dl><dd>Button 4</dl>
 

 SND_JACK_BTN_5
<dl><dd>Button 5</dl>

<h2>Description</h2>

These values are used as a bitmask. 

 Note that this must be kept in sync with the lookup table in sound/core/jack.c.

<h2>Copyright</h2>


