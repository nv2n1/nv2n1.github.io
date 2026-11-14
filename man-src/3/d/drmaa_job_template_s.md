---
title: "drmaa_job_template_s(3)"
name: "drmaa_job_template_s"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_job_template_s/"
description: "drmaa_job_template_s –"
---

<h2 class="name">NAME</h2>
<p> drmaa_job_template_s &#8211; </p>
<p> Job template data.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;drmaa_impl.h&gt;</p>
<h3>Data Fields</h3>
<p> <code>drmaa_session_t</code> * <code>session</code><br />
 <i>DRMAA session in which job template was created. </i><br />
 <code>drmaa_job_template_t</code> * <code>prev</code><br />
 <i>Previous job template in list. </i><br />
 <code>drmaa_job_template_t</code> * <code>next</code><br />
 <i>Next job template in list. </i><br />
 void ** <code>attrib</code><br />
 <i>Table of DRMAA attributes. </i><br />
 pthread_mutex_t <code>mutex</code><br />
 <i>Mutex for accessing job attributes. </i></p>
<h2>Detailed Description</h2>
<p> Job template data. </p>
<h2>Field Documentation</h2>
<h3><code>drmaa_session_t</code>* drmaa_job_template_s::session</h3>
<p> DRMAA session in which job template was created.</p>
<h3><code>drmaa_job_template_t</code>* drmaa_job_template_s::prev</h3>
<p> Previous job template in list.</p>
<h3><code>drmaa_job_template_t</code>* drmaa_job_template_s::next</h3>
<p> Next job template in list.</p>
<h3>void** drmaa_job_template_s::attrib</h3>
<p> Table of DRMAA attributes. It is filled with N_DRMAA_ATTRIBS values which are either NULL (attribute not set) or string (scalar attribute) or NULL terminated array of strings (vector attribute).</p>
<h3>pthread_mutex_t drmaa_job_template_s::mutex</h3>
<p> Mutex for accessing job attributes. </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for torque from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAL">Author</a></p>
<dd></dl>
