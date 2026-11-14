---
title: "itofix(3)"
name: "itofix"
section: "3"
letter: "i"
url: "/docs/linux/man/3-itofix/"
description: "itofix – Converts an integer to fixed point. Allegro game programming library."
---

<h2>NAME</h2>
<p> itofix &#8211; Converts an integer to fixed point. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed itofix(int x);</code></p>
<h2>DESCRIPTION</h2>
<p> Converts an integer to fixed point. This is the same thing as x&lt;&lt;16. Remember that overflows (trying to convert an integer greater than 32767) and underflows (trying to convert an integer lesser than -32768) are not detected even in debug builds! The values simply &quot;wrap around&quot;. Example: </p>
<pre><code>
fixed number;
/* This conversion is OK. */
number = itofix(100);
ASSERT(fixtoi(number) == 100);
number = itofix(64000);
/* This check will fail in debug builds. */
ASSERT(fixtoi(number) == 64000);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the value of the integer converted to fixed point ignoring overflows. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixtoi/">fixtoi</a></code>(3), <code><a href="/docs/linux/man/3-ftofix/">ftofix</a></code>(3), <code><a href="/docs/linux/man/3-fixtof/">fixtof</a></code>(3), <code><a href="/docs/linux/man/3-ex12bit/">ex12bit</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-ex3d/">ex3d</a></code>(3), <code><a href="/docs/linux/man/3-exblend/">exblend</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exfixed/">exfixed</a></code>(3), <code><a href="/docs/linux/man/3-exlights/">exlights</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exsprite/">exsprite</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3) </p>
<h2>Index</h2>
