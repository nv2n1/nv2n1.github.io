---
title: "sc_symmscmatrix(3)"
name: "sc_symmscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_symmscmatrix/"
description: "sc::SymmSCMatrix –"
---

<p>sc::SymmSCMatrix &#8211; </p>
<p> The <code>SymmSCMatrix</code> class is the abstract base class for symmetric double valued matrices.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;abstract.h&gt;</code></pre>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::BlockedSymmSCMatrix</code>, <code>sc::DistSymmSCMatrix</code>, <code>sc::LocalSymmSCMatrix</code>, and <code>sc::ReplSymmSCMatrix</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SymmSCMatrix (const RefSCDimension &amp;, SCMatrixKit *)



Ref&lt; SCMatrixKit &gt; kit () const


Return the SCMatrixKit object that created this object.


virtual void save (StateOut &amp;)


Save and restore this in an implementation independent way.


virtual void restore (StateIn &amp;)



virtual double maxabs () const


Return the maximum absolute value element of this vector.


virtual void randomize ()


Assign each element to a random number between -1 and 1.


void assign (double val)


Set all elements to val.


void assign (const double *m)


Assign element i, j to m[i*(i+1)/2+j].


void assign (const double **m)


Assign element i, j to m[i][j].


void assign (SymmSCMatrix *m)


Make this have the same elements as m.


virtual void assign_val (double val)


Overridden to implement the assign functions.


virtual void assign_p (const double *m)



virtual void assign_pp (const double **m)



virtual void assign_s (SymmSCMatrix *m)



virtual void convert (double *) const


Like the assign members, but these write values to the arguments.


virtual void convert (double **) const



virtual void convert (SymmSCMatrix *)


Convert an SCSymmSCMatrix of a different specialization to this specialization and possibly accumulate the data.


virtual void convert_accumulate (SymmSCMatrix *)



virtual void scale (double)


Multiply all elements by val.


virtual void scale_diagonal (double)


Scale the diagonal elements by val.


virtual void shift_diagonal (double)


Shift the diagonal elements by val.


virtual void unit ()


Make this equal to the unit matrix.


int n () const


Return the dimension.


virtual SymmSCMatrix * copy ()


Return a matrix with the same dimension and same elements.


virtual SymmSCMatrix * clone ()


Return a matrix with the same dimension but uninitialized memory.


RefSCDimension dim () const


Return the dimension.


virtual double get_element (int, int) const =0


Return or modify an element.


virtual void set_element (int, int, double)=0



virtual void accumulate_element (int, int, double)=0



virtual SCMatrix * get_subblock (int br, int er, int bc, int ec)=0


Return a subblock of this.


virtual SymmSCMatrix * get_subblock (int br, int er)=0



virtual void assign_subblock (SCMatrix *m, int, int, int, int)=0


Assign m to a subblock of this.


virtual void assign_subblock (SymmSCMatrix *m, int, int)=0



virtual void accumulate_subblock (SCMatrix *m, int, int, int, int)=0


Sum m into a subblock of this.


virtual void accumulate_subblock (SymmSCMatrix *m, int, int)=0



virtual SCVector * get_row (int i)=0


Return a row of this.


virtual void assign_row (SCVector *v, int i)=0


Assign v to a row of this.


virtual void accumulate_row (SCVector *v, int i)=0


Sum v to a row of this.


virtual void diagonalize (DiagSCMatrix *d, SCMatrix *m)=0


Diagonalize this, placing the eigenvalues in d and the eigenvectors in m.


virtual void accumulate (const SymmSCMatrix *m)=0


Sum m into this.


virtual void accumulate_symmetric_sum (SCMatrix *)=0


Sum into this the products of various vectors or matrices.


virtual void accumulate_symmetric_product (SCMatrix *)



virtual void accumulate_transform (SCMatrix *, SymmSCMatrix *, SCMatrix::Transform=SCMatrix::NormalTransform)



virtual void accumulate_transform (SCMatrix *, DiagSCMatrix *, SCMatrix::Transform=SCMatrix::NormalTransform)



virtual void accumulate_transform (SymmSCMatrix *, SymmSCMatrix *)



virtual void accumulate_symmetric_outer_product (SCVector *)



virtual double scalar_product (SCVector *v)


Return the scalar obtained by multiplying this on the left and right by v.


virtual double trace ()=0


Return the trace.


virtual double invert_this ()=0


Invert this.


virtual double determ_this ()=0


Return the determinant of this. this is overwritten.


virtual double solve_this (SCVector *)=0



virtual void gen_invert_this ()=0



virtual void element_op (const Ref&lt; SCElementOp &gt; &amp;)=0


Perform the element operation op on each element of this.


virtual void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, SymmSCMatrix *)=0



virtual void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, SymmSCMatrix *, SymmSCMatrix *)=0



void print (std::ostream &amp;o=ExEnv::out0()) const


Print out the matrix.


void print (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



virtual void vprint (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



Ref&lt; MessageGrp &gt; messagegrp () const


Returns the message group used by the matrix kit.


virtual Ref&lt; SCMatrixSubblockIter &gt; local_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the local (rapidly accessible) blocks used in this matrix.


virtual Ref&lt; SCMatrixSubblockIter &gt; all_blocks (SCMatrixSubblockIter::Access)=0


Returns iterators for the all blocks used in this matrix.



Protected Attributes</code></pre>
<p> <code>RefSCDimension</code> <code>d</code> </p>
<p> <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; <code>kit_</code></p>
<h2>Detailed Description</h2>
<p>The <code>SymmSCMatrix</code> class is the abstract base class for symmetric double valued matrices.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::SymmSCMatrix::assign (<code>SymmSCMatrix</code> * m) [inline]</h3>
<p>Make this have the same elements as m. The dimensions must match.</p>
<h3>void sc::SymmSCMatrix::assign (const double * m) [inline]</h3>
<p>Assign element i, j to m[i*(i+1)/2+j].</p>
<h3>virtual void sc::SymmSCMatrix::convert (<code>SymmSCMatrix</code> *) [virtual]</h3>
<p>Convert an SCSymmSCMatrix of a different specialization to this specialization and possibly accumulate the data.</p>
<h3>virtual void sc::SymmSCMatrix::diagonalize (<code>DiagSCMatrix</code> * d, <code>SCMatrix</code> * m) [pure virtual]</h3>
<p>Diagonalize this, placing the eigenvalues in d and the eigenvectors in m. </p>
<p> Implemented in <code>sc::BlockedSymmSCMatrix</code>, <code>sc::DistSymmSCMatrix</code>, <code>sc::LocalSymmSCMatrix</code>, and <code>sc::ReplSymmSCMatrix</code>.</p>
<h3>virtual <code>SCMatrix</code>* sc::SymmSCMatrix::get_subblock (int br, int er, int bc, int ec) [pure virtual]</h3>
<p>Return a subblock of this. The subblock is defined as the rows starting at br and ending at er, and the columns beginning at bc and ending at ec. </p>
<p> Implemented in <code>sc::BlockedSymmSCMatrix</code>, <code>sc::DistSymmSCMatrix</code>, <code>sc::LocalSymmSCMatrix</code>, and <code>sc::ReplSymmSCMatrix</code>.</p>
<h3>virtual <code>Ref</code>&lt;<code>SCMatrixSubblockIter</code>&gt; sc::SymmSCMatrix::local_blocks (SCMatrixSubblockIter::Access) [pure virtual]</h3>
<p>Returns iterators for the local (rapidly accessible) blocks used in this matrix. </p>
<p> Implemented in <code>sc::BlockedSymmSCMatrix</code>, <code>sc::DistSymmSCMatrix</code>, <code>sc::LocalSymmSCMatrix</code>, and <code>sc::ReplSymmSCMatrix</code>.</p>
<h3>virtual double sc::SymmSCMatrix::scalar_product (<code>SCVector</code> * v) [virtual]</h3>
<p>Return the scalar obtained by multiplying this on the left and right by v. </p>
<p> Reimplemented in <code>sc::BlockedSymmSCMatrix</code>, <code>sc::LocalSymmSCMatrix</code>, and <code>sc::ReplSymmSCMatrix</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
