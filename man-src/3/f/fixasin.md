---
title: "fixasin(3)"
name: "fixasin"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixasin/"
description: "fixasin – Fixed point inverse sine lookup table. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixasin &#8211; Fixed point inverse sine lookup table. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixasin(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> This function finds the inverse sine of a value using a lookup table. The input value must be a fixed point value. The inverse sine is defined only in the domain from `-1&#8242; to `1&#8242;. Outside of this input range, the function will set `errno&#8217; to EDOM and return zero. Example: </p>
<pre><code>
float angle;
fixed val;

/* Sets `val' to a right binary angle (`64'). */
val = fixasin(itofix(1));
/* Sets `angle' to 0.2405. */
angle = fixtof(fixmul(fixasin(ftofix(0.238)), fixtorad_r));
/* This will trigger the assert. */
val = fixasin(ftofix(-1.09));
ASSERT(!errno);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the inverse sine of a fixed point value, measured as fixed point binary format angle, or zero if the input was out of the range. All return values of this function will be in the range `-64&#8242; to `64&#8242;. </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
