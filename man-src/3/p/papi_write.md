---
title: "papi_write(3)"
name: "papi_write"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_write/"
description: "PAPI_write –"
---

<p>PAPI_write &#8211; </p>
<p> Write counter values into counters.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> an integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code><br />
 <i>*values</i> an array to hold the counter values of the counting events</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_ENOEVST</i> The EventSet specified does not exist.<br />
 <i>PAPI_ECMP</i> <code>PAPI_write()</code> is not implemented for this architecture.<br />
 <i>PAPI_ESYS</i> The EventSet is currently counting events and the component could not change the values of the running counters.</dl>
<p> <code>PAPI_write()</code> writes the counter values provided in the array values into the event set EventSet. The virtual counters managed by the PAPI library will be set to the values provided. If the event set is running, an attempt will be made to write the values to the running counters. This operation is not permitted by all components and may result in a run-time error. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_read</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
