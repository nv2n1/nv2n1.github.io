---
title: "is_compatible_font(3)"
name: "is_compatible_font"
section: "3"
letter: "i"
url: "/docs/linux/man/3-is_compatible_font/"
description: "is_compatible_font – Check if two fonts are of the same type. Allegro game programming library."
---

<h2>NAME</h2>
<p> is_compatible_font &#8211; Check if two fonts are of the same type. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int *is_compatible_font(FONT *f1, FONT *f2)</code></p>
<h2>DESCRIPTION</h2>
<p> This function compares the two fonts, which you can use to find out if Allegro is capable of merging them.</p>
<h2>RETURN VALUE</h2>
<p> Returns TRUE if the two fonts are of the same general type (both are color fonts or both are monochrome fonts, for instance). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-merge_fonts/">merge_fonts</a></code>(3), <code><a href="/docs/linux/man/3-is_trans_font/">is_trans_font</a></code>(3), <code><a href="/docs/linux/man/3-is_color_font/">is_color_font</a></code>(3), <code><a href="/docs/linux/man/3-is_mono_font/">is_mono_font</a></code>(3) </p>
<h2>Index</h2>
