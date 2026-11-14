---
title: "sc_armcimemorygrp(3)"
name: "sc_armcimemorygrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_armcimemorygrp/"
description: "sc::ARMCIMemoryGrp –"
---

<p>sc::ARMCIMemoryGrp &#8211; </p>
<p> The <code>ARMCIMemoryGrp</code> concrete class provides an implementation of <code>MsgMemoryGrp</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;memarmci.h&gt;</code></pre>
<p> Inherits <code>sc::RDMAMemoryGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ARMCIMemoryGrp</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;msg) </p>
<p> <code>ARMCIMemoryGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>set_localsize</code> (size_t)<br />
 <i>Set the size of locally held memory. </i><br />
 void <code>retrieve_data</code> (void *, int node, int offset, int size, int lock) </p>
<p> void <code>replace_data</code> (void *, int node, int offset, int size, int unlock) </p>
<p> void <code>sum_data</code> (double *data, int node, int doffset, int dsize) </p>
<p> void <code>sync</code> ()<br />
 <i>Synchronizes all the nodes. </i><br />
 void <code>deactivate</code> ()<br />
 <i>Deactivate is called after the memory has been used. </i><br />
 void * <code>malloc_local</code> (size_t nbyte)<br />
 <i>Allocate data that will be accessed locally only. </i><br />
 void <code>free_local</code> (void *data)<br />
 <i>Free data that was allocated with malloc_local_double. </i><br />
 void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Prints out information about the object. </i></p>
<h2>Detailed Description</h2>
<p>The <code>ARMCIMemoryGrp</code> concrete class provides an implementation of <code>MsgMemoryGrp</code>. </p>
<p> It uses the ARMCI interface.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::ARMCIMemoryGrp::free_local (void * data) [virtual]</h3>
<p>Free data that was allocated with malloc_local_double. </p>
<p> Reimplemented from <code>sc::MemoryGrp</code>.</p>
<h3>void* sc::ARMCIMemoryGrp::malloc_local (size_t nbyte) [virtual]</h3>
<p>Allocate data that will be accessed locally only. Using this for data that will be used for global operation can improve efficiency. Data allocated in this way must be freed with free_local_double. </p>
<p> Reimplemented from <code>sc::MemoryGrp</code>.</p>
<h3>void sc::ARMCIMemoryGrp::set_localsize (size_t) [virtual]</h3>
<p>Set the size of locally held memory. When memory is accessed using a global offset counting starts at node 0 and proceeds up to node <code>n()</code> &#8211; 1. </p>
<p> Reimplemented from <code>sc::RDMAMemoryGrp</code>.</p>
<h3>void sc::ARMCIMemoryGrp::sync () [virtual]</h3>
<p>Synchronizes all the nodes. This is useful after remote memory writes to be certain that all of the writes have completed and the data can be accessed locally, for example. </p>
<p> Reimplemented from <code>sc::MsgMemoryGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
