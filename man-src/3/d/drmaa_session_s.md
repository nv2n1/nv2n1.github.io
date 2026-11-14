---
title: "drmaa_session_s(3)"
name: "drmaa_session_s"
section: "3"
letter: "d"
url: "/docs/linux/man/3-drmaa_session_s/"
description: "drmaa_session_s –"
---

<h2 class="name">NAME</h2>
<p> drmaa_session_s &#8211; </p>
<p> DRMAA session data.</p>
<h2>SYNOPSIS</h2>
<p> #include &lt;drmaa_impl.h&gt;</p>
<h3>Data Fields</h3>
<p> int <code>pbs_conn</code><br />
 <i>PBS connection (or -1). </i><br />
 char * <code>contact</code><br />
 <i>Contact to PBS server &#8212; `host[:port]&#8217;. </i><br />
 <code>drmaa_job_template_t</code> * <code>jt_list</code><br />
 <i></i> </p>
<pre>
             Cyclic list (with sentinel) of job
</pre>
<p>&nbsp;<wbr>templates created in this DRMAA session.&nbsp;<wbr>&quot;<br />
 <code>drmaa_job_t</code> ** <code>job_hashtab</code><br />
 <i></i> </p>
<pre>
               Hash table of jobs
</pre>
<p>&nbsp;<wbr>which have to be remembered in DRMAA session&nbsp;<wbr>(was submitted in this session and its status was not removed).&nbsp;<wbr>&quot;<br />
 int <code>next_time_label</code><br />
 <i>Will be assigned to next submitted job. </i><br />
 pthread_mutex_t <code>conn_mutex</code><br />
 <i>Mutex for PBS connection. </i><br />
 pthread_mutex_t <code>jobs_mutex</code><br />
 <i></i> </p>
<pre>
               Mutex for #jt_list, #job_list
</pre>
<p>&nbsp;<wbr>and&nbsp;<wbr><code>next_time_label</code>.&nbsp;<wbr>&quot;</p>
<h2>Detailed Description</h2>
<p> DRMAA session data. </p>
<h2>Field Documentation</h2>
<h3>int drmaa_session_s::pbs_conn</h3>
<p> PBS connection (or -1).</p>
<h3>char* drmaa_session_s::contact</h3>
<p> Contact to PBS server &#8212; `host[:port]&#8217;.</p>
<h3><code>drmaa_job_template_t</code>* drmaa_session_s::jt_list</h3>
<pre>
             Cyclic list (with sentinel) of job
</pre>
<p>&nbsp;<wbr>templates created in this DRMAA session.&nbsp;<wbr></p>
<h3><code>drmaa_job_t</code>** drmaa_session_s::job_hashtab</h3>
<pre>
               Hash table of jobs
</pre>
<p>&nbsp;<wbr>which have to be remembered in DRMAA session&nbsp;<wbr>(was submitted in this session and its status was not removed).&nbsp;<wbr></p>
<h3>int drmaa_session_s::next_time_label</h3>
<p> Will be assigned to next submitted job.</p>
<h3>pthread_mutex_t drmaa_session_s::conn_mutex</h3>
<p> Mutex for PBS connection.</p>
<h3>pthread_mutex_t drmaa_session_s::jobs_mutex</h3>
<pre>
               Mutex for #jt_list, #job_list
</pre>
<p>&nbsp;<wbr>and&nbsp;<wbr><code>next_time_label</code>.&nbsp;<wbr> </p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for torque from the source code. </p>
<h2>Index</h2>
<dt><a href="#lbAN">Author</a></p>
<dd></dl>
