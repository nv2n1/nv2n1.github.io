---
title: "papi_library_init(3)"
name: "papi_library_init"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_library_init/"
description: "PAPI_library_init –"
---

<p>PAPI_library_init &#8211; </p>
<p> initialize the PAPI library.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@param version 
 upon initialization, PAPI checks the argument against the internal 
 value of PAPI_VER_CURRENT when the library was compiled. 
 This guards against portability problems when updating the PAPI shared 
 libraries on your system. 
@retval PAPI_EINVAL 
 papi.h is different from the version used to compile the PAPI library.
@retval PAPI_ENOMEM 
 Insufficient memory to complete the operation.
@retval PAPI_ECMP 
 This component does not support the underlying hardware.
@retval PAPI_ESYS 
 A system or C library call failed inside PAPI, see the errno variable. 
PAPI_library_init() initializes the PAPI library. 
PAPI_is_initialized() check for initialization.
It must be called before any low level PAPI functions can be used. 
If your application is making use of threads PAPI_thread_init must also be 
called prior to making any calls to the library other than PAPI_library_init() . 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* int retval;
* retval = PAPI_library_init(PAPI_VER_CURRENT);
* if (retval != PAPI_VER_CURRENT &amp;&amp; retval &gt; 0) {
* fprintf(stderr,&quot;PAPI library version mismatch!
&quot;);
* <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1); }
* if (retval &lt; 0)
* handle_error(retval);
* retval = PAPI_is_initialized();
* if (retval != PAPI_LOW_LEVEL_INITED)
* handle_error(retval) 
* </pre>
<p>&nbsp;<wbr>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_thread_init</code> PAPI</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
