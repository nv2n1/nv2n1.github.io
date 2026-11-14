---
title: "fixsub(3)"
name: "fixsub"
section: "3"
letter: "f"
url: "/docs/linux/man/3-fixsub/"
description: "fixsub – Safe function to subtract fixed point numbers clamping underflow. Allegro game programming library."
---

<h2>NAME</h2>
<p> fixsub &#8211; Safe function to subtract fixed point numbers clamping underflow. Allegro game programming library.</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;<a href="file:/usr/include/allegro.h">allegro.h</a>&gt;</code> </p>
<p> <code>fixed fixsub(fixed x, fixed y);</code></p>
<h2>DESCRIPTION</h2>
<p> Although fixed point numbers can be subtracted with the normal &#8216;-&#8216; integer operator, that doesn&#8217;t provide any protection against overflow. If overflow is a problem, you should use this function instead. It is slower than using integer operators, but if an overflow occurs it will set `errno&#8217; and clamp the result, rather than just letting it wrap. Example: </p>
<pre><code>
fixed result;
/* This will put 4965 into `result'. */
result = fixsub(itofix(5000), itofix(35));
/* Sets `errno' and puts -32768 into `result'. */
result = fixsub(itofix(-31000), itofix(3000));
ASSERT(!errno); /* This will fail. */
</code></pre>
<h2>RETURN VALUE</h2>
<p> Returns the clamped result of subtracting `y&#8217; from `x&#8217;, setting `errno&#8217; to ERANGE if there was an overflow. </p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-fixadd/">fixadd</a></code>(3), <code><a href="/docs/linux/man/3-fixmul/">fixmul</a></code>(3), <code><a href="/docs/linux/man/3-fixdiv/">fixdiv</a></code>(3) </p>
<h2>Index</h2>
