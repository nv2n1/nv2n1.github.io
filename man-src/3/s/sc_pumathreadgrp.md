---
title: "sc_pumathreadgrp(3)"
name: "sc_pumathreadgrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_pumathreadgrp/"
description: "sc::PumaThreadGrp –"
---

<p>sc::PumaThreadGrp &#8211; </p>
<p> The <code>PumaThreadGrp</code> class privides a concrete thread group appropriate for the intel teraflops machine.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;thpuma.h&gt;</code></pre>
<p> Inherits <code>sc::ThreadGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>PumaThreadGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> int <code>start_threads</code> ()<br />
 <i>Starts the threads running. </i><br />
 int <code>wait_threads</code> ()<br />
 <i>Wait for all the threads to complete. </i><br />
 <code>Ref</code>&lt; <code>ThreadLock</code> &gt; <code>new_lock</code> ()<br />
 <i>Return a local object. </i></p>
<h2>Detailed Description</h2>
<p>The <code>PumaThreadGrp</code> class privides a concrete thread group appropriate for the intel teraflops machine.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::PumaThreadGrp::start_threads () [virtual]</h3>
<p>Starts the threads running. <code>Thread</code> 0 will be run by the thread that calls start_threads. </p>
<p> Implements <code>sc::ThreadGrp</code>.</p>
<h3>int sc::PumaThreadGrp::wait_threads () [virtual]</h3>
<p>Wait for all the threads to complete. This must be called before start_threads is called again or the object is destroyed. </p>
<p> Implements <code>sc::ThreadGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
