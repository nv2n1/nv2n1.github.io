---
title: "zstein-f(3)"
name: "zstein-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zstein-f/"
description: "zstein.f –"
---

<p>zstein.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zstein</code> (N, D, E, M, W, IBLOCK, ISPLIT, Z, LDZ, WORK, IWORK, IFAIL, INFO)<br />
 <i></i><code>ZSTEIN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zstein (integerN, double precision, dimension( * )D, double precision, dimension( * )E, integerM, double precision, dimension( * )W, integer, dimension( * )IBLOCK, integer, dimension( * )ISPLIT, complex*16, dimension( ldz, * )Z, integerLDZ, double precision, dimension( * )WORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p><code>ZSTEIN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZSTEIN computes the eigenvectors of a real symmetric tridiagonal
 matrix T corresponding to specified eigenvalues, using inverse
 iteration.
 The maximum number of iterations allowed for each eigenvector is
 specified by an internal parameter MAXITS (currently set to 5).
 Although the eigenvectors are real, they are stored in a complex
 array, which may be passed to ZUNMTR or ZUPMTR for back
 transformation to the eigenvectors of a complex Hermitian matrix
 which was reduced to tridiagonal form.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 The n diagonal elements of the tridiagonal matrix T.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 The (n-1) subdiagonal elements of the tridiagonal matrix
 T, stored in elements 1 to N-1.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of eigenvectors to be found. 0 &lt;= M &lt;= N.</pre>
<p><i>W</i> </p>
<pre> W is DOUBLE PRECISION array, dimension (N)
 The first M elements of W contain the eigenvalues for
 which eigenvectors are to be computed. The eigenvalues
 should be grouped by split-off block and ordered from
 smallest to largest within the block. ( The output array
 W from DSTEBZ with ORDER = 'B' is expected here. )</pre>
<p><i>IBLOCK</i> </p>
<pre> IBLOCK is INTEGER array, dimension (N)
 The submatrix indices associated with the corresponding
 eigenvalues in W; IBLOCK(i)=1 if eigenvalue W(i) belongs to
 the first submatrix from the top, =2 if W(i) belongs to
 the second submatrix, etc. ( The output array IBLOCK
 from DSTEBZ is expected here. )</pre>
<p><i>ISPLIT</i> </p>
<pre> ISPLIT is INTEGER array, dimension (N)
 The splitting points, at which T breaks up into submatrices.
 The first submatrix consists of rows/columns 1 to
 ISPLIT( 1 ), the second of rows/columns ISPLIT( 1 )+1
 through ISPLIT( 2 ), etc.
 ( The output array ISPLIT from DSTEBZ is expected here. )</pre>
<p><i>Z</i> </p>
<pre> Z is COMPLEX*16 array, dimension (LDZ, M)
 The computed eigenvectors. The eigenvector associated
 with the eigenvalue W(i) is stored in the i-th column of
 Z. Any vector which fails to converge is set to its current
 iterate after MAXITS iterations.
 The imaginary parts of the eigenvectors are set to zero.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (5*N)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N)</pre>
<p><i>IFAIL</i> </p>
<pre> IFAIL is INTEGER array, dimension (M)
 On normal exit, all elements of IFAIL are zero.
 If one or more eigenvectors fail to converge after
 MAXITS iterations, then their indices are stored in
 array IFAIL.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = i, then i eigenvectors failed to converge
 in MAXITS iterations. Their indices are stored in
 array IFAIL.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dd>
<pre> MAXITS INTEGER, default = 5
 The maximum number of iterations performed.
 EXTRA INTEGER, default = 2
 The number of iterations performed after norm growth
 criterion is satisfied, should be at least 1.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 182 of file zstein.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
