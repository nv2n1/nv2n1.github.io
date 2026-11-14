---
title: "papi_read_counters(3)"
name: "papi_read_counters"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_read_counters/"
description: "PAPI_read_counters –"
---

<p>PAPI_read_counters &#8211; </p>
<p> Read and reset counters.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_read_counters( long long *values, int array_len );</pre>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*values</i> an array to hold the counter values of the counting events<br />
 <i>arry_len</i> the number of items in the *events array</dl>
<p> <code>Precondition:</code></p>
<dl COMPACT>
<dd>These calls assume an initialized PAPI library and a properly added event set.</dl>
<p> <code>Postcondition:</code></p>
<dl COMPACT>
<dd>The counters are reset and left running after the call.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ESYS</i> A system or C library call failed inside PAPI, see the errno variable.</dl>
<p> <code>PAPI_read_counters()</code> copies the event counters into the array *values. </p>
<pre>do_100events();
if ( PAPI_read_counters( values, num_hwcntrs ) != PAPI_OK )
 <a href="//www.systutorials.com/docs/linux/man/1-handlw_error/">handlw_error</a>(1);
// values[0] now equals 100 
do_100events();
if ( PAPI_accum_counters( values, num_hwcntrs ) != PAPI_OK )
 <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
// values[0] now equals 200
values[0] = -100;
do_100events();
if ( PAPI_accum_counters(values, num_hwcntrs ) != PAPI_OK )
 handle_error();
// values[0] now equals 0
 * </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_opt()</code> <code>PAPI_start_counters()</code></dl>
<p> <code>Fortran Interface:</code></p>
<dl COMPACT>
<dd>#include &#8216;fpapi.h&#8217; </p>
<p>&nbsp;<wbr>PAPIF_read_counters(&nbsp;<wbr>C_LONG_LONG(*)&nbsp;<wbr>values, C_INT array_len, C_INT check&nbsp;<wbr>)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_read_counters</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
