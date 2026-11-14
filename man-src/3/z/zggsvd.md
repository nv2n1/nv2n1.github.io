---
title: "zggsvd(3)"
name: "zggsvd"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zggsvd/"
description: "zggsvd.f –"
---

<p>zggsvd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zggsvd</code> (JOBU, JOBV, JOBQ, M, N, P, K, L, A, LDA, B, LDB, ALPHA, BETA, U, LDU, V, LDV, Q, LDQ, WORK, RWORK, IWORK, INFO)<br />
 <i></i><code> ZGGSVD computes the singular value decomposition (SVD) for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zggsvd (characterJOBU, characterJOBV, characterJOBQ, integerM, integerN, integerP, integerK, integerL, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( ldb, * )B, integerLDB, double precision, dimension( * )ALPHA, double precision, dimension( * )BETA, complex*16, dimension( ldu, * )U, integerLDU, complex*16, dimension( ldv, * )V, integerLDV, complex*16, dimension( ldq, * )Q, integerLDQ, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code> ZGGSVD computes the singular value decomposition (SVD) for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGGSVD computes the generalized singular value decomposition (GSVD)
 of an M-by-N complex matrix A and P-by-N complex matrix B:
 U**H*A*Q = D1*( 0 R ), V**H*B*Q = D2*( 0 R )
 where U, V and Q are unitary matrices.
 Let K+L = the effective numerical rank of the
 matrix (A**H,B**H)**H, then R is a (K+L)-by-(K+L) nonsingular upper
 triangular matrix, D1 and D2 are M-by-(K+L) and P-by-(K+L) &quot;diagonal&quot;
 matrices and of the following structures, respectively:
 If M-K-L &gt;= 0,
 K L
 D1 = K ( I 0 )
 L ( 0 C )
 M-K-L ( 0 0 )
 K L
 D2 = L ( 0 S )
 P-L ( 0 0 )
 N-K-L K L
 ( 0 R ) = K ( 0 R11 R12 )
 L ( 0 0 R22 )
 where
 C = diag( ALPHA(K+1), ... , ALPHA(K+L) ),
 S = diag( BETA(K+1), ... , BETA(K+L) ),
 C**2 + S**2 = I.
 R is stored in A(1:K+L,N-K-L+1:N) on exit.
 If M-K-L &lt; 0,
 K M-K K+L-M
 D1 = K ( I 0 0 )
 M-K ( 0 C 0 )
 K M-K K+L-M
 D2 = M-K ( 0 S 0 )
 K+L-M ( 0 0 I )
 P-L ( 0 0 0 )
 N-K-L K M-K K+L-M
 ( 0 R ) = K ( 0 R11 R12 R13 )
 M-K ( 0 0 R22 R23 )
 K+L-M ( 0 0 0 R33 )
 where
 C = diag( ALPHA(K+1), ... , ALPHA(M) ),
 S = diag( BETA(K+1), ... , BETA(M) ),
 C**2 + S**2 = I.
 (R11 R12 R13 ) is stored in A(1:M, N-K-L+1:N), and R33 is stored
 ( 0 R22 R23 )
 in B(M-K+1:L,N+M-K-L+1:N) on exit.
 The routine computes C, S, R, and optionally the unitary
 transformation matrices U, V and Q.
 In particular, if B is an N-by-N nonsingular matrix, then the GSVD of
 A and B implicitly gives the SVD of A*inv(B):
 A*inv(B) = U*(D1*inv(D2))*V**H.
 If ( A**H,B**H)**H has orthnormal columns, then the GSVD of A and B is also
 equal to the CS decomposition of A and B. Furthermore, the GSVD can
 be used to derive the solution of the eigenvalue problem:
 A**H*A x = lambda* B**H*B x.
 In some literature, the GSVD of A and B is presented in the form
 U**H*A*X = ( 0 D1 ), V**H*B*X = ( 0 D2 )
 where U and V are orthogonal and X is nonsingular, and D1 and D2 are
 ``diagonal''. The former GSVD form can be converted to the latter
 form by taking the nonsingular matrix X as
 X = Q*( I 0 )
 ( 0 inv(R) )</pre>
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
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrices A and B. N &gt;= 0.</pre>
<p><i>P</i> </p>
<pre> P is INTEGER
 The number of rows of the matrix B. P &gt;= 0.</pre>
<p><i>K</i> </p>
<pre> K is INTEGER</pre>
<p><i>L</i> </p>
<pre> L is INTEGER
 On exit, K and L specify the dimension of the subblocks
 described in Purpose.
 K + L = effective numerical rank of (A**H,B**H)**H.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, A contains the triangular matrix R, or part of R.
 See Purpose for details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,N)
 On entry, the P-by-N matrix B.
 On exit, B contains part of the triangular matrix R if
 M-K-L &lt; 0. See Purpose for details.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,P).</pre>
<p><i>ALPHA</i> </p>
<pre> ALPHA is DOUBLE PRECISION array, dimension (N)</pre>
<p><i>BETA</i> </p>
<pre> BETA is DOUBLE PRECISION array, dimension (N)
 On exit, ALPHA and BETA contain the generalized singular
 value pairs of A and B;
 ALPHA(1:K) = 1,
 BETA(1:K) = 0,
 and if M-K-L &gt;= 0,
 ALPHA(K+1:K+L) = C,
 BETA(K+1:K+L) = S,
 or if M-K-L &lt; 0,
 ALPHA(K+1:M)=C, ALPHA(M+1:K+L)=0
 BETA(K+1:M) =S, BETA(M+1:K+L) =1
 and
 ALPHA(K+L+1:N) = 0
 BETA(K+L+1:N) = 0</pre>
<p><i>U</i> </p>
<pre> U is COMPLEX*16 array, dimension (LDU,M)
 If JOBU = 'U', U contains the M-by-M unitary matrix U.
 If JOBU = 'N', U is not referenced.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= max(1,M) if
 JOBU = 'U'; LDU &gt;= 1 otherwise.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension (LDV,P)
 If JOBV = 'V', V contains the P-by-P unitary matrix V.
 If JOBV = 'N', V is not referenced.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V. LDV &gt;= max(1,P) if
 JOBV = 'V'; LDV &gt;= 1 otherwise.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX*16 array, dimension (LDQ,N)
 If JOBQ = 'Q', Q contains the N-by-N unitary matrix Q.
 If JOBQ = 'N', Q is not referenced.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N) if
 JOBQ = 'Q'; LDQ &gt;= 1 otherwise.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (max(3*N,M,P)+N)</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (2*N)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (N)
 On exit, IWORK stores the sorting information. More
 precisely, the following loop will sort ALPHA
 for I = K+1, min(M,K+L)
 swap ALPHA(I) and ALPHA(IWORK(I))
 endfor
 such that <a href="//www.systutorials.com/docs/linux/man/1-ALPHA/">ALPHA</a>(1) &gt;= <a href="//www.systutorials.com/docs/linux/man/2-ALPHA/">ALPHA</a>(2) &gt;= ... &gt;= ALPHA(N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = 1, the Jacobi-type procedure failed to
 converge. For further details, see subroutine ZTGSJA.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dd>
<pre> TOLA DOUBLE PRECISION
 TOLB DOUBLE PRECISION
 TOLA and TOLB are the thresholds to determine the effective
 rank of (A**H,B**H)**H. Generally, they are set to
 TOLA = MAX(M,N)*norm(A)*MAZHEPS,
 TOLB = MAX(P,N)*norm(B)*MAZHEPS.
 The size of TOLA and TOLB may affect the size of backward
 errors of the decomposition.</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 334 of file zggsvd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
