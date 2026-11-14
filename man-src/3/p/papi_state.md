---
title: "papi_state(3)"
name: "papi_state"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_state/"
description: "PAPI_state –"
---

<p>PAPI_state &#8211; </p>
<p> Return the counting state of an EventSet.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_state(&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>EventSet, int&nbsp;<wbr>*&nbsp;<wbr>status&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> &#8212; an integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code><br />
 <i>status</i> &#8212; an integer containing a boolean combination of one or more of the following nonzero constants as defined in the PAPI header file <code>papi.h</code>: </p>
<dl COMPACT>
<dt>&bull;</p>
<dd>PAPI_STOPPED &#8212; EventSet is stopped</p>
<dt>&bull;</p>
<dd>PAPI_RUNNING &#8212; EventSet is running</p>
<dt>&bull;</p>
<dd>PAPI_PAUSED &#8212; EventSet temporarily disabled by the library</p>
<dt>&bull;</p>
<dd>PAPI_NOT_INIT &#8212; EventSet defined, but not initialized</p>
<dt>&bull;</p>
<dd>PAPI_OVERFLOWING &#8212; EventSet has overflowing enabled</p>
<dt>&bull;</p>
<dd>PAPI_PROFILING &#8212; EventSet has profiling enabled</p>
<dt>&bull;</p>
<dd>PAPI_MULTIPLEXING &#8212; EventSet has multiplexing enabled</p>
<dt>&bull;</p>
<dd>PAPI_ACCUMULATING &#8212; reserved for future use</p>
<dt>&bull;</p>
<dd>PAPI_HWPROFILING &#8212; reserved for future use
</dl>
</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.
</dl>
<p> <code>PAPI_state()</code> returns the counting state of the specified event set. </p>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>* int EventSet = PAPI_NULL;
* int status = 0;
* int ret;
* 
* ret = PAPI_create_eventset(&amp;EventSet);
* if (ret != PAPI_OK) handle_error(ret);
* 
* // Add Total Instructions Executed to our EventSet
* ret = PAPI_add_event(EventSet, PAPI_TOT_INS);
* if (ret != PAPI_OK) handle_error(ret);
* 
* // Start counting
* ret = PAPI_state(EventSet, &amp;status);
* if (ret != PAPI_OK) handle_error(ret);
* printf(&quot;State is now %d,status);
* ret = PAPI_start(EventSet);
* if (ret != PAPI_OK) handle_error(ret);
* ret = PAPI_state(EventSet, &amp;status);
* if (ret != PAPI_OK) handle_error(ret);
* printf(&quot;State is now %d,status);
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_stop</code> <code>PAPI_start</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
