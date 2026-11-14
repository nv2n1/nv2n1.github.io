---
title: "digi_recorder(3)"
name: "digi_recorder"
section: "3"
letter: "d"
url: "/docs/linux/man/3-digi_recorder/"
description: "digi_recorder – Hook notifying you when a new sample buffer becomes available. Allegro game programming library."
---

<h2>NAME</h2>
<p> digi_recorder &#8211; Hook notifying you when a new sample buffer becomes available. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern void (*digi_recorder)();</code></p>
<h2>DESCRIPTION</h2>
<p> If set, this function is called by the input driver whenever a new sample buffer becomes available, at which point you can use read_sound_input() to copy the data into a more permanent location. It runs in an interrupt context, so it must execute very quickly, the code and all memory that it touches must be locked, and you cannot call any operating system routines or access disk files. This currently works only under DOS. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-install_sound_input/">install_sound_input</a></code>(3), <code><a href="/docs/linux/man/3-start_sound_input/">start_sound_input</a></code>(3) </p>
<h2>Index</h2>
