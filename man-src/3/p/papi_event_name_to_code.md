---
title: "papi_event_name_to_code(3)"
name: "papi_event_name_to_code"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_event_name_to_code/"
description: "PAPI_event_name_to_code –"
---

<p>PAPI_event_name_to_code &#8211; </p>
<p> Convert a name to a numeric hardware event code.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_event_name_to_code( char * EventName, int * EventCode );
PAPI_event_name_to_code is used to translate an ASCII PAPI event name 
into an integer PAPI event code. 
@param *EventCode 
 The numeric code for the event. 
@param *EventName
 A string containing the event name as listed in PAPI_presets or discussed in PAPI_native.
@retval PAPI_EINVAL 
 One or more of the arguments is invalid.
@retval PAPI_ENOTPRESET 
 The hardware event specified is not a valid PAPI preset.
@retval PAPI_ENOINIT 
 The PAPI library has not been initialized.
@retval PAPI_ENOEVNT 
 The hardware event is not available on the underlying hardware. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* int EventCode, EventSet = PAPI_NULL;
* // Convert to integer
* if ( PAPI_event_name_to_code( &quot;PAPI_TOT_INS&quot;, &amp;EventCode ) != PAPI_OK )
* handle_error( 1 );
* // Create the EventSet
* if ( PAPI_create_eventset( &amp;EventSet ) != PAPI_OK )
* handle_error( 1 );
* // Add Total Instructions Executed to our EventSet
* if ( PAPI_add_event( EventSet, EventCode ) != PAPI_OK )
* handle_error( 1 );
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_event_code_to_name</code> </p>
<p> <code>PAPI_remove_event</code> </p>
<p> <code>PAPI_get_event_info</code> </p>
<p> <code>PAPI_enum_event</code> </p>
<p> <code>PAPI_add_event</code> </p>
<p> <code>PAPI_add_named_event</code> </p>
<p> PAPI_presets </p>
<p> PAPI_native</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
