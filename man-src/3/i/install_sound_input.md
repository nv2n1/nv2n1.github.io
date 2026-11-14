---
title: "install_sound_input(3)"
name: "install_sound_input"
section: "3"
letter: "i"
url: "/docs/linux/man/3-install_sound_input/"
description: "install_sound_input – Initialises the sound recorder module. Allegro game programming library."
---

<h2>NAME</h2>
<p> install_sound_input &#8211; Initialises the sound recorder module. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int install_sound_input(int digi, int midi);</code></p>
<h2>DESCRIPTION</h2>
<p> Initialises the sound recorder module. You must install the normal sound playback system before calling this routine. The two card parameters should use the same constants as install_sound(), including DIGI_NONE and MIDI_NONE to disable parts of the module, or DIGI_AUTODETECT and MIDI_AUTODETECT to guess the hardware.</p>
<h2>RETURN VALUE</h2>
<p> This function returns zero on success, and any other value if the machine or driver doesn&#8217;t support sound recording. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-start_sound_input/">start_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-midi_recorder/">midi_recorder</a></code>(3) </p>
<h2>Index</h2>
