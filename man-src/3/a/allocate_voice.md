---
title: "allocate_voice(3)"
name: "allocate_voice"
section: "3"
letter: "a"
url: "/docs/linux/man/3-allocate_voice/"
description: "allocate_voice – Allocates a sound card voice for a sample. Allegro game programming library."
---

<h2>NAME</h2>
<p> allocate_voice &#8211; Allocates a sound card voice for a sample. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int allocate_voice(const SAMPLE *spl);</code></p>
<h2>DESCRIPTION</h2>
<p> Allocates a sound card voice and prepares it for playing the specified sample, setting up sensible default parameters (maximum volume, centre pan, no change of pitch, no looping). When you are finished with the voice you must free it by calling deallocate_voice() or release_voice(). Allegro can manage up to 256 simultaneous voices, but that limit may be lower due to hardware reasons.</p>
<h2>RETURN VALUE</h2>
<p> Returns the voice number, or -1 if no voices are available. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-deallocate_voice/">deallocate_voice</a></code>(3), <code><a href="/docs/linux/man/3-reallocate_voice/">reallocate_voice</a></code>(3), <code><a href="/docs/linux/man/3-release_voice/">release_voice</a></code>(3), <code><a href="/docs/linux/man/3-load_sample/">load_sample</a></code>(3) </p>
<h2>Index</h2>
