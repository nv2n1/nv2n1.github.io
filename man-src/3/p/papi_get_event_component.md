---
title: "papi_get_event_component(3)"
name: "papi_get_event_component"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_event_component/"
description: "PAPI_get_event_component –"
---

<p>PAPI_get_event_component &#8211; </p>
<p> return component an event belongs to</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@retval ENOCMP
 component does not exist
@param EventCode
 EventCode for which we want to know the component index
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> int cidx,eventcode;
 cidx = PAPI_get_event_component(eventcode);
* </pre>
<p>&nbsp;<wbr><code>PAPI_get_event_component()</code>&nbsp;<wbr>returns the component an event belongs to.&nbsp;<wbr>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_event_info</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
