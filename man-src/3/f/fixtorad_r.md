---
title: "fixtorad_r(3)"
name: "fixtorad_r"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixtorad_r/"
description: "fixtorad_r – Constant to convert angles in fixed point format to radians. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixtorad_r &#8211; Constant to convert angles in fixed point format to radians. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>extern const fixed fixtorad_r;</code></p>
<h2>DESCRIPTION</h2>
<p> This constant gives a ratio which can be used to convert a fixed point number in binary angle format to a fixed point number in radians. Example: </p>
<pre><code>
fixed rad_angle, binary_angle;
/* Set the binary angle to 90 degrees. */
binary_angle = 64;
/* Now convert to radians (about 1.57). */
rad_angle = fixmul(binary_angle, fixtorad_r);
</code></pre>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixmul/">fixmul</a></code>(3), <code><a href="/docs/linux/man/3-radtofix_r/">radtofix_r</a></code>(3) </p>
<h2>Index</h2>
