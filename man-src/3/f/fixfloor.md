---
title: "fixfloor(3)"
name: "fixfloor"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixfloor/"
description: "fixfloor – Returns the greatest integer not greater than x. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixfloor &#8211; Returns the greatest integer not greater than x. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int fixfloor(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns the greatest integer not greater than x. That is, it rounds towards negative infinity. Example: </p>
<pre><code>
int result;
/* This will put 33 into `result'. */
result = fixfloor(itofix(100) / 3);
/* And this will round down to 16. */
result = fixfloor(itofix(100) / 6);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixtoi/">fixtoi</a></code>(3), <code><a href="/docs/linux/man/3-fixceil/">fixceil</a></code>(3) </p>
<h2>Index</h2>
