---
title: "papi_get_event_info(3)"
name: "papi_get_event_info"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_event_info/"
description: "PAPI_get_event_info –"
---

<p>PAPI_get_event_info &#8211; </p>
<p> Get the event&#8217;s name and description info.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventCode</i> event code (preset or native)<br />
 <i>info</i> structure with the event information <code>PAPI_event_info_t</code></dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ENOTPRESET</i> The PAPI preset mask was set, but the hardware event specified is not a valid PAPI preset.<br />
 <i>PAPI_ENOEVNT</i> The PAPI preset is not available on the underlying hardware.</dl>
<p> This function fills the event information into a structure. In Fortran, some fields of the structure are returned explicitly. This function works with existing PAPI preset and native event codes. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_event_name_to_code</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
