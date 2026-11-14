---
title: "papi_is_initialized(3)"
name: "papi_is_initialized"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_is_initialized/"
description: "PAPI_is_initialized –"
---

<p>PAPI_is_initialized &#8211; </p>
<p> check for initialization</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@retval PAPI_NOT_INITED
 Library has not been initialized
@retval PAPI_LOW_LEVEL_INITED
 Low level has called library init
@retval PAPI_HIGH_LEVEL_INITED
 High level has called library init 
@retval PAPI_THREAD_LEVEL_INITED 
 Threads have been inited 
@param version
 upon initialization, PAPI checks the argument against the internal value of PAPI_VER_CURRENT when the library was compiled. 
This guards against portability problems when updating the PAPI shared libraries on your system.
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> int retval;
 retval = PAPI_library_init(PAPI_VER_CURRENT);
 if (retval != PAPI_VER_CURRENT &amp;&amp; retval &gt; 0) {
 fprintf(stderr,&quot;PAPI library version mismatch!
&quot;);
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1); }
 if (retval &lt; 0)
 handle_error(retval);
 retval = PAPI_is_initialized();
 if (retval != PAPI_LOW_LEVEL_INITED)
 handle_error(retval);
* </pre>
<p>&nbsp;<wbr><code>PAPI_is_initialized()</code>&nbsp;<wbr>returns the status of the PAPI library. The PAPI library can be in one of four states, as described under RETURN VALUES.&nbsp;<wbr>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd>PAPI </p>
<p> <code>PAPI_thread_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
