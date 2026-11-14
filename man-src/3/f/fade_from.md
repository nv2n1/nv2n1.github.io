---
title: "fade_from(3)"
name: "fade_from"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fade_from/"
description: "fade_from – Gradually fades the palette between two others. Allegro game programming library."
---

<h2>NAME</h2>
<p> fade_from &#8211; Gradually fades the palette between two others. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void fade_from(const PALETTE source, const PALETTE dest, int speed);</code></p>
<h2>DESCRIPTION</h2>
<p> Fades gradually from the source palette to the dest palette. The speed is from 1 (the slowest) up to 64 (instantaneous). </p>
<p> Note that this function will block your game while the fade is in effect, and it won&#8217;t work right visually if you are not in an 8 bit color depth resolution. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fade_in/">fade_in</a></code>(3), <code><a href="/docs/linux/man/3-fade_out/">fade_out</a></code>(3), <code><a href="/docs/linux/man/3-fade_interpolate/">fade_interpolate</a></code>(3), <code><a href="/docs/linux/man/3-fade_from_range/">fade_from_range</a></code>(3) </p>
<h2>Index</h2>
