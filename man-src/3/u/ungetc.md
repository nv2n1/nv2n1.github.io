---
title: "ungetc(3)"
name: "ungetc"
section: "3"
letter: "u"
url: "/docs/linux/man/3-ungetc/"
description: "fgetc, fgets, getc, getchar, ungetc – input of characters and strings"
---

<p>fgetc, fgets, getc, getchar, ungetc &#8211; input of characters and strings</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;stdio.h&gt;

int fgetc(FILE *stream);

char *fgets(char *s, int size, FILE *stream);

int getc(FILE *stream);

int getchar(void);

int ungetc(int c, FILE *stream);</code></pre>
<h2>Description</h2>
<p><code>fgetc</code>() reads the next character from <i>stream</i> and returns it as an <i>unsigned char</i> cast to an <i>int</i>, or <code>EOF</code> on end of file or error. </p>
<p> <code>getc</code>() is equivalent to <code>fgetc</code>() except that it may be implemented as a macro which evaluates <i>stream</i> more than once. </p>
<p> <code>getchar</code>() is equivalent to <code>getc(</code><i>stdin</i><code>)</code><i></i>. </p>
<p> <code>fgets</code>() reads in at most one less than <i>size</i> characters from <i>stream</i> and stores them into the buffer pointed to by <i>s</i>. Reading stops after an <code>EOF</code> or a newline. If a newline is read, it is stored into the buffer. A terminating null byte (&#8216;
