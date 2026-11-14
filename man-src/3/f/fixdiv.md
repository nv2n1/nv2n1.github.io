---
title: "fixdiv(3)"
name: "fixdiv"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixdiv/"
description: "fixdiv – Fixed point division. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixdiv &#8211; Fixed point division. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixdiv(fixed x, fixed y);</code></p>
<h2>DESCRIPTION</h2>
<p> A fixed point value can be divided by an integer with the normal `/&#8217; operator. To divide two fixed point values, though, you must use this function. If a division by zero occurs, `errno&#8217; will be set and the maximum possible value will be returned, but `errno&#8217; is not cleared if the operation is successful. This means that if you are going to test for division by zero you should set `errno=0&#8242; before calling fixdiv(). Example: </p>
<pre><code>
fixed result;
/* This will put 0.06060 `result'. */
result = fixdiv(itofix(2), itofix(33));
/* This will put 0 into `result'. */
result = fixdiv(0, itofix(-30));
/* Sets `errno' and puts -32768 into `result'. */
result = fixdiv(itofix(-100), itofix(0));
ASSERT(!errno); /* This will fail. */
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the result of dividing `x&#8217; by `y&#8217;. If `y&#8217; is zero, returns the maximum possible fixed point value and sets `errno&#8217; to ERANGE. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixadd/">fixadd</a></code>(3), <code><a href="/docs/linux/man/3-fixsub/">fixsub</a></code>(3), <code><a href="/docs/linux/man/3-fixmul/">fixmul</a></code>(3), <code><a href="/docs/linux/man/3-exfixed/">exfixed</a></code>(3) </p>
<h2>Index</h2>
