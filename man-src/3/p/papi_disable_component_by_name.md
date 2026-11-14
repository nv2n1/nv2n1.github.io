---
title: "papi_disable_component_by_name(3)"
name: "papi_disable_component_by_name"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_disable_component_by_name/"
description: "PAPI_disable_component_by_name –"
---

<p>PAPI_disable_component_by_name &#8211; </p>
<p> disables the named component</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>etval ENOCMP
 component does not exist
etval ENOINIT
 unable to disable the component, the library has already been initialized
<br>
aram component_name
 name of the component to disable.
<br>
ar Example:</pre>
<p>&nbsp;<wbr> </p>
<pre> int result;
 result = PAPI_disable_component_by_name(&quot;example&quot;);
 if (result==PAPI_OK)
 printf(&quot;component //...
 PAPI_library_init(PAPI_VER_CURRENT);
* </pre>
<p>&nbsp;<wbr><code>PAPI_disable_component_by_name()</code>&nbsp;<wbr>allows the user to disable a component before&nbsp;<wbr><code>PAPI_library_init()</code>&nbsp;<wbr>time. This is useful if the user knows they do not with to use events from that component and want to reduce the PAPI library overhead. </p>
<p> <code>PAPI_disable_component_by_name()</code> must be called before <code>PAPI_library_init()</code>. </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_library_init</code> </p>
<p> <code>PAPI_disable_component</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
