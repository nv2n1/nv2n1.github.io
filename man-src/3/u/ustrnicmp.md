---
title: "ustrnicmp(3)"
name: "ustrnicmp"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrnicmp/"
description: "ustrnicmp – Compares up to n letters of two strings ignoring case. Allegro game programming library."
---

<p>ustrnicmp &#8211; Compares up to n letters of two strings ignoring case. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ustrnicmp(const char *s1, const char *s2, int n);</code></pre>
<h2>Description</h2>
<p>This function compares up to `n&#8217; characters of `s1&#8242; and `s2&#8242;, ignoring case. Example: </p>
<pre><code>if (ustrnicmp(prefix, long_string, ustrlen(prefix)) == 0) {
    /* long_string starts with prefix (ignoring case) */
}</code></pre>
<h2>Return Value</h2>
<p>Returns zero if the strings are equal, a positive number if `s1&#8242; comes after `s2&#8242; in the ASCII collating sequence, else a negative number. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrsize/">ustrsize</a></code>(3), <code><a href="/docs/linux/man/3-ustrsizez/">ustrsizez</a></code>(3), <code><a href="/docs/linux/man/3-ustricmp/">ustricmp</a></code>(3), <code><a href="/docs/linux/man/3-ustrcmp/">ustrcmp</a></code>(3), <code><a href="/docs/linux/man/3-ustrncmp/">ustrncmp</a></code>(3) </p>
