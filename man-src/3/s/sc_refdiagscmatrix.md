---
title: "sc_refdiagscmatrix(3)"
name: "sc_refdiagscmatrix"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_refdiagscmatrix/"
description: "sc::RefDiagSCMatrix –"
---

<p>sc::RefDiagSCMatrix &#8211; </p>
<p> The <code>RefDiagSCMatrix</code> class is a smart pointer to an <code>DiagSCMatrix</code> specialization.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;matrix.h&gt;</code></pre>
<p> Inherits <code>Ref&lt; DiagSCMatrix &gt;</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RefDiagSCMatrix ()


Initializes the matrix pointer to 0.


RefDiagSCMatrix (const RefDiagSCMatrix &amp;m)


Make this and m refer to the same SCMatrix.


RefDiagSCMatrix (DiagSCMatrix *m)


Make this refer to m.


RefDiagSCMatrix &amp; operator= (DiagSCMatrix *m)


Make this refer to m.


RefDiagSCMatrix &amp; operator= (const RefDiagSCMatrix &amp;m)


Make this and m refer to the same matrix.


RefDiagSCMatrix (const RefSCDimension &amp;, const Ref&lt; SCMatrixKit &gt; &amp;)


Create a diagonal matrix with dimension d by d.


RefSCMatrix operator* (const RefSCMatrix &amp;) const


Multiply this by a matrix and return a matrix.


RefDiagSCMatrix operator* (double) const



RefDiagSCMatrix operator+ (const RefDiagSCMatrix &amp;) const


Matrix addition and subtraction.


RefDiagSCMatrix operator- (const RefDiagSCMatrix &amp;) const



RefDiagSCMatrix i () const


Return the inverse of this.


RefDiagSCMatrix gi () const


Return the generalized inverse of this.


RefDiagSCMatrix clone () const


These call the SCMatrix members of the same name after checking for references to 0.


RefDiagSCMatrix copy () const



void set_element (int, double) const



void accumulate_element (int, double) const



double get_element (int) const



void randomize () const



void assign (const RefDiagSCMatrix &amp;) const



void scale (double) const



void assign (double) const



void assign (const double *) const



void convert (double *) const



void accumulate (const RefDiagSCMatrix &amp;) const



void element_op (const Ref&lt; SCElementOp &gt; &amp;) const



void element_op (const Ref&lt; SCElementOp2 &gt; &amp;, const RefDiagSCMatrix &amp;) const



void element_op (const Ref&lt; SCElementOp3 &gt; &amp;, const RefDiagSCMatrix &amp;, const RefDiagSCMatrix &amp;) const



int n () const



RefSCDimension dim () const



Ref&lt; SCMatrixKit &gt; kit () const



double trace () const



void print (std::ostream &amp;) const



void print (const char *title=0, std::ostream &amp;out=ExEnv::out0(), int=10) const



void save (StateOut &amp;)



void restore (StateIn &amp;)


Restores the matrix from StateIn object. The matrix must have been initialized already.


double determ () const


Returns the determinant of the referenced matrix.


DiagSCMatrixdouble operator() (int i) const


Assign and examine matrix elements.


int nblock () const


If this matrix is blocked return the number of blocks.


RefDiagSCMatrix block (int i) const


If this matrix is blocked return block i.</code></pre>
<h2>Detailed Description</h2>
<p>The <code>RefDiagSCMatrix</code> class is a smart pointer to an <code>DiagSCMatrix</code> specialization.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::RefDiagSCMatrix::RefDiagSCMatrix ()</h3>
<p>Initializes the matrix pointer to 0. The reference must be initialized before it is used.</p>
<h3>sc::RefDiagSCMatrix::RefDiagSCMatrix (const <code>RefSCDimension</code> &amp;, const <code>Ref</code>&lt; <code>SCMatrixKit</code> &gt; &amp;)</h3>
<p>Create a diagonal matrix with dimension d by d. The data values are undefined.</p>
<h2>Member Function Documentation</h2>
<h3><code>RefDiagSCMatrix</code> sc::RefDiagSCMatrix::block (int i) const</h3>
<p>If this matrix is blocked return block i. Otherwise return this as block 0.</p>
<h3><code>RefDiagSCMatrix</code> sc::RefDiagSCMatrix::clone () const</h3>
<p>These call the <code>SCMatrix</code> members of the same name after checking for references to 0.</p>
<h3>int sc::RefDiagSCMatrix::nblock () const</h3>
<p>If this matrix is blocked return the number of blocks. Otherwise return 1.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
