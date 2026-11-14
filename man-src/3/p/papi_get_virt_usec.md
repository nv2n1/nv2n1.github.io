---
title: "papi_get_virt_usec(3)"
name: "papi_get_virt_usec"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_virt_usec/"
description: "PAPI_get_virt_usec –"
---

<p>PAPI_get_virt_usec &#8211; </p>
<p> get virtual time counter values in microseconds</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@retval PAPI_ECNFLCT 
 If there is no master event set. 
 This will happen if the library has not been initialized, or for threaded 
 applications, if there has been no thread id function defined by the 
 PAPI_thread_init function.
@retval PAPI_ENOMEM
 For threaded applications, if there has not yet been any thread 
 specific master event created for the current thread, and if the 
 allocation of such an event set fails, the call will return PAPI_ENOMEM or PAPI_ESYS . 
This function returns the total number of virtual units from some 
arbitrary starting point. 
Virtual units accrue every time the process is running in user-mode on 
behalf of the process. 
Like the real time counters, this count is guaranteed to exist on every 
platform PAPI supports. However on some platforms, the resolution can be 
as bad as 1/Hz as defined by the operating system.
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> s = PAPI_get_virt_cyc();
 your_slow_code();
 e = PAPI_get_virt_cyc();
 printf(&quot;Process has run for cycles: %lld
&quot;,e-s);
* </pre>
<p>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>PAPIF </p>
<p> PAPI </p>
<p> PAPI </p>
<p> <code>PAPI_get_real_cyc</code> </p>
<p> <code>PAPI_get_virt_cyc</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
