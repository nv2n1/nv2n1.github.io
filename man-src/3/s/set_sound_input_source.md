---
title: "set_sound_input_source(3)"
name: "set_sound_input_source"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_sound_input_source/"
description: "set_sound_input_source – Selects the audio input source. Allegro game programming library."
---

<p>set_sound_input_source &#8211; Selects the audio input source. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int set_sound_input_source(int source);</code></pre>
<h2>Description</h2>
<p>Selects the audio input source. The parameter should be one of the values: </p>
<pre> SOUND_INPUT_MIC
 SOUND_INPUT_LINE
 SOUND_INPUT_CD</pre>
<h2>Return Value</h2>
<p>The function returns zero on success, or -1 if the hardware does not provide an input select register (ie. you have no control over the input source). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-start_sound_input/">start_sound_input</a></code>(3) </p>
