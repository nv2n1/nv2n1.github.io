---
title: "sc_blockeddiagscmatrix(3)"
name: "sc_blockeddiagscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_blockeddiagscmatrix/"
description: "sc::BlockedDiagSCMatrix –"
---

<p>sc::BlockedDiagSCMatrix &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DiagSCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>BlockedDiagSCMatrix (const RefSCDimension &amp;, BlockedSCMatrixKit *)



void save (StateOut &amp;)


Save and restore this in an implementation independent way.


void restore (StateIn &amp;)



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



RefSCDimension dim () const


Return the dimension.


RefSCDimension dim (int) const



int nblocks () const



RefDiagSCMatrix block (int)



Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the local (rapidly accessible) blocks used in this matrix.


Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the all blocks used in this matrix.



Friends</code></pre>
<p> class <code>BlockedSCMatrix</code> </p>
<p> class <code>BlockedSymmSCMatrix</code> </p>
<p> class <code>BlockedSCVector</code></p>
<h2>Member Function Documentation</h2>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::BlockedDiagSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implements <code>sc::DiagSCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
