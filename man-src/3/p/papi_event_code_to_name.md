---
title: "papi_event_code_to_name(3)"
name: "papi_event_code_to_name"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_event_code_to_name/"
description: "PAPI_event_code_to_name –"
---

<p>PAPI_event_code_to_name &#8211; </p>
<p> Convert a numeric hardware event code to a name.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_event_code_to_name( int EventCode, char * EventName );
PAPI_event_code_to_name is used to translate a 32-bit integer PAPI event 
code into an ASCII PAPI event name. 
Either Preset event codes or Native event codes can be passed to this routine. 
Native event codes and names differ from platform to platform.
@param EventCode 
 The numeric code for the event. 
@param *EventName
 A string containing the event name as listed in PAPI_presets or discussed in PAPI_native.
@retval PAPI_EINVAL 
 One or more of the arguments is invalid.
@retval PAPI_ENOTPRESET 
 The hardware event specified is not a valid PAPI preset.
@retval PAPI_ENOEVNT 
 The hardware event is not available on the underlying hardware. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* int EventCode, EventSet = PAPI_NULL;
* int Event, number;
* char EventCodeStr[PAPI_MAX_STR_LEN];
* // Create the EventSet
* if ( PAPI_create_eventset( &amp;EventSet ) != PAPI_OK )
* handle_error( 1 );
* // Add Total Instructions Executed to our EventSet
* if ( PAPI_add_event( EventSet, PAPI_TOT_INS ) != PAPI_OK )
* handle_error( 1 );
* number = 1;
* if ( PAPI_list_events( EventSet, &amp;Event, &amp;number ) != PAPI_OK )
* <a href="//www.systutorials.com/docs/linux/man/1-handle_error/">handle_error</a>(1);
* // Convert integer code to name string
* if ( PAPI_event_code_to_name( Event, EventCodeStr ) != PAPI_OK )
* handle_error( 1 );
* printf( &quot;Event Name: %s, EventCodeStr );
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_event_name_to_code</code> </p>
<p> <code>PAPI_remove_event</code> </p>
<p> <code>PAPI_get_event_info</code> </p>
<p> <code>PAPI_enum_event</code> </p>
<p> <code>PAPI_add_event</code> </p>
<p> PAPI_presets </p>
<p> PAPI_native</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
