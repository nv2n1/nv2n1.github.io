---
title: "papi_set_cmp_domain(3)"
name: "papi_set_cmp_domain"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_set_cmp_domain/"
description: "PAPI_set_cmp_domain –"
---

<p>PAPI_set_cmp_domain &#8211; </p>
<p> Set the default counting domain for new event sets bound to the specified component.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Prototype:
 #include &lt;papi.h&gt; @n
 int PAPI_set_cmp_domain( int domain, int cidx );
@param domain one of the following constants as defined in the papi.h header file
@arg PAPI_DOM_USER User context counted
@arg PAPI_DOM_KERNEL Kernel/OS context counted
@arg PAPI_DOM_OTHER Exception/transient mode counted
@arg PAPI_DOM_SUPERVISOR Supervisor/hypervisor context counted
@arg PAPI_DOM_ALL All above contexts counted
@arg PAPI_DOM_MIN The smallest available context
@arg PAPI_DOM_MAX The largest available context 
@arg PAPI_DOM_HWSPEC Something other than CPU like stuff. Individual components can decode
low order bits for more meaning
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
<p> <code>PAPI_set_cmp_domain</code> sets the default counting domain for all new event sets in all threads, and requires an explicit component argument. Event sets that are already in existence are not affected. To change the domain of an existing event set, please see <code>PAPI_set_opt</code>. The reader should note that the domain of an event set affects only the mode in which the counter continues to run. Counts are still aggregated for the current process, and not for any other processes in the system. Thus when requesting PAPI_DOM_KERNEL , the user is asking for events that occur on behalf of the process, inside the kernel. </p>
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
// Set the default domain for the cpu component
ret = PAPI_set_cmp_domain(PAPI_DOM_KERNEL,0);
if (ret != PAPI_OK) handle_error(ret);
ret = PAPI_create_eventset(&amp;EventSet);
if (ret != PAPI_OK) handle_error(ret);
 * </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_domain</code> <code>PAPI_set_granularity</code> <code>PAPI_set_opt</code> <code>PAPI_get_opt</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
