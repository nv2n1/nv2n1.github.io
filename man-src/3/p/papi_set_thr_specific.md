---
title: "papi_set_thr_specific(3)"
name: "papi_set_thr_specific"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_set_thr_specific/"
description: "PAPI_set_thr_specific –"
---

<p>PAPI_set_thr_specific &#8211; </p>
<p> Store a pointer to a thread specific data structure.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>@par Prototype:
 #include &lt;papi.h&gt; @n
 int PAPI_set_thr_specific( int tag, void *ptr );
@param tag
 An identifier, the value of which is either PAPI_USR1_TLS or 
 PAPI_USR2_TLS. This identifier indicates which of several data 
 structures associated with this thread is to be accessed.
@param ptr
 A pointer to the memory containing the data structure. 
@retval PAPI_OK
@retval PAPI_EINVAL 
 The @em tag argument is out of range. 
In C, PAPI_set_thr_specific will save @em ptr into an array indexed by @em tag. 
There are 2 user available locations and @em tag can be either 
PAPI_USR1_TLS or PAPI_USR2_TLS. 
The array mentioned above is managed by PAPI and allocated to each 
thread which has called PAPI_thread_init. 
There is no Fortran equivalent function. 
@par Example:</pre>
<p>&nbsp;<wbr> </p>
<pre>int ret;
HighLevelInfo *state = NULL;
ret = PAPI_thread_init(pthread_self);
if (ret != PAPI_OK) handle_error(ret);
 
// Do we have the thread specific data setup yet?
ret = PAPI_get_thr_specific(PAPI_USR1_TLS, (void *) &amp;state);
if (ret != PAPI_OK || state == NULL) {
 state = (HighLevelInfo *) malloc(sizeof(HighLevelInfo));
 if (state == NULL) return (PAPI_ESYS);
 memset(state, 0, sizeof(HighLevelInfo));
 state-&gt;EventSet = PAPI_NULL;
 ret = PAPI_create_eventset(&amp;state-&gt;EventSet);
 if (ret != PAPI_OK) return (PAPI_ESYS);
 ret = PAPI_set_thr_specific(PAPI_USR1_TLS, state);
 if (ret != PAPI_OK) return (ret);
}
 * </pre>
<p>&nbsp;<wbr> </p>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_register_thread</code> <code>PAPI_thread_init</code> <code>PAPI_thread_id</code> <code>PAPI_get_thr_specific</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
