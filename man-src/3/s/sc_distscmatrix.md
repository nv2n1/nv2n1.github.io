---
title: "sc_distscmatrix(3)"
name: "sc_distscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_distscmatrix/"
description: "sc::DistSCMatrix –"
---

<p>sc::DistSCMatrix &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>DistSCMatrix (const RefSCDimension &amp;, const RefSCDimension &amp;, DistSCMatrixKit *)



double get_element (int, int) const


Return or modify an element.


void set_element (int, int, double)



void accumulate_element (int, int, double)



SCMatrix * get_subblock (int, int, int, int)


Return a subblock of this.


void assign_subblock (SCMatrix *, int, int, int, int, int=0, int=0)



void accumulate_subblock (SCMatrix *, int, int, int, int, int=0, int=0)



SCVector * get_row (int i)


Return a row or column of this.


SCVector * get_column (int i)



void assign_row (SCVector *v, int i)


Assign v to a row or column of this.


void assign_column (SCVector *v, int i)



void accumulate_row (SCVector *v, int i)


Sum v to a row or column of this.


void accumulate_column (SCVector *v, int i)



void accumulate_outer_product (SCVector *, SCVector *)


Sum into this the products of various vectors or matrices.


void accumulate_product_rr (SCMatrix *, SCMatrix *)



void accumulate (const SCMatrix *)



void accumulate (const SymmSCMatrix *)



void accumulate (const DiagSCMatrix *)



void accumulate (const SCVector *)



void transpose_this ()


Transpose this.


double invert_this ()


Invert this.


double solve_this (SCVector *)



double determ_this ()


Return the determinant of this. this is overwritten.


double trace ()


Return the trace.


void gen_invert_this ()



void schmidt_orthog (SymmSCMatrix *, int)


Schmidt orthogonalize this.


int schmidt_orthog_tol (SymmSCMatrix *, double tol, double *res=0)


Schmidt orthogonalize this.


void element_op (const Ref&lt; SCElementOp &gt; &amp;)


Perform the element operation op on each element of this.


void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, SCMatrix *)



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, SCMatrix *, SCMatrix *)



void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10)



void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the local (rapidly accessible) blocks used in this matrix.


Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)


Returns iterators for the all blocks used in this matrix.


Ref&lt; DistSCMatrixKit &gt; skit ()



Protected Types</code></pre>
<p> enum <code>VecOp</code> { <code>CopyFromVec</code>, <code>CopyToVec</code>, <code>AccumFromVec</code>, <code>AccumToVec</code> } </p>
<p> enum <code>Form</code> { <code>Row</code>, <code>Col</code> }</p>
<h3>Protected Member Functions</h3>
<pre><code>void init_blocklist ()



void error (const char *)



double * find_element (int i, int j) const



int element_to_node (int i, int j) const



int block_to_node (int, int) const



Ref&lt; SCMatrixBlock &gt; block_to_block (int, int) const



Ref&lt; SCBlockInfo &gt; rowblocks () const



Ref&lt; SCBlockInfo &gt; colblocks () const



void create_vecform (Form, int nvec=-1)



void delete_vecform ()



void vecform_op (VecOp op, int *ivec=0)



void vecform_zero ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>SCMatrixBlockList</code> &gt; <code>blocklist</code> </p>
<p> int <code>vecoff</code> </p>
<p> int <code>nvec</code> </p>
<p> double ** <code>vec</code> </p>
<p> enum sc::DistSCMatrix::Form <code>form</code></p>
<h3>Friends</h3>
<p>class <code>DistSymmSCMatrix</code> </p>
<p> class <code>DistDiagSCMatrix</code> </p>
<p> class <code>DistSCVector</code></p>
<h2>Member Function Documentation</h2>
<h3><code>SCMatrix</code>* sc::DistSCMatrix::get_subblock (int br, int er, int bc, int ec) [virtual]</h3>
<p>Return a subblock of this. The subblock is defined as the rows starting at br and ending at er, and the columns beginning at bc and ending at ec. </p>
<p> Implements <code>sc::SCMatrix</code>.</p>
<h3><code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::DistSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implements <code>sc::SCMatrix</code>.</p>
<h3>void sc::DistSCMatrix::schmidt_orthog (<code>SymmSCMatrix</code> *, int n) [virtual]</h3>
<p>Schmidt orthogonalize this. S is the overlap matrix. n is the number of columns to orthogonalize. </p>
<p> Implements <code>sc::SCMatrix</code>.</p>
<h3>int sc::DistSCMatrix::schmidt_orthog_tol (<code>SymmSCMatrix</code> *, double tol, double * res = 0) [virtual]</h3>
<p>Schmidt orthogonalize this. S is the overlap matrix. tol is the tolerance. The number of linearly independent vectors is returned. </p>
<p> Implements <code>sc::SCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
