---
title: "jobs-h(3)"
name: "jobs-h"
section: "3"
letter: "j"
url: "/docs/linux/man/3-jobs-h/"
description: "src/jobs.h –"
---

<p>src/jobs.h &#8211; </p>
<p> Remembering submitted job in session.</p>
<h2>Synopsis</h2>
<p>#include &lt;drmaa_impl.h&gt; </p>
<h3>Data Structures</h3>
<p>struct <code>drmaa_job_s</code><br />
 <i>Job data stored for each submitted job. </i><br />
 struct <code>drmaa_job_iter_s</code><br />
 <i>Iterates over submitted jobs set. </i></p>
<h3>Functions</h3>
<p>void <code>drmaa_get_job_list_iter</code> (<code>drmaa_session_t</code> *session, <code>drmaa_job_iter_t</code> *iter)<br />
 <i>Returns iterator to jobs held in DRMAA session. </i><br />
 <code>drmaa_job_t</code> * <code>drmaa_get_next_job</code> (<code>drmaa_job_iter_t</code> *iter)<br />
 <i>Returns next job identifier from set or </i>NULL if set finished.<br />
 void <code>drmaa_add_job</code> (<code>drmaa_session_t</code> *c, <code>drmaa_job_t</code> *job)<br />
 <i>Adds job identifier to session. </i><br />
 bool <code>drmaa_find_job</code> (<code>drmaa_session_t</code> *c, const char *jobid, <code>drmaa_job_t</code> *found, unsigned flags)<br />
 <i>Checks if job with given identifier exist in hash table and optionally removes it. </i></p>
<h2>Detailed Description</h2>
<p>Remembering submitted job in session. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for torque from the source code.</p>
