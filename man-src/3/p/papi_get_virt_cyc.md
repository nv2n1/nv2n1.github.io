---
title: "papi_get_virt_cyc(3)"
name: "papi_get_virt_cyc"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_virt_cyc/"
---

PAPI_get_virt_cyc - 

 get virtual time counter value in clock cycles
<h2>Synopsis</h2><h2>Detailed Description</h2><pre>@retval PAPI_ECNFLCT 
 If there is no master event set. 
 This will happen if the library has not been initialized, or 
 for threaded applications, if there has been no thread id 
 function defined by the PAPI_thread_init function.
@retval PAPI_ENOMEM
 For threaded applications, if there has not yet been any thread 
 specific master event created for the current thread, and if 
 the allocation of such an event set fails, the call will return 
 PAPI_ENOMEM or PAPI_ESYS . 
This function returns the total number of virtual units from some 
arbitrary starting point. 
Virtual units accrue every time the process is running in user-mode on 
behalf of the process. 
Like the real time counters, this count is guaranteed to exist on every platform 
PAPI supports. 
However on some platforms, the resolution can be as bad as 1/Hz as defined 
by the operating system.
@par Examples:</pre>&nbsp;<wbr> 

 <pre> s = PAPI_get_virt_cyc();
 your_slow_code();
 e = PAPI_get_virt_cyc();
 printf(&quot;Process has run for cycles: %lld\n&quot;,e-s);
* </pre>&nbsp;<wbr> 

<h2>Author</h2>Generated automatically by Doxygen for PAPI from the source code.
