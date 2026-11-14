---
title: "sc_scmatrix(3)"
name: "sc_scmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_scmatrix/"
description: "sc::SCMatrix –"
---

<p>sc::SCMatrix &#8211; </p>
<p> The <code>SCMatrix</code> class is the abstract base class for general double valued n by m matrices.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;abstract.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::BlockedSCMatrix</code>, <code>sc::DistSCMatrix</code>, <code>sc::LocalSCMatrix</code>, and <code>sc::ReplSCMatrix</code>.</p>
<h3>Public Types</h3>
<pre><code>enum Transform { NormalTransform =  0, TransposeTransform =  1 }



Public Member Functions
SCMatrix (const RefSCDimension &amp;, const RefSCDimension &amp;, SCMatrixKit *)



virtual void save (StateOut &amp;)


Save and restore this in an implementation independent way.


virtual void restore (StateIn &amp;)



Ref&lt; SCMatrixKit &gt; kit () const


Return the SCMatrixKit used to create this object.


int nrow () const


Return the number of rows.


int ncol () const


Return the number of columns.


virtual double maxabs () const


Return the maximum absolute value element.


virtual void randomize ()


Assign each element to a random number between -1 and 1.


void assign (double val)


Set all elements to val.


void assign (const double *m)


Assign element i, j to m[ir*nrow()+j].


void assign (const double **m)


Assign element i, j to m[i][j].


void assign (SCMatrix *m)


Make this have the same elements as m. The dimensions must match.


virtual void assign_val (double val)


Overridden to implement to assign members.


virtual void assign_p (const double *m)



virtual void assign_pp (const double **m)



virtual void assign_r (SCMatrix *m)



virtual void convert (double *) const


Like the assign members, but these write values to the arguments.


virtual void convert (double **) const



virtual void convert (SCMatrix *)


Convert an SCMatrix of a different specialization to this specialization and possibly accumulate the data.


virtual void convert_accumulate (SCMatrix *)



virtual void scale (double val)


Multiply all elements by val.


virtual void scale_diagonal (double val)


Scale the diagonal elements by val.


virtual void shift_diagonal (double val)


Shift the diagonal elements by val.


virtual void unit ()


Make this equal to the unit matrix.


virtual SCMatrix * copy ()


Return a matrix with the same dimension and same elements.


virtual SCMatrix * clone ()


Return a matrix with the same dimension but uninitialized memory.


RefSCDimension rowdim () const


Return the row or column dimension.


RefSCDimension coldim () const



virtual double get_element (int, int) const =0


Return or modify an element.


virtual void set_element (int, int, double)=0



virtual void accumulate_element (int, int, double)=0



virtual SCMatrix * get_subblock (int br, int er, int bc, int ec)=0


Return a subblock of this.


virtual void assign_subblock (SCMatrix *m, int, int, int, int, int=0, int=0)=0


Assign m to a subblock of this.


virtual void accumulate_subblock (SCMatrix *m, int, int, int, int, int=0, int=0)=0


Sum m into a subblock of this.


virtual SCVector * get_row (int i)=0


Return a row or column of this.


virtual SCVector * get_column (int i)=0



virtual void assign_row (SCVector *v, int i)=0


Assign v to a row or column of this.


virtual void assign_column (SCVector *v, int i)=0



virtual void accumulate_row (SCVector *v, int i)=0


Sum v to a row or column of this.


virtual void accumulate_column (SCVector *v, int i)=0



virtual void accumulate (const SCMatrix *m)=0


Sum m into this.


virtual void accumulate (const SymmSCMatrix *m)=0



virtual void accumulate (const DiagSCMatrix *m)=0



virtual void accumulate (const SCVector *)=0



virtual void accumulate_outer_product (SCVector *, SCVector *)=0


Sum into this the products of various vectors or matrices.


void accumulate_product (SCMatrix *m1, SCMatrix *m2)



void accumulate_product (SCMatrix *m1, SymmSCMatrix *m2)



void accumulate_product (SCMatrix *m1, DiagSCMatrix *m2)



void accumulate_product (SymmSCMatrix *m1, SCMatrix *m2)



void accumulate_product (DiagSCMatrix *m1, SCMatrix *m2)



void accumulate_product (SymmSCMatrix *m1, SymmSCMatrix *m2)



virtual void accumulate_product_rr (SCMatrix *, SCMatrix *)=0



virtual void accumulate_product_rs (SCMatrix *, SymmSCMatrix *)



virtual void accumulate_product_rd (SCMatrix *, DiagSCMatrix *)



virtual void accumulate_product_sr (SymmSCMatrix *, SCMatrix *)



virtual void accumulate_product_dr (DiagSCMatrix *, SCMatrix *)



virtual void accumulate_product_ss (SymmSCMatrix *, SymmSCMatrix *)



virtual void transpose_this ()=0


Transpose this.


virtual double trace ()=0


Return the trace.


virtual double invert_this ()=0


Invert this.


virtual double determ_this ()=0


Return the determinant of this. this is overwritten.


virtual void svd_this (SCMatrix *U, DiagSCMatrix *sigma, SCMatrix *V)


Compute the singular value decomposition for this, possibly destroying this.


virtual double solve_this (SCVector *)=0



virtual void gen_invert_this ()



virtual void schmidt_orthog (SymmSCMatrix *, int n)=0


Schmidt orthogonalize this.


virtual int schmidt_orthog_tol (SymmSCMatrix *, double tol, double *res=0)=0


Schmidt orthogonalize this.


virtual void element_op (const Ref&lt; SCElementOp &gt; &amp;)=0


Perform the element operation op on each element of this.


virtual void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, SCMatrix *)=0



virtual void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, SCMatrix *, SCMatrix *)=0



void print (std::ostream &amp;o=ExEnv::out0()) const


Print out the matrix.


void print (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



virtual void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const =0



Ref&lt; MessageGrp &gt; messagegrp () const


Returns the message group used by the matrix kit.


virtual Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the local (rapidly accessible) blocks used in this matrix.


virtual Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the all blocks used in this matrix.



Protected Attributes</code></pre>
<p> <code>RefSCDimension</code> <code>d1</code> </p>
<p> <code>RefSCDimension</code> <code>d2</code> </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>kit_</code></p>
<h2>Detailed Description</h2>
<p>The <code>SCMatrix</code> class is the abstract base class for general double valued n by m matrices. </p>
<p> For symmetric matrices use <code>SymmSCMatrix</code> and for diagonal matrices use <code>DiagSCMatrix</code>.</p>
<h2>Member Function Documentation</h2>
<h3>virtual void sc::SCMatrix::convert (<code>SCMatrix</code> *) [virtual]</h3>
<p>Convert an <code>SCMatrix</code> of a different specialization to this specialization and possibly accumulate the data.</p>
<h3>virtual void sc::SCMatrix::convert (double *) const [virtual]</h3>
<p>Like the assign members, but these write values to the arguments.</p>
<h3>virtual <code>SCMatrix</code>* sc::SCMatrix::get_subblock (int br, int er, int bc, int ec) [pure virtual]</h3>
<p>Return a subblock of this. The subblock is defined as the rows starting at br and ending at er, and the columns beginning at bc and ending at ec. </p>
<p> Implemented in <code>sc::BlockedSCMatrix</code>, <code>sc::DistSCMatrix</code>, <code>sc::LocalSCMatrix</code>, and <code>sc::ReplSCMatrix</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::SCMatrix::local_blocks (SCMatrixSubblockIter::Access) [pure virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implemented in <code>sc::BlockedSCMatrix</code>, <code>sc::DistSCMatrix</code>, <code>sc::LocalSCMatrix</code>, and <code>sc::ReplSCMatrix</code>.</p>
<h3>virtual void sc::SCMatrix::schmidt_orthog (<code>SymmSCMatrix</code> *, int n) [pure virtual]</h3>
<p>Schmidt orthogonalize this. S is the overlap matrix. n is the number of columns to orthogonalize. </p>
<p> Implemented in <code>sc::BlockedSCMatrix</code>, <code>sc::DistSCMatrix</code>, <code>sc::LocalSCMatrix</code>, and <code>sc::ReplSCMatrix</code>.</p>
<h3>virtual int sc::SCMatrix::schmidt_orthog_tol (<code>SymmSCMatrix</code> *, double tol, double * res = 0) [pure virtual]</h3>
<p>Schmidt orthogonalize this. S is the overlap matrix. tol is the tolerance. The number of linearly independent vectors is returned. </p>
<p> Implemented in <code>sc::BlockedSCMatrix</code>, <code>sc::DistSCMatrix</code>, <code>sc::LocalSCMatrix</code>, and <code>sc::ReplSCMatrix</code>.</p>
<h3>virtual void sc::SCMatrix::svd_this (<code>SCMatrix</code> * U, <code>DiagSCMatrix</code> * sigma, <code>SCMatrix</code> * V) [virtual]</h3>
<p><code>Compute</code> the singular value decomposition for this, possibly destroying this.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
