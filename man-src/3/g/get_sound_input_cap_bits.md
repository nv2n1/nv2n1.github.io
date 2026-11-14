---
title: "get_sound_input_cap_bits(3)"
name: "get_sound_input_cap_bits"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_sound_input_cap_bits/"
description: "get_sound_input_cap_bits – Checks which audio input sample formats are supported. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_sound_input_cap_bits &#8211; Checks which audio input sample formats are supported. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int get_sound_input_cap_bits();</code></p>
<h2>DESCRIPTION</h2>
<p> Checks which sample formats are supported by the current audio input driver, returning one of the bitfield values: </p>
<pre>
   0 = audio input not supported
   8 = eight bit audio input is supported
   16 = sixteen bit audio input is supported
   24 = both eight and sixteen bit audio input are supported
</pre>
<p> Example: </p>
<pre><code>
cap = get_sound_input_cap_bits();
if (cap == 0) {
    /* Ugh, no audio input supported? */
} else {
    if (cap &amp; 8) {
        /* We have eight bit audio input. */
    }
    if (cap &amp; 16) {
        /* We have sixteen bit audio input. */
    }
}
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-start_sound_input/">start_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_parm/">get_sound_input_cap_parm</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_rate/">get_sound_input_cap_rate</a></code>(3), <code><a href="/docs/linux/man/3-get_sound_input_cap_stereo/">get_sound_input_cap_stereo</a></code>(3) </p>
<h2>Index</h2>
