---
title: "sc_threadgrp(3)"
name: "sc_threadgrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_threadgrp/"
description: "sc::ThreadGrp –"
---

<p>sc::ThreadGrp &#8211; </p>
<p> The <code>ThreadGrp</code> abstract class provides a means to manage separate threads of control.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;thread.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::ProcThreadGrp</code>, <code>sc::PthreadThreadGrp</code>, and <code>sc::PumaThreadGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ThreadGrp (const Ref&lt; KeyVal &gt; &amp;)



ThreadGrp (const ThreadGrp &amp;, int nthread=-1)



virtual void add_thread (int threadnum, Thread *thread)


Assigns a Thread object to each thread.


virtual void add_thread (int threadnum, Thread *thread, int priority)


Like add_thread(threadnum, thread), but assign a priority that the thread is to use.


int nthread () const


The number of threads that will be run by start_thread.


void delete_threads ()



virtual int start_threads ()=0


Starts the threads running.


virtual int wait_threads ()=0


Wait for all the threads to complete.


virtual Ref&lt; ThreadLock &gt; new_lock ()=0


Return a local object.


virtual ThreadGrp * clone (int nthread=-1)


Create a ThreadGrp like the current one.



Static Public Member Functions
static void set_default_threadgrp (const Ref&lt; ThreadGrp &gt; &amp;)



static ThreadGrp * get_default_threadgrp ()



static ThreadGrp * initial_threadgrp (int &amp;argc, char **argv)



Protected Attributes</code></pre>
<p> <code>Thread</code> ** <code>threads_</code> </p>
<p> int <code>nthread_</code></p>
<h2>Detailed Description</h2>
<p>The <code>ThreadGrp</code> abstract class provides a means to manage separate threads of control.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::ThreadGrp::add_thread (int threadnum, <code>Thread</code> * thread, int priority) [virtual]</h3>
<p>Like add_thread(threadnum, thread), but assign a priority that the thread is to use. The member is primarily for experimentation, the priority argument is currently not well defined and ignored. </p>
<p> Reimplemented in <code>sc::PthreadThreadGrp</code>.</p>
<h3>virtual void sc::ThreadGrp::add_thread (int threadnum, <code>Thread</code> * thread) [virtual]</h3>
<p>Assigns a <code>Thread</code> object to each thread. If 0 is assigned to a thread, then that thread will be skipped. </p>
<p> Reimplemented in <code>sc::PthreadThreadGrp</code>.</p>
<h3>virtual <code>ThreadGrp</code>* sc::ThreadGrp::clone (int nthread = -1) [virtual]</h3>
<p>Create a <code>ThreadGrp</code> like the current one. If nthread is given, the new <code>ThreadGrp</code> will attempt to support that number of threads, but the actual number supported may be less. If nthread is -1, the number of threads in the current group will be used. </p>
<p> Reimplemented in <code>sc::PthreadThreadGrp</code>, and <code>sc::ProcThreadGrp</code>.</p>
<h3>virtual int sc::ThreadGrp::start_threads () [pure virtual]</h3>
<p>Starts the threads running. <code>Thread</code> 0 will be run by the thread that calls start_threads. </p>
<p> Implemented in <code>sc::PthreadThreadGrp</code>, <code>sc::PumaThreadGrp</code>, and <code>sc::ProcThreadGrp</code>.</p>
<h3>virtual int sc::ThreadGrp::wait_threads () [pure virtual]</h3>
<p>Wait for all the threads to complete. This must be called before start_threads is called again or the object is destroyed. </p>
<p> Implemented in <code>sc::PthreadThreadGrp</code>, <code>sc::PumaThreadGrp</code>, and <code>sc::ProcThreadGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
