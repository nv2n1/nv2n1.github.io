---
title: "papi_xml_event_info(1)"
name: "papi_xml_event_info"
section: "1"
letter: "p"
url: "/docs/linux/man/1-papi_xml_event_info/"
---

<h2 class="name">NAME</h2>
 

 papi_xml_event_info - papi_xml_event_info utility. 

 file event_info.c 

<h2 class="name">NAME</h2>
 

 

 papi_xml_event_info - provides detailed information for PAPI events in XML format 

<h2>Synopsis</h2>

 

<h2>Description</h2>

 

 papi_native_avail is a PAPI utility program that reports information about the events available on the current platform in an XML format. 

 It will attempt to create an EventSet with each event in it, which can be slow.

<h2>Options</h2>

 

<dl>
<dt>&bull;
<dd> -h print help message
<dt>&bull;
<dd> -p print only preset events
<dt>&bull;
<dd> -n print only native events
<dt>&bull;
<dd> -c COMPONENT print only events from component number COMPONENT event1, event2, ... Print only events that can be created in the same event set with the events event1, event2, etc.</dl>
 

<h2>Bugs</h2>

 

 There are no known bugs in this utility. If you find a bug, it should be reported to the PAPI Mailing List at ptools-perfapi [at] ptools.org. 

<h2>Index</h2>


