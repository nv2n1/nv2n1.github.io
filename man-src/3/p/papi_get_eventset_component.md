---
title: "papi_get_eventset_component(3)"
name: "papi_get_eventset_component"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_eventset_component/"
description: "PAPI_get_eventset_component –"
---

<p>PAPI_get_eventset_component &#8211; </p>
<p> return index for component an eventset is assigned to</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@retval PAPI_ENOEVST
 eventset does not exist
@retval PAPI_ENOCMP
 component is invalid or does not exist
@retval positive value
 valid component index
@param EventSet
 EventSet for which we want to know the component index
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre> int cidx,eventcode;
 cidx = PAPI_get_eventset_component(eventset);
* </pre>
<p>&nbsp;<wbr><code>PAPI_get_eventset_component()</code>&nbsp;<wbr>returns the component an event belongs to.&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_get_event_component</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
