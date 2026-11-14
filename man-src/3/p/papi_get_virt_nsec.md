---
title: "papi_get_virt_nsec(3)"
name: "papi_get_virt_nsec"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_virt_nsec/"
description: "PAPI_get_virt_nsec –"
---

<p>PAPI_get_virt_nsec &#8211; </p>
<p> Get virtual time counter values in nanoseconds.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_ECNFLCT</i> If there is no master event set. This will happen if the library has not been initialized, or for threaded applications, if there has been no thread id function defined by the <code>PAPI_thread_init</code> function.<br />
 <i>PAPI_ENOMEM</i> For threaded applications, if there has not yet been any thread specific master event created for the current thread, and if the allocation of such an event set fails, the call will return PAPI_ENOMEM or PAPI_ESYS .</dl>
<p> This function returns the total number of virtual units from some arbitrary starting point. Virtual units accrue every time the process is running in user-mode on behalf of the process. Like the real time counters, this count is guaranteed to exist on every platform PAPI supports. However on some platforms, the resolution can be as bad as 1/Hz as defined by the operating system. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
