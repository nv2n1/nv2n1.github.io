---
title: "ustricmp(3)"
name: "ustricmp"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustricmp/"
description: "ustricmp – Compares two strings ignoring case. Allegro game programming library."
---

<p>ustricmp &#8211; Compares two strings ignoring case. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ustricmp(const char *s1, const char *s2);</code></pre>
<h2>Description</h2>
<p>This function compares `s1&#8242; and `s2&#8242;, ignoring case. Example: </p>
<pre><code>if (ustricmp(string, user_input) == 0) {
    /* string and user_input are equal (ignoring case) */
}</code></pre>
<h2>Return Value</h2>
<p>Returns zero if the strings are equal, a positive number if `s1&#8242; comes after `s2&#8242; in the ASCII collating sequence, else a negative number. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrsize/">ustrsize</a></code>(3), <code><a href="/docs/linux/man/3-ustrsizez/">ustrsizez</a></code>(3), <code><a href="/docs/linux/man/3-ustrnicmp/">ustrnicmp</a></code>(3), <code><a href="/docs/linux/man/3-ustrcmp/">ustrcmp</a></code>(3), <code><a href="/docs/linux/man/3-ustrncmp/">ustrncmp</a></code>(3), <code><a href="/docs/linux/man/3-exconfig/">exconfig</a></code>(3) </p>
