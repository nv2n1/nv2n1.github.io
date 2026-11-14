---
title: "papi_attach(3)"
name: "papi_attach"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_attach/"
description: "PAPI_attach –"
---

<p>PAPI_attach &#8211; </p>
<p> Attach PAPI event set to the specified thread id.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_attach( int EventSet, unsigned long tid );
PAPI_attach is a wrapper function that calls PAPI_set_opt to allow PAPI to 
monitor performance counts on a thread other than the one currently executing. 
This is sometimes referred to as third party monitoring. 
PAPI_attach connects the specified EventSet to the specifed thread;
PAPI_detach breaks that connection and restores the EventSet to the 
original executing thread. 
@param EventSet 
 An integer handle for a PAPI EventSet as created by PAPI_create_eventset.
@param tid 
 A thread id as obtained from, for example, PAPI_list_threads or PAPI_thread_id.
@retval PAPI_ECMP 
 This feature is unsupported on this component.
@retval PAPI_EINVAL 
 One or more of the arguments is invalid.
@retval PAPI_ENOEVST 
 The event set specified does not exist.
@retval PAPI_EISRUN 
 The event set is currently counting events. 
@par Examples:</pre>
<p>&nbsp;<wbr> </p>
<pre>* int EventSet = PAPI_NULL;
* unsigned long pid;
* pid = fork( );
* if ( pid &lt;= 0 )
* exit( 1 );
* if ( PAPI_create_eventset( &amp;EventSet ) != PAPI_OK )
* exit( 1 );
* // Add Total Instructions Executed to our EventSet
* if ( PAPI_add_event( EventSet, PAPI_TOT_INS ) != PAPI_OK )
* exit( 1 );
* // Attach this EventSet to the forked process
* if ( PAPI_attach( EventSet, pid ) != PAPI_OK )
* exit( 1 );
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_set_opt</code> </p>
<p> <code>PAPI_list_threads</code> </p>
<p> <code>PAPI_thread_id</code> </p>
<p> <code>PAPI_thread_init</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
