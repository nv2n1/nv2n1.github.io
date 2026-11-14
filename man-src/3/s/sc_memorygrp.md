---
title: "sc_memorygrp(3)"
name: "sc_memorygrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_memorygrp/"
description: "sc::MemoryGrp –"
---

<p>sc::MemoryGrp &#8211; </p>
<p> The <code>MemoryGrp</code> abstract class provides a way of accessing distributed memory in a parallel machine.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;memory.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::MsgMemoryGrp</code>, and <code>sc::ProcMemoryGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MemoryGrp (const Ref&lt; KeyVal &gt; &amp;)



int me () const


Returns who I am.


int n () const


Returns how many nodes there are.


virtual void set_localsize (size_t)=0


Set the size of locally held memory.


size_t localsize ()


Returns the amount of memory residing locally on me().


virtual void * localdata ()=0


Returns a pointer to the local data.


distsize_t localoffset ()


Returns the global offset to this node's memory.


int size (int node)


Returns the amount of memory residing on node.


distsize_t offset (int node)


Returns the global offset to node's memory.


distsize_t totalsize ()


Returns the sum of all memory allocated on all nodes.


virtual void activate ()


Activate is called before the memory is to be used.


virtual void deactivate ()


Deactivate is called after the memory has been used.


virtual void * obtain_writeonly (distsize_t offset, int size)=0


This gives write access to the memory location. No locking is done.


virtual void * obtain_readwrite (distsize_t offset, int size)=0


Only one thread can have an unreleased obtain_readwrite at a time.


virtual void * obtain_readonly (distsize_t offset, int size)=0


This gives read access to the memory location. No locking is done.


virtual void release_readonly (void *data, distsize_t offset, int size)=0


This is called when read access is no longer needed.


virtual void release_writeonly (void *data, distsize_t offset, int size)=0


This is called when write access is no longer needed.


virtual void release_readwrite (void *data, distsize_t offset, int size)=0


This is called when read/write access is no longer needed.


virtual void sum_reduction (double *data, distsize_t doffset, int dsize)



virtual void sum_reduction_on_node (double *data, size_t doffset, int dsize, int node=-1)



virtual void sync ()=0


Synchronizes all the nodes.


virtual void * malloc_local (size_t nbyte)


Allocate data that will be accessed locally only.


virtual double * malloc_local_double (size_t ndouble)



virtual void free_local (void *data)


Free data that was allocated with malloc_local_double.


virtual void free_local_double (double *data)



virtual void catchup ()


Processes outstanding requests.


virtual void print (std::ostream &amp;o=ExEnv::out0()) const


Prints out information about the object.



Static Public Member Functions
static MemoryGrp * initial_memorygrp (int &amp;argc, char **argv)


Create a memory group.


static MemoryGrp * initial_memorygrp ()



static void set_default_memorygrp (const Ref&lt; MemoryGrp &gt; &amp;)


The default memory group contains the primary memory group to be used by an application.


static MemoryGrp * get_default_memorygrp ()


Returns the default memory group.



Protected Member Functions
void obtain_local_lock (size_t start, size_t fence)



void release_local_lock (size_t start, size_t fence)



Protected Attributes
int me_



int n_



distsize_t * offsets_



int debug_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>MemoryGrp</code> abstract class provides a way of accessing distributed memory in a parallel machine. </p>
<p> Several specializations are available. For one processor, <code>ProcMemoryGrp</code> provides a simple stub implementation. Parallel specializations include <code>ShmMemoryGrp</code>, <code>MTMPIMemoryGrp</code>, and <code>ARMCIMemoryGrp</code>. The particular specializations that work depend highly on the target hardware and software environment.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::MemoryGrp::catchup () [virtual]</h3>
<p>Processes outstanding requests. Some memory group implementations don&#8217;t have access to real shared memory or even active messages. Instead, requests are processed whenever certain memory group routines are called. This can cause large latencies and buffer overflows. If this is a problem, then the catchup member can be called to process all outstanding requests.</p>
<h3>virtual void sc::MemoryGrp::free_local (void * data) [virtual]</h3>
<p>Free data that was allocated with malloc_local_double. </p>
<p> Reimplemented in <code>sc::ARMCIMemoryGrp</code>.</p>
<h3>static <code>MemoryGrp</code>* sc::MemoryGrp::get_default_memorygrp () [static]</h3>
<p>Returns the default memory group. If the default memory group has not yet been set, then one is created. The particular specialization used is determined by configuration options and which specializations are being used for <code>MessageGrp</code> and <code>ThreadGrp</code>.</p>
<h3>static <code>MemoryGrp</code>* sc::MemoryGrp::initial_memorygrp (int &amp; argc, char ** argv) [static]</h3>
<p>Create a memory group. This routine looks for a -memorygrp argument, and then the environmental variable MEMORYGRP to decide which specialization of <code>MemoryGrp</code> would be appropriate. The argument to -memorygrp or the value of the environmental variable should be either string for a <code>ParsedKeyVal</code> constructor or a classname. The default <code>ThreadGrp</code> and <code>MessageGrp</code> objects should be initialized before this is called.</p>
<h3>virtual void* sc::MemoryGrp::malloc_local (size_t nbyte) [virtual]</h3>
<p>Allocate data that will be accessed locally only. Using this for data that will be used for global operation can improve efficiency. Data allocated in this way must be freed with free_local_double. </p>
<p> Reimplemented in <code>sc::ARMCIMemoryGrp</code>.</p>
<h3>virtual void* sc::MemoryGrp::obtain_readwrite (<code>distsize_t</code> offset, int size) [pure virtual]</h3>
<p>Only one thread can have an unreleased obtain_readwrite at a time. The actual memory region locked can be larger than that requested. If the memory region is already locked this will block. For this reason, data should be held as read/write for as short a time as possible. </p>
<p> Implemented in <code>sc::ActiveMsgMemoryGrp</code>, <code>sc::ProcMemoryGrp</code>, <code>sc::RDMAMemoryGrp</code>, and <code>sc::ShmMemoryGrp</code>.</p>
<h3>virtual void sc::MemoryGrp::release_readwrite (void * data, <code>distsize_t</code> offset, int size) [pure virtual]</h3>
<p>This is called when read/write access is no longer needed. The memory will be unlocked. </p>
<p> Implemented in <code>sc::ActiveMsgMemoryGrp</code>, <code>sc::ProcMemoryGrp</code>, <code>sc::RDMAMemoryGrp</code>, and <code>sc::ShmMemoryGrp</code>.</p>
<h3>static void sc::MemoryGrp::set_default_memorygrp (const <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;) [static]</h3>
<p>The default memory group contains the primary memory group to be used by an application.</p>
<h3>virtual void sc::MemoryGrp::set_localsize (size_t) [pure virtual]</h3>
<p>Set the size of locally held memory. When memory is accessed using a global offset counting starts at node 0 and proceeds up to node <code>n()</code> &#8211; 1. </p>
<p> Implemented in <code>sc::ActiveMsgMemoryGrp</code>, <code>sc::ARMCIMemoryGrp</code>, <code>sc::MsgMemoryGrp</code>, <code>sc::ProcMemoryGrp</code>, <code>sc::RDMAMemoryGrp</code>, and <code>sc::ShmMemoryGrp</code>.</p>
<h3>virtual void sc::MemoryGrp::sync () [pure virtual]</h3>
<p>Synchronizes all the nodes. This is useful after remote memory writes to be certain that all of the writes have completed and the data can be accessed locally, for example. </p>
<p> Implemented in <code>sc::ARMCIMemoryGrp</code>, <code>sc::MsgMemoryGrp</code>, <code>sc::MTMPIMemoryGrp</code>, and <code>sc::ProcMemoryGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
