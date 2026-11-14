---
title: "sc_memorygrpbuf(3)"
name: "sc_memorygrpbuf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_memorygrpbuf/"
description: "sc::MemoryGrpBuf –"
---

<p>sc::MemoryGrpBuf &#8211; </p>
<p> The <code>MemoryGrpBuf</code> class provides access to pieces of the global shared memory that have been obtained with <code>MemoryGrp</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;memory.h&gt;

Public Member Functions</code></pre>
<p> <code>MemoryGrpBuf</code> (const <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp;)<br />
 <i>Creates a new </i><code>MemoryGrpBuf</code> given a <code>MemoryGrp</code> reference.<br />
 data_t * <code>writeonly</code> (<code>distsize_t</code> offset, int length)<br />
 <i>Request write only access to global memory at the global address offset and with size length. </i><br />
 data_t * <code>readwrite</code> (<code>distsize_t</code> offset, int length)<br />
 <i>Request read write access to global memory at the global address offset and with size length. </i><br />
 const data_t * <code>readonly</code> (<code>distsize_t</code> offset, int length)<br />
 <i>Request read only access to global memory at the global address offset and with size length. </i><br />
 data_t * <code>writeonly_on_node</code> (size_t offset, int length, int node=-1)<br />
 <i>These behave like writeonly, readwrite, and readonly, except the offset is local to the node specified by node. </i><br />
 data_t * <code>readwrite_on_node</code> (size_t offset, int length, int node=-1) </p>
<p> const data_t * <code>readonly_on_node</code> (size_t offset, int length, int node=-1) </p>
<p> void <code>release</code> ()<br />
 <i>Release the access to the chunk of global memory that was obtained with writeonly, readwrite, readonly, writeonly_on_node, readwrite_on_node, and readonly_on_node. </i><br />
 int <code>length</code> () const<br />
 <i>The length of the current bit of memory. </i></p>
<h2>Detailed Description</h2>
<h3>template&lt;class data_t&gt; class sc::MemoryGrpBuf&lt; data_t &gt;</h3>
<p>The <code>MemoryGrpBuf</code> class provides access to pieces of the global shared memory that have been obtained with <code>MemoryGrp</code>. </p>
<p> <code>MemoryGrpBuf</code> is a template class that is parameterized on data_t. All lengths and offsets of given in terms of sizeof(data_t).</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>template&lt;class data_t &gt; <code>sc::MemoryGrpBuf</code>&lt; data_t &gt;::<code>MemoryGrpBuf</code> (const <code>Ref</code>&lt; <code>MemoryGrp</code> &gt; &amp; grp) [inline]</h3>
<p>Creates a new <code>MemoryGrpBuf</code> given a <code>MemoryGrp</code> reference. This is a template class parameterized on data_t.</p>
<h2>Member Function Documentation</h2>
<h3>template&lt;class data_t &gt; const data_t * <code>sc::MemoryGrpBuf</code>&lt; data_t &gt;::readonly (<code>distsize_t</code> offset, int length) [inline]</h3>
<p>Request read only access to global memory at the global address offset and with size length. Writing to the specified region without an intervening sync of the <code>MemoryGrp</code> will have undefined results. </p>
<p> References sc::MemoryGrpBuf&lt; data_t &gt;::release().</p>
<h3>template&lt;class data_t &gt; data_t * <code>sc::MemoryGrpBuf</code>&lt; data_t &gt;::readwrite (<code>distsize_t</code> offset, int length) [inline]</h3>
<p>Request read write access to global memory at the global address offset and with size length. This will lock the memory it uses until release is called unless locking has been turned off in the <code>MemoryGrp</code> object. </p>
<p> References sc::MemoryGrpBuf&lt; data_t &gt;::release().</p>
<h3>template&lt;class data_t &gt; void <code>sc::MemoryGrpBuf</code>&lt; data_t &gt;::release () [inline]</h3>
<p>Release the access to the chunk of global memory that was obtained with writeonly, readwrite, readonly, writeonly_on_node, readwrite_on_node, and readonly_on_node. </p>
<p> Referenced by sc::MemoryGrpBuf&lt; data_t &gt;::readonly(), sc::MemoryGrpBuf&lt; data_t &gt;::readwrite(), and sc::MemoryGrpBuf&lt; data_t &gt;::writeonly().</p>
<h3>template&lt;class data_t &gt; data_t * <code>sc::MemoryGrpBuf</code>&lt; data_t &gt;::writeonly (<code>distsize_t</code> offset, int length) [inline]</h3>
<p>Request write only access to global memory at the global address offset and with size length. Writing the same bit of memory twice without an intervening sync of the <code>MemoryGrp</code> will have undefined results. </p>
<p> References sc::MemoryGrpBuf&lt; data_t &gt;::release(). </p>
<p> Referenced by sc::MemoryGrpBuf&lt; data_t &gt;::writeonly_on_node().</p>
<h3>template&lt;class data_t &gt; data_t * <code>sc::MemoryGrpBuf</code>&lt; data_t &gt;::writeonly_on_node (size_t offset, int length, int node = -1) [inline]</h3>
<p>These behave like writeonly, readwrite, and readonly, except the offset is local to the node specified by node. If node = -1, then the local node is used. </p>
<p> References sc::MemoryGrpBuf&lt; data_t &gt;::writeonly().</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
