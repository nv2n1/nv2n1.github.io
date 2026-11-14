---
title: "fixsin(3)"
name: "fixsin"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixsin/"
description: "fixsin – Fixed point sine of binary angles. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixsin &#8211; Fixed point sine of binary angles. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixsin(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> This function finds the sine of a value using a lookup table. The input value must be a fixed point binary angle. Example: </p>
<pre><code>
fixed angle;
int result;

/* Set the binary angle to 90 degrees. */
angle = itofix(64);
/* The sine of 90 degrees is one. */
result = fixtoi(fixsin(angle));
ASSERT(result == 1);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the sine of a fixed point binary format angle. The return value will be in radians. </p>
<h2>SEE ALSO</h2>
<p> , <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
