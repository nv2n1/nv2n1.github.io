---
title: "papi_unlock(3)"
name: "papi_unlock"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_unlock/"
description: "PAPI_unlock –"
---

<p>PAPI_unlock &#8211; </p>
<p> Unlock one of the mutex variables defined in <code>papi.h</code>.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>lck</i> an integer value specifying one of the two user locks: PAPI_USR1_LOCK or PAPI_USR2_LOCK</dl>
<p> <code>PAPI_unlock()</code> unlocks the mutex acquired by a call to <code>PAPI_lock</code> . </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_thread_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
