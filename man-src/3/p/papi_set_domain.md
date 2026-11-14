---
title: "papi_set_domain(3)"
name: "papi_set_domain"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_set_domain/"
description: "PAPI_set_domain –"
---

<p>PAPI_set_domain &#8211; </p>
<p> Set the default counting domain for new event sets bound to the cpu component.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Prototype:
 #include &lt;papi.h&gt; @n
 int PAPI_set_domain( int domain );
@param domain one of the following constants as defined in the papi.h header file
@arg PAPI_DOM_USER User context counted
@arg PAPI_DOM_KERNEL Kernel/OS context counted
@arg PAPI_DOM_OTHER Exception/transient mode counted
@arg PAPI_DOM_SUPERVISOR Supervisor/hypervisor context counted
@arg PAPI_DOM_ALL All above contexts counted
@arg PAPI_DOM_MIN The smallest available context
@arg PAPI_DOM_MAX The largest available context </pre>
<p>&nbsp;<wbr>&nbsp;<wbr><br />
&nbsp;<wbr> </p>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
&nbsp;<wbr></dl>
<p> <code>PAPI_set_domain</code> sets the default counting domain for all new event sets created by <code>PAPI_create_eventset</code> in all threads. This call implicitly sets the domain for the cpu component (component 0) and is included to preserve backward compatibility. </p>
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
ret = PAPI_set_domain(PAPI_DOM_KERNEL);
if (ret != PAPI_OK) handle_error(ret);
ret = PAPI_create_eventset(&amp;EventSet);
if (ret != PAPI_OK) handle_error(ret);
 * </pre>
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_cmp_domain</code> <code>PAPI_set_granularity</code> <code>PAPI_set_opt</code> <code>PAPI_get_opt</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
