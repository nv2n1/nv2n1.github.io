---
title: "pcre2_general_context_create(3)"
name: "pcre2_general_context_create"
section: "3"
letter: "p"
url: "/docs/linux/man/3-pcre2_general_context_create/"
description: "PCRE2 – Perl-compatible regular expressions (revised API)"
---

<p>PCRE2 &#8211; Perl-compatible regular expressions (revised API)</p>
<h2>Synopsis</h2>
<pre><code>#include &lt;pcre2.h&gt;</code></pre>
<pre><code>pcre2_general_context *pcre2_general_context_create(</code>
<code> void *(*</code><i>private_malloc</i>)(PCRE2_SIZE, void *),
<code> void (*</code><i>private_free</i>)(void *, void *), void *<i>memory_data</i>);</pre>
<h2>Description</h2>
<p>This function creates and initializes a general context. The arguments define custom memory management functions and a data value that is passed to them when they are called. The <code>private_malloc()</code> function is used to get memory for the context. If either of the first two arguments is NULL, the system memory management function is used. The result is NULL if no memory could be obtained. There is a complete description of the PCRE2 native API in the <code>pcre2api</code> page and a description of the POSIX API in the <code>pcre2posix</code> page. </p>
