---
title: "papi_get_multiplex(3)"
name: "papi_get_multiplex"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_get_multiplex/"
description: "PAPI_get_multiplex –"
---

<p>PAPI_get_multiplex &#8211; </p>
<p> Get the multiplexing status of specified event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_get_multiplex(&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>EventSet&nbsp;<wbr>)</code>;</dl>
<p> <code>Fortran Interface:</code></p>
<dl COMPACT>
<dd>#include fpapi.h </p>
<p>&nbsp;<wbr><code>PAPIF_get_multiplex(&nbsp;<wbr>C_INT&nbsp;<wbr>&nbsp;<wbr>EventSet,&nbsp;<wbr>&nbsp;<wbr>C_INT&nbsp;<wbr>&nbsp;<wbr>check&nbsp;<wbr>)</code></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> an integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code></dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> One or more of the arguments is invalid, or the EventSet is already multiplexed.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.<br />
 <i>PAPI_EISRUN</i> The EventSet is currently counting events.<br />
 <i>PAPI_ENOMEM</i> Insufficient memory to complete the operation.</dl>
<p> <code>PAPI_get_multiplex</code> tests the state of the PAPI_MULTIPLEXING flag in the specified event set, returning <i>TRUE</i> if a PAPI event set is multiplexed, or FALSE if not. </p>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>* int EventSet = PAPI_NULL;
* int ret;
* 
* // Create an empty EventSet
* ret = PAPI_create_eventset(&amp;EventSet);
* if (ret != PAPI_OK) handle_error(ret);
* 
* // Bind it to the CPU component
* ret = PAPI_assign_eventset_component(EventSet, 0);
* if (ret != PAPI_OK) handle_error(ret);
* 
* // Check current multiplex status
* ret = PAPI_get_multiplex(EventSet);
* if (ret == TRUE) printf(&quot;This event set is ready for multiplexing&amp;.&quot;)
* if (ret == FALSE) printf(&quot;This event set is not enabled for multiplexing&amp;.&quot;)
* if (ret &lt; 0) handle_error(ret);
* 
* // Turn on multiplexing
* ret = PAPI_set_multiplex(EventSet);
* if ((ret == PAPI_EINVAL) &amp;&amp; (PAPI_get_multiplex(EventSet) == TRUE))
* printf(&quot;This event set already has multiplexing enabled);
* else if (ret != PAPI_OK) handle_error(ret);
* </pre>
<p>&nbsp;<wbr></dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_multiplex_init</code> </p>
<p> <code>PAPI_set_opt</code> </p>
<p> <code>PAPI_create_eventset</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
