---
title: "ustrcmp(3)"
name: "ustrcmp"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrcmp/"
description: "ustrcmp – Compares two strings. Allegro game programming library."
---

<p>ustrcmp &#8211; Compares two strings. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ustrcmp(const char *s1, const char *s2);</code></pre>
<h2>Description</h2>
<p>This function compares `s1&#8242; and `s2&#8242;.</p>
<h2>Return Value</h2>
<p>Returns zero if the strings are equal, a positive number if `s1&#8242; comes after `s2&#8242; in the ASCII collating sequence, else a negative number. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrsize/">ustrsize</a></code>(3), <code><a href="/docs/linux/man/3-ustrsizez/">ustrsizez</a></code>(3), <code><a href="/docs/linux/man/3-ustrncmp/">ustrncmp</a></code>(3), <code><a href="/docs/linux/man/3-ustricmp/">ustricmp</a></code>(3), <code><a href="/docs/linux/man/3-ustrnicmp/">ustrnicmp</a></code>(3) </p>
