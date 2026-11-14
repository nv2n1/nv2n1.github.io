---
title: "papi_set_opt(3)"
name: "papi_set_opt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_set_opt/"
description: "PAPI_set_opt –"
---

<p>PAPI_set_opt &#8211; </p>
<p> Set PAPI library or event set options.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_set_opt(&nbsp;<wbr>&nbsp;<wbr>int option, PAPI_option_t&nbsp;<wbr>*&nbsp;<wbr>ptr&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>option</i> Defines the option to be set. Possible values are briefly described in the table below.<br />
 <i>ptr</i> Pointer to a structure determined by the selected option. See <code>PAPI_option_t</code> for a description of possible structures.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> The specified option or parameter is invalid.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.<br />
 <i>PAPI_EISRUN</i> The EventSet is currently counting events.<br />
 <i>PAPI_ECMP</i> The option is not implemented for the current component.<br />
 <i>PAPI_ENOINIT</i> PAPI has not been initialized.<br />
 <i>PAPI_EINVAL_DOM</i> Invalid domain has been requested.</dl>
<p> <code>PAPI_set_opt()</code> changes the options of the PAPI library or a specific EventSet created by <code>PAPI_create_eventset</code>. Some options may require that the EventSet be bound to a component before they can execute successfully. This can be done either by adding an event or by explicitly calling <code>PAPI_assign_eventset_component</code>. </p>
<p> Ptr is a pointer to the <code>PAPI_option_t</code> structure, which is actually a union of different structures for different options. Not all options require or return information in these structures. Each requires different values to be set. Some options require a component index to be provided. These options are handled implicitly through the option structures. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Some options, such as PAPI_DOMAIN and PAPI_MULTIPLEX are also available as separate entry points in both C and Fortran.</dl>
<p> The reader is encouraged to peruse the ctests code in the PAPI distribution for examples of usage of <code>PAPI_set_opt</code>. </p>
<p> <code>Possible values for the PAPI_set_opt option parameter</code></p>
<dl COMPACT>
<dd>&nbsp;<wbr> OPTION DEFINITION PAPI_DEFDOM Set default counting domain for newly created event sets. Requires a<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>component index. PAPI_DEFGRN Set default counting granularity. Requires a component index. PAPI_DEBUG Set the PAPI debug state and the debug handler. The debug state is<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specified in ptr-&gt;debug.level. The debug handler is specified in&nbsp;<wbr><br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ptr-&gt;debug.handler. For further information regarding debug states and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>the behavior of the handler, see PAPI_set_debug. PAPI_MULTIPLEX Enable specified EventSet for multiplexing. PAPI_DEF_ITIMER Set the type of itimer used in software multiplexing, overflowing<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>and profiling. PAPI_DEF_MPX_NS Set the sampling time slice in nanoseconds for multiplexing and overflow. PAPI_DEF_ITIMER_NS See PAPI_DEF_MPX_NS. PAPI_ATTACH Attach EventSet specified in ptr-&gt;attach.eventset to thread or process id<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>specified in in ptr-&gt;attach.tid. PAPI_CPU_ATTACH Attach EventSet specified in ptr-&gt;cpu.eventset to cpu specified in in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ptr-&gt;cpu.cpu_num. PAPI_DETACH Detach EventSet specified in ptr-&gt;attach.eventset from any thread<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>or process id. PAPI_DOMAIN Set domain for EventSet specified in ptr-&gt;domain.eventset.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Will error if eventset is not bound to a component. PAPI_GRANUL Set granularity for EventSet specified in ptr-&gt;granularity.eventset.<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>Will error if eventset is not bound to a component. PAPI_INHERIT Enable or disable inheritance for specified EventSet. PAPI_DATA_ADDRESS Set data address range to restrict event counting for EventSet specified<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>in ptr-&gt;addr.eventset. Starting and ending addresses are specified in<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ptr-&gt;addr.start and ptr-&gt;addr.end, respectively. If exact addresses<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>cannot be instantiated, offsets are returned in ptr-&gt;addr.start_off and<br />
&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>&nbsp;<wbr>ptr-&gt;addr.end_off. Currently implemented on Itanium only. PAPI_INSTR_ADDRESS Set instruction address range as described above. Itanium only.<br />
&nbsp;<wbr></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_debug</code> </p>
<p> <code>PAPI_set_multiplex</code> </p>
<p> <code>PAPI_set_domain</code> </p>
<p> <code>PAPI_option_t</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
