---
title: "ftofix(3)"
name: "ftofix"
section: "3"
letter: "f"
url: "/docs/linux/man/3-ftofix/"
description: "ftofix – Converts a floating point value to fixed point. Allegro game programming library."
---

<h2>NAME</h2>
<p> ftofix &#8211; Converts a floating point value to fixed point. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed ftofix(double x);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts a floating point value to fixed point. Unlike itofix(), this function clamps values which could overflow the type conversion, setting `errno&#8217; to ERANGE in the process if this happens. Example: </p>
<pre><code>
fixed number;
number = itofix(-40000);
ASSERT(fixfloor(number) == -32768);
number = itofix(64000);
ASSERT(fixfloor(number) == 32767);
ASSERT(!errno); /* This will fail. */
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the value of the floating point value converted to fixed point clamping overflows (and setting `errno&#8217;). </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixtof/">fixtof</a></code>(3), <code><a href="/docs/linux/man/3-itofix/">itofix</a></code>(3), <code><a href="/docs/linux/man/3-fixtoi/">fixtoi</a></code>(3), <code><a href="/docs/linux/man/3-exfixed/">exfixed</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
