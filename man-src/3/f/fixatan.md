---
title: "fixatan(3)"
name: "fixatan"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixatan/"
description: "fixatan – Fixed point inverse tangent lookup table. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixatan &#8211; Fixed point inverse tangent lookup table. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixatan(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> This function finds the inverse tangent of a value using a lookup table. The input value must be a fixed point radian. The inverse tangent is the value whose tangent is `x&#8217;. Example: </p>
<pre>
   fixed result;
   
   /* Sets `result' to binary angle 13. */
   result = fixatan(ftofix(0.326));
</pre>
<h2>RETURN VALUE</h2>
<p> Returns the inverse tangent of a fixed point value, measured as a fixed point binary format angle. </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
