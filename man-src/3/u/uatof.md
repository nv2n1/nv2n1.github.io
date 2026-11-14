---
title: "uatof(3)"
name: "uatof"
section: "3"
letter: "u"
url: "/docs/linux/man/3-uatof/"
description: "uatof – Converts a string into a double. Allegro game programming library."
---

<p>uatof &#8211; Converts a string into a double. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

double uatof(const char *s);</code></pre>
<h2>Description</h2>
<p>Convert as much of the string as possible to an equivalent double precision real number. This function is almost like `ustrtod(s, NULL)&#8217;.</p>
<h2>Return Value</h2>
<p>Returns the equivalent value, or zero if the string does not represent a number. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrtol/">ustrtol</a></code>(3), <code><a href="/docs/linux/man/3-ustrtod/">ustrtod</a></code>(3) </p>
