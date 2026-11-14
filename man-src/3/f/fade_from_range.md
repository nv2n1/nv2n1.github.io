---
title: "fade_from_range(3)"
name: "fade_from_range"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fade_from_range/"
description: "fade_from_range – Gradually fades a part of the palette between two others. Allegro game programming library."
---

<h2>NAME</h2>
<p> fade_from_range &#8211; Gradually fades a part of the palette between two others. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void fade_from_range(const PALETTE source, const PALETTE dest,</code> <code>int speed, int from, int to);</code></p>
<h2>DESCRIPTION</h2>
<p> Gradually fades a part of the palette from the source palette to the dest palette. The speed is from 1 (the slowest) up to 64 (instantaneous). This routine only affects colors between from and to (inclusive: pass 0 and 255 to fade the entire palette). </p>
<p> Note that this function will block your game while the fade is in effect, and it won&#8217;t work right visually if you are not in an 8 bit color depth resolution. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fade_from/">fade_from</a></code>(3) </p>
<h2>Index</h2>
