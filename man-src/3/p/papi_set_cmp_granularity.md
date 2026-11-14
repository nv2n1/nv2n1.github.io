---
title: "papi_set_cmp_granularity(3)"
name: "papi_set_cmp_granularity"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_set_cmp_granularity/"
description: "PAPI_set_cmp_granularity –"
---

<p>PAPI_set_cmp_granularity &#8211; </p>
<p> Set the default counting granularity for eventsets bound to the specified component.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Prototype:
 #include &lt;papi.h&gt; @n
 int PAPI_set_cmp_granularity( int granularity, int cidx );
@param granularity one of the following constants as defined in the papi.h header file
@arg PAPI_GRN_THR Count each individual thread
@arg PAPI_GRN_PROC Count each individual process
@arg PAPI_GRN_PROCG Count each individual process group
@arg PAPI_GRN_SYS Count the current CPU
@arg PAPI_GRN_SYS_CPU Count all CPUs individually
@arg PAPI_GRN_MIN The finest available granularity
@arg PAPI_GRN_MAX The coarsest available granularity
@param cidx
 An integer identifier for a component. 
 By convention, component 0 is always the cpu component. </pre>
<p>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr> </p>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ENOCMP</i> The argument cidx is not a valid component.<br />
&nbsp;<wbr></dl>
<p> <code>PAPI_set_cmp_granularity</code> sets the default counting granularity for all new event sets, and requires an explicit component argument. Event sets that are already in existence are not affected. </p>
<p> To change the granularity of an existing event set, please see <code>PAPI_set_opt</code>. The reader should note that the granularity of an event set affects only the mode in which the counter continues to run. </p>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>int ret;
// Initialize the library
ret = PAPI_library_init(PAPI_VER_CURRENT);
if (ret &gt; 0 &amp;&amp; ret != PAPI_VER_CURRENT) {
 fprintf(stderr,&quot;PAPI library version mismatch!);
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1); 
}
if (ret &lt; 0) handle_error(ret);
// Set the default granularity for the cpu component
ret = PAPI_set_cmp_granularity(PAPI_GRN_PROC, 0);
if (ret != PAPI_OK) handle_error(ret);
ret = PAPI_create_eventset(&amp;EventSet);
if (ret != PAPI_OK) handle_error(ret);
 * </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_granularity</code> <code>PAPI_set_domain</code> <code>PAPI_set_opt</code> <code>PAPI_get_opt</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
