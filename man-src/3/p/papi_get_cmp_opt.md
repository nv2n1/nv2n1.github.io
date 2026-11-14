---
title: "papi_get_cmp_opt(3)"
name: "papi_get_cmp_opt"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_cmp_opt/"
description: "PAPI_get_cmp_opt –"
---

<p>PAPI_get_cmp_opt &#8211; </p>
<p> Get component specific PAPI options.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>option</i> is an input parameter describing the course of action. Possible values are defined in <code>papi.h</code> and briefly described in the table below. The Fortran calls are implementations of specific options.<br />
 <i>ptr</i> is a pointer to a structure that acts as both an input and output parameter.<br />
 <i>cidx</i> An integer identifier for a component. By convention, component 0 is always the cpu component.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.</dl>
<p> <code>PAPI_get_opt()</code> and <code>PAPI_set_opt()</code> query or change the options of the PAPI library or a specific event set created by <code>PAPI_create_eventset</code> . Some options may require that the eventset be bound to a component before they can execute successfully. This can be done either by adding an event or by explicitly calling <code>PAPI_assign_eventset_component</code> . </p>
<p> The C interface for these functions passes a pointer to the <code>PAPI_option_t</code> structure. Not all options require or return information in this structure, and not all options are implemented for both get and set. Some options require a component index to be provided. These options are handled explicitly by the <code>PAPI_get_cmp_opt()</code> call for &#8216;get&#8217; and implicitly through the option structure for &#8216;set&#8217;. The Fortran interface is a series of calls implementing various subsets of the C interface. Not all options in C are available in Fortran. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Some options, such as PAPI_DOMAIN and PAPI_MULTIPLEX, are also available as separate entry points in both C and Fortran.</dl>
<p> The reader is urged to see the example code in the PAPI distribution for usage of <code>PAPI_get_opt</code>. The file <code>papi.h</code> contains definitions for the structures unioned in the <code>PAPI_option_t</code> structure. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_debug</code> <code>PAPI_set_multiplex</code> <code>PAPI_set_domain</code> <code>PAPI_option_t</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
