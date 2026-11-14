---
title: "papi_set_multiplex(3)"
name: "papi_set_multiplex"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_set_multiplex/"
description: "PAPI_set_multiplex –"
---

<p>PAPI_set_multiplex &#8211; </p>
<p> Convert a standard event set to a multiplexed event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p><code>C Interface:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_set_multiplex(&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>EventSet&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> an integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code></dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>PAPI_OK</i><br />
 <i>PAPI_EINVAL</i> &#8212; One or more of the arguments is invalid, or the EventSet is already multiplexed.<br />
 <i>PAPI_ENOCMP</i> &#8212; The EventSet specified is not yet bound to a component.<br />
 <i>PAPI_ENOEVST</i> &#8212; The EventSet specified does not exist.<br />
 <i>PAPI_EISRUN</i> &#8212; The EventSet is currently counting events.<br />
 <i>PAPI_ENOMEM</i> &#8212; Insufficient memory to complete the operation.</dl>
<p> <code>PAPI_set_multiplex</code> converts a standard PAPI event set created by a call to <code>PAPI_create_eventset</code> into an event set capable of handling multiplexed events. This must be done after calling <code>PAPI_multiplex_init</code>, and either <code>PAPI_add_event</code> or <code>PAPI_assign_eventset_component</code>, but prior to calling <code>PAPI_start()</code>. </p>
<p> Events can be added to an event set either before or after converting it into a multiplexed set, but the conversion must be done prior to using it as a multiplexed set. </p>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Multiplexing can&#8217;t be enabled until PAPI knows which component is targeted. Due to the late binding nature of PAPI event sets, this only happens after adding an event to an event set or explicitly binding the component with a call to <code>PAPI_assign_eventset_component</code>.</dl>
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
</dl>
<p> <code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_multiplex_init</code> </p>
<p> <code>PAPI_get_multiplex</code> </p>
<p> <code>PAPI_set_opt</code> </p>
<p> <code>PAPI_create_eventset</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
