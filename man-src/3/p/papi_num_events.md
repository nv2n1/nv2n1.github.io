---
title: "papi_num_events(3)"
name: "papi_num_events"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_num_events/"
description: "PAPI_num_events –"
---

<p>PAPI_num_events &#8211; </p>
<p> Return the number of events in an event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>PAPI_num_events()</code> returns the number of preset and/or native events contained in an event set. The event set should be created by <code>PAPI_create_eventset</code> . </p>
<p> <code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_num_events(int&nbsp;<wbr>&nbsp;<wbr>EventSet&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> &#8212; an integer handle for a PAPI event set created by <code>PAPI_create_eventset</code>.<br />
 <i>*count</i> &#8212; (Fortran only) On output the variable contains the number of events in the event set</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>On</i> success, this function returns the positive number of events in the event set.<br />
 <i>PAPI_EINVAL</i> The event count is zero; only if code is compiled with debug enabled.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.</dl>
<p> <code>Example</code></p>
<dl COMPACT>
<dd>
<pre>* // Count the events in our EventSet 
* printf(* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_add_event</code> </p>
<p> <code>PAPI_create_eventset</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
