---
title: "seg_api(3)"
name: "seg_api"
section: "3"
letter: "s"
url: "/docs/linux/man/3-seg_api/"
description: "Scheduler Implementation API – Scheduler-specific SEG module implementations use this API to issue events to the Job State Monitor."
---

<p>Scheduler Implementation API &#8211; Scheduler-specific SEG module implementations use this API to issue events to the Job State Monitor.</p>
<h3>Enumerations</h3>
<pre><code>enum globus_scheduler_event_generator_error_t { GLOBUS_SEG_ERROR_TYPE_NULL =  1024, GLOBUS_SEG_ERROR_TYPE_ALREADY_SET, GLOBUS_SEG_ERROR_TYPE_INVALID_MODULE, GLOBUS_SEG_ERROR_TYPE_INVALID_FORMAT, GLOBUS_SEG_ERROR_TYPE_OUT_OF_MEMORY, GLOBUS_SEG_ERROR_TYPE_LOADING_MODULE }



Functions</code></pre>
<p> globus_result_t <code>globus_scheduler_event</code> (const char *format,&#8230;) </p>
<p> globus_result_t <code>globus_scheduler_event_pending</code> (time_t timestamp, const char *jobid) </p>
<p> globus_result_t <code>globus_scheduler_event_active</code> (time_t timestamp, const char *jobid) </p>
<p> globus_result_t <code>globus_scheduler_event_failed</code> (time_t timestamp, const char *jobid, int failure_code) </p>
<p> globus_result_t <code>globus_scheduler_event_done</code> (time_t timestamp, const char *jobid, int exit_code) </p>
<p> globus_result_t <code>globus_scheduler_event_generator_get_timestamp</code> (time_t *timestamp)</p>
<h2>Detailed Description</h2>
<p>Scheduler-specific SEG module implementations use this API to issue events to the Job State Monitor. </p>
<p> Events occur whenever a job is placed in the scheduler&#8217;s queue (PENDING), begins execution (ACTIVE), terminates successfully (DONE), or ends abnormally (FAILED). </p>
<p> A SEG module should register an event with the Globus event driver (most likely using either the Globus Callback or Globus XIO interfaces) in its activation function and then return. All events should be triggered from callbacks. When the SEG detects that it should terminate, it will deactivate the SEG module it started. The SEG module should wait for any outstanding callbacks to subside and before returning from its deactivation function to ensure that all events will be properly dispatched. After deactivation is complete, the SEG will unload the shared module and terminate.</p>
<h2>Enumeration Type Documentation</h2>
<h3>enum <code>globus_scheduler_event_generator_error_t</code></h3>
<p>Error types used by the SEG. </p>
<p> <code>Enumerator: </code></p>
<dl>
<dt><i>GLOBUS_SEG_ERROR_TYPE_NULL </i></p>
<dd>NULL Parameter.</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_ALREADY_SET </i></p>
<dd>Already called a one-time function.</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_INVALID_MODULE </i></p>
<dd>Shared module missing descriptor.</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_INVALID_FORMAT </i></p>
<dd>Invalid printf format for SEG protocol message.</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_OUT_OF_MEMORY </i></p>
<dd>Out of memory.</p>
<dt><i>GLOBUS_SEG_ERROR_TYPE_LOADING_MODULE </i></p>
<dd>Unable to load scheduler module.</dl>
<h2>Function Documentation</h2>
<h3>globus_result_t globus_scheduler_event (const char * format, &#8230;)</h3>
<p>Send an arbitrary SEG notification. <code>Parameters:</code></p>
<dl>
<dd><i>format</i> Printf-style format of the SEG notification message<br />
 <i>&#8230;</i> Varargs which will be interpreted as per format.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>GLOBUS_SUCCESS</i> Scheduler message sent or queued.<br />
 <i>GLOBUS_SEG_ERROR_NULL</i> Null format.<br />
 <i>GLOBUS_SEG_ERROR_INVALID_FORMAT</i> Unable to determine length of formatted string.</dl>
<h3>globus_result_t globus_scheduler_event_pending (time_t timestamp, const char * jobid)</h3>
<p>Send a job pending event to the JobSchedulerMonitor implementation. <code>Parameters:</code></p>
<dl>
<dd><i>timestamp</i> Timestamp to use for the event. If set to 0, the time which this function was called is used.<br />
 <i>jobid</i> String indicating the scheduler-specific name of the job.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>GLOBUS_SUCCESS</i> Scheduler message sent or queued.<br />
 <i>GLOBUS_SEG_ERROR_NULL</i> Null jobid.<br />
 <i>GLOBUS_SEG_ERROR_INVALID_FORMAT</i> Unable to determine length of formatted string.</dl>
<h3>globus_result_t globus_scheduler_event_active (time_t timestamp, const char * jobid)</h3>
<p>Send a job active event to the JobSchedulerMonitor implementation. <code>Parameters:</code></p>
<dl>
<dd><i>timestamp</i> Timestamp to use for the event. If set to 0, the time which this function was called is used.<br />
 <i>jobid</i> String indicating the scheduler-specific name of the job.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>GLOBUS_SUCCESS</i> Scheduler message sent or queued.<br />
 <i>GLOBUS_SEG_ERROR_NULL</i> Null jobid.<br />
 <i>GLOBUS_SEG_ERROR_INVALID_FORMAT</i> Unable to determine length of formatted string.</dl>
<h3>globus_result_t globus_scheduler_event_failed (time_t timestamp, const char * jobid, int failure_code)</h3>
<p>Send a job failed event to the JobSchedulerMonitor implementation. <code>Parameters:</code></p>
<dl>
<dd><i>timestamp</i> Timestamp to use for the event. If set to 0, the time which this function was called is used.<br />
 <i>jobid</i> String indicating the scheduler-specific name of the job.<br />
 <i>failure_code</i> Failure code of the process if known.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>GLOBUS_SUCCESS</i> Scheduler message sent or queued.<br />
 <i>GLOBUS_SEG_ERROR_NULL</i> Null jobid.<br />
 <i>GLOBUS_SEG_ERROR_INVALID_FORMAT</i> Unable to determine length of formatted string.</dl>
<h3>globus_result_t globus_scheduler_event_done (time_t timestamp, const char * jobid, int exit_code)</h3>
<p>Send a job done event to the JobSchedulerMonitor implementation. <code>Parameters:</code></p>
<dl>
<dd><i>timestamp</i> Timestamp to use for the event. If set to 0, the time which this function was called is used.<br />
 <i>jobid</i> String indicating the scheduler-specific name of the job.<br />
 <i>exit_code</i> Exit code of the process if known.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>GLOBUS_SUCCESS</i> Scheduler message sent or queued.<br />
 <i>GLOBUS_SEG_ERROR_NULL</i> Null jobid.<br />
 <i>GLOBUS_SEG_ERROR_INVALID_FORMAT</i> Unable to determine length of formatted string.</dl>
<h3>globus_result_t globus_scheduler_event_generator_get_timestamp (time_t * timestamp)</h3>
<p>Get the timestamp for the earliest event an SEG module should send. <code>Parameters:</code></p>
<dl>
<dd><i>timestamp</i> Pointer to a time_t which will be set to the timestamp passed to the SEG executable. The module should not send any events which occur prior to this timestamp.</dl>
<p> <code>Return values:</code></p>
<dl>
<dd><i>GLOBUS_SEG_ERROR_NULL</i> Null timestamp.<br />
 <i>GLOBUS_SUCCESS</i> Timestamp value updated. If the timestamp was not set on the SEG command-line, then the value pointed to by <i>timestamp</i> will be set to 0.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for globus scheduler event generator from the source code.</p>
