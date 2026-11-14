---
title: "midi_meta_callback(3)"
name: "midi_meta_callback"
section: "3"
letter: "m"
url: "/docs/linux/man/3-midi_meta_callback/"
description: "midi_msg_callback, midi_meta_callback, midi_sysex_callback – Hook functions allowing you to intercept MIDI player events. Allegro game programming library."
---

<h2>NAME</h2>
<p> midi_msg_callback, midi_meta_callback, midi_sysex_callback &#8211; Hook functions allowing you to intercept MIDI player events. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern void (*midi_msg_callback)(int msg, int byte1, int byte2);</code> </p>
<p> <code>extern void (*midi_meta_callback)(int type, const unsigned char *data, int length);</code> </p>
<p> <code>extern void (*midi_sysex_callback)(const unsigned char *data, int length);</code></p>
<h2>DESCRIPTION</h2>
<p> Hook functions allowing you to intercept MIDI player events. If set to anything other than NULL, these routines will be called for each MIDI message, meta-event, and system exclusive data block respectively. They will execute in an interrupt handler context, so all the code and data they use should be locked, and they must not call any operating system functions. In general you just use these routines to set some flags and respond to them later in your mainline code. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-play_midi/">play_midi</a></code>(3) </p>
<h2>Index</h2>
