---
title: "papi_list_events(3)"
name: "papi_list_events"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_list_events/"
description: "PAPI_list_events –"
---

<p>PAPI_list_events &#8211; </p>
<p> list the events in an event set</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p>List the events in an event set. </p>
<pre>PAPI_list_events() returns an array of events and a count of the</pre>
<p>&nbsp;<wbr>total number of events in an event set. This call assumes an initialized PAPI library and a successfully created event set. </p>
<p> <code>C Interface</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_list_events(int&nbsp;<wbr>*EventSet, int&nbsp;<wbr>*Events, int&nbsp;<wbr>*number&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> An integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code><br />
 <i>*Events</i> A pointer to a preallocated array of codes for events, such as PAPI_INT_INS. No more than *number codes will be stored into the array.<br />
 <i>*number</i> On input, the size of the Events array, or maximum number of event codes to be returned. A value of 0 can be used to probe an event set. On output, the number of events actually in the event set. This value may be greater than the actually stored number of event codes.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i><br />
 <i>PAPI_ENOEVST</i></dl>
<p> <code>Examples:</code></p>
<dl COMPACT>
<dd>
<pre> if (PAPI_event_name_to_code(&quot;PAPI_TOT_INS&quot;,&amp;EventCode) != PAPI_OK)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 if (PAPI_add_event(EventSet, EventCode) != PAPI_OK)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 Convert a second event name to an event code 
 if (PAPI_event_name_to_code(&quot;PAPI_L1_LDM&quot;,&amp;EventCode) != PAPI_OK)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 if (PAPI_add_event(EventSet, EventCode) != PAPI_OK)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 number = 0;
 if(PAPI_list_events(EventSet, NULL, &amp;number))
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 if(number != 2)
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
 if(PAPI_list_events(EventSet, Events, &amp;number))
 <a href="//www.systutorials.com/docs/linux/man/1-exit/">exit</a>(1);
* </pre>
<p>&nbsp;<wbr></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_event_code_to_name</code> </p>
<p> <code>PAPI_event_name_to_code</code> </p>
<p> <code>PAPI_add_event</code> </p>
<p> <code>PAPI_create_eventset</code></dl>
<p> <code>Fortran Interface:</code></p>
<dl COMPACT>
<dd>#include &#8216;fpapi.h&#8217; </p>
<p>&nbsp;<wbr><code>PAPI_list_events</code>(&nbsp;<wbr>C_INT EventSet, C_INT(*)&nbsp;<wbr>Events, C_INT number, C_INT check&nbsp;<wbr>)</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_list_events</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
