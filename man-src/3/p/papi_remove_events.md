---
title: "papi_remove_events(3)"
name: "papi_remove_events"
section: "3"
letter: "p"
url: "/docs/linux/man/3-papi_remove_events/"
description: "PAPI_remove_events –"
---

<p>PAPI_remove_events &#8211; </p>
<p> Remove an array of hardware event codes from a PAPI event set.</p>
<h2>Synopsis</h2>
<h2>Detailed Description</h2>
<p>A hardware event can be either a PAPI Preset or a native hardware event code. For a list of PAPI preset events, see PAPI_presets or run the papi_avail utility in the PAPI distribution. PAPI Presets can be passed to <code>PAPI_query_event</code> to see if they exist on the underlying architecture. For a list of native events available on current platform, run papi_native_avail in the PAPI distribution. It should be noted that <code>PAPI_remove_events</code> can partially succeed, exactly like <code>PAPI_add_events</code>. </p>
<p> <code>C Prototype:</code></p>
<dl COMPACT>
<dd>#include &lt;<code>papi.h</code>&gt; </p>
<p>&nbsp;<wbr>int&nbsp;<wbr><code>PAPI_remove_events(&nbsp;<wbr>int&nbsp;<wbr>&nbsp;<wbr>EventSet, int&nbsp;<wbr>*&nbsp;<wbr>EventCode, int&nbsp;<wbr>&nbsp;<wbr>number&nbsp;<wbr>)</code>;</dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>EventSet</i> an integer handle for a PAPI event set as created by <code>PAPI_create_eventset</code><br />
 <i>*Events</i> an array of defined events<br />
 <i>number</i> an integer indicating the number of events in the array *EventCode</dl>
<p> <code>Return values:</code></p>
<dl COMPACT>
<dd><i>Positive</i> integer The number of consecutive elements that succeeded before the error.<br />
 <i>PAPI_EINVAL</i> One or more of the arguments is invalid.<br />
 <i>PAPI_ENOEVST</i> The EventSet specified does not exist.<br />
 <i>PAPI_EISRUN</i> The EventSet is currently counting events.<br />
 <i>PAPI_ECNFLCT</i> The underlying counter hardware can not count this event and other events in the EventSet simultaneously.<br />
 <i>PAPI_ENOEVNT</i> The PAPI preset is not available on the underlying hardware.</dl>
<p> <code>Example:</code></p>
<dl COMPACT>
<dd>
<pre>int EventSet = PAPI_NULL;
int Events[] = {PAPI_TOT_INS, PAPI_FP_OPS};
int ret;
 
 // Create an empty EventSet
ret = PAPI_create_eventset(&amp;EventSet);
if (ret != PAPI_OK) handle_error(ret);
// Add two events to our EventSet
ret = PAPI_add_events(EventSet, Events, 2);
if (ret != PAPI_OK) handle_error(ret);
// Start counting
ret = PAPI_start(EventSet);
if (ret != PAPI_OK) handle_error(ret);
// Stop counting, ignore values
ret = PAPI_stop(EventSet, NULL);
if (ret != PAPI_OK) handle_error(ret);
// Remove event
ret = PAPI_remove_events(EventSet, Events, 2);
if (ret != PAPI_OK) handle_error(ret);
 * </pre>
</dl>
<pre>@see PAPI_cleanup_eventset PAPI_destroy_eventset PAPI_event_name_to_code 
 PAPI_presets PAPI_add_event PAPI_add_events.fi</pre>
<h2>Author</h2>
<p>Generated automatically by Doxygen for PAPI from the source code.</p>
