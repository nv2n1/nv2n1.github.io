---
title: "zggsvp(3)"
name: "zggsvp"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zggsvp/"
description: "zggsvp.f –"
---

<p>zggsvp.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zggsvp</code> (JOBU, JOBV, JOBQ, M, P, N, A, LDA, B, LDB, TOLA, TOLB, K, L, U, LDU, V, LDV, Q, LDQ, IWORK, RWORK, TAU, WORK, INFO)<br />
 <i></i><code>ZGGSVP</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zggsvp (characterJOBU, characterJOBV, characterJOBQ, integerM, integerP, integerN, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, double precisionTOLA, double precisionTOLB, integerK, integerL, complex*16, dimension( ldu, * )U, integerLDU, complex*16, dimension( ldv, * )V, integerLDV, complex*16, dimension( ldq, * )Q, integerLDQ, integer, dimension( * )IWORK, double precision, dimension( * )RWORK, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, integerINFO)</h3>
<p><code>ZGGSVP</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGGSVP computes unitary matrices U, V and Q such that
 N-K-L K L
 U**H*A*Q = K ( 0 A12 A13 ) if M-K-L &gt;= 0;
 L ( 0 0 A23 )
 M-K-L ( 0 0 0 )
 N-K-L K L
 = K ( 0 A12 A13 ) if M-K-L &lt; 0;
 M-K ( 0 0 A23 )
 N-K-L K L
 V**H*B*Q = L ( 0 0 B13 )
 P-L ( 0 0 0 )
 where the K-by-K matrix A12 and L-by-L matrix B13 are nonsingular
 upper triangular; A23 is L-by-L upper triangular if M-K-L &gt;= 0,
 otherwise A23 is (M-K)-by-L upper trapezoidal. K+L = the effective
 numerical rank of the (M+P)-by-N matrix (A**H,B**H)**H. 
 This decomposition is the preprocessing step for computing the
 Generalized Singular Value Decomposition (GSVD), see subroutine
 ZGGSVD.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBU</i> </p>
<pre> JOBU is CHARACTER*1
 = 'U': Unitary matrix U is computed;
 = 'N': U is not computed.</pre>
<p><i>JOBV</i> </p>
<pre> JOBV is CHARACTER*1
 = 'V': Unitary matrix V is computed;
 = 'N': V is not computed.</pre>
<p><i>JOBQ</i> </p>
<pre> JOBQ is CHARACTER*1
 = 'Q': Unitary matrix Q is computed;
 = 'N': Q is not computed.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>P</i> </p>
<pre> P is INTEGER
 The number of rows of the matrix B. P &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrices A and B. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, A contains the triangular (or trapezoidal) matrix
 described in the Purpose section.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,N)
 On entry, the P-by-N matrix B.
 On exit, B contains the triangular matrix described in
 the Purpose section.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,P).</pre>
<p><i>TOLA</i> </p>
<pre> TOLA is DOUBLE PRECISION</pre>
<p><i>TOLB</i> </p>
<pre> TOLB is DOUBLE PRECISION
 TOLA and TOLB are the thresholds to determine the effective
 numerical rank of matrix B and a subblock of A. Generally,
 they are set to
 TOLA = MAX(M,N)*norm(A)*MAZHEPS,
 TOLB = MAX(P,N)*norm(B)*MAZHEPS.
 The size of TOLA and TOLB may affect the size of backward
 errors of the decomposition.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER</pre>
<p><i>L</i> </p>
<pre> L is INTEGER
 On exit, K and L specify the dimension of the subblocks
 described in Purpose section.
 K + L = effective numerical rank of (A**H,B**H)**H.</pre>
<p><i>U</i> </p>
<pre> U is COMPLEX*16 array, dimension (LDU,M)
 If JOBU = 'U', U contains the unitary matrix U.
 If JOBU = 'N', U is not referenced.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= max(1,M) if
 JOBU = 'U'; LDU &gt;= 1 otherwise.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension (LDV,P)
 If JOBV = 'V', V contains the unitary matrix V.
 If JOBV = 'N', V is not referenced.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V. LDV &gt;= max(1,P) if
 JOBV = 'V'; LDV &gt;= 1 otherwise.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX*16 array, dimension (LDQ,N)
 If JOBQ = 'Q', Q contains the unitary matrix Q.
 If JOBQ = 'N', Q is not referenced.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N) if
 JOBQ = 'Q'; LDQ &gt;= 1 otherwise.</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*N)</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (N)</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (max(3*N,M,P))</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The subroutine uses LAPACK subroutine ZGEQPF for the QR factorization
 with column pivoting to detect the effective numerical rank of the
 a matrix. It may be replaced by a better rank determination strategy.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 262 of file zggsvp.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
