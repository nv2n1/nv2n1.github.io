---
title: "sc_rdmamemorygrp(3)"
name: "sc_rdmamemorygrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_rdmamemorygrp/"
description: "sc::RDMAMemoryGrp –"
---

<p>sc::RDMAMemoryGrp &#8211; </p>
<p> The <code>RDMAMemoryGrp</code> abstract class specializes the <code>MsgMemoryGrp</code> class.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;memrdma.h&gt;</code></pre>
<p> Inherits <code>sc::MsgMemoryGrp</code>. Inherited by <code>sc::ARMCIMemoryGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RDMAMemoryGrp (const Ref&lt; MessageGrp &gt; &amp;msg)



RDMAMemoryGrp (const Ref&lt; KeyVal &gt; &amp;)



void * localdata ()


Returns a pointer to the local data.


void set_localsize (size_t localsize)


Set the size of locally held memory.


void * obtain_writeonly (distsize_t offset, int size)


This gives write access to the memory location. No locking is done.


void * obtain_readwrite (distsize_t offset, int size)


Only one thread can have an unreleased obtain_readwrite at a time.


void * obtain_readonly (distsize_t offset, int size)


This gives read access to the memory location. No locking is done.


void release_readonly (void *data, distsize_t offset, int size)


This is called when read access is no longer needed.


void release_writeonly (void *data, distsize_t offset, int size)


This is called when write access is no longer needed.


void release_readwrite (void *data, distsize_t offset, int size)


This is called when read/write access is no longer needed.


void sum_reduction (double *data, distsize_t doffset, int dsize)



void sum_reduction_on_node (double *data, size_t doffset, int dsize, int node=-1)



void print (std::ostream &amp;o=ExEnv::out0()) const


Prints out information about the object.



Protected Member Functions
virtual void retrieve_data (void *, int node, int offset, int size, int lock)=0



virtual void replace_data (void *, int node, int offset, int size, int unlock)=0



virtual void sum_data (double *data, int node, int doffset, int dsize)=0



void * malloc_region (size_t nbyte)



void free_region (void *)



Protected Attributes
char * data_



std::vector&lt; Pool * &gt; pools_



size_t default_pool_size_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>RDMAMemoryGrp</code> abstract class specializes the <code>MsgMemoryGrp</code> class. </p>
<p> It uses RDMA to implement global shared memory.</p>
<h2>Member Function Documentation</h2>
<h3>void* sc::RDMAMemoryGrp::obtain_readwrite (<code>distsize_t</code> offset, int size) [virtual]</h3>
<p>Only one thread can have an unreleased obtain_readwrite at a time. The actual memory region locked can be larger than that requested. If the memory region is already locked this will block. For this reason, data should be held as read/write for as short a time as possible. </p>
<p> Implements <code>sc::MemoryGrp</code>.</p>
<h3>void sc::RDMAMemoryGrp::release_readwrite (void * data, <code>distsize_t</code> offset, int size) [virtual]</h3>
<p>This is called when read/write access is no longer needed. The memory will be unlocked. </p>
<p> Implements <code>sc::MemoryGrp</code>.</p>
<h3>void sc::RDMAMemoryGrp::set_localsize (size_t) [virtual]</h3>
<p>Set the size of locally held memory. When memory is accessed using a global offset counting starts at node 0 and proceeds up to node <code>n()</code> &#8211; 1. </p>
<p> Reimplemented from <code>sc::MsgMemoryGrp</code>. </p>
<p> Reimplemented in <code>sc::ARMCIMemoryGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
