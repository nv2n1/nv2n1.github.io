---
title: "papi_get_opt(3)"
name: "papi_get_opt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_opt/"
description: "PAPI_get_opt –"
---

<p>PAPI_get_opt &#8211; </p>
<p> Get PAPI library or event set options.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_get_opt(&nbsp;<wbr>&nbsp;<wbr>int option, PAPI_option_t&nbsp;<wbr>*&nbsp;<wbr>ptr&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>option</i> Defines the option to get. Possible values are briefly described in the table below.<br />
 <i>ptr</i> Pointer to a structure determined by the selected option. See <code>PAPI_option_t</code> for a description of possible structures.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> The specified option or parameter is invalid.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.<br />
 <i>PAPI_ECMP</i> The option is not implemented for the current component.<br />
 <i>PAPI_ENOINIT</i> PAPI has not been initialized.</dl>
<p> <code>PAPI_get_opt()</code> queries the options of the PAPI library or a specific event set created by <code>PAPI_create_eventset</code>. Some options may require that the eventset be bound to a component before they can execute successfully. This can be done either by adding an event or by explicitly calling <code>PAPI_assign_eventset_component</code>. </p>
<p> Ptr is a pointer to the <code>PAPI_option_t</code> structure, which is actually a union of different structures for different options. Not all options require or return information in these structures. Each returns different values in the structure. Some options require a component index to be provided. These options are handled explicitly by the <code>PAPI_get_cmp_opt()</code> call. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Some options, such as PAPI_DOMAIN and PAPI_MULTIPLEX are also available as separate entry points in both C and Fortran.</dl>
<p> The reader is encouraged to peruse the ctests code in the PAPI distribution for examples of usage of <code>PAPI_set_opt</code>. </p>
<p> <code>Possible values for the PAPI_get_opt option parameter</code></p>
<dl COMPACT>
<dd>&nbsp;<wbr> OPTION DEFINITION PAPI_DEFDOM Get default counting domain for newly created event sets. Requires a component index. PAPI_DEFGRN Get default counting granularity. Requires a component index. PAPI_DEBUG Get the PAPI debug state and the debug handler. The debug state is specified in ptr-&gt;debug.level. The debug handler is specified in ptr-&gt;debug.handler.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>For further information regarding debug states and the behavior of the handler, see PAPI_set_debug. PAPI_MULTIPLEX Get current multiplexing state for specified EventSet. PAPI_DEF_ITIMER Get the type of itimer used in software multiplexing, overflowing and profiling. PAPI_DEF_MPX_NS Get the sampling time slice in nanoseconds for multiplexing and overflow. PAPI_DEF_ITIMER_NS See PAPI_DEF_MPX_NS. PAPI_ATTACH Get thread or process id to which event set is attached. Returns TRUE if currently attached. PAPI_CPU_ATTACH Get ptr-&gt;cpu.cpu_num and Attach state for EventSet specified in ptr-&gt;cpu.eventset. PAPI_DETACH Get thread or process id to which event set is attached. Returns TRUE if currently attached. PAPI_DOMAIN Get domain for EventSet specified in ptr-&gt;domain.eventset. Will error if eventset is not bound to a component. PAPI_GRANUL Get granularity for EventSet specified in ptr-&gt;granularity.eventset. Will error if eventset is not bound to a component. PAPI_INHERIT Get current inheritance state for specified EventSet. PAPI_PRELOAD Get LD_PRELOAD environment equivalent. PAPI_CLOCKRATE Get clockrate in MHz. PAPI_MAX_CPUS Get number of CPUs. PAPI_EXEINFO Get Executable addresses for text/data/bss. PAPI_HWINFO Get information about the hardware. PAPI_LIB_VERSION Get the full PAPI version of the library. PAPI_MAX_HWCTRS Get number of counters. Requires a component index. PAPI_MAX_MPX_CTRS Get maximum number of multiplexing counters. Requires a component index. PAPI_SHLIBINFO Get shared library information used by the program. PAPI_COMPONENTINFO Get the PAPI features the specified component supports. Requires a component index.<br />
&nbsp;<wbr></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_multiplex</code> </p>
<p> <code>PAPI_get_cmp_opt</code> </p>
<p> <code>PAPI_set_opt</code> </p>
<p> <code>PAPI_option_t</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
