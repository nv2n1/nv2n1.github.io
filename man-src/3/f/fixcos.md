---
title: "fixcos(3)"
name: "fixcos"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixcos/"
description: "fixcos – Fixed point cosine of binary angles. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixcos &#8211; Fixed point cosine of binary angles. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixcos(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> This function finds the cosine of a value using a lookup table. The input value must be a fixed point binary angle. Example: </p>
<pre><code>
fixed angle;
float result;

/* Set the binary angle to 45 degrees. */
angle = itofix(32);
/* The cosine of 45 degrees is about 0.7071. */
result = fixtof(fixcos(angle));
ASSERT(result &gt; 0.7 &amp;&amp; result &lt; 0.71);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the cosine of a fixed point binary format angle. The return value will be in radians. </p>
<h2>SEE ALSO</h2>
<p> , <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
