---
title: "ustrchr(3)"
name: "ustrchr"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrchr/"
description: "ustrchr – Finds the first occurrence of a character in a string. Allegro game programming library."
---

<p>ustrchr &#8211; Finds the first occurrence of a character in a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrchr(const char *s, int c);</code></pre>
<h2>Description</h2>
<p>Finds the first occurrence of the character `c&#8217; in the string `s&#8217;. Example: </p>
<pre><code>char *p = ustrchr(&quot;one,two,three,four&quot;, ',');</code></pre>
<h2>Return Value</h2>
<p>Returns a pointer to the first occurrence of `c&#8217; in `s&#8217;, or NULL if no match was found. Note that if `c&#8217; is NULL, this will return a pointer to the end of the string. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrrchr/">ustrrchr</a></code>(3), <code><a href="/docs/linux/man/3-ustrstr/">ustrstr</a></code>(3), <code><a href="/docs/linux/man/3-ustrpbrk/">ustrpbrk</a></code>(3), <code><a href="/docs/linux/man/3-ustrtok/">ustrtok</a></code>(3) </p>
