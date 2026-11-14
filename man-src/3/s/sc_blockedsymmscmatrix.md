---
title: "sc_blockedsymmscmatrix(3)"
name: "sc_blockedsymmscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_blockedsymmscmatrix/"
description: "sc::BlockedSymmSCMatrix –"
---

<p>sc::BlockedSymmSCMatrix &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SymmSCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>BlockedSymmSCMatrix (const RefSCDimension &amp;, BlockedSCMatrixKit *)



void save (StateOut &amp;)


Save and restore this in an implementation independent way.


void restore (StateIn &amp;)



double get_element (int, int) const


Return or modify an element.


void set_element (int, int, double)



void accumulate_element (int, int, double)



void scale (double)


Multiply all elements by val.


void assign_val (double)


Overridden to implement the assign functions.


void assign_s (SymmSCMatrix *m)



SCMatrix * get_subblock (int, int, int, int)


Return a subblock of this.


SymmSCMatrix * get_subblock (int, int)



void assign_subblock (SCMatrix *, int, int, int, int)


Assign m to a subblock of this.


void assign_subblock (SymmSCMatrix *, int, int)



void accumulate_subblock (SCMatrix *, int, int, int, int)


Sum m into a subblock of this.


void accumulate_subblock (SymmSCMatrix *, int, int)



SCVector * get_row (int i)


Return a row of this.


void assign_row (SCVector *v, int i)


Assign v to a row of this.


void accumulate_row (SCVector *v, int i)


Sum v to a row of this.


double invert_this ()


Invert this.


double determ_this ()


Return the determinant of this. this is overwritten.


double trace ()


Return the trace.


double solve_this (SCVector *)



void gen_invert_this ()



double scalar_product (SCVector *)


Return the scalar obtained by multiplying this on the left and right by v.


void diagonalize (DiagSCMatrix *, SCMatrix *)


Diagonalize this, placing the eigenvalues in d and the eigenvectors in m.


void accumulate (const SymmSCMatrix *)



void accumulate_symmetric_outer_product (SCVector *)



void accumulate_symmetric_product (SCMatrix *)



void accumulate_symmetric_sum (SCMatrix *)


Sum into this the products of various vectors or matrices.


void accumulate_transform (SCMatrix *, SymmSCMatrix *, SCMatrix::Transform=SCMatrix::NormalTransform)



void accumulate_transform (SCMatrix *, DiagSCMatrix *, SCMatrix::Transform=SCMatrix::NormalTransform)



void accumulate_transform (SymmSCMatrix *, SymmSCMatrix *)



void convert_accumulate (SymmSCMatrix *a)



void element_op (const Ref&lt; SCElementOp &gt; &amp;)


Perform the element operation op on each element of this.


void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, SymmSCMatrix *)



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, SymmSCMatrix *, SymmSCMatrix *)



void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



RefSCDimension dim () const


Return the dimension.


RefSCDimension dim (int) const



int nblocks () const



RefSymmSCMatrix block (int)



Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the local (rapidly accessible) blocks used in this matrix.


Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the all blocks used in this matrix.



Friends</code></pre>
<p> class <code>BlockedSCMatrix</code> </p>
<p> class <code>BlockedDiagSCMatrix</code> </p>
<p> class <code>BlockedSCVector</code></p>
<h2>Member Function Documentation</h2>
<h3>void sc::BlockedSymmSCMatrix::diagonalize (<code>DiagSCMatrix</code> * d, <code>SCMatrix</code> * m) [virtual]</h3>
<p>Diagonalize this, placing the eigenvalues in d and the eigenvectors in m. </p>
<p> Implements <code>sc::SymmSCMatrix</code>.</p>
<h3><code>SCMatrix</code>* sc::BlockedSymmSCMatrix::get_subblock (int br, int er, int bc, int ec) [virtual]</h3>
<p>Return a subblock of this. The subblock is defined as the rows starting at br and ending at er, and the columns beginning at bc and ending at ec. </p>
<p> Implements <code>sc::SymmSCMatrix</code>.</p>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::BlockedSymmSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implements <code>sc::SymmSCMatrix</code>.</p>
<h3>double sc::BlockedSymmSCMatrix::scalar_product (<code>SCVector</code> * v) [virtual]</h3>
<p>Return the scalar obtained by multiplying this on the left and right by v. </p>
<p> Reimplemented from <code>sc::SymmSCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
