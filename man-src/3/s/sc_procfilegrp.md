---
title: "sc_procfilegrp(3)"
name: "sc_procfilegrp"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_procfilegrp/"
description: "sc::ProcFileGrp –"
---

<p>sc::ProcFileGrp &#8211; </p>
<p> The <code>ProcFileGrp</code> concrete class provides an implementation of <code>FileGrp</code> for a single processor.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;fileproc.h&gt;</code></pre>
<p> Inherits <code>sc::FileGrp</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ProcFileGrp</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> <code>ProcFileGrp</code> * <code>clone</code> ()<br />
 <i>Clones the given </i><code>FileGrp</code>. The new <code>FileGrp</code> may need to be initialized additionally.<br />
 void <code>set_localsize</code> (size_t)<br />
 <i>Set the size of locally held data. </i><br />
 void * <code>localdata</code> () </p>
<p> void * <code>obtain_readwrite</code> (<code>distsize_t</code> offset, int size)<br />
 <i>Only one thread can have an unreleased obtain_readwrite at a time. </i><br />
 void * <code>obtain_readonly</code> (<code>distsize_t</code> offset, int size)<br />
 <i>This gives read access to the file location. No locking is done. </i><br />
 void * <code>obtain_writeonly</code> (<code>distsize_t</code> offset, int size)<br />
 <i>This gives write access to the data location. No locking is done. </i><br />
 void <code>release_readonly</code> (void *data, <code>distsize_t</code> offset, int size)<br />
 <i>This is called when read access is no longer needed. </i><br />
 void <code>release_writeonly</code> (void *data, <code>distsize_t</code> offset, int size)<br />
 <i>This is called when write access is no longer needed. </i><br />
 void <code>release_readwrite</code> (void *data, <code>distsize_t</code> offset, int size)<br />
 <i>This is called when read/write access is no longer needed. </i><br />
 void <code>sync</code> ()<br />
 <i>Synchronizes all the nodes. </i></p>
<h2>Detailed Description</h2>
<p>The <code>ProcFileGrp</code> concrete class provides an implementation of <code>FileGrp</code> for a single processor.</p>
<h2>Member Function Documentation</h2>
<h3>void* sc::ProcFileGrp::obtain_readwrite (<code>distsize_t</code> offset, int size) [virtual]</h3>
<p>Only one thread can have an unreleased obtain_readwrite at a time. The actual file region locked can be larger than that requested. If the file region is already locked this will block. For this reason, data should be held as read/write for as short a time as possible. </p>
<p> Implements <code>sc::FileGrp</code>.</p>
<h3>void sc::ProcFileGrp::release_readwrite (void * data, <code>distsize_t</code> offset, int size) [virtual]</h3>
<p>This is called when read/write access is no longer needed. The data will be unlocked. </p>
<p> Implements <code>sc::FileGrp</code>.</p>
<h3>void sc::ProcFileGrp::set_localsize (size_t) [virtual]</h3>
<p>Set the size of locally held data. When data is accessed using a global offset counting starts at node 0 and proceeds up to node <code>n()</code> &#8211; 1. </p>
<p> Implements <code>sc::FileGrp</code>.</p>
<h3>void sc::ProcFileGrp::sync () [virtual]</h3>
<p>Synchronizes all the nodes. Consider using this when the way you you access data changes. </p>
<p> Implements <code>sc::FileGrp</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
