---
title: "fixatan2(3)"
name: "fixatan2"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixatan2/"
description: "fixatan2 – Fixed point version of the libc atan2() routine. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixatan2 &#8211; Fixed point version of the libc atan2() routine. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixatan2(fixed y, fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> This is a fixed point version of the libc atan2() routine. It computes the arc tangent of `y / x&#8217;, but the signs of both arguments are used to determine the quadrant of the result, and `x&#8217; is permitted to be zero. This function is useful to convert Cartesian coordinates to polar coordinates. Example: </p>
<pre><code>
fixed result;

/* Sets `result' to binary angle 64. */
result = fixatan2(itofix(1), 0);
/* Sets `result' to binary angle -109. */
result = fixatan2(itofix(-1), itofix(-2));
/* Fails the assert. */
result = fixatan2(0, 0);
ASSERT(!errno);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the arc tangent of `y / x&#8217; in fixed point binary format angle, from `-128&#8242; to `128&#8242;. If both `x&#8217; and `y&#8217; are zero, returns zero and sets `errno&#8217; to EDOM. </p>
<h2>SEE ALSO</h2>
<p> , <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3) </p>
<h2>Index</h2>
