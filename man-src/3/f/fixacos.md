---
title: "fixacos(3)"
name: "fixacos"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixacos/"
description: "fixacos – Fixed point inverse cosine lookup table. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixacos &#8211; Fixed point inverse cosine lookup table. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixacos(fixed x);</code></p>
<h2>DESCRIPTION</h2>
<p> This function finds the inverse cosine of a value using a lookup table. The input value must be a fixed point radian. The inverse cosine is defined only in the domain from `-1&#8242; to `1&#8242;. Outside of this input range, the function will set `errno&#8217; to EDOM and return zero. Example: </p>
<pre>
   fixed result;
   
   /* Sets `result' to binary angle 128. */
   result = fixacos(itofix(-1));
</pre>
<h2>RETURN VALUE</h2>
<p> Returns the inverse sine of a fixed point value, measured as fixed point binary format angle, or zero if the input was out of range. All return values of this function will be in the range `0&#8242; to `128&#8242;. </p>
<h2>SEE ALSO</h2>
<h2>Index</h2>
