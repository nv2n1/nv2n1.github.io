---
title: "fixtof(3)"
name: "fixtof"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixtof/"
description: "fixtof – Converts a fixed point to floating point. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixtof &#8211; Converts a fixed point to floating point. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>double fixtof(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts fixed point to floating point. Example: </p>
<pre><code>
float result;

/* This will put 33.33333 into `result'. */
result = fixtof(itofix(100) / 3);
/* This will put 16.66666 into `result'. */
result = fixtof(itofix(100) / 6);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-ftofix/">ftofix</a></code>(3), <code><a href="/docs/linux/man/3-itofix/">itofix</a></code>(3), <code><a href="/docs/linux/man/3-fixtoi/">fixtoi</a></code>(3), <code><a href="/docs/linux/man/3-exfixed/">exfixed</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
<h2>Index</h2>
