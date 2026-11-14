---
title: "papi_num_counters(3)"
name: "papi_num_counters"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_num_counters/"
description: "PAPI_num_counters –"
---

<p>PAPI_num_counters &#8211; </p>
<p> Get the number of hardware counters available on the system.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_num_counters( void );</pre>
<p><code>Postcondition:</code></p>
<dl COMPACT>
<dd>Initializes the library to PAPI_HIGH_LEVEL_INITED if necessary.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> <code>papi.h</code> is different from the version used to compile the PAPI library.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.<br />
 <i>PAPI_ESYS</i> A system or C library call failed inside PAPI, see the errno variable.</dl>
<p> <code>Examples:</code></p>
<dl COMPACT>
<dd>
<pre>* int num_hwcntrs;
* // The installation does not support PAPI 
* if ((num_hwcntrs = PAPI_num_counters()) &lt; 0 )
* <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
* // The installation supports PAPI, but has no counters 
* if ((num_hwcntrs = PAPI_num_counters()) == 0 )
* fprintf(stderr,&quot;Info:: This machine does not provide hardware counters.);
* </pre>
</dl>
<p> <code>PAPI_num_counters()</code> returns the optimal length of the values array for the high level functions. This value corresponds to the number of hardware counters supported by the current CPU component. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This function only works for the CPU component. To determine the number of counters on another component, use the low level <code>PAPI_num_cmp_hwctrs()</code>.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
