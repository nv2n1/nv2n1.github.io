---
title: "ustrstr(3)"
name: "ustrstr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrstr/"
description: "ustrstr – Finds the first occurrence of a string in another one. Allegro game programming library."
---

<p>ustrstr &#8211; Finds the first occurrence of a string in another one. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrstr(const char *s1, const char *s2);</code></pre>
<h2>Description</h2>
<p>This function finds the first occurrence of string `s2&#8242; in string `s1&#8242;. Example: </p>
<pre><code>char *p = ustrstr(&quot;hello world&quot;, &quot;world&quot;);</code></pre>
<h2>Return Value</h2>
<p>Returns a pointer within `s1&#8242;, or NULL if `s2&#8242; wasn&#8217;t found. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrchr/">ustrchr</a></code>(3), <code><a href="/docs/linux/man/3-ustrrchr/">ustrrchr</a></code>(3), <code><a href="/docs/linux/man/3-ustrpbrk/">ustrpbrk</a></code>(3), <code><a href="/docs/linux/man/3-ustrtok/">ustrtok</a></code>(3) </p>
