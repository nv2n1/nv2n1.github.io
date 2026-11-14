---
title: "papi_get_dmem_info(3)"
name: "papi_get_dmem_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_dmem_info/"
description: "PAPI_get_dmem_info –"
---

<p>PAPI_get_dmem_info &#8211; </p>
<p> Get information about the dynamic memory usage of the current program.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Prototype:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_get_dmem_info(&nbsp;<wbr>PAPI_dmem_info_t&nbsp;<wbr>*dest&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>dest</i> structure to be filled in <code>PAPI_dmem_info_t</code></dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_ECMP</i> The funtion is not implemented for the current component.<br />
 <i>PAPI_EINVAL</i> Any value in the structure or array may be undefined as indicated by this error value.<br />
 <i>PAPI_SYS</i> A system error occured.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>This function is only implemented for the Linux operating system. This function takes a pointer to a <code>PAPI_dmem_info_t</code> structure and returns with the structure fields filled in. A value of PAPI_EINVAL in any field indicates an undefined parameter.</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_executable_info</code> <code>PAPI_get_hardware_info</code> <code>PAPI_get_opt</code> <code>PAPI_library_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
