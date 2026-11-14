---
title: "ustrdup(3)"
name: "ustrdup"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ustrdup/"
description: "ustrdup – Duplicates a string. Allegro game programming library."
---

<p>ustrdup &#8211; Duplicates a string. Allegro game programming library.</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;allegro.h&gt;
</code></pre>
<p> <code>char *ustrdup(const char *src)</code></p>
<h2>Description</h2>
<p>This functions copies the null-terminated string `src&#8217; into a newly allocated area of memory, effectively duplicating it. Example: </p>
<pre><code>void manipulate_string(const char *input_string)
{
    char *temp_buffer = ustrdup(input_string);
    /* Now we can modify temp_buffer */
    ...</code></pre>
<h2>Return Value</h2>
<p>Returns the newly allocated string. This memory must be freed by the caller. Returns NULL if it cannot allocate space for the duplicated string. </p>
<h2>See Also</h2>
<p><code><a href="/docs/linux/man/3-_ustrdup/">_ustrdup</a></code>(3), <code><a href="/docs/linux/man/3-uconvert/">uconvert</a></code>(3), <code><a href="/docs/linux/man/3-ustrsize/">ustrsize</a></code>(3), <code><a href="/docs/linux/man/3-ustrsizez/">ustrsizez</a></code>(3), <code><a href="/docs/linux/man/3-exconfig/">exconfig</a></code>(3) </p>
