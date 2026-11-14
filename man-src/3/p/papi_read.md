---
title: "papi_read(3)"
name: "papi_read"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_read/"
description: "PAPI_read –"
---

<p>PAPI_read &#8211; </p>
<p> Read hardware counters from an event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_read(int&nbsp;<wbr>&nbsp;<wbr>EventSet, long_long&nbsp;<wbr>*&nbsp;<wbr>values&nbsp;<wbr>)</code>;</dl>
<p> <code>PAPI_read()</code> copies the counters of the indicated event set into the provided array. </p>
<p> The counters continue counting after the read. </p>
<p> Note the differences between <code>PAPI_read()</code> and <code>PAPI_accum()</code>, specifically that <code>PAPI_accum()</code> resets the values array to zero. </p>
<p> <code>PAPI_read()</code> assumes an initialized PAPI library and a properly added event set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> &#8212; an integer handle for a PAPI Event Set as created by <code>PAPI_create_eventset()</code><br />
 <i>*values</i> &#8212; an array to hold the counter values of the counting events</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ESYS</i> A system or C library call failed inside PAPI, see the errno variable.<br />
 <i>PAPI_ENOEVST</i> The event set specified does not exist.</dl>
<p> <code>Examples</code></p>
<dl COMPACT>
<dd>
<pre>* do_100events();
* if (PAPI_read(EventSet, values) != PAPI_OK)
* <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
* // values[0] now equals 100
* do_100events();
* if (PAPI_accum(EventSet, values) != PAPI_OK)
* <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
* // values[0] now equals 200
* values[0] = -100;
* do_100events();
* if (PAPI_accum(EventSet, values) != PAPI_OK)
* <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
* // values[0] now equals 0 
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_accum</code> </p>
<p> <code>PAPI_start</code> </p>
<p> <code>PAPI_stop</code> </p>
<p> <code>PAPI_reset</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
