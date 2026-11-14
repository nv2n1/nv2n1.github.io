---
title: "papi_read_ts(3)"
name: "papi_read_ts"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_read_ts/"
description: "PAPI_read_ts –"
---

<p>PAPI_read_ts &#8211; </p>
<p> Read hardware counters with a timestamp.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_read_ts(int EventSet, long long&nbsp;<wbr>*values, long long&nbsp;<wbr>*cycles&nbsp;<wbr>)</code>;</dl>
<p> <code>PAPI_read_ts()</code> copies the counters of the indicated event set into the provided array. It also places a real-time cycle timestamp into the cycles array. </p>
<p> The counters continue counting after the read. </p>
<p> <code>PAPI_read_ts()</code> assumes an initialized PAPI library and a properly added event set. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> &#8212; an integer handle for a PAPI Event Set as created by <code>PAPI_create_eventset()</code><br />
 <i>*values</i> &#8212; an array to hold the counter values of the counting events<br />
 <i>*cycles</i> &#8212; an array to hold the timestamp values</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ESYS</i> A system or C library call failed inside PAPI, see the errno variable.<br />
 <i>PAPI_ENOEVST</i> The event set specified does not exist.</dl>
<p> <code>Examples</code></p>
<dl COMPACT>
<dd>
<pre>* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_read</code> </p>
<p> <code>PAPI_accum</code> </p>
<p> <code>PAPI_start</code> </p>
<p> <code>PAPI_stop</code> </p>
<p> <code>PAPI_reset</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
