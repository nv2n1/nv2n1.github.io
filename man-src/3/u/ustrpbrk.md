---
title: "ustrpbrk(3)"
name: "ustrpbrk"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrpbrk/"
description: "ustrpbrk – Finds the first character that matches any in a set. Allegro game programming library."
---

<p>ustrpbrk &#8211; Finds the first character that matches any in a set. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

char *ustrpbrk(const char *s, const char *set);</code></pre>
<h2>Description</h2>
<p>This function finds the first character in `s&#8217; that matches any character in `set&#8217;. Example: </p>
<pre><code>char *p = ustrpbrk(&quot;one,two-three.four&quot;, &quot;-. &quot;);</code></pre>
<h2>Return Value</h2>
<p>Returns a pointer to the first match, or NULL if none are found. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrchr/">ustrchr</a></code>(3), <code><a href="/docs/linux/man/3-ustrrchr/">ustrrchr</a></code>(3), <code><a href="/docs/linux/man/3-ustrstr/">ustrstr</a></code>(3), <code><a href="/docs/linux/man/3-ustrtok/">ustrtok</a></code>(3) </p>
