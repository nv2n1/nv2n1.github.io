---
title: "sc_scmatrixblockiter(3)"
name: "sc_scmatrixblockiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrixblockiter/"
description: "sc::SCMatrixBlockIter –"
---

<p>sc::SCMatrixBlockIter &#8211; </p>
<p> The <code>SCMatrixBlockIter</code> class is used to described iterates that loop through the elements in a block.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;blkiter.h&gt;</code></pre>
<p> Inherited by <code>sc::SCMatrixDiagBlockIter</code>, <code>sc::SCMatrixDiagSubBlockIter</code>, <code>sc::SCMatrixLTriBlockIter</code>, <code>sc::SCMatrixLTriSubBlockIter</code>, <code>sc::SCMatrixRectBlockIter</code>, <code>sc::SCMatrixRectSubBlockIter</code>, <code>sc::SCVectorSimpleBlockIter</code>, and <code>sc::SCVectorSimpleSubBlockIter</code>.</p>
<h3>Public Member Functions</h3>
<p>virtual int <code>i</code> ()=0<br />
 <i>Returns the row index. </i><br />
 virtual int <code>j</code> ()=0<br />
 <i>Returns the column index. </i><br />
 virtual void <code>set</code> (double val)=0<br />
 <i>Set the current element to val. </i><br />
 virtual void <code>accum</code> (double val)<br />
 <i>Add val to the current element. </i><br />
 virtual double <code>get</code> ()=0<br />
 <i>Return the value of the current element. </i><br />
 virtual <code>operator int</code> ()=0<br />
 <i>Return nonzero if there are more elements. </i><br />
 virtual void <code>operator++</code> ()=0<br />
 <i>Move to the next element. </i><br />
 void <code>operator++</code> (int) </p>
<p> virtual void <code>reset</code> ()=0<br />
 <i>Start the iteration over. </i></p>
<h2>Detailed Description</h2>
<p>The <code>SCMatrixBlockIter</code> class is used to described iterates that loop through the elements in a block.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
