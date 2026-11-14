---
title: "papi_get_component_info(3)"
name: "papi_get_component_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_component_info/"
description: "PAPI_get_component_info –"
---

<p>PAPI_get_component_info &#8211; </p>
<p> get information about a specific software component</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@param cidx
 Component index
This function returns a pointer to a structure containing detailed 
information about a specific software component in the PAPI library. 
This includes versioning information, preset and native event 
information, and more. 
For full details, see @ref PAPI_component_info_t. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> const PAPI_component_info_t *cmpinfo = NULL;
 if (PAPI_library_init(PAPI_VER_CURRENT) != PAPI_VER_CURRENT)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 if ((cmpinfo = PAPI_get_component_info(0)) == NULL)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 printf(&quot;This component supports %d Preset Events and %d Native events.,
 cmpinfo-&gt;num_preset_events, cmpinfo-&gt;num_native_events);
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_executable_info</code> </p>
<p> <code>PAPI_get_hardware_info</code> </p>
<p> <code>PAPI_get_dmem_info</code> </p>
<p> <code>PAPI_get_opt</code> </p>
<p> <code>PAPI_component_info_t</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
