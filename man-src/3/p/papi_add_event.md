---
title: "papi_add_event(3)"
name: "papi_add_event"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_add_event/"
---

PAPI_add_event - 

 add PAPI preset or native hardware event to an event set
<h2>Synopsis</h2><h2>Detailed Description</h2><pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_add_event( int EventSet, int EventCode );
PAPI_add_event adds one event to a PAPI Event Set. @n
A hardware event can be either a PAPI preset or a native hardware event code.
For a list of PAPI preset events, see PAPI_presets or run the avail test case
in the PAPI distribution. PAPI presets can be passed to PAPI_query_event to see
if they exist on the underlying architecture.
For a list of native events available on current platform, run the papi_native_avail
utility in the PAPI distribution. For the encoding of native events,
see PAPI_event_name_to_code to learn how to generate native code for the
supported native event on the underlying architecture.
@param EventSet
 An integer handle for a PAPI Event Set as created by PAPI_create_eventset.
@param EventCode 
 A defined event such as PAPI_TOT_INS. 
@retval Positive-Integer
 The number of consecutive elements that succeeded before the error. 
@retval PAPI_EINVAL 
 One or more of the arguments is invalid.
@retval PAPI_ENOMEM 
 Insufficient memory to complete the operation.
@retval PAPI_ENOEVST 
 The event set specified does not exist.
@retval PAPI_EISRUN 
 The event set is currently counting events.
@retval PAPI_ECNFLCT 
 The underlying counter hardware can not count this event and other events 
 in the event set simultaneously.
@retval PAPI_ENOEVNT 
 The PAPI preset is not available on the underlying hardware.
@retval PAPI_EBUG 
 Internal error, please send mail to the developers. 
@par Examples:</pre>&nbsp;<wbr> 

 <pre>* int EventSet = PAPI_NULL;
* unsigned int native = 0x0;
* if ( PAPI_create_eventset( &amp;EventSet ) != PAPI_OK )
* handle_error( 1 );
* // Add Total Instructions Executed to our EventSet
* if ( PAPI_add_event( EventSet, PAPI_TOT_INS ) != PAPI_OK )
* handle_error( 1 );
* // Add native event PM_CYC to EventSet
* if ( PAPI_event_name_to_code( &quot;PM_CYC&quot;, &amp;native ) != PAPI_OK )
* handle_error( 1 );
* if ( PAPI_add_event( EventSet, native ) != PAPI_OK )
* handle_error( 1 );
* </pre><pre>@see PAPI_cleanup_eventset @n
PAPI_destroy_eventset @n
PAPI_event_code_to_name @n
PAPI_remove_events @n
PAPI_query_event @n
PAPI_presets @n
PAPI_native @n
PAPI_remove_event.fi</pre><h2>Author</h2>Generated automatically by Doxygen for PAPI from the source code.
