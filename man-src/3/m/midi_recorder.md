---
title: "midi_recorder(3)"
name: "midi_recorder"
section: "3"
letter: "m"
url: "/docs/linux/man/3-midi_recorder/"
description: "midi_recorder – Hook notifying you when new MIDI data becomes available. Allegro game programming library."
---

<h2>NAME</h2>
<p> midi_recorder &#8211; Hook notifying you when new MIDI data becomes available. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern void (*midi_recorder)(unsigned char data);</code></p>
<h2>DESCRIPTION</h2>
<p> If set, this function is called by the MIDI input driver whenever a new byte of MIDI data becomes available. It runs in an interrupt context, so it must execute very quickly and all the code/data must be locked. This currently works only under DOS and Windows. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_sound_input/">install_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-midi_out/">midi_out</a></code>(3) </p>
<h2>Index</h2>
