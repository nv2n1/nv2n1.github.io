---
title: "fade_in_range(3)"
name: "fade_in_range"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fade_in_range/"
description: "fade_in_range – Gradually fades a part of the palette from black. Allegro game programming library."
---

<h2>NAME</h2>
<p> fade_in_range &#8211; Gradually fades a part of the palette from black. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void fade_in_range(const PALETTE p, int speed, int from, int to);</code></p>
<h2>DESCRIPTION</h2>
<p> Gradually fades a part of the palette from a black screen to the specified palette. The speed is from 1 (the slowest) up to 64 (instantaneous). This routine only affects colors between from and to (inclusive: pass 0 and 255 to fade the entire palette). </p>
<p> Note that this function will block your game while the fade is in effect, and it won&#8217;t work right visually if you are not in an 8 bit color depth resolution. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fade_in/">fade_in</a></code>(3) </p>
<h2>Index</h2>
