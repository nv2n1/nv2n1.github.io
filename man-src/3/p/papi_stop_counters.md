---
title: "papi_stop_counters(3)"
name: "papi_stop_counters"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_stop_counters/"
description: "PAPI_stop_counters –"
---

<p>PAPI_stop_counters &#8211; </p>
<p> Stop counting hardware events and reset values to zero.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_stop_counters( long long *values, int array_len );</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*values</i> an array where to put the counter values<br />
 <i>array_len</i> the number of items in the *values array</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>After this function is called, the values are reset to zero.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ENOTRUN</i> The EventSet is not started yet.<br />
 <i>PAPI_ENOEVST</i> The EventSet has not been added yet.</dl>
<p> The <code>PAPI_stop_counters()</code> function stops the counters and copies the counts into the *values array. The counters must have been started by a previous call to <code>PAPI_start_counters()</code>. </p>
<pre>int Events[2] = { PAPI_TOT_CYC, PAPI_TOT_INS };
long long values[2];
if ( PAPI_start_counters( Events, 2 ) != PAPI_OK )
 <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
your_slow_code();
if ( PAPI_stop_counters( values, 2 ) != PAPI_OK )
 <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
 * </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_read_counters()</code> <code>PAPI_start_counters()</code> <code>PAPI_set_opt()</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
