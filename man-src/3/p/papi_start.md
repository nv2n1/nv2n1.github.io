---
title: "papi_start(3)"
name: "papi_start"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_start/"
description: "PAPI_start –"
---

<p>PAPI_start &#8211; </p>
<p> Start counting hardware events in an event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_start(&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>EventSet&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> &#8212; an integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code></dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> &#8212; One or more of the arguments is invalid.<br />
 <i>PAPI_ESYS</i> &#8212; A system or C library call failed inside PAPI, see the errno variable.<br />
 <i>PAPI_ENOEVST</i> &#8212; The EventSet specified does not exist.<br />
 <i>PAPI_EISRUN</i> &#8212; The EventSet is currently counting events.<br />
 <i>PAPI_ECNFLCT</i> &#8212; The underlying counter hardware can not count this event and other events in the EventSet simultaneously.<br />
 <i>PAPI_ENOEVNT</i> &#8212; The PAPI preset is not available on the underlying hardware.</dl>
<p> <code>PAPI_start</code> starts counting all of the hardware events contained in the previously defined EventSet. All counters are implicitly set to zero before counting. Assumes an initialized PAPI library and a properly added event set. </p>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>* int EventSet = PAPI_NULL;
* long long values[2];
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
* ret = PAPI_start(EventSet);
* if (ret != PAPI_OK) handle_error(ret);
* poorly_tuned_function();
* ret = PAPI_stop(EventSet, values);
* if (ret != PAPI_OK) handle_error(ret);
* printf(&quot;%lld
&quot;,values[0]);
* </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_create_eventset</code> <code>PAPI_add_event</code> <code>PAPI_stop</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
