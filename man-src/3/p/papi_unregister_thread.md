---
title: "papi_unregister_thread(3)"
name: "papi_unregister_thread"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_unregister_thread/"
description: "PAPI_unregister_thread –"
---

<p>PAPI_unregister_thread &#8211; </p>
<p> Notify PAPI that a thread has &#8216;disappeared&#8217;.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_ENOMEM</i> Space could not be allocated to store the new thread information.<br />
 <i>PAPI_ESYS</i> A system or C library call failed inside PAPI, see the errno variable.<br />
 <i>PAPI_ECMP</i> Hardware counters for this thread could not be initialized.</dl>
<p> <code>PAPI_unregister_thread</code> should be called when the user wants to shutdown a particular thread and free the associated thread ID. THIS IS IMPORTANT IF YOUR THREAD LIBRARY REUSES THE SAME THREAD ID FOR A NEW KERNEL LWP. OpenMP does this. OpenMP parallel regions, if separated by a call to omp_set_num_threads() will often kill off the underlying kernel LWPs and then start new ones for the next region. However, omp_get_thread_id() does not reflect this, as the thread IDs for the new LWPs will be the same as the old LWPs. PAPI needs to know that the underlying LWP has changed so it can set up the counters for that new thread. This is accomplished by calling this function. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
