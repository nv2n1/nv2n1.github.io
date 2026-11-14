---
title: "papi_reset(3)"
name: "papi_reset"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_reset/"
description: "PAPI_reset –"
---

<p>PAPI_reset &#8211; </p>
<p> Reset the hardware event counts in an event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Prototype:
 #include &lt;papi.h&gt; @n
 int PAPI_reset( int EventSet );
@param EventSet
 an integer handle for a PAPI event set as created by PAPI_create_eventset 
@retval PAPI_OK 
@retval PAPI_ESYS 
 A system or C library call failed inside PAPI, see the errno variable.
@retval PAPI_ENOEVST 
 The EventSet specified does not exist. 
PAPI_reset() zeroes the values of the counters contained in EventSet. 
This call assumes an initialized PAPI library and a properly added event set 
@par Example:</pre>
<p>&nbsp;<wbr> </p>
<pre>int EventSet = PAPI_NULL;
int Events[] = {PAPI_TOT_INS, PAPI_FP_OPS};
int ret;
 
// Create an empty EventSet
ret = PAPI_create_eventset(&amp;EventSet);
if (ret != PAPI_OK) handle_error(ret);
// Add two events to our EventSet
ret = PAPI_add_events(EventSet, Events, 2);
if (ret != PAPI_OK) handle_error(ret);
// Start counting
ret = PAPI_start(EventSet);
if (ret != PAPI_OK) handle_error(ret);
// Stop counting, ignore values
ret = PAPI_stop(EventSet, NULL);
if (ret != PAPI_OK) handle_error(ret);
// reset the counters in this EventSet
ret = PAPI_reset(EventSet);
if (ret != PAPI_OK) handle_error(ret);
 * </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_create_eventset</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
