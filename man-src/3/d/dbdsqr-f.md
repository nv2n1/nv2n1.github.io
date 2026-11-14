---
title: "dbdsqr-f(3)"
name: "dbdsqr-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dbdsqr-f/"
description: "dbdsqr.f –"
---

<p>dbdsqr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dbdsqr</code> (UPLO, N, NCVT, NRU, NCC, D, E, VT, LDVT, U, LDU, C, LDC, WORK, INFO)<br />
 <i></i><code>DBDSQR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dbdsqr (characterUPLO, integerN, integerNCVT, integerNRU, integerNCC, double precision, dimension( * )D, double precision, dimension( * )E, double precision, dimension( ldvt, * )VT, integerLDVT, double precision, dimension( ldu, * )U, integerLDU, double precision, dimension( ldc, * )C, integerLDC, double precision, dimension( * )WORK, integerINFO)</h3>
<p><code>DBDSQR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DBDSQR computes the singular values and, optionally, the right and/or
 left singular vectors from the singular value decomposition (SVD) of
 a real N-by-N (upper or lower) bidiagonal matrix B using the implicit
 zero-shift QR algorithm. The SVD of B has the form
 
 B = Q * S * P**T
 
 where S is the diagonal matrix of singular values, Q is an orthogonal
 matrix of left singular vectors, and P is an orthogonal matrix of
 right singular vectors. If left singular vectors are requested, this
 subroutine actually returns U*Q instead of Q, and, if right singular
 vectors are requested, this subroutine returns P**T*VT instead of
 P**T, for given real input matrices U and VT. When U and VT are the
 orthogonal matrices that reduce a general matrix A to bidiagonal
 form: A = U*B*VT, as computed by DGEBRD, then
 A = (U*Q) * S * (P**T*VT)
 is the SVD of A. Optionally, the subroutine may also compute Q**T*C
 for a given real input matrix C.
 See &quot;Computing Small Singular Values of Bidiagonal Matrices With
 Guaranteed High Relative Accuracy,&quot; by J. Demmel and W. Kahan,
 LAPACK Working Note #3 (or SIAM J. Sci. Statist. Comput. vol. 11,
 no. 5, pp. 873-912, Sept 1990) and
 &quot;Accurate singular values and differential qd algorithms,&quot; by
 B. Parlett and V. Fernando, Technical Report CPAM-554, Mathematics
 Department, University of California at Berkeley, July 1992
 for a detailed description of the algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': B is upper bidiagonal;
 = 'L': B is lower bidiagonal.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix B. N &gt;= 0.</pre>
<p><i>NCVT</i> </p>
<pre> NCVT is INTEGER
 The number of columns of the matrix VT. NCVT &gt;= 0.</pre>
<p><i>NRU</i> </p>
<pre> NRU is INTEGER
 The number of rows of the matrix U. NRU &gt;= 0.</pre>
<p><i>NCC</i> </p>
<pre> NCC is INTEGER
 The number of columns of the matrix C. NCC &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the n diagonal elements of the bidiagonal matrix B.
 On exit, if INFO=0, the singular values of B in decreasing
 order.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 On entry, the N-1 offdiagonal elements of the bidiagonal
 matrix B. 
 On exit, if INFO = 0, E is destroyed; if INFO &gt; 0, D and E
 will contain the diagonal and superdiagonal elements of a
 bidiagonal matrix orthogonally equivalent to the one given
 as input.</pre>
<p><i>VT</i> </p>
<pre> VT is DOUBLE PRECISION array, dimension (LDVT, NCVT)
 On entry, an N-by-NCVT matrix VT.
 On exit, VT is overwritten by P**T * VT.
 Not referenced if NCVT = 0.</pre>
<p><i>LDVT</i> </p>
<pre> LDVT is INTEGER
 The leading dimension of the array VT.
 LDVT &gt;= max(1,N) if NCVT &gt; 0; LDVT &gt;= 1 if NCVT = 0.</pre>
<p><i>U</i> </p>
<pre> U is DOUBLE PRECISION array, dimension (LDU, N)
 On entry, an NRU-by-N matrix U.
 On exit, U is overwritten by U * Q.
 Not referenced if NRU = 0.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= max(1,NRU).</pre>
<p><i>C</i> </p>
<pre> C is DOUBLE PRECISION array, dimension (LDC, NCC)
 On entry, an N-by-NCC matrix C.
 On exit, C is overwritten by Q**T * C.
 Not referenced if NCC = 0.</pre>
<p><i>LDC</i> </p>
<pre> LDC is INTEGER
 The leading dimension of the array C.
 LDC &gt;= max(1,N) if NCC &gt; 0; LDC &gt;=1 if NCC = 0.</pre>
<p><i>WORK</i> </p>
<pre> WORK is DOUBLE PRECISION array, dimension (4*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: If INFO = -i, the i-th argument had an illegal value
 &gt; 0:
 if NCVT = NRU = NCC = 0,
 = 1, a split was marked by a positive value in E
 = 2, current block of Z not diagonalized after 30*N
 iterations (in inner while loop)
 = 3, termination criterion of outer while loop not met 
 (program created more than N unreduced blocks)
 else NCVT = NRU = NCC = 0,
 the algorithm did not converge; D and E contain the
 elements of a bidiagonal matrix which is orthogonally
 similar to the input matrix B; if INFO = i, i
 elements of E have not converged to zero.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl COMPACT>
<dd>
<pre> TOLMUL DOUBLE PRECISION, default = max(10,min(100,EPS**(-1/8)))
 TOLMUL controls the convergence criterion of the QR loop.
 If it is positive, TOLMUL*EPS is the desired relative
 precision in the computed singular values.
 If it is negative, abs(TOLMUL*EPS*sigma_max) is the
 desired absolute accuracy in the computed singular
 values (corresponds to relative accuracy
 abs(TOLMUL*EPS) in the largest singular value.
 abs(TOLMUL) should be between 1 and 1/EPS, and preferably
 between 10 (for fast convergence) and .1/EPS
 (for there to be some accuracy in the results).
 Default is to lose at either one eighth or 2 of the
 available decimal digits in each computed singular value
 (whichever is smaller).
 MAXITR INTEGER, default = 6
 MAXITR controls the maximum number of passes of the
 algorithm through its inner loop. The algorithms stops
 (and so fails to converge) if the number of passes
 through the inner loop exceeds MAXITR*N**2.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 230 of file dbdsqr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
