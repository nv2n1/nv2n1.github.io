---
title: "sc_distdiagscmatrix(3)"
name: "sc_distdiagscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distdiagscmatrix/"
description: "sc::DistDiagSCMatrix –"
---

<p>sc::DistDiagSCMatrix &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DiagSCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<p><code>DistDiagSCMatrix</code> (const <code>RefSCDimension</code> &amp;, <code>DistSCMatrixKit</code> *) </p>
<p> double <code>get_element</code> (int) const<br />
 <i>Return or modify an element. </i><br />
 void <code>set_element</code> (int, double) </p>
<p> void <code>accumulate_element</code> (int, double) </p>
<p> void <code>accumulate</code> (const <code>DiagSCMatrix</code> *) </p>
<p> double <code>invert_this</code> ()<br />
 <i>Invert this. </i><br />
 double <code>determ_this</code> ()<br />
 <i>Return the determinant of this. this is overwritten. </i><br />
 double <code>trace</code> ()<br />
 <i>Return the trace. </i><br />
 void <code>gen_invert_this</code> ()<br />
 <i>Do a generalized inversion of this. </i><br />
 void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp</code> &gt; &amp;)<br />
 <i>Perform the element operation op on each element of this. </i><br />
 void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp2</code> &gt; &amp;, <code>DiagSCMatrix</code> *) </p>
<p> void <code>element_op</code> (const <code>Ref</code>&lt; <code>SCElementOp3</code> &gt; &amp;, <code>DiagSCMatrix</code> *, <code>DiagSCMatrix</code> *) </p>
<p> <code>Ref</code>&lt; <code>SCMatrixSubblockIter</code> &gt; <code>local_blocks</code> (SCMatrixSubblockIter::Access)<br />
 <i>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </i><br />
 <code>Ref</code>&lt; <code>SCMatrixSubblockIter</code> &gt; <code>all_blocks</code> (SCMatrixSubblockIter::Access)<br />
 <i>Returns iterators for the all blocks used in this matrix. </i><br />
 <code>Ref</code>&lt; <code>DistSCMatrixKit</code> &gt; <code>skit</code> ()</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_blocklist ()



double * find_element (int i) const



int element_to_node (int i) const



int block_to_node (int) const



Ref&lt; SCMatrixBlock &gt; block_to_block (int) const



void error (const char *msg)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; <code>blocklist</code></p>
<h3>Friends</h3>
<p>class <code>DistSCMatrix</code> </p>
<p> class <code>DistSymmSCMatrix</code> </p>
<p> class <code>DistSCVector</code></p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::DistDiagSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implements <code>sc::DiagSCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
