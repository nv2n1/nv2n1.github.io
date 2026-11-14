---
title: "fixmul(3)"
name: "fixmul"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixmul/"
description: "fixmul – Multiplies two fixed point values together. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixmul &#8211; Multiplies two fixed point values together. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixmul(fixed x, fixed y);</code></p>
<h2>DESCRIPTION</h2>
<p> A fixed point value can be multiplied or divided by an integer with the normal `*&#8217; and `/&#8217; operators. To multiply two fixed point values, though, you must use this function. </p>
<p> If an overflow occurs, `errno&#8217; will be set and the maximum possible value will be returned, but `errno&#8217; is not cleared if the operation is successful. This means that if you are going to test for overflow you should set `errno=0&#8242; before calling fixmul(). Example: </p>
<pre><code>
fixed result;

/* This will put 30000 into `result'. */
result = fixmul(itofix(10), itofix(3000));
/* But this overflows, and sets `errno'. */
result = fixmul(itofix(100), itofix(3000));
ASSERT(!errno);
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the clamped result of multiplying `x&#8217; by `y&#8217;, setting `errno&#8217; to ERANGE if there was an overflow. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixadd/">fixadd</a></code>(3), <code><a href="/docs/linux/man/3-fixsub/">fixsub</a></code>(3), <code><a href="/docs/linux/man/3-fixdiv/">fixdiv</a></code>(3), <code><a href="/docs/linux/man/3-ex3buf/">ex3buf</a></code>(3), <code><a href="/docs/linux/man/3-excustom/">excustom</a></code>(3), <code><a href="/docs/linux/man/3-exfixed/">exfixed</a></code>(3), <code><a href="/docs/linux/man/3-exspline/">exspline</a></code>(3), <code><a href="/docs/linux/man/3-exstars/">exstars</a></code>(3), <code><a href="/docs/linux/man/3-exupdate/">exupdate</a></code>(3) </p>
<h2>Index</h2>
