---
title: "dlag2-f(3)"
name: "dlag2-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlag2-f/"
description: "dlag2.f –"
---

<p>dlag2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlag2</code> (A, LDA, B, LDB, SAFMIN, SCALE1, SCALE2, WR1, WR2, WI)<br />
 <i></i><code>DLAG2</code> computes the eigenvalues of a 2-by-2 generalized eigenvalue problem, with scaling as necessary to avoid over-/underflow.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlag2 (double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precisionSAFMIN, double precisionSCALE1, double precisionSCALE2, double precisionWR1, double precisionWR2, double precisionWI)</h3>
<p><code>DLAG2</code> computes the eigenvalues of a 2-by-2 generalized eigenvalue problem, with scaling as necessary to avoid over-/underflow. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAG2 computes the eigenvalues of a 2 x 2 generalized eigenvalue
 problem A - w B, with scaling as necessary to avoid over-/underflow.
 The scaling factor &quot;s&quot; results in a modified eigenvalue equation
 s A - w B
 where s is a non-negative scaling factor chosen so that w, w B,
 and s A do not overflow and, if possible, do not underflow, either.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA, 2)
 On entry, the 2 x 2 matrix A. It is assumed that its 1-norm
 is less than 1/SAFMIN. Entries less than
 sqrt(SAFMIN)*norm(A) are subject to being treated as zero.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= 2.</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB, 2)
 On entry, the 2 x 2 upper triangular matrix B. It is
 assumed that the one-norm of B is less than 1/SAFMIN. The
 diagonals should be at least sqrt(SAFMIN) times the largest
 element of B (in absolute value); if a diagonal is smaller
 than that, then +/- sqrt(SAFMIN) will be used instead of
 that diagonal.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= 2.</pre>
<p><i>SAFMIN</i> </p>
<pre> SAFMIN is DOUBLE PRECISION
 The smallest positive number s.t. 1/SAFMIN does not
 overflow. (This should always be DLAMCH('S') -- it is an
 argument in order to avoid having to call DLAMCH frequently.)</pre>
<p><i>SCALE1</i> </p>
<pre> SCALE1 is DOUBLE PRECISION
 A scaling factor used to avoid over-/underflow in the
 eigenvalue equation which defines the first eigenvalue. If
 the eigenvalues are complex, then the eigenvalues are
 ( WR1 +/- WI i ) / SCALE1 (which may lie outside the
 exponent range of the machine), SCALE1=SCALE2, and SCALE1
 will always be positive. If the eigenvalues are real, then
 the first (real) eigenvalue is WR1 / SCALE1 , but this may
 overflow or underflow, and in fact, SCALE1 may be zero or
 less than the underflow threshhold if the exact eigenvalue
 is sufficiently large.</pre>
<p><i>SCALE2</i> </p>
<pre> SCALE2 is DOUBLE PRECISION
 A scaling factor used to avoid over-/underflow in the
 eigenvalue equation which defines the second eigenvalue. If
 the eigenvalues are complex, then SCALE2=SCALE1. If the
 eigenvalues are real, then the second (real) eigenvalue is
 WR2 / SCALE2 , but this may overflow or underflow, and in
 fact, SCALE2 may be zero or less than the underflow
 threshhold if the exact eigenvalue is sufficiently large.</pre>
<p><i>WR1</i> </p>
<pre> WR1 is DOUBLE PRECISION
 If the eigenvalue is real, then WR1 is SCALE1 times the
 eigenvalue closest to the (2,2) element of A B**(-1). If the
 eigenvalue is complex, then WR1=WR2 is SCALE1 times the real
 part of the eigenvalues.</pre>
<p><i>WR2</i> </p>
<pre> WR2 is DOUBLE PRECISION
 If the eigenvalue is real, then WR2 is SCALE2 times the
 other eigenvalue. If the eigenvalue is complex, then
 WR1=WR2 is SCALE1 times the real part of the eigenvalues.</pre>
<p><i>WI</i> </p>
<pre> WI is DOUBLE PRECISION
 If the eigenvalue is real, then WI is zero. If the
 eigenvalue is complex, then WI is SCALE1 times the imaginary
 part of the eigenvalues. WI will always be non-negative.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> Definition at line 156 of file dlag2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
