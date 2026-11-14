---
title: "dlasdq-f(3)"
name: "dlasdq-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasdq-f/"
description: "dlasdq.f –"
---

<p>dlasdq.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlasdq</code> (UPLO, SQRE, N, NCVT, NRU, NCC, D, E, VT, LDVT, U, LDU, C, LDC, WORK, INFO)<br />
 <i></i><code>DLASDQ</code> computes the SVD of a real bidiagonal matrix with diagonal d and off-diagonal e. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasdq (characterUPLO, integerSQRE, integerN, integerNCVT, integerNRU, integerNCC, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( ldvt, * )VT, integerLDVT, double precision, dimension( ldu, * )U, integerLDU, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>DLASDQ</code> computes the SVD of a real bidiagonal matrix with diagonal d and off-diagonal e. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLASDQ computes the singular value decomposition (SVD) of a real
 (upper or lower) bidiagonal matrix with diagonal D and offdiagonal
 E, accumulating the transformations if desired. Letting B denote
 the input bidiagonal matrix, the algorithm computes orthogonal
 matrices Q and P such that B = Q * S * P**T (P**T denotes the transpose
 of P). The singular values S are overwritten on D.
 The input matrix U is changed to U * Q if desired.
 The input matrix VT is changed to P**T * VT if desired.
 The input matrix C is changed to Q**T * C if desired.
 See &quot;Computing Small Singular Values of Bidiagonal Matrices With
 Guaranteed High Relative Accuracy,&quot; by J. Demmel and W. Kahan,
 LAPACK Working Note #3, for a detailed description of the algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 On entry, UPLO specifies whether the input bidiagonal matrix
 is upper or lower bidiagonal, and wether it is square are
 not.
 UPLO = 'U' or 'u' B is upper bidiagonal.
 UPLO = 'L' or 'l' B is lower bidiagonal.</pre>
<p><i>SQRE</i> </p>
<pre> SQRE is INTEGER
 = 0: then the input matrix is N-by-N.
 = 1: then the input matrix is N-by-(N+1) if UPLU = 'U' and
 (N+1)-by-N if UPLU = 'L'.
 The bidiagonal matrix has
 N = NL + NR + 1 rows and
 M = N + SQRE &gt;= N columns.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 On entry, N specifies the number of rows and columns
 in the matrix. N must be at least 0.</pre>
<p><i>NCVT</i> </p>
<pre> NCVT is INTEGER
 On entry, NCVT specifies the number of columns of
 the matrix VT. NCVT must be at least 0.</pre>
<p><i>NRU</i> </p>
<pre> NRU is INTEGER
 On entry, NRU specifies the number of rows of
 the matrix U. NRU must be at least 0.</pre>
<p><i>NCC</i> </p>
<pre> NCC is INTEGER
 On entry, NCC specifies the number of columns of
 the matrix C. NCC must be at least 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, D contains the diagonal entries of the
 bidiagonal matrix whose SVD is desired. On normal exit,
 D contains the singular values in ascending order.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array.
 dimension is (N-1) if SQRE = 0 and N if SQRE = 1.
 On entry, the entries of E contain the offdiagonal entries
 of the bidiagonal matrix whose SVD is desired. On normal
 exit, E will contain 0. If the algorithm does not converge,
 D and E will contain the diagonal and superdiagonal entries
 of a bidiagonal matrix orthogonally equivalent to the one
 given as input.</pre>
<p><i>VT</i> </p>
<pre> VT is DOUBLE PRECISION array, dimension (LDVT, NCVT)
 On entry, contains a matrix which on exit has been
 premultiplied by P**T, dimension N-by-NCVT if SQRE = 0
 and (N+1)-by-NCVT if SQRE = 1 (not referenced if NCVT=0).</pre>
<p><i>LDVT</i> </p>
<pre> LDVT is INTEGER
 On entry, LDVT specifies the leading dimension of VT as
 declared in the calling (sub) program. LDVT must be at
 least 1. If NCVT is nonzero LDVT must also be at least N.</pre>
<p><i>U</i> </p>
<pre> U is DOUBLE PRECISION array, dimension (LDU, N)
 On entry, contains a matrix which on exit has been
 postmultiplied by Q, dimension NRU-by-N if SQRE = 0
 and NRU-by-(N+1) if SQRE = 1 (not referenced if NRU=0).</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 On entry, LDU specifies the leading dimension of U as
 declared in the calling (sub) program. LDU must be at
 least max( 1, NRU ) .</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (LDC, NCC)
 On entry, contains an N-by-NCC matrix which on exit
 has been premultiplied by Q**T dimension N-by-NCC if SQRE = 0
 and (N+1)-by-NCC if SQRE = 1 (not referenced if NCC=0).</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 On entry, LDC specifies the leading dimension of C as
 declared in the calling (sub) program. LDC must be at
 least 1. If NCC is nonzero, LDC must also be at least N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (4*N)
 Workspace. Only referenced if one of NCVT, NRU, or NCC is
 nonzero, and if N is at least 2.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 On exit, a value of 0 indicates a successful exit.
 If INFO &lt; 0, argument number -INFO is illegal.
 If INFO &gt; 0, the algorithm did not converge, and INFO
 specifies how many superdiagonals did not converge.</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 211 of file dlasdq.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
