---
title: "sc_filegrp(3)"
name: "sc_filegrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_filegrp/"
description: "sc::FileGrp –"
---

<p>sc::FileGrp &#8211; </p>
<p> The <code>FileGrp</code> abstract class provides a way of accessing distributed file in a parallel machine.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;file.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::ProcFileGrp</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>FileGrp (const Ref&lt; KeyVal &gt; &amp;)



void open ()


Opens the files.


void close ()


Closes the files.


void set_filename (char *name)


Sets the filename for the FileGrp.


const char * get_filename () const


Returns the filename for the FileGrp.


int me () const


Returns who I am.


int n () const


Returns how many nodes there are.


virtual void set_localsize (size_t)=0


Set the size of locally held data.


size_t localsize ()


Returns the amount of data residing locally on me().


distsize_t localoffset ()


Returns the global offset to this node's data.


int size (int node)


Returns the amount of data residing on node.


distsize_t offset (int node)


Returns the global offset to node's data.


distsize_t totalsize ()


Returns the sum of all data allocated on all nodes.


virtual void activate ()


Activate is called before the data is to be used.


virtual void deactivate ()


Deactivate is called after the data has been used.


virtual void * obtain_writeonly (distsize_t offset, int size)=0


This gives write access to the data location. No locking is done.


virtual void * obtain_readwrite (distsize_t offset, int size)=0


Only one thread can have an unreleased obtain_readwrite at a time.


virtual void * obtain_readonly (distsize_t offset, int size)=0


This gives read access to the file location. No locking is done.


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


virtual void catchup ()


Processes outstanding requests.


virtual void print (std::ostream &amp;o=ExEnv::out0()) const


Prints out information about the object.


virtual FileGrp * clone ()=0


Clones the given FileGrp. The new FileGrp may need to be initialized additionally.



Static Public Member Functions
static FileGrp * initial_filegrp (int &amp;argc, char **argv)


Create a file group.


static FileGrp * initial_filegrp ()



static void set_default_filegrp (const Ref&lt; FileGrp &gt; &amp;)


The default file group contains the primary file group to be used by an application.


static FileGrp * get_default_filegrp ()


Returns the default file group.



Protected Member Functions
void obtain_local_lock (size_t start, size_t fence)



void release_local_lock (size_t start, size_t fence)



Protected Attributes
int me_



int n_



distsize_t * offsets_



int debug_</code></pre>
<h2>Detailed Description</h2>
<p>The <code>FileGrp</code> abstract class provides a way of accessing distributed file in a parallel machine. </p>
<p> Several specializations are available. For one processor, <code>ProcFileGrp</code> provides a simple stub implementation. Otherwise, the specializations that should work are MPIIOIFileGrp and MTMPIFileGrp. </p>
<p> If a <code>FileGrp</code> is not given to the program, then one will be automatically chosen depending on which <code>MessageGrp</code> is used by default, the type of machine on which the code was compiled, and what options were given at configuration time.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::FileGrp::catchup () [virtual]</h3>
<p>Processes outstanding requests. Some file group implementations don&#8217;t have access to real shared memory or even active messages. Instead, requests are processed whenever certain file group routines are called. This can cause large latencies and buffer overflows. If this is a problem, then the catchup member can be called to process all outstanding requests.</p>
<h3>static <code>FileGrp</code>* sc::FileGrp::initial_filegrp (int &amp; argc, char ** argv) [static]</h3>
<p>Create a file group. This routine looks for a -filegrp argument, then the environmental variable FILEGRP, and, finally, the default <code>MessageGrp</code> object to decide which specialization of <code>FileGrp</code> would be appropriate. The argument to -integralgrp should be either string for a <code>ParsedKeyVal</code> constructor or a classname. The default <code>ThreadGrp</code> and <code>MessageGrp</code> objects should be initialized before this is called.</p>
<h3>virtual void* sc::FileGrp::obtain_readwrite (<code>distsize_t</code> offset, int size) [pure virtual]</h3>
<p>Only one thread can have an unreleased obtain_readwrite at a time. The actual file region locked can be larger than that requested. If the file region is already locked this will block. For this reason, data should be held as read/write for as short a time as possible. </p>
<p> Implemented in <code>sc::ProcFileGrp</code>.</p>
<h3>virtual void sc::FileGrp::release_readwrite (void * data, <code>distsize_t</code> offset, int size) [pure virtual]</h3>
<p>This is called when read/write access is no longer needed. The data will be unlocked. </p>
<p> Implemented in <code>sc::ProcFileGrp</code>.</p>
<h3>static void sc::FileGrp::set_default_filegrp (const <code>Ref</code>&lt; <code>FileGrp</code> &gt; &amp;) [static]</h3>
<p>The default file group contains the primary file group to be used by an application.</p>
<h3>virtual void sc::FileGrp::set_localsize (size_t) [pure virtual]</h3>
<p>Set the size of locally held data. When data is accessed using a global offset counting starts at node 0 and proceeds up to node <code>n()</code> &#8211; 1. </p>
<p> Implemented in <code>sc::ProcFileGrp</code>.</p>
<h3>virtual void sc::FileGrp::sync () [pure virtual]</h3>
<p>Synchronizes all the nodes. Consider using this when the way you you access data changes. </p>
<p> Implemented in <code>sc::ProcFileGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
