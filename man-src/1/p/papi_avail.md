---
title: "papi_avail(1)"
name: "papi_avail"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_avail/"
---

<h2 class="name">NAME</h2>
 

 papi_avail - papi_avail utility. 

 file avail.c 

<h2>Name</h2>

 

 papi_avail - provides availability and detail information for PAPI preset events.

<h2>Synopsis</h2>

 

 papi_avail [-adht] [-e event]

<h2>Description</h2>

 

 papi_avail is a PAPI utility program that reports information about the current PAPI installation and supported preset events. Using the -e option, it will also display information about specific native events.

<h2>Options</h2>

 

<dl>
<dt>&bull;
<dd> -a Display only the available PAPI preset events.
<dt>&bull;
<dd> -d Display PAPI preset event information in a more detailed format.
<dt>&bull;
<dd> -h Display help information about this utility.
<dt>&bull;
<dd> -t Display the PAPI preset event information in a tabular format. This is the default.
<dt>&bull;
<dd> -e &lt; event &gt; Display detailed event information for the named event. This event can be either a preset or a native event.</dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org. 

<h2>Index</h2>


