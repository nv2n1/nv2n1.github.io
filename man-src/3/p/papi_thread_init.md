---
title: "papi_thread_init(3)"
name: "papi_thread_init"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_thread_init/"
description: "PAPI_thread_init –"
---

<p>PAPI_thread_init &#8211; </p>
<p> Initialize thread support in the PAPI library.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@param *id_fn 
 Pointer to a function that returns current thread ID. 
PAPI_thread_init initializes thread support in the PAPI library. 
Applications that make no use of threads do not need to call this routine. 
This function MUST return a UNIQUE thread ID for every new thread/LWP created. 
The OpenMP call omp_get_thread_num() violates this rule, as the underlying 
LWPs may have been killed off by the run-time system or by a call to omp_set_num_threads() . 
In that case, it may still possible to use omp_get_thread_num() in 
conjunction with PAPI_unregister_thread() when the OpenMP thread has finished. 
However it is much better to use the underlying thread subsystem's call, 
which is pthread_self() on Linux platforms. </pre>
<pre>if ( PAPI_thread_init(pthread_self) != PAPI_OK )
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 * </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_register_thread</code> <code>PAPI_unregister_thread</code> <code>PAPI_get_thr_specific</code> <code>PAPI_set_thr_specific</code> <code>PAPI_thread_id</code> <code>PAPI_list_threads</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
