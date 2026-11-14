---
title: "ne_strdup(3)"
name: "ne_strdup"
section: "3"
letter: "n"
url: "/docs/linux/man/3-ne_strdup/"
description: "ne_malloc, ne_calloc, ne_realloc, ne_strdup, ne_strndup, ne_oom_callback – memory allocation wrappers"
---

<p>ne_malloc, ne_calloc, ne_realloc, ne_strdup, ne_strndup, ne_oom_callback &#8211; memory allocation wrappers</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;ne_alloc.h&gt;

void *ne_malloc(size_t size);

void *ne_calloc(size_t size);

void *ne_realloc(void *size, size_t len);

char *ne_strdup(const char *s);

char *ne_strndup(const char *s, size_t size);

void ne_oom_callback(void (*callback)(void));</code></pre>
<h2>Description</h2>
<dd>The functions <code>ne_malloc</code>, <code>ne_calloc</code>, <code>ne_realloc</code>, <code>ne_strdup</code> and <code>ne_strdnup</code> provide wrappers for the equivalent functions in the standard C library. The wrappers provide the extra guarantee that if the C library equivalent returns NULL when no memory is available, an optional callback will be called, and the library will then call <code>abort</code>(). </p>
<p> <code>ne_oom_callback</code> registers a callback which will be invoked if an out of memory error is detected.</p>
<h2>Notes</h2>
<p>If the operating system uses optimistic memory allocation, the C library memory allocation routines will not return NULL, so it is not possible to gracefully handle memory allocation failures.</p>
<h2>Author</h2>
<p><code>Joe Orton</code> &lt;neon [at] lists.manyfish.co.uk&gt;</p>
<dl>
<dd>Author.</dl>
<h2>Copyright</h2>
