---
title: "pthread_setname_np(3)"
name: "pthread_setname_np"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pthread_setname_np/"
description: "pthread_setname_np, pthread_getname_np – set/get the name of a thread"
---

<p>pthread_setname_np, pthread_getname_np &#8211; set/get the name of a thread</p>
<h2>Synopsis</h2>
<pre><code>#define _GNU_SOURCE /* See feature_test_macros(7) */
#include &lt;pthread.h&gt;
int pthread_setname_np(pthread_t thread, const char *name);
int pthread_getname_np(pthread_t thread,
                       char *name, size_t len);</code></pre>
<p> Compile and link with <i>-pthread</i>.</p>
<h2>Description</h2>
<p>By default, all the threads created using <code>pthread_create</code>() inherit the program name. The <code>pthread_setname_np</code>() function can be used to set a unique name for a thread, which can be useful for debugging multithreaded applications. The thread name is a meaningful C language string, whose length is restricted to 16 characters, including the terminating null byte (&#8216;
