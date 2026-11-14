---
title: "papi_list_threads(3)"
name: "papi_list_threads"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_list_threads/"
description: "PAPI_list_threads –"
---

<p>PAPI_list_threads &#8211; </p>
<p> List the registered thread ids.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>PAPI_list_threads()</code> returns to the caller a list of all thread IDs known to PAPI. </p>
<p> This call assumes an initialized PAPI library. </p>
<p> <code>C Interface</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt;<br />
 int <code>PAPI_list_threads(PAPI_thread_id_t *tids, int * number )</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*tids</i> &#8212; A pointer to a preallocated array. This may be NULL to only return a count of threads. No more than *number codes will be stored in the array.<br />
 <i>*number</i> &#8212; An input and output parameter. Input specifies the number of allocated elements in *tids (if non-NULL) and output specifies the number of threads.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i> The call returned successfully.<br />
 <i>PAPI_EINVAL</i> *number has an improper value</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_thr_specific</code> </p>
<p> <code>PAPI_set_thr_specific</code> </p>
<p> <code>PAPI_register_thread</code> </p>
<p> <code>PAPI_unregister_thread</code> </p>
<p> <code>PAPI_thread_init</code> <code>PAPI_thread_id</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
