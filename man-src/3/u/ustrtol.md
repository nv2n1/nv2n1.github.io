---
title: "ustrtol(3)"
name: "ustrtol"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrtol/"
description: "ustrtol – Converts a string into an integer. Allegro game programming library."
---

<p>ustrtol &#8211; Converts a string into an integer. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

long ustrtol(const char *s, char **endp, int base);</code></pre>
<h2>Description</h2>
<p>This function converts the initial part of `s&#8217; to a signed integer, setting `*endp&#8217; to point to the first unused character, if `endp&#8217; is not a NULL pointer. The `base&#8217; argument indicates what base the digits (or letters) should be treated as. If `base&#8217; is zero, the base is determined by looking for `0x&#8217;, `0X&#8217;, or `0&#8242; as the first part of the string, and sets the base used to 16, 16, or 8 if it finds one. The default base is 10 if none of those prefixes are found. Example: </p>
<pre><code>char *endp, *string = &quot;456.203 askdfg&quot;;
int number = ustrtol(string, &amp;endp, 10);</code></pre>
<h2>Return Value</h2>
<p>Returns the string converted as a value of type `long int&#8217;. If nothing was converted, returns zero with `*endp&#8217; pointing to the beginning of `s&#8217;. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrtod/">ustrtod</a></code>(3), <code><a href="/docs/linux/man/3-uatof/">uatof</a></code>(3) </p>
