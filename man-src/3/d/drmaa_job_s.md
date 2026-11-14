---
title: "drmaa_job_s(3)"
name: "drmaa_job_s"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_job_s/"
description: "drmaa_job_s –"
---

<h2 class="name">NAME</h2>
<p> drmaa_job_s &#8211; </p>
<p> Job data stored for each submitted job.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;jobs.h&gt;</p>
<h3>Data Fields</h3>
<p> <code>drmaa_job_t</code> * <code>next</code><br />
 <i>Next job in list or </i>NULL.<br />
 char * <code>jobid</code><br />
 <i>Job identifier from DRM. </i><br />
 int <code>time_label</code><br />
 <i>Job submission timestamp increased in DRMAA session with each submitted job. </i><br />
 bool <code>terminated</code><br />
 <i>Whether we know that job terminated and its status is waiting to rip. </i><br />
 bool <code>suspended</code><br />
 <i>Whether job was suspended within session by </i><code>drmaa_control()</code>.</p>
<h2>Detailed Description</h2>
<p> Job data stored for each submitted job. </p>
<p> It is freed when job terminates and it&#8217;s status is disposed by <code>drmaa_wait()</code> or <code>drmaa_synchronize()</code>.</p>
<h2>Field Documentation</h2>
<h3><code>drmaa_job_t</code>* drmaa_job_s::next</h3>
<p> Next job in list or NULL.</p>
<h3>char* drmaa_job_s::jobid</h3>
<p> Job identifier from DRM. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for torque from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAI">Author</a></p>
<dd></dl>
