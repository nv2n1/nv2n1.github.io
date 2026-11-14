---
title: "papi_assign_eventset_component(3)"
name: "papi_assign_eventset_component"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_assign_eventset_component/"
description: "PAPI_assign_eventset_component –"
---

<p>PAPI_assign_eventset_component &#8211; </p>
<p> Assign a component index to an existing but empty EventSet.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
PAPI_assign_eventset_component( int EventSet, int cidx );
@param EventSet 
 An integer identifier for an existing EventSet.
@param cidx 
 An integer identifier for a component. 
 By convention, component 0 is always the cpu component. 
@retval PAPI_ENOCMP 
 The argument cidx is not a valid component.
@retval PAPI_ENOEVST 
 The EventSet doesn't exist.
@retval PAPI_ENOMEM 
 Insufficient memory to complete the operation. 
PAPI_assign_eventset_component assigns a specific component index, 
as specified by cidx, to a new EventSet identified by EventSet, as obtained 
from PAPI_create_eventset. EventSets are ordinarily automatically bound 
to components when the first event is added. This routine is useful to 
explicitly bind an EventSet to a component before setting component related 
options. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* int EventSet = PAPI_NULL;
* if ( PAPI_create_eventset( &amp;EventSet ) != PAPI_OK )
* handle_error( 1 );
* // Bind our EventSet to the cpu component
* if ( PAPI_assign_eventset_component( EventSet, 0 ) != PAPI_OK )
* handle_error( 1 );
* // Convert our EventSet to multiplexing
* if ( PAPI_set_multiplex( EventSet ) != PAPI_OK )
* handle_error( 1 );
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_opt</code> </p>
<p>&nbsp;<wbr><code>PAPI_create_eventset</code>&nbsp;<wbr> </p>
<p>&nbsp;<wbr><code>PAPI_add_events</code>&nbsp;<wbr> </p>
<p>&nbsp;<wbr><code>PAPI_set_multiplex</code>&nbsp;<wbr></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
