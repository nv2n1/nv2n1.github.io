---
title: "sc_mtmpimemorygrp(3)"
name: "sc_mtmpimemorygrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_mtmpimemorygrp/"
description: "sc::MTMPIMemoryGrp –"
---

<p>sc::MTMPIMemoryGrp &#8211; </p>
<p> This <code>MemoryGrp</code> class requires a MT-safe MPI implementation.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;memmtmpi.h&gt;</code></pre>
<p> Inherits <code>sc::ActiveMsgMemoryGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MTMPIMemoryGrp (const Ref&lt; MessageGrp &gt; &amp;msg, const Ref&lt; ThreadGrp &gt; &amp;th, MPI_Comm comm=MPI_COMM_WORLD)


Construct a MTMPIMemoryGrp given a MessageGrp, ThreadGrp, and an MPI communicator.


MTMPIMemoryGrp (const Ref&lt; KeyVal &gt; &amp;)


Construct a MTMPIMemoryGrp given a KeyVal input object.


void activate ()


Activate is called before the memory is to be used.


void deactivate ()


Deactivate is called after the memory has been used.


void sync ()


Synchronizes all the nodes.



Friends</code></pre>
<p> class <code>MTMPIThread</code></p>
<h2>Detailed Description</h2>
<p>This <code>MemoryGrp</code> class requires a MT-safe MPI implementation. </p>
<p> The default <code>MessageGrp</code> must be a <code>MPIMessageGrp</code>. MPI must be safe with respect to the default <code>ThreadGrp</code>. Alternately, a <code>MessageGrp</code> and a <code>ThreadGrp</code> can be passed to the constructor.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::MTMPIMemoryGrp::MTMPIMemoryGrp (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp; msg, const <code>Ref</code>&lt; <code>ThreadGrp</code> &gt; &amp; th, MPI_Comm comm = MPI_COMM_WORLD)</h3>
<p>Construct a <code>MTMPIMemoryGrp</code> given a <code>MessageGrp</code>, <code>ThreadGrp</code>, and an MPI communicator. The communicator can be a subset of MPI_COMM_WORLD, in which case, the <code>MessageGrp</code> must refer to the same subset.</p>
<h3>sc::MTMPIMemoryGrp::MTMPIMemoryGrp (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>Construct a <code>MTMPIMemoryGrp</code> given a <code>KeyVal</code> input object. A fully thread safe MPI is needed (MPI_THREAD_MULTIPLE).</p>
<h2>Member Function Documentation</h2>
<h3>void sc::MTMPIMemoryGrp::sync () [virtual]</h3>
<p>Synchronizes all the nodes. This is useful after remote memory writes to be certain that all of the writes have completed and the data can be accessed locally, for example. </p>
<p> Reimplemented from <code>sc::MsgMemoryGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
