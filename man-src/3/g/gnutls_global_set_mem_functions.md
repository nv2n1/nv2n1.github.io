---
title: "gnutls_global_set_mem_functions(3)"
name: "gnutls_global_set_mem_functions"
section: "3"
letter: "g"
url: "/docs/linux/man/3-gnutls_global_set_mem_functions/"
description: "gnutls_global_set_mem_functions – API function"
---

<h2>NAME</h2>
<p> gnutls_global_set_mem_functions &#8211; API function</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;gnutls/compat.h&gt;</code> </p>
<p> <code>void gnutls_global_set_mem_functions(gnutls_alloc_function </code><i>alloc_func</i><code>, gnutls_alloc_function </code><i>secure_alloc_func</i><code>, gnutls_is_secure_function </code><i>is_secure_func</i><code>, gnutls_realloc_function </code><i>realloc_func</i><code>, gnutls_free_function </code><i>free_func</i><code>);</code></p>
<h2>ARGUMENTS</h2>
<dl>
<dt>gnutls_alloc_function alloc_func</p>
<dd> it&#8217;s the default memory allocation function. Like <code>malloc()</code>.</p>
<dt>gnutls_alloc_function secure_alloc_func</p>
<dd> This is the memory allocation function that will be used for sensitive data.</p>
<dt>gnutls_is_secure_function is_secure_func</p>
<dd> a function that returns 0 if the memory given is not secure. May be NULL.</p>
<dt>gnutls_realloc_function realloc_func</p>
<dd> A realloc function</p>
<dt>gnutls_free_function free_func</p>
<dd> The function that frees allocated data. Must accept a NULL pointer.</dl>
<h2>DEPRECATED</h2>
<p> since 3.3.0 it is no longer possible to replace the internally used memory allocation functions </p>
<p> This is the function where you set the memory allocation functions gnutls is going to use. By default the libc&#8217;s allocation functions (<code>malloc()</code>, <code>free()</code>), are used by gnutls, to allocate both sensitive and not sensitive data. This function is provided to set the memory allocation functions to something other than the defaults </p>
<p> This function must be called before <code>gnutls_global_init()</code> is called. This function is not thread safe.</p>
<h2>REPORTING BUGS</h2>
<p> Report bugs to &lt;bugs [at] gnutls.org&gt;.<br />
 Home page: <a rel="nofollow" href="http://www.gnutls.org">http://www.gnutls.org</a> </p>
<h2>COPYRIGHT</h2>
<p> Copyright &#169; 2001-2014 Free Software Foundation, Inc..<br />
 Copying and distribution of this file, with or without modification, are permitted in any medium without royalty provided the copyright notice and this notice are preserved.</p>
<h2>SEE ALSO</h2>
<p> The full documentation for <code>gnutls</code> is maintained as a Texinfo manual. If the /usr/share/doc/gnutls/ directory does not contain the HTML form visit <code></p>
<dl>
<dt><a rel="nofollow" href="http://www.gnutls.org/manual/">http://www.gnutls.org/manual/</a></p>
<dd> </code></dl>
<h2>Index</h2>
