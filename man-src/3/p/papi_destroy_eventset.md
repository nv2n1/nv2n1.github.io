---
title: "papi_destroy_eventset(3)"
name: "papi_destroy_eventset"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_destroy_eventset/"
description: "PAPI_destroy_eventset –"
---

<p>PAPI_destroy_eventset &#8211; </p>
<p> Empty and destroy an EventSet.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_destroy_eventset( int * EventSet );</pre>
<p><code>PAPI_destroy_eventset</code> deallocates the memory associated with an empty PAPI EventSet. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>*EventSet</i> A pointer to the integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code>. The value pointed to by EventSet is then set to PAPI_NULL on success.</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_EINVAL</i> One or more of the arguments is invalid. Attempting to destroy a non-empty event set or passing in a null pointer to be destroyed.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.<br />
 <i>PAPI_EISRUN</i> The EventSet is currently counting events.<br />
 <i>PAPI_EBUG</i> Internal error, send mail to ptools-perfapi [at] ptools.org and complain.</dl>
<p> <code>Examples:</code></p>
<dl COMPACT>
<dd>
<pre>* // Free all memory and data structures, EventSet must be empty.
* if ( PAPI_destroy_eventset( &amp;EventSet ) != PAPI_OK )
* handle_error( 1 );
* </pre>
</dl>
<pre>@see PAPI_profil @n
PAPI_create_eventset @n
PAPI_add_event @n
PAPI_stop.fi</pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
