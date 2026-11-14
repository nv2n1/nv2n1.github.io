---
title: "papi_lock(3)"
name: "papi_lock"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_lock/"
description: "PAPI_lock –"
---

<p>PAPI_lock &#8211; </p>
<p> Lock one of two mutex variables defined in <code>papi.h</code>.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>PAPI_lock()</code> grabs access to one of the two PAPI mutex variables. This function is provided to the user to have a platform independent call to a (hopefully) efficiently implemented mutex. </p>
<p> <code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt;<br />
 void <code>PAPI_lock(int lock)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lock</i> &#8212; an integer value specifying one of the two user locks: PAPI_USR1_LOCK or PAPI_USR2_LOCK</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>There is no return value for this call. Upon return from <code>PAPI_lock</code> the current thread has acquired exclusive access to the specified PAPI mutex.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_unlock</code> </p>
<p> <code>PAPI_thread_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
