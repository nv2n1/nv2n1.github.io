---
title: "papi_create_eventset(3)"
name: "papi_create_eventset"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_create_eventset/"
description: "PAPI_create_eventset –"
---

<p>PAPI_create_eventset &#8211; </p>
<p> Create a new empty PAPI EventSet.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
PAPI_create_eventset( int * EventSet );
PAPI_create_eventset creates a new EventSet pointed to by EventSet, 
which must be initialized to PAPI_NULL before calling this routine. 
The user may then add hardware events to the event set by calling 
PAPI_add_event or similar routines.
@note PAPI-C uses a late binding model to bind EventSets to components. 
When an EventSet is first created it is not bound to a component. 
This will cause some API calls that modify EventSet options to fail. 
An EventSet can be bound to a component explicitly by calling 
PAPI_assign_eventset_component or implicitly by calling PAPI_add_event
or similar routines. 
@param *EventSet
 Address of an integer location to store the new EventSet handle.
@exception PAPI_EINVAL 
 The argument handle has not been initialized to PAPI_NULL or the argument is a NULL pointer.
@exception PAPI_ENOMEM 
 Insufficient memory to complete the operation. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* int EventSet = PAPI_NULL;
* if ( PAPI_create_eventset( &amp;EventSet ) != PAPI_OK )
* handle_error( 1 );
* // Add Total Instructions Executed to our EventSet
* if ( PAPI_add_event( EventSet, PAPI_TOT_INS) != PAPI_OK )
* handle_error( 1 ); 
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_add_event</code> </p>
<p>&nbsp;<wbr><code>PAPI_assign_eventset_component</code>&nbsp;<wbr> </p>
<p>&nbsp;<wbr><code>PAPI_destroy_eventset</code>&nbsp;<wbr> </p>
<p>&nbsp;<wbr><code>PAPI_cleanup_eventset</code>&nbsp;<wbr></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
