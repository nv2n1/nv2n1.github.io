---
title: "sc_pthreadthreadgrp(3)"
name: "sc_pthreadthreadgrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pthreadthreadgrp/"
description: "sc::PthreadThreadGrp –"
---

<p>sc::PthreadThreadGrp &#8211; </p>
<p> The <code>PthreadThreadGrp</code> class privides a concrete thread group appropriate for an environment where pthreads is available.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;thpthd.h&gt;</code></pre>
<p> Inherits <code>sc::ThreadGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PthreadThreadGrp</code> (const <code>PthreadThreadGrp</code> &amp;, int nthread=-1) </p>
<p> <code>PthreadThreadGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> int <code>start_threads</code> ()<br />
 <i>Starts the threads running. </i><br />
 int <code>wait_threads</code> ()<br />
 <i>Wait for all the threads to complete. </i><br />
 void <code>add_thread</code> (int i, <code>Thread</code> *t)<br />
 <i>Assigns a </i><code>Thread</code> object to each thread.<br />
 void <code>add_thread</code> (int i, <code>Thread</code> *t, int priority)<br />
 <i>Like add_thread(threadnum, thread), but assign a priority that the thread is to use. </i><br />
 <code>Ref</code>&lt; <code>ThreadLock</code> &gt; <code>new_lock</code> ()<br />
 <i>Return a local object. </i><br />
 <code>ThreadGrp</code> * <code>clone</code> (int nthread=-1)<br />
 <i>Create a </i><code>ThreadGrp</code> like the current one.</p>
<h2>Detailed Description</h2>
<p>The <code>PthreadThreadGrp</code> class privides a concrete thread group appropriate for an environment where pthreads is available.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::PthreadThreadGrp::add_thread (int threadnum, <code>Thread</code> * thread, int priority) [virtual]</h3>
<p>Like add_thread(threadnum, thread), but assign a priority that the thread is to use. The member is primarily for experimentation, the priority argument is currently not well defined and ignored. </p>
<p> Reimplemented from <code>sc::ThreadGrp</code>.</p>
<h3>void sc::PthreadThreadGrp::add_thread (int threadnum, <code>Thread</code> * thread) [inline, virtual]</h3>
<p>Assigns a <code>Thread</code> object to each thread. If 0 is assigned to a thread, then that thread will be skipped. </p>
<p> Reimplemented from <code>sc::ThreadGrp</code>.</p>
<h3><code>ThreadGrp</code>* sc::PthreadThreadGrp::clone (int nthread = -1) [virtual]</h3>
<p>Create a <code>ThreadGrp</code> like the current one. If nthread is given, the new <code>ThreadGrp</code> will attempt to support that number of threads, but the actual number supported may be less. If nthread is -1, the number of threads in the current group will be used. </p>
<p> Reimplemented from <code>sc::ThreadGrp</code>.</p>
<h3>int sc::PthreadThreadGrp::start_threads () [virtual]</h3>
<p>Starts the threads running. <code>Thread</code> 0 will be run by the thread that calls start_threads. </p>
<p> Implements <code>sc::ThreadGrp</code>.</p>
<h3>int sc::PthreadThreadGrp::wait_threads () [virtual]</h3>
<p>Wait for all the threads to complete. This must be called before start_threads is called again or the object is destroyed. </p>
<p> Implements <code>sc::ThreadGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
