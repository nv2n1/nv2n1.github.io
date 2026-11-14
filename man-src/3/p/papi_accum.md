---
title: "papi_accum(3)"
name: "papi_accum"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_accum/"
description: "PAPI_accum –"
---

<p>PAPI_accum &#8211; </p>
<p> Accumulate and reset counters in an EventSet.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_accum( int EventSet, long_long * values );
These calls assume an initialized PAPI library and a properly added event set. 
PAPI_accum adds the counters of the indicated event set into the array values. 
The counters are zeroed and continue counting after the operation.
Note the differences between PAPI_read and PAPI_accum, specifically 
that PAPI_accum resets the values array to zero. 
@param EventSet
 an integer handle for a PAPI Event Set 
 as created by PAPI_create_eventset
@param *values 
 an array to hold the counter values of the counting events 
@retval PAPI_EINVAL 
 One or more of the arguments is invalid.
@retval PAPI_ESYS 
 A system or C library call failed inside PAPI, see the errno variable.
@retval PAPI_ENOEVST 
 The event set specified does not exist. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* do_100events( );
* if ( PAPI_read( EventSet, values) != PAPI_OK )
* handle_error( 1 );
* // values[0] now equals 100
* do_100events( );
* if (PAPI_accum( EventSet, values ) != PAPI_OK )
* handle_error( 1 );
* // values[0] now equals 200
* values[0] = -100;
* do_100events( );
* if (PAPI_accum( EventSet, values ) != PAPI_OK )
* handle_error( 1 );
* // values[0] now equals 0
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPIF_accum</code> </p>
<p> <code>PAPI_start</code> </p>
<p> <code>PAPI_set_opt</code> </p>
<p> <code>PAPI_reset</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
