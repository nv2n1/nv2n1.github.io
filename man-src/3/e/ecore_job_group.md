---
title: "ecore_job_group(3)"
name: "ecore_job_group"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_job_group/"
description: "Ecore Jobs – You can queue jobs that are to be done by the main loop when the current event is dealt with."
---

<p>Ecore Jobs &#8211; You can queue jobs that are to be done by the main loop when the current event is dealt with. </p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Job</code> * <code>ecore_job_add</code> (void(*func)(void *data), const void *data)<br />
 <i>Add a job to the event queue. </i><br />
 EAPI void * <code>ecore_job_del</code> (<code>Ecore_Job</code> *job)<br />
 <i>Delete a queued job that has not yet been executed. </i></p>
<h2>Detailed Description</h2>
<p>You can queue jobs that are to be done by the main loop when the current event is dealt with.</p>
<h2>Function Documentation</h2>
<h3>EAPI <code>Ecore_Job</code>* ecore_job_add (void(*)(void *data) func, const void * data)</h3>
<p>Add a job to the event queue. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>func</i> The function to call when the job gets handled.<br />
 <i>data</i> Data pointer to be passed to the job function when the job is handled.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The handle of the job. NULL is returned if the job could not be added to the queue.</dl>
<p> <code>Note:</code></p>
<dl COMPACT>
<dd>Once the job has been executed, the job handle is invalid.</dl>
<p> References ecore_event_add().</p>
<h3>EAPI void* ecore_job_del (<code>Ecore_Job</code> * job)</h3>
<p>Delete a queued job that has not yet been executed. </p>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>job</i> Handle of the job to delete.</dl>
<p> <code>Returns:</code></p>
<dl COMPACT>
<dd>The data pointer that was to be passed to the job.</dl>
<p> References ecore_event_del().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
