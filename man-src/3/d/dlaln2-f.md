---
title: "dlaln2-f(3)"
name: "dlaln2-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaln2-f/"
description: "dlaln2.f –"
---

<p>dlaln2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlaln2</code> (LTRANS, NA, NW, SMIN, CA, A, LDA, D1, D2, B, LDB, WR, WI, X, LDX, SCALE, XNORM, INFO)<br />
 <i></i><code>DLALN2</code> solves a 1-by-1 or 2-by-2 linear system of equations of the specified form.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaln2 (logicalLTRANS, integerNA, integerNW, double precisionSMIN, double precisionCA, double precision, dimension( lda, * )A, integerLDA, double precisionD1, double precisionD2, double precision, dimension( ldb, * )B, integerLDB, double precisionWR, double precisionWI, double precision, dimension( ldx, * )X, integerLDX, double precisionSCALE, double precisionXNORM, integerINFO)</h3>
<p><code>DLALN2</code> solves a 1-by-1 or 2-by-2 linear system of equations of the specified form. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLALN2 solves a system of the form (ca A - w D ) X = s B
 or (ca A**T - w D) X = s B with possible scaling (&quot;s&quot;) and
 perturbation of A. (A**T means A-transpose.)
 A is an NA x NA real matrix, ca is a real scalar, D is an NA x NA
 real diagonal matrix, w is a real or complex value, and X and B are
 NA x 1 matrices -- real if w is real, complex if w is complex. NA
 may be 1 or 2.
 If w is complex, X and B are represented as NA x 2 matrices,
 the first column of each being the real part and the second
 being the imaginary part.
 &quot;s&quot; is a scaling factor (.LE. 1), computed by DLALN2, which is
 so chosen that X can be computed without overflow. X is further
 scaled if necessary to assure that norm(ca A - w D)*norm(X) is less
 than overflow.
 If both singular values of (ca A - w D) are less than SMIN,
 SMIN*identity will be used instead of (ca A - w D). If only one
 singular value is less than SMIN, one element of (ca A - w D) will be
 perturbed enough to make the smallest singular value roughly SMIN.
 If both singular values are at least SMIN, (ca A - w D) will not be
 perturbed. In any case, the perturbation will be at most some small
 multiple of max( SMIN, ulp*norm(ca A - w D) ). The singular values
 are computed by infinity-norm approximations, and thus will only be
 correct to a factor of 2 or so.
 Note: all input quantities are assumed to be smaller than overflow
 by a reasonable factor. (See BIGNUM.)</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>LTRANS</i> </p>
<pre> LTRANS is LOGICAL
 =.TRUE.: A-transpose will be used.
 =.FALSE.: A will be used (not transposed.)</pre>
<p><i>NA</i> </p>
<pre> NA is INTEGER
 The size of the matrix A. It may (only) be 1 or 2.</pre>
<p><i>NW</i> </p>
<pre> NW is INTEGER
 1 if &quot;w&quot; is real, 2 if &quot;w&quot; is complex. It may only be 1
 or 2.</pre>
<p><i>SMIN</i> </p>
<pre> SMIN is DOUBLE PRECISION
 The desired lower bound on the singular values of A. This
 should be a safe distance away from underflow or overflow,
 say, between (underflow/machine precision) and (machine
 precision * overflow ). (See BIGNUM and ULP.)</pre>
<p><i>CA</i> </p>
<pre> CA is DOUBLE PRECISION
 The coefficient c, which A is multiplied by.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (LDA,NA)
 The NA x NA matrix A.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of A. It must be at least NA.</pre>
<p><i>D1</i> </p>
<pre> D1 is DOUBLE PRECISION
 The 1,1 element in the diagonal matrix D.</pre>
<p><i>D2</i> </p>
<pre> D2 is DOUBLE PRECISION
 The 2,2 element in the diagonal matrix D. Not used if NW=1.</pre>
<p><i>B</i> </p>
<pre> B is DOUBLE PRECISION array, dimension (LDB,NW)
 The NA x NW matrix B (right-hand side). If NW=2 (&quot;w&quot; is
 complex), column 1 contains the real part of B and column 2
 contains the imaginary part.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of B. It must be at least NA.</pre>
<p><i>WR</i> </p>
<pre> WR is DOUBLE PRECISION
 The real part of the scalar &quot;w&quot;.</pre>
<p><i>WI</i> </p>
<pre> WI is DOUBLE PRECISION
 The imaginary part of the scalar &quot;w&quot;. Not used if NW=1.</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array, dimension (LDX,NW)
 The NA x NW matrix X (unknowns), as computed by DLALN2.
 If NW=2 (&quot;w&quot; is complex), on exit, column 1 will contain
 the real part of X and column 2 will contain the imaginary
 part.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of X. It must be at least NA.</pre>
<p><i>SCALE</i> </p>
<pre> SCALE is DOUBLE PRECISION
 The scale factor that B must be multiplied by to insure
 that overflow does not occur when computing X. Thus,
 (ca A - w D) X will be SCALE*B, not B (ignoring
 perturbations of A.) It will be at most 1.</pre>
<p><i>XNORM</i> </p>
<pre> XNORM is DOUBLE PRECISION
 The infinity-norm of X, when X is regarded as an NA x NW
 real matrix.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 An error flag. It will be set to zero if no error occurs,
 a negative number if an argument is in error, or a positive
 number if ca A - w D had to be perturbed.
 The possible values are:
 = 0: No error occurred, and (ca A - w D) did not have to be
 perturbed.
 = 1: (ca A - w D) had to be perturbed to make its smallest
 (or only) singular value greater than SMIN.
 NOTE: In the interests of speed, this routine does not
 check the inputs for errors.</pre>
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
<p> Definition at line 218 of file dlaln2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
