---
title: "papi_query_named_event(3)"
name: "papi_query_named_event"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_query_named_event/"
description: "PAPI_query_named_event –"
---

<p>PAPI_query_named_event &#8211; </p>
<p> Query if a named PAPI event exists.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_query_named_event(char&nbsp;<wbr>*EventName)</code>;</dl>
<p> <code>PAPI_query_named_event()</code> asks the PAPI library if the PAPI named event can be counted on this architecture. If the event CAN be counted, the function returns PAPI_OK. If the event CANNOT be counted, the function returns an error code. This function also can be used to check the syntax of native and user events. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventName</i> &#8212; a defined event such as PAPI_TOT_INS.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ENOEVNT</i> The PAPI preset is not available on the underlying hardware.</dl>
<p> <code>Examples</code></p>
<dl COMPACT>
<dd>
<pre>* int retval;
* // Initialize the library
* retval = PAPI_library_init(PAPI_VER_CURRENT);
* if (retval != PAPI_VER_CURRENT) {
* fprintf(stderr,* <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1); 
* }
* if (PAPI_query_named_event(&quot;PAPI_TOT_INS&quot;) != PAPI_OK) {
* fprintf(stderr,* <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
* }
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_query_event</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
