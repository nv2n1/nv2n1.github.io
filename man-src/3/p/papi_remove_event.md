---
title: "papi_remove_event(3)"
name: "papi_remove_event"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_remove_event/"
description: "PAPI_remove_event –"
---

<p>PAPI_remove_event &#8211; </p>
<p> removes a hardware event from a PAPI event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<pre>A hardware event can be either a PAPI Preset or a native hardware 
event code. For a list of PAPI preset events, see PAPI_presets or 
run the papi_avail utility in the PAPI distribution. PAPI Presets 
can be passed to PAPI_query_event to see if they exist on the 
underlying architecture. For a list of native events available on 
the current platform, run papi_native_avail in the PAPI distribution. 
@par C Interface:
#include &lt;papi.h&gt; @n
int PAPI_remove_event( int EventSet, int EventCode );
@param[in] EventSet
 -- an integer handle for a PAPI event set as created 
 by PAPI_create_eventset
@param[in] EventCode
 -- a defined event such as PAPI_TOT_INS or a native event. 
@retval PAPI_OK 
 Everything worked.
@retval PAPI_EINVAL 
 One or more of the arguments is invalid.
@retval PAPI_ENOEVST 
 The EventSet specified does not exist.
@retval PAPI_EISRUN 
 The EventSet is currently counting events.
@retval PAPI_ECNFLCT 
 The underlying counter hardware can not count this 
 event and other events in the EventSet simultaneously.
@retval PAPI_ENOEVNT 
 The PAPI preset is not available on the underlying hardware. 
@par Example:</pre>
<p>&nbsp;<wbr> </p>
<pre>* int EventSet = PAPI_NULL;
* int ret;
*
* // Create an empty EventSet
* ret = PAPI_create_eventset(&amp;EventSet);
* if (ret != PAPI_OK) handle_error(ret);
*
* // Add Total Instructions Executed to our EventSet
* ret = PAPI_add_event(EventSet, PAPI_TOT_INS);
* if (ret != PAPI_OK) handle_error(ret);
*
* // Start counting
* ret = PAPI_start(EventSet);
* if (ret != PAPI_OK) handle_error(ret);
*
* // Stop counting, ignore values
* ret = PAPI_stop(EventSet, NULL);
* if (ret != PAPI_OK) handle_error(ret);
*
* // Remove event
* ret = PAPI_remove_event(EventSet, PAPI_TOT_INS);
* if (ret != PAPI_OK) handle_error(ret);
* </pre>
<p><code>See Also:</code></p>
<dl COMPACT>
<dd><code>PAPI_cleanup_eventset</code> </p>
<p> <code>PAPI_destroy_eventset</code> </p>
<p> <code>PAPI_event_name_to_code</code> </p>
<p> PAPI_presets </p>
<p> <code>PAPI_add_event</code> </p>
<p> <code>PAPI_add_events</code></dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
