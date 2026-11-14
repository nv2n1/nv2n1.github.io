---
title: "papi_start_counters(3)"
name: "papi_start_counters"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_start_counters/"
description: "PAPI_start_counters –"
---

<p>PAPI_start_counters &#8211; </p>
<p> Start counting hardware events.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_start_counters( int *events, int array_len );</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*events</i> an array of codes for events such as PAPI_INT_INS or a native event code<br />
 <i>array_len</i> the number of items in the *events array</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_EISRUN</i> Counters have already been started, you must call <code>PAPI_stop_counters()</code> before you call this function again.<br />
 <i>PAPI_ESYS</i> A system or C library call failed inside PAPI, see the errno variable.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.<br />
 <i>PAPI_ECNFLCT</i> The underlying counter hardware cannot count this event and other events in the EventSet simultaneously.<br />
 <i>PAPI_ENOEVNT</i> The PAPI preset is not available on the underlying hardware.</dl>
<p> <code>PAPI_start_counters()</code> starts counting the events named in the *events array. This function cannot be called if the counters have already been started. The user must call <code>PAPI_stop_counters()</code> to stop the events explicitly if he/she wants to call this function again. It is the user&#8217;s responsibility to choose events that can be counted simultaneously by reading the vendor&#8217;s documentation. The length of the *events array should be no longer than the value returned by <code>PAPI_num_counters()</code>. </p>
<pre>if( PAPI_start_counters( Events, num_hwcntrs ) != PAPI_OK )
 <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
 * </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_stop_counters()</code> <code>PAPI_add_event()</code> <code>PAPI_create_eventset()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
