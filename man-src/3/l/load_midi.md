---
title: "load_midi(3)"
name: "load_midi"
section: "3"
letter: "l"
url: "/docs/linux/man/3-load_midi/"
description: "load_midi – Loads a MIDI file. Allegro game programming library."
---

<h2>NAME</h2>
<p> load_midi &#8211; Loads a MIDI file. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>MIDI *load_midi(const char *filename);</code></p>
<h2>DESCRIPTION</h2>
<p> Loads a MIDI file (handles both format 0 and format 1). Example: </p>
<pre><code>
MIDI *music;
music = load_midi("backmus.mid");
if (!music)
    abort_on_error("Couldn't load background music!");
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns a pointer to a MIDI structure, or NULL on error. Remember to free this MIDI file later to avoid memory leaks. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-destroy_midi/">destroy_midi</a></code>(3), <code><a href="/docs/linux/man/3-play_midi/">play_midi</a></code>(3), <code><a href="/docs/linux/man/3-get_midi_length/">get_midi_length</a></code>(3), <code><a href="/docs/linux/man/3-exmidi/">exmidi</a></code>(3) </p>
<h2>Index</h2>
