---
title: "erealloc(3)"
name: "erealloc"
section: "3"
letter: "e"
url: "/docs/linux/man/3-erealloc/"
description: "ecalloc emalloc eread erealloc esetenv estrdup ewrite – exit-on-failure wrapper functions"
---

<h2 class="name">NAME</h2>
<p> <code>ecalloc</code> <code>emalloc</code> <code>eread</code> <code>erealloc</code> <code>esetenv</code> <code>estrdup</code> <code>ewrite</code> &#8211; exit-on-failure wrapper functions </p>
<h2>LIBRARY</h2>
<p> The roken library (libroken, -lroken)</p>
<h2>SYNOPSIS</h2>
<p> Fd #include &lt;roken.h&gt; Ft void * Fn ecalloc size_t number size_t size Ft void * Fn emalloc size_t sz Ft ssize_t Fn eread int fd void *buf size_t nbytes Ft void * Fn erealloc void *ptr size_t sz Ft void Fn esetenv const char *var const char *val int rewrite Ft char * Fn estrdup const char *str Ft ssize_t Fn ewrite int fd const void *buf size_t nbytes</p>
<h2>DESCRIPTION</h2>
<p> These functions do the same as the ones without the &#8220;e&#8221; prefix, but if there is an error they will print a message with <a href="/docs/linux/man/3-errx/">errx</a>(3), and exit. For <code>eread</code> and <code>ewrite</code> this is also true for partial data. </p>
<p> This is useful in applications when there is no need for a more advanced failure mode.</p>
<h2>SEE ALSO</h2>
<p> <a href="/docs/linux/man/2-read/">read</a>(2), <a href="/docs/linux/man/2-write/">write</a>(2), <a href="/docs/linux/man/3-calloc/">calloc</a>(3), <a href="/docs/linux/man/3-errx/">errx</a>(3), <a href="/docs/linux/man/3-malloc/">malloc</a>(3), <a href="/docs/linux/man/3-realloc/">realloc</a>(3), <a href="/docs/linux/man/3-setenv/">setenv</a>(3), <a href="/docs/linux/man/3-strdup/">strdup</a>(3) </p>
<h2>Index</h2>
