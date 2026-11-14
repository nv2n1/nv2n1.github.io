---
title: "papi_thread_id(3)"
name: "papi_thread_id"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_thread_id/"
description: "PAPI_thread_id –"
---

<p>PAPI_thread_id &#8211; </p>
<p> Get the thread identifier of the current thread.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@retval PAPI_EMISC 
 is returned if there are no threads registered.
@retval -1 
 is returned if the thread id function returns an error. 
This function returns a valid thread identifier. 
It calls the function registered with PAPI through a call to 
PAPI_thread_init().</pre>
<pre>unsigned long tid;
if ((tid = PAPI_thread_id()) == (unsigned long int)-1 )
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
printf(&quot;Initial thread id is: %lu, tid );
 * </pre>
<p>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_thread_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
