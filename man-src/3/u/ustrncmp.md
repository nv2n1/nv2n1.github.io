---
title: "ustrncmp(3)"
name: "ustrncmp"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrncmp/"
description: "ustrncmp – Compares up to n letters of two strings. Allegro game programming library."
---

<p>ustrncmp &#8211; Compares up to n letters of two strings. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;

int ustrncmp(const char *s1, const char *s2, int n);</code></pre>
<h2>Description</h2>
<p>This function compares up to `n&#8217; characters of `s1&#8242; and `s2&#8242;. Example: </p>
<pre><code>if (ustrncmp(prefix, long_string, ustrlen(prefix)) == 0) {
    /* long_string starts with prefix */
}</code></pre>
<h2>Return Value</h2>
<p>Returns zero if the substrings are equal, a positive number if `s1&#8242; comes after `s2&#8242; in the ASCII collating sequence, else a negative number. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrsize/">ustrsize</a></code>(3), <code><a href="/docs/linux/man/3-ustrsizez/">ustrsizez</a></code>(3), <code><a href="/docs/linux/man/3-ustrcmp/">ustrcmp</a></code>(3), <code><a href="/docs/linux/man/3-ustricmp/">ustricmp</a></code>(3), <code><a href="/docs/linux/man/3-ustrnicmp/">ustrnicmp</a></code>(3) </p>
