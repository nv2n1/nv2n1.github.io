---
title: "sc_refscmatrix(3)"
name: "sc_refscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_refscmatrix/"
description: "sc::RefSCMatrix –"
---

<p>sc::RefSCMatrix &#8211; </p>
<p> The <code>RefSCMatrix</code> class is a smart pointer to an <code>SCMatrix</code> specialization.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;matrix.h&gt;</code></pre>
<p> Inherits <code>Ref&lt; SCMatrix &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RefSCMatrix ()


Initializes the matrix pointer to 0.


RefSCMatrix (const RefSCMatrix &amp;m)


Make this and m refer to the same SCMatrix.


RefSCMatrix (SCMatrix *m)


Make this refer to m.


RefSCMatrix &amp; operator= (SCMatrix *m)


Make this refer to m.


RefSCMatrix &amp; operator= (const RefSCMatrix &amp;m)


Make this and m refer to the same matrix.


RefSCMatrix (const RefSCDimension &amp;d1, const RefSCDimension &amp;d2, const Ref&lt; SCMatrixKit &gt; &amp;)


Create a vector with dimension d1 by d2.


RefSCVector operator* (const RefSCVector &amp;) const


Multiply this by a vector and return a vector.


RefSCMatrix operator* (const RefSCMatrix &amp;) const


Multiply this by a matrix and return a matrix.


RefSCMatrix operator* (const RefSymmSCMatrix &amp;) const



RefSCMatrix operator* (const RefDiagSCMatrix &amp;) const



RefSCMatrix operator* (double) const


Multiply this by a scalar and return the result.


RefSCMatrix operator+ (const RefSCMatrix &amp;) const


Matrix addition.


RefSCMatrix operator- (const RefSCMatrix &amp;) const


Matrix subtraction.


RefSCMatrix t () const


Return the transpose of this.


RefSCMatrix i () const


Return the inverse of this.


RefSCMatrix gi () const


Return the generalized inverse of this.


RefSCMatrix clone () const


These call the SCMatrix members of the same name after checking for references to 0.


RefSCMatrix copy () const



RefSCMatrix get_subblock (int br, int er, int bc, int ec)



void assign_subblock (const RefSCMatrix &amp;, int br, int er, int bc, int ec, int source_br=0, int source_bc=0)



void accumulate_subblock (const RefSCMatrix &amp;, int, int, int, int, int source_br=0, int source_bc=0)



RefSCVector get_row (int) const



RefSCVector get_column (int) const



void assign_row (const RefSCVector &amp;, int) const



void assign_column (const RefSCVector &amp;, int) const



void accumulate_row (const RefSCVector &amp;, int) const



void accumulate_column (const RefSCVector &amp;, int) const



void accumulate_outer_product (const RefSCVector &amp;, const RefSCVector &amp;) const



void accumulate_product (const RefSCMatrix &amp;, const RefSCMatrix &amp;) const



void assign (const RefSCMatrix &amp;) const



void scale (double) const



void randomize () const



void assign (double) const



void assign (const double *) const



void assign (const double **) const



void convert (double *) const



void convert (double **) const



void accumulate (const RefSCMatrix &amp;) const



void accumulate (const RefSymmSCMatrix &amp;) const



void accumulate (const RefDiagSCMatrix &amp;) const



void element_op (const Ref&lt; SCElementOp &gt; &amp;) const



void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, const RefSCMatrix &amp;) const



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, const RefSCMatrix &amp;, const RefSCMatrix &amp;) const



int nrow () const



int ncol () const



RefSCDimension rowdim () const



RefSCDimension coldim () const



Ref&lt; SCMatrixKit &gt; kit () const



void set_element (int, int, double) const



void accumulate_element (int, int, double) const



double get_element (int, int) const



void print (std::ostream &amp;) const



void print (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



double trace () const



void save (StateOut &amp;)



void restore (StateIn &amp;)


Restores the matrix from StateIn object. The matrix must have been initialized already.


void svd (const RefSCMatrix &amp;U, const RefDiagSCMatrix &amp;sigma, const RefSCMatrix &amp;V)


Compute the singular value decomposition, this = U sigma V.t().


double solve_lin (const RefSCVector &amp;v) const


Solves this x = v.


double determ () const


Returns the determinant of the referenced matrix.


SCMatrixdouble operator() (int i, int j) const


Assign and examine matrix elements.


int nblock () const


If this matrix is blocked return the number of blocks.


RefSCMatrix block (int i) const


If this matrix is blocked return block i.</code></pre>
<h2>Detailed Description</h2>
<p>The <code>RefSCMatrix</code> class is a smart pointer to an <code>SCMatrix</code> specialization.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::RefSCMatrix::RefSCMatrix ()</h3>
<p>Initializes the matrix pointer to 0. The reference must be initialized before it is used.</p>
<h3>sc::RefSCMatrix::RefSCMatrix (const <code>RefSCDimension</code> &amp; d1, const <code>RefSCDimension</code> &amp; d2, const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;)</h3>
<p>Create a vector with dimension d1 by d2. The data values are undefined.</p>
<h2>Member Function Documentation</h2>
<h3><code>RefSCMatrix</code> sc::RefSCMatrix::block (int i) const</h3>
<p>If this matrix is blocked return block i. Otherwise return this as block 0.</p>
<h3><code>RefSCMatrix</code> sc::RefSCMatrix::clone () const</h3>
<p>These call the <code>SCMatrix</code> members of the same name after checking for references to 0.</p>
<h3>int sc::RefSCMatrix::nblock () const</h3>
<p>If this matrix is blocked return the number of blocks. Otherwise return 1.</p>
<h3>double sc::RefSCMatrix::solve_lin (const <code>RefSCVector</code> &amp; v) const</h3>
<p>Solves this x = v. Overwrites v with x.</p>
<h3>void sc::RefSCMatrix::svd (const <code>RefSCMatrix</code> &amp; U, const <code>RefDiagSCMatrix</code> &amp; sigma, const <code>RefSCMatrix</code> &amp; V)</h3>
<p><code>Compute</code> the singular value decomposition, this = U sigma V.t(). The dimension of sigma is the smallest dimension of this. U, V, and sigma must already have the correct dimensions and are overwritten.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
