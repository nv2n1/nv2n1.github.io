---
title: "load_midi_patches(3)"
name: "load_midi_patches"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_midi_patches/"
description: "load_midi_patches – Forces the MIDI driver to load a set of patches. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_midi_patches &#8211; Forces the MIDI driver to load a set of patches. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int load_midi_patches();</code></p>
<h2>DESCRIPTION</h2>
<p> Forces the MIDI driver to load the entire set of patches ready for use. You will not normally need to call this, because Allegro automatically loads whatever data is required for the current MIDI file, but you must call it before sending any program change messages via the midi_out() command.</p>
<h2>RETURN VALUE</h2>
<p> Returns non-zero if an error occurred. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_sound/">install_sound</a></code>(3), <code><a href="/docs/linux/man/3-midi_out/">midi_out</a></code>(3) </p>
<h2>Index</h2>
