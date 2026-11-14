---
title: "sstein-f(3)"
name: "sstein-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sstein-f/"
description: "sstein.f –"
---

<p>sstein.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sstein</code> (N, D, E, M, W, IBLOCK, ISPLIT, Z, LDZ, WORK, IWORK, IFAIL, INFO)<br />
 <i></i><code>SSTEIN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sstein (integerN, real, dimension( * )D, real, dimension( * )E, integerM, real, dimension( * )W, integer, dimension( * )IBLOCK, integer, dimension( * )ISPLIT, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p><code>SSTEIN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SSTEIN computes the eigenvectors of a real symmetric tridiagonal
 matrix T corresponding to specified eigenvalues, using inverse
 iteration.
 The maximum number of iterations allowed for each eigenvector is
 specified by an internal parameter MAXITS (currently set to 5).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 The n diagonal elements of the tridiagonal matrix T.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N-1)
 The (n-1) subdiagonal elements of the tridiagonal matrix
 T, in elements 1 to N-1.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of eigenvectors to be found. 0 &lt;= M &lt;= N.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (N)
 The first M elements of W contain the eigenvalues for
 which eigenvectors are to be computed. The eigenvalues
 should be grouped by split-off block and ordered from
 smallest to largest within the block. ( The output array
 W from SSTEBZ with ORDER = 'B' is expected here. )</pre>
<p><i>IBLOCK</i> </p>
<pre> IBLOCK is INTEGER array, dimension (N)
 The submatrix indices associated with the corresponding
 eigenvalues in W; IBLOCK(i)=1 if eigenvalue W(i) belongs to
 the first submatrix from the top, =2 if W(i) belongs to
 the second submatrix, etc. ( The output array IBLOCK
 from SSTEBZ is expected here. )</pre>
<p><i>ISPLIT</i> </p>
<pre> ISPLIT is INTEGER array, dimension (N)
 The splitting points, at which T breaks up into submatrices.
 The first submatrix consists of rows/columns 1 to
 ISPLIT( 1 ), the second of rows/columns ISPLIT( 1 )+1
 through ISPLIT( 2 ), etc.
 ( The output array ISPLIT from SSTEBZ is expected here. )</pre>
<p><i>Z</i> </p>
<pre> Z is REAL array, dimension (LDZ, M)
 The computed eigenvectors. The eigenvector associated
 with the eigenvalue W(i) is stored in the i-th column of
 Z. Any vector which fails to converge is set to its current
 iterate after MAXITS iterations.</pre>
<p><i>LDZ</i> </p>
<pre> LDZ is INTEGER
 The leading dimension of the array Z. LDZ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (5*N)</pre>
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
 = 0: successful exit.
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
<p> Definition at line 174 of file sstein.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
