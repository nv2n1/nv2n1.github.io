---
title: "sc_refsymmscmatrix(3)"
name: "sc_refsymmscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_refsymmscmatrix/"
description: "sc::RefSymmSCMatrix –"
---

<p>sc::RefSymmSCMatrix &#8211; </p>
<p> The <code>RefSymmSCMatrix</code> class is a smart pointer to an SCSymmSCMatrix specialization.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;matrix.h&gt;</code></pre>
<p> Inherits <code>Ref&lt; SymmSCMatrix &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RefSymmSCMatrix ()


Initializes the matrix pointer to 0.


RefSymmSCMatrix (const RefSymmSCMatrix &amp;m)


Make this and m refer to the same SCMatrix.


RefSymmSCMatrix (SymmSCMatrix *m)


Make this refer to m.


RefSymmSCMatrix &amp; operator= (SymmSCMatrix *m)


Make this refer to m.


RefSymmSCMatrix &amp; operator= (const RefSymmSCMatrix &amp;m)


Make this and m refer to the same matrix.


RefSymmSCMatrix (const RefSCDimension &amp;d, const Ref&lt; SCMatrixKit &gt; &amp;)


Create a vector with dimension d by d.


RefSCMatrix operator* (const RefSCMatrix &amp;) const


Multiply this by a matrix and return a matrix.


RefSCMatrix operator* (const RefSymmSCMatrix &amp;) const



RefSCVector operator* (const RefSCVector &amp;a) const


Multiply this by a vector and return a vector.


RefSymmSCMatrix operator* (double) const



RefSymmSCMatrix operator+ (const RefSymmSCMatrix &amp;) const


Matrix addition and subtraction.


RefSymmSCMatrix operator- (const RefSymmSCMatrix &amp;) const



RefSymmSCMatrix i () const


Return the inverse of this.


RefSymmSCMatrix gi () const


Return the generalized inverse of this.


RefSymmSCMatrix clone () const


These call the SCMatrix members of the same name after checking for references to 0.


RefSymmSCMatrix copy () const



void set_element (int, int, double) const



void accumulate_element (int, int, double) const



double get_element (int, int) const



RefSCMatrix get_subblock (int br, int er, int bc, int ec)



RefSymmSCMatrix get_subblock (int br, int er)



void assign_subblock (const RefSCMatrix &amp;, int br, int er, int bc, int ec)



void assign_subblock (const RefSymmSCMatrix &amp;, int br, int er)



void accumulate_subblock (const RefSCMatrix &amp;, int, int, int, int)



void accumulate_subblock (const RefSymmSCMatrix &amp;, int, int)



RefSCVector get_row (int)



void assign_row (const RefSCVector &amp;, int)



void accumulate_row (const RefSCVector &amp;, int)



void accumulate_symmetric_outer_product (const RefSCVector &amp;) const



double scalar_product (const RefSCVector &amp;) const



void accumulate_symmetric_product (const RefSCMatrix &amp;) const



void accumulate_symmetric_sum (const RefSCMatrix &amp;) const



void accumulate_transform (const RefSCMatrix &amp;a, const RefSymmSCMatrix &amp;b, SCMatrix::Transform=SCMatrix::NormalTransform) const


Add a * b * a.t() to this.


void accumulate_transform (const RefSCMatrix &amp;a, const RefDiagSCMatrix &amp;b, SCMatrix::Transform=SCMatrix::NormalTransform) const



void accumulate_transform (const RefSymmSCMatrix &amp;a, const RefSymmSCMatrix &amp;b) const



void randomize () const



void assign (const RefSymmSCMatrix &amp;) const



void scale (double) const



void assign (double) const



void assign (const double *) const



void assign (const double **) const



void convert (double *) const



void convert (double **) const



void accumulate (const RefSymmSCMatrix &amp;) const



void element_op (const Ref&lt; SCElementOp &gt; &amp;) const



void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, const RefSymmSCMatrix &amp;) const



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, const RefSymmSCMatrix &amp;, const RefSymmSCMatrix &amp;) const



double trace () const



int n () const



RefSCDimension dim () const



Ref&lt; SCMatrixKit &gt; kit () const



void print (std::ostream &amp;) const



void print (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



void save (StateOut &amp;)



void restore (StateIn &amp;)


Restores the matrix from StateIn object. The matrix must have been initialized already.


double solve_lin (const RefSCVector &amp;) const


Solves this x = v.


double determ () const


Returns the determinant of the referenced matrix.


RefDiagSCMatrix eigvals () const


Returns the eigenvalues of the reference matrix.


RefSCMatrix eigvecs () const


Returns the eigenvectors of the reference matrix.


void diagonalize (const RefDiagSCMatrix &amp;eigvals, const RefSCMatrix &amp;eigvecs) const


Sets eigvals to the eigenvalues and eigvecs to the eigenvalues and eigenvectors of the referenced matrix.


SymmSCMatrixdouble operator() (int i, int j) const


Assign and examine matrix elements.


int nblock () const


If this matrix is blocked return the number of blocks.


RefSymmSCMatrix block (int i) const


If this matrix is blocked return block i.</code></pre>
<h2>Detailed Description</h2>
<p>The <code>RefSymmSCMatrix</code> class is a smart pointer to an SCSymmSCMatrix specialization.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::RefSymmSCMatrix::RefSymmSCMatrix ()</h3>
<p>Initializes the matrix pointer to 0. The reference must be initialized before it is used.</p>
<h3>sc::RefSymmSCMatrix::RefSymmSCMatrix (const <code>RefSCDimension</code> &amp; d, const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;)</h3>
<p>Create a vector with dimension d by d. The data values are undefined.</p>
<h2>Member Function Documentation</h2>
<h3><code>RefSymmSCMatrix</code> sc::RefSymmSCMatrix::block (int i) const</h3>
<p>If this matrix is blocked return block i. Otherwise return this as block 0.</p>
<h3><code>RefSymmSCMatrix</code> sc::RefSymmSCMatrix::clone () const</h3>
<p>These call the <code>SCMatrix</code> members of the same name after checking for references to 0.</p>
<h3>void sc::RefSymmSCMatrix::diagonalize (const <code>RefDiagSCMatrix</code> &amp; eigvals, const <code>RefSCMatrix</code> &amp; eigvecs) const</h3>
<p>Sets eigvals to the eigenvalues and eigvecs to the eigenvalues and eigenvectors of the referenced matrix. The result satisfies eigvecs * eigvals * eigvecs.t() = (*this).</p>
<h3>int sc::RefSymmSCMatrix::nblock () const</h3>
<p>If this matrix is blocked return the number of blocks. Otherwise return 1.</p>
<h3>double sc::RefSymmSCMatrix::solve_lin (const <code>RefSCVector</code> &amp;) const</h3>
<p>Solves this x = v. Overwrites v with x.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
