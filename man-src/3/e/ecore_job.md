---
title: "ecore_job(3)"
name: "ecore_job"
section: "3"
letter: "e"
url: "/docs/linux/man/3-ecore_job/"
description: "Ecore_Job.h – Functions for dealing with Ecore jobs."
---

<p>Ecore_Job.h &#8211; Functions for dealing with Ecore jobs. </p>
<h2>Synopsis</h2>
<h3>Typedefs</h3>
<p>typedef void <code>Ecore_Job</code><br />
 <i>A job handle. </i></p>
<h3>Functions</h3>
<p>EAPI <code>Ecore_Job</code> * <code>ecore_job_add</code> (void(*func)(void *data), const void *data)<br />
 <i>Add a job to the event queue. </i><br />
 EAPI void * <code>ecore_job_del</code> (<code>Ecore_Job</code> *job)<br />
 <i>Delete a queued job that has not yet been executed. </i></p>
<h2>Detailed Description</h2>
<p>Functions for dealing with Ecore jobs. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for Ecore from the source code.</p>
