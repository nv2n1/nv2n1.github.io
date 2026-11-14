---
title: "papi_get_component_index(3)"
name: "papi_get_component_index"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_component_index/"
description: "PAPI_get_component_index –"
---

<p>PAPI_get_component_index &#8211; </p>
<p> returns the component index for the named component</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@retval ENOCMP
 component does not exist
@param name
 name of component to find index for
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> int cidx;
 cidx = PAPI_get_component_index(&quot;cuda&quot;);
 if (cidx==PAPI_OK) {
 printf(&quot;The CUDA component is cidx %d,cidx);
 }
* </pre>
<p>&nbsp;<wbr><code>PAPI_get_component_index()</code>&nbsp;<wbr>returns the component index of the named component. This is useful for finding out if a specified component exists.&nbsp;<wbr>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_event_component</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
