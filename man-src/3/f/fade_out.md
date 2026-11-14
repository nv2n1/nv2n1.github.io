---
title: "fade_out(3)"
name: "fade_out"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fade_out/"
description: "fade_out – Gradually fades the palette to black. Allegro game programming library."
---

<h2>NAME</h2>
<p> fade_out &#8211; Gradually fades the palette to black. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void fade_out(int speed);</code></p>
<h2>DESCRIPTION</h2>
<p> Fades gradually from the current palette to a black screen. The speed is from 1 (the slowest) up to 64 (instantaneous). </p>
<p> Note that this function will block your game while the fade is in effect, and it won&#8217;t work right visually if you are not in an 8 bit color depth resolution. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fade_in/">fade_in</a></code>(3), <code><a href="/docs/linux/man/3-fade_from/">fade_from</a></code>(3), <code><a href="/docs/linux/man/3-fade_interpolate/">fade_interpolate</a></code>(3), <code><a href="/docs/linux/man/3-fade_in_range/">fade_in_range</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3) </p>
<h2>Index</h2>
