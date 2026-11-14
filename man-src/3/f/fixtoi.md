---
title: "fixtoi(3)"
name: "fixtoi"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixtoi/"
description: "fixtoi – Converts a fixed point to integer with rounding. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixtoi &#8211; Converts a fixed point to integer with rounding. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int fixtoi(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts fixed point to integer, rounding as required to the nearest integer. Example: </p>
<pre><code>
int result;
/* This will put 33 into `result'. */
result = fixtoi(itofix(100) / 3);
/* But this will round up to 17. */
result = fixtoi(itofix(100) / 6);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-itofix/">itofix</a></code>(3), <code><a href="/docs/linux/man/3-ftofix/">ftofix</a></code>(3), <code><a href="/docs/linux/man/3-fixtof/">fixtof</a></code>(3), <code><a href="/docs/linux/man/3-fixfloor/">fixfloor</a></code>(3), <code><a href="/docs/linux/man/3-fixceil/">fixceil</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
