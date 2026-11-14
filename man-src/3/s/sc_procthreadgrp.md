---
title: "sc_procthreadgrp(3)"
name: "sc_procthreadgrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_procthreadgrp/"
description: "sc::ProcThreadGrp –"
---

<p>sc::ProcThreadGrp &#8211; </p>
<p> The <code>ProcThreadGrp</code> class privides a concrete thread group appropriate for an environment where there is only one thread.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;thread.h&gt;</code></pre>
<p> Inherits <code>sc::ThreadGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ProcThreadGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> int <code>start_threads</code> ()<br />
 <i>Starts the threads running. </i><br />
 int <code>wait_threads</code> ()<br />
 <i>Wait for all the threads to complete. </i><br />
 <code>Ref</code>&lt; <code>ThreadLock</code> &gt; <code>new_lock</code> ()<br />
 <i>Return a local object. </i><br />
 <code>ThreadGrp</code> * <code>clone</code> (int nthread=-1)<br />
 <i>Create a </i><code>ThreadGrp</code> like the current one.</p>
<h2>Detailed Description</h2>
<p>The <code>ProcThreadGrp</code> class privides a concrete thread group appropriate for an environment where there is only one thread.</p>
<h2>Member Function Documentation</h2>
<h3><code>ThreadGrp</code>* sc::ProcThreadGrp::clone (int nthread = -1) [virtual]</h3>
<p>Create a <code>ThreadGrp</code> like the current one. If nthread is given, the new <code>ThreadGrp</code> will attempt to support that number of threads, but the actual number supported may be less. If nthread is -1, the number of threads in the current group will be used. </p>
<p> Reimplemented from <code>sc::ThreadGrp</code>.</p>
<h3>int sc::ProcThreadGrp::start_threads () [virtual]</h3>
<p>Starts the threads running. <code>Thread</code> 0 will be run by the thread that calls start_threads. </p>
<p> Implements <code>sc::ThreadGrp</code>.</p>
<h3>int sc::ProcThreadGrp::wait_threads () [virtual]</h3>
<p>Wait for all the threads to complete. This must be called before start_threads is called again or the object is destroyed. </p>
<p> Implements <code>sc::ThreadGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
