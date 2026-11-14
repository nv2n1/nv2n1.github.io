---
title: "globus_seg_error_type_invalid_module(3)"
name: "globus_seg_error_type_invalid_module"
section: "3"
letter: "g"
url: "/docs/linux/man/3-globus_seg_error_type_invalid_module/"
description: "Scheduler Implementation API –"
---

<p>Scheduler Implementation API &#8211; </p>
<h3>Enumerations</h3>
<p>enum <code>globus_scheduler_event_generator_error_t</code> { <code>GLOBUS_SEG_ERROR_TYPE_NULL</code> = 1024, <code>GLOBUS_SEG_ERROR_TYPE_ALREADY_SET</code>, <code>GLOBUS_SEG_ERROR_TYPE_INVALID_MODULE</code>, <code>GLOBUS_SEG_ERROR_TYPE_INVALID_FORMAT</code>, <code>GLOBUS_SEG_ERROR_TYPE_OUT_OF_MEMORY</code>, <code>GLOBUS_SEG_ERROR_TYPE_LOADING_MODULE</code> } </p>
<h2>Detailed Description</h2>
<p>Scheduler-specific SEG module implementations use this API to issue events to the Job State Monitor. Events occur whenever a job is placed in the scheduler&#8217;s queue (PENDING), begins execution (ACTIVE), terminates successfully (DONE), or ends abnormally (FAILED). </p>
<p> A SEG module should register an event with the Globus event driver (most likely using either the Globus Callback or Globus XIO interfaces) in its activation function and then return. All events should be triggered from callbacks. When the SEG detects that it should terminate, it will deactivate the SEG module it started. The SEG module should wait for any outstanding callbacks to subside and before returning from its deactivation function to ensure that all events will be properly dispatched. After deactivation is complete, the SEG will unload the shared module and terminate.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_scheduler_event_generator_error_t</code></h3>
<p>Error types used by the SEG. </p>
<p> <code>Enumerator</code></p>
<dl COMPACT>
<dt><i>GLOBUS_SEG_ERROR_TYPE_NULL </i></p>
<dd>NULL Parameter</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_ALREADY_SET </i></p>
<dd>Already called a one-time function</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_INVALID_MODULE </i></p>
<dd>Shared module missing descriptor</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_INVALID_FORMAT </i></p>
<dd>Invalid printf format for SEG protocol message</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_OUT_OF_MEMORY </i></p>
<dd>Out of memory</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_LOADING_MODULE </i></p>
<dd>Unable to load scheduler module</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus_scheduler_event_generator from the source code.</p>
