---
title: "set_hardware_volume(3)"
name: "set_hardware_volume"
section: "3"
letter: "s"
url: "/docs/linux/man/3-set_hardware_volume/"
description: "set_hardware_volume – Alters the hardware sound output volume. Allegro game programming library."
---

<p>set_hardware_volume &#8211; Alters the hardware sound output volume. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

void set_hardware_volume(int digi_volume, int midi_volume);</code></pre>
<h2>Description</h2>
<p>Alters the hardware sound output volume. Specify volumes for both digital samples and MIDI playback, as integers from 0 to 255, or pass a negative value to leave one of the settings unchanged. Values bigger than 255 will be reduced to 255. This routine will use the hardware mixer to control the volume if it exists (i.e. the volume of all the applications on your machine will be affected), otherwise do nothing. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-set_volume/">set_volume</a></code>(3) </p>
