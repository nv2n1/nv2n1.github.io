---
title: "fixceil(3)"
name: "fixceil"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixceil/"
description: "fixceil – Returns the smallest integer not less than x. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixceil &#8211; Returns the smallest integer not less than x. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>int fixceil(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> Returns the smallest integer not less than x. That is, it rounds towards positive infinity. Example: </p>
<pre><code>
int result;
/* This will put 34 into `result'. */
result = fixceil(itofix(100) / 3);
/* This will round up to 17. */
result = fixceil(itofix(100) / 6);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixtoi/">fixtoi</a></code>(3), <code><a href="/docs/linux/man/3-fixfloor/">fixfloor</a></code>(3) </p>
<h2>Index</h2>
