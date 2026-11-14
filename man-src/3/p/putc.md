---
title: "putc(3)"
name: "putc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-putc/"
description: "fputc, fputs, putc, putchar, puts – output of characters and strings"
---

<p>fputc, fputs, putc, putchar, puts &#8211; output of characters and strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

int fputc(int c, FILE *stream);

int fputs(const char *s, FILE *stream);

int putc(int c, FILE *stream);

int putchar(int c);

int puts(const char *s);</code></pre>
<h2>Description</h2>
<p><code>fputc</code>() writes the character <i>c</i>, cast to an <i>unsigned char</i>, to <i>stream</i>. </p>
<p> <code>fputs</code>() writes the string <i>s</i> to <i>stream</i>, without its terminating null byte (&#8216;
