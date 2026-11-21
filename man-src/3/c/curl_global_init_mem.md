---

title: "curl_global_init_mem(3)"
name: "curl_global_init_mem"
section: "3"
letter: "c"
url: "/docs/linux/man/3-curl_global_init_mem/"
description: "curl_global_init_mem – Global libcurl initialisation with memory callbacks"
---

<p> curl_global_init_mem &#8211; Global libcurl initialisation with memory callbacks</p>
<h2>SYNOPSIS</h2>
<p> <code>#include &lt;curl/curl.h&gt;</code> </p>
<pre>
<code>CURLcode curl_global_init_mem(long  flags,</code>
<code> curl_malloc_callback m,</code>
<code> curl_free_callback f,</code>
<code> curl_realloc_callback r,</code>
<code> curl_strdup_callback s,</code>
<code> curl_calloc_callback c );</code>
</pre>
<h2>DESCRIPTION</h2>
<p> This function works exactly as <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> with one addition: it allows the application to set callbacks to replace the otherwise used internal memory functions. </p>
<p> This man page only adds documentation for the callbacks, see the <i><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a>(3)</i> man page for all the rest. When you use this function, all callback arguments must be set to valid function pointers. </p>
<p> The prototypes for the given callbacks should match these:</p>
<dl>
<dt>void *malloc_callback(size_t size);</dt>
<dd> To replace malloc()</dd>
<dt>void free_callback(void *ptr);</dt>
<dd> To replace free()</dd>
<dt>void *realloc_callback(void *ptr, size_t size);</dt>
<dd> To replace realloc()</dd>
<dt>char *strdup_callback(const char *str);</dt>
<dd> To replace strdup()</dd>
<dt>void *calloc_callback(size_t nmemb, size_t size);</dt>
<dd> To replace calloc()</dd></dl>
<h2>CAUTION</h2>
<p> Manipulating these gives considerable powers to the application to severely screw things up for libcurl. Take care!</p>
<h2>SEE ALSO</h2>
<p> <code><a href="/docs/linux/man/3-curl_global_init/">curl_global_init</a></code>(3), <code><a href="/docs/linux/man/3-curl_global_cleanup/">curl_global_cleanup</a></code>(3), </p>
