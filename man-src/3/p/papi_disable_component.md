---
title: "papi_disable_component(3)"
name: "papi_disable_component"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_disable_component/"
description: "PAPI_disable_component –"
---

<p>PAPI_disable_component &#8211; </p>
<p> disables the specified component</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@retval ENOCMP
 component does not exist
 @retval ENOINIT
 cannot disable as PAPI has already been initialized
@param cidx
 component index of component to be disabled
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> int cidx, result;
 cidx = PAPI_get_component_index(&quot;example&quot;);
 if (cidx&gt;=0) {
 result = PAPI_disable_component(cidx);
 if (result==PAPI_OK)
 printf(&quot;The example component is disabled);
 }
 // ... 
 PAPI_library_init();
* </pre>
<p>&nbsp;<wbr><code>PAPI_disable_component()</code>&nbsp;<wbr>allows the user to disable components before&nbsp;<wbr><code>PAPI_library_init()</code>&nbsp;<wbr>time. This is useful if the user knows they do not wish to use events from that component and want to reduce the PAPI library overhead. </p>
<p> <code>PAPI_disable_component()</code> must be called before <code>PAPI_library_init()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_event_component</code> </p>
<p> <code>PAPI_library_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
