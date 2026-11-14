---
title: "get_volume(3)"
name: "get_volume"
section: "3"
letter: "g"
url: "/docs/linux/man/3-get_volume/"
description: "get_volume – Retrieves the global sound output volume. Allegro game programming library."
---

<h2>NAME</h2>
<p> get_volume &#8211; Retrieves the global sound output volume. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void get_volume(int *digi_volume, int *midi_volume);</code></p>
<h2>DESCRIPTION</h2>
<p> Retrieves the global sound output volume, both for digital samples and MIDI playback, as integers from 0 to 255. Parameters digi_volume and midi_volume must be valid pointers to int, or NULL if not interested in specific value. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-set_volume/">set_volume</a></code>(3), <code><a href="/docs/linux/man/3-get_hardware_volume/">get_hardware_volume</a></code>(3) </p>
<h2>Index</h2>
