---
title: "sggqrf-f(3)"
name: "sggqrf-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sggqrf-f/"
description: "sggqrf.f –"
---

<p>sggqrf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sggqrf</code> (N, M, P, A, LDA, TAUA, B, LDB, TAUB, WORK, LWORK, INFO)<br />
 <i></i><code>SGGQRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sggqrf (integerN, integerM, integerP, real, dimension( lda, * )A, integerLDA, real, dimension( * )TAUA, real, dimension( ldb, * )B, integerLDB, real, dimension( * )TAUB, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>SGGQRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SGGQRF computes a generalized QR factorization of an N-by-M matrix A
 and an N-by-P matrix B:
 A = Q*R, B = Q*T*Z,
 where Q is an N-by-N orthogonal matrix, Z is a P-by-P orthogonal
 matrix, and R and T assume one of the forms:
 if N &gt;= M, R = ( R11 ) M , or if N &lt; M, R = ( R11 R12 ) N,
 ( 0 ) N-M N M-N
 M
 where R11 is upper triangular, and
 if N &lt;= P, T = ( 0 T12 ) N, or if N &gt; P, T = ( T11 ) N-P,
 P-N N ( T21 ) P
 P
 where T12 or T21 is upper triangular.
 In particular, if B is square and nonsingular, the GQR factorization
 of A and B implicitly gives the QR factorization of inv(B)*A:
 inv(B)*A = Z**T*(inv(T)*R)
 where inv(B) denotes the inverse of the matrix B, and Z**T denotes the
 transpose of the matrix Z.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The number of rows of the matrices A and B. N &gt;= 0.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of columns of the matrix A. M &gt;= 0.</pre>
<p><i>P</i> </p>
<pre> P is INTEGER
 The number of columns of the matrix B. P &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,M)
 On entry, the N-by-M matrix A.
 On exit, the elements on and above the diagonal of the array
 contain the min(N,M)-by-M upper trapezoidal matrix R (R is
 upper triangular if N &gt;= M); the elements below the diagonal,
 with the array TAUA, represent the orthogonal matrix Q as a
 product of min(N,M) elementary reflectors (see Further
 Details).</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>TAUA</i> </p>
<pre> TAUA is REAL array, dimension (min(N,M))
 The scalar factors of the elementary reflectors which
 represent the orthogonal matrix Q (see Further Details).</pre>
<p><i>B</i> </p>
<pre> B is REAL array, dimension (LDB,P)
 On entry, the N-by-P matrix B.
 On exit, if N &lt;= P, the upper triangle of the subarray
 B(1:N,P-N+1:P) contains the N-by-N upper triangular matrix T;
 if N &gt; P, the elements on and above the (N-P)-th subdiagonal
 contain the N-by-P upper trapezoidal matrix T; the remaining
 elements, with the array TAUB, represent the orthogonal
 matrix Z as a product of elementary reflectors (see Further
 Details).</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of the array B. LDB &gt;= max(1,N).</pre>
<p><i>TAUB</i> </p>
<pre> TAUB is REAL array, dimension (min(N,P))
 The scalar factors of the elementary reflectors which
 represent the orthogonal matrix Z (see Further Details).</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,N,M,P).
 For optimum performance LWORK &gt;= max(N,M,P)*max(NB1,NB2,NB3),
 where NB1 is the optimal blocksize for the QR factorization
 of an N-by-M matrix, NB2 is the optimal blocksize for the
 RQ factorization of an N-by-P matrix, and NB3 is the optimal
 blocksize for a call of SORMQR.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
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
<pre> The matrix Q is represented as a product of elementary reflectors
 Q = H(1) H(2) . . . H(k), where k = min(n,m).
 Each H(i) has the form
 H(i) = I - taua * v * v**T
 where taua is a real scalar, and v is a real vector with
 v(1:i-1) = 0 and v(i) = 1; v(i+1:n) is stored on exit in A(i+1:n,i),
 and taua in TAUA(i).
 To form Q explicitly, use LAPACK subroutine SORGQR.
 To use Q to update another matrix, use LAPACK subroutine SORMQR.
 The matrix Z is represented as a product of elementary reflectors
 Z = H(1) H(2) . . . H(k), where k = min(n,p).
 Each H(i) has the form
 H(i) = I - taub * v * v**T
 where taub is a real scalar, and v is a real vector with
 v(p-k+i+1:p) = 0 and v(p-k+i) = 1; v(1:p-k+i-1) is stored on exit in
 B(n-k+i,1:p-k+i-1), and taub in TAUB(i).
 To form Z explicitly, use LAPACK subroutine SORGRQ.
 To use Z to update another matrix, use LAPACK subroutine SORMRQ.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 215 of file sggqrf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
