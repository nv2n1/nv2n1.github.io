---
title: "set_volume(3)"
name: "set_volume"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_volume/"
description: "set_volume – Alters the global sound output volume. Allegro game programming library."
---

<p>set_volume &#8211; Alters the global sound output volume. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_volume(int digi_volume, int midi_volume);</code></pre>
<h2>Description</h2>
<p>Alters the global sound output volume. Specify volumes for both digital samples and MIDI playback, as integers from 0 to 255, or pass a negative value to leave one of the settings unchanged. Values bigger than 255 will be reduced to 255. This routine will not alter the volume of the hardware mixer if it exists (i.e. only your application will be affected). </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-set_hardware_volume/">set_hardware_volume</a></code>(3) </p>
