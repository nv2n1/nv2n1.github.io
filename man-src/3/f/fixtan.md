---
title: "fixtan(3)"
name: "fixtan"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixtan/"
description: "fixtan – Fixed point tangent of binary angles. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixtan &#8211; Fixed point tangent of binary angles. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixtan(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> This function finds the tangent of a value using a lookup table. The input value must be a fixed point binary angle. Example: </p>
<pre><code>
fixed angle, res_a, res_b;
float dif;

angle = itofix(37);
/* Prove that tan(angle) == sin(angle) / cos(angle). */
res_a = fixdiv(fixsin(angle), fixcos(angle));
res_b = fixtan(angle);
dif = fixtof(fixsub(res_a, res_b));
allegro_message("Precision error: %f
", dif);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the tangent of a fixed point binary format angle. The return value will be in radians. </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
