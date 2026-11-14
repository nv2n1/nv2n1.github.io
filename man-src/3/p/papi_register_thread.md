---
title: "papi_register_thread(3)"
name: "papi_register_thread"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_register_thread/"
description: "PAPI_register_thread –"
---

<p>PAPI_register_thread &#8211; </p>
<p> Notify PAPI that a thread has &#8216;appeared&#8217;.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt;<br />
 int <code>PAPI_register_thread</code> (void);</dl>
<p> <code>PAPI_register_thread()</code> should be called when the user wants to force PAPI to initialize a thread that PAPI has not seen before. </p>
<p> Usually this is not necessary as PAPI implicitly detects the thread when an eventset is created or other thread local PAPI functions are called. However, it can be useful for debugging and performance enhancements in the run-time systems of performance tools. </p>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_ENOMEM</i> Space could not be allocated to store the new thread information.<br />
 <i>PAPI_ESYS</i> A system or C library call failed inside PAPI, see the errno variable.<br />
 <i>PAPI_ECMP</i> Hardware counters for this thread could not be initialized.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_unregister_thread</code> </p>
<p> <code>PAPI_thread_id</code> </p>
<p> <code>PAPI_thread_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
