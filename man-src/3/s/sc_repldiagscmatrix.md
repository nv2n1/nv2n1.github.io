---
title: "sc_repldiagscmatrix(3)"
name: "sc_repldiagscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_repldiagscmatrix/"
description: "sc::ReplDiagSCMatrix –"
---

<p>sc::ReplDiagSCMatrix &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DiagSCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>ReplDiagSCMatrix (const RefSCDimension &amp;, ReplSCMatrixKit *)



void assign_val (double)


Overridden to implement the assign members.


double get_element (int) const


Return or modify an element.


void set_element (int, double)



void accumulate_element (int, double)



void accumulate (const DiagSCMatrix *)



double invert_this ()


Invert this.


double determ_this ()


Return the determinant of this. this is overwritten.


double trace ()


Return the trace.


void gen_invert_this ()


Do a generalized inversion of this.


void element_op (const Ref&lt; SCElementOp &gt; &amp;)


Perform the element operation op on each element of this.


void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, DiagSCMatrix *)



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, DiagSCMatrix *, DiagSCMatrix *)



void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



double * get_data ()



Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the local (rapidly accessible) blocks used in this matrix.


Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the all blocks used in this matrix.


Ref&lt; ReplSCMatrixKit &gt; skit ()



Protected Member Functions
void init_blocklist ()



void before_elemop ()



void after_elemop ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; <code>blocklist</code> </p>
<p> double * <code>matrix</code></p>
<h3>Friends</h3>
<p>class <code>ReplSCMatrix</code> </p>
<p> class <code>ReplSymmSCMatrix</code> </p>
<p> class <code>ReplSCVector</code></p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::ReplDiagSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implements <code>sc::DiagSCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
