---
title: "jobs(3)"
name: "jobs"
section: "3"
letter: "j"
url: "/docs/linux/man/3-jobs/"
description: "Remembering submitted job in session. –"
---

<h2 class="name">NAME</h2>
<p> Remembering submitted job in session. &#8211; </p>
<h3>Data Structures</h3>
<p> struct <code>drmaa_job_s</code><br />
 <i>Job data stored for each submitted job. </i><br />
 struct <code>drmaa_job_iter_s</code><br />
 <i>Iterates over submitted jobs set. </i></p>
<h3>Functions</h3>
<p> void <code>drmaa_get_job_list_iter</code> (<code>drmaa_session_t</code> *session, <code>drmaa_job_iter_t</code> *iter)<br />
 <i>Returns iterator to jobs held in DRMAA session. </i><br />
 <code>drmaa_job_t</code> * <code>drmaa_get_next_job</code> (<code>drmaa_job_iter_t</code> *iter)<br />
 <i>Returns next job identifier from set or </i>NULL if set finished.<br />
 void <code>drmaa_add_job</code> (<code>drmaa_session_t</code> *c, <code>drmaa_job_t</code> *job)<br />
 <i>Adds job identifier to session. </i><br />
 bool <code>drmaa_find_job</code> (<code>drmaa_session_t</code> *c, const char *jobid, <code>drmaa_job_t</code> *found, unsigned flags)<br />
 <i>Checks if job with given identifier exist in hash table and optionally removes it. </i></p>
<h2>Detailed Description</h2>
<h2>Function Documentation</h2>
<h3>void drmaa_get_job_list_iter (<code>drmaa_session_t</code> *session, <code>drmaa_job_iter_t</code> *iter)</h3>
<p> Returns iterator to jobs held in DRMAA session. Caller thread should have <code>drmaa_session_s::jobs_mutex</code> acquired iterator remains valid until job list is modified (or lock is released).</p>
<h3><code>drmaa_job_t</code>* drmaa_get_next_job (<code>drmaa_job_iter_t</code> *iter)</h3>
<p> Returns next job identifier from set or NULL if set finished.</p>
<h3>void drmaa_add_job (<code>drmaa_session_t</code> *c, <code>drmaa_job_t</code> *job)</h3>
<p> Adds job identifier to session. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>c</i> DRMAA session.<br />
 <i>job</i> Malloced drmaa_job_t structure with filled jobid field (also malloced).</dl>
<h3>bool drmaa_find_job (<code>drmaa_session_t</code> *c, const char *jobid, <code>drmaa_job_t</code> *found, unsignedflags)</h3>
<p> Checks if job with given identifier exist in hash table and optionally removes it. </p>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>c</i> Opened DRMAA session.<br />
 <i>jobid</i> Job identifier.<br />
 <i>found</i> If not NULL and job was found job session data will be stored here.<br />
 <i>flags</i> Information to store into session. If DRMAA_JOB_DISPOSE bit is set session data will be removed.</dl>
<p> <code>See Also:</code></p>
<dl>
<dt>
<dd> job_flag_t</dl>
<h2>Author</h2>
<p> Generated automatically by Doxygen for torque from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAK">Author</a></p>
<dd></dl>
