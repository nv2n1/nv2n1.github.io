---
title: "sc_shmmemorygrp(3)"
name: "sc_shmmemorygrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_shmmemorygrp/"
description: "sc::ShmMemoryGrp –"
---

<p>sc::ShmMemoryGrp &#8211; </p>
<p> The <code>ShmMemoryGrp</code> concrete class provides an implementation of <code>MsgMemoryGrp</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;memshm.h&gt;</code></pre>
<p> Inherits <code>sc::MsgMemoryGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ShmMemoryGrp</code> (const <code>Ref</code>&lt; <code>MessageGrp</code> &gt; &amp;msg) </p>
<p> <code>ShmMemoryGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>set_localsize</code> (size_t)<br />
 <i>Set the size of locally held memory. </i><br />
 void * <code>localdata</code> ()<br />
 <i>Returns a pointer to the local data. </i><br />
 void * <code>obtain_readwrite</code> (<code>distsize_t</code> offset, int size)<br />
 <i>Only one thread can have an unreleased obtain_readwrite at a time. </i><br />
 void * <code>obtain_readonly</code> (<code>distsize_t</code> offset, int size)<br />
 <i>This gives read access to the memory location. No locking is done. </i><br />
 void * <code>obtain_writeonly</code> (<code>distsize_t</code> offset, int size)<br />
 <i>This gives write access to the memory location. No locking is done. </i><br />
 void <code>release_readonly</code> (void *data, <code>distsize_t</code> offset, int size)<br />
 <i>This is called when read access is no longer needed. </i><br />
 void <code>release_writeonly</code> (void *data, <code>distsize_t</code> offset, int size)<br />
 <i>This is called when write access is no longer needed. </i><br />
 void <code>release_readwrite</code> (void *data, <code>distsize_t</code> offset, int size)<br />
 <i>This is called when read/write access is no longer needed. </i><br />
 void <code>print</code> (std::ostream &amp;o=ExEnv::out0()) const<br />
 <i>Prints out information about the object. </i></p>
<h2>Detailed Description</h2>
<p>The <code>ShmMemoryGrp</code> concrete class provides an implementation of <code>MsgMemoryGrp</code>. </p>
<p> It uses SYSV IPC to provided shared memory in a system that provide shared memory in hardware. It is very fast and reliable.</p>
<h2>Member Function Documentation</h2>
<h3>void* sc::ShmMemoryGrp::obtain_readwrite (<code>distsize_t</code> offset, int size) [virtual]</h3>
<p>Only one thread can have an unreleased obtain_readwrite at a time. The actual memory region locked can be larger than that requested. If the memory region is already locked this will block. For this reason, data should be held as read/write for as short a time as possible. </p>
<p> Implements <code>sc::MemoryGrp</code>.</p>
<h3>void sc::ShmMemoryGrp::release_readwrite (void * data, <code>distsize_t</code> offset, int size) [virtual]</h3>
<p>This is called when read/write access is no longer needed. The memory will be unlocked. </p>
<p> Implements <code>sc::MemoryGrp</code>.</p>
<h3>void sc::ShmMemoryGrp::set_localsize (size_t) [virtual]</h3>
<p>Set the size of locally held memory. When memory is accessed using a global offset counting starts at node 0 and proceeds up to node <code>n()</code> &#8211; 1. </p>
<p> Reimplemented from <code>sc::MsgMemoryGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
