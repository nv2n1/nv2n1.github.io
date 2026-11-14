---
title: "fade_interpolate(3)"
name: "fade_interpolate"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fade_interpolate/"
description: "fade_interpolate – Calculates a new palette interpolated between two others. Allegro game programming library."
---

<h2>NAME</h2>
<p> fade_interpolate &#8211; Calculates a new palette interpolated between two others. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>void fade_interpolate(const PALETTE source, const PALETTE dest,</code> <code>PALETTE output, int pos, int from, int to);</code></p>
<h2>DESCRIPTION</h2>
<p> Calculates a temporary palette part way between source and dest, returning it in the output parameter. The position between the two extremes is specified by the pos value: 0 returns an exact copy of source, 64 returns dest, 32 returns a palette half way between the two, etc. This routine only affects colors between from and to (inclusive: pass 0 and 255 to interpolate the entire palette). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fade_in/">fade_in</a></code>(3), <code><a href="/docs/linux/man/3-fade_out/">fade_out</a></code>(3), <code><a href="/docs/linux/man/3-fade_from/">fade_from</a></code>(3) </p>
<h2>Index</h2>
