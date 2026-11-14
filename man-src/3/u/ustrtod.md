---
title: "ustrtod(3)"
name: "ustrtod"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrtod/"
description: "ustrtod – Converts a string into a floating point number. Allegro game programming library."
---

<p>ustrtod &#8211; Converts a string into a floating point number. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

double ustrtod(const char *s, char **endp);</code></pre>
<h2>Description</h2>
<p>This function converts as many characters of `s&#8217; that look like a floating point number into one, and sets `*endp&#8217; to point to the first unused character, if `endp&#8217; is not a NULL pointer. Example: </p>
<pre><code>char *endp, *string = &quot;456.203 askdfg&quot;;
double number = ustrtod(string, &amp;endp);</code></pre>
<h2>Return Value</h2>
<p>Returns the string converted as a value of type `double&#8217;. If nothing was converted, returns zero with *endp pointing to the beginning of s. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrtol/">ustrtol</a></code>(3), <code><a href="/docs/linux/man/3-uatof/">uatof</a></code>(3) </p>
