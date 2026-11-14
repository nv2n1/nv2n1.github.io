---
title: "cggsvp(3)"
name: "cggsvp"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cggsvp/"
description: "cggsvp.f –"
---

<h2 class="name">NAME</h2>
<p> cggsvp.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cggsvp</code> (JOBU, JOBV, JOBQ, M, P, N, A, LDA, B, LDB, TOLA, TOLB, K, L, U, LDU, V, LDV, Q, LDQ, IWORK, RWORK, TAU, WORK, INFO)<br />
 <i></i><code>CGGSVP</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cggsvp (characterJOBU, characterJOBV, characterJOBQ, integerM, integerP, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, realTOLA, realTOLB, integerK, integerL, complex, dimension( ldu, * )U, integerLDU, complex, dimension( ldv, * )V, integerLDV, complex, dimension( ldq, * )Q, integerLDQ, integer, dimension( * )IWORK, real, dimension( * )RWORK, complex, dimension( * )TAU, complex, dimension( * )WORK, integerINFO)</h3>
<p> <code>CGGSVP</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
CGGSVP computes unitary matrices U, V and Q such that
                                            N -
                                        K - L K L U **H *A *Q = K(0 A12 A13) if M - K - L &gt;= 0;
L(0 0 A23)
M - K - L(0 0 0) N - K - L K L = K(0 A12 A13) if M - K - L &lt; 0;
M - K(0 0 A23) N - K - L K L V **H *B *Q = L(0 0 B13)
                                                   P
                                               - L(0 0 0) where the K - by - K matrix A12
                                           and L - by - L matrix B13 are nonsingular upper triangular; A23 is L-by-L upper triangular if M-K-L &gt;= 0,
 otherwise A23 is (M-K)-by-L upper trapezoidal.  K+L = the effective
 numerical rank of the (M+P)-by-N matrix (A**H,B**H)**H. 
 This decomposition is the preprocessing step for computing the
 Generalized Singular Value Decomposition (GSVD), see subroutine
 CGGSVD.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBU</i> </p>
<pre>
          JOBU is CHARACTER*1
          = 'U':  Unitary matrix U is computed;
          = 'N':  U is not computed.
</pre>
<p> <i>JOBV</i> </p>
<pre>
          JOBV is CHARACTER*1
          = 'V':  Unitary matrix V is computed;
          = 'N':  V is not computed.
</pre>
<p> <i>JOBQ</i> </p>
<pre>
          JOBQ is CHARACTER*1
          = 'Q':  Unitary matrix Q is computed;
          = 'N':  Q is not computed.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre>
<p> <i>P</i> </p>
<pre>
          P is INTEGER
          The number of rows of the matrix B.  P &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrices A and B.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the M-by-N matrix A.
          On exit, A contains the triangular (or trapezoidal) matrix
          described in the Purpose section.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,N)
          On entry, the P-by-N matrix B.
          On exit, B contains the triangular matrix described in
          the Purpose section.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1,P).
</pre>
<p> <i>TOLA</i> </p>
<pre>
          TOLA is REAL
</pre>
<p> <i>TOLB</i> </p>
<pre>
          TOLB is REAL
          TOLA and TOLB are the thresholds to determine the effective
          numerical rank of matrix B and a subblock of A. Generally,
          they are set to
             TOLA = MAX(M,N)*norm(A)*MACHEPS,
             TOLB = MAX(P,N)*norm(B)*MACHEPS.
          The size of TOLA and TOLB may affect the size of backward
          errors of the decomposition.
</pre>
<p> <i>K</i> </p>
<pre>
          K is INTEGER
</pre>
<p> <i>L</i> </p>
<pre>
          L is INTEGER
          On exit, K and L specify the dimension of the subblocks
          described in Purpose section.
          K + L = effective numerical rank of (A**H,B**H)**H.
</pre>
<p> <i>U</i> </p>
<pre>
          U is COMPLEX array, dimension (LDU,M)
          If JOBU = 'U', U contains the unitary matrix U.
          If JOBU = 'N', U is not referenced.
</pre>
<p> <i>LDU</i> </p>
<p>LDU is INTEGER<br />
        The leading dimension of the array U.LDU &gt;= max(1, M) if JOBU = &#8216;U&#8217;;<br />
LDU &gt;= 1 otherwise.</p>
<p> <i>V</i> </p>
<pre>
          V is COMPLEX array, dimension (LDV,P)
          If JOBV = 'V', V contains the unitary matrix V.
          If JOBV = 'N', V is not referenced.
</pre>
<p> <i>LDV</i> </p>
<p>LDV is INTEGER<br />
        The leading dimension of the array V.LDV &gt;= max(1, P) if JOBV = &#8216;V&#8217;;<br />
LDV &gt;= 1 otherwise.</p>
<p> <i>Q</i> </p>
<pre>
          Q is COMPLEX array, dimension (LDQ,N)
          If JOBQ = 'Q', Q contains the unitary matrix Q.
          If JOBQ = 'N', Q is not referenced.
</pre>
<p> <i>LDQ</i> </p>
<pre><code>
LDQ is INTEGER
        The leading dimension of the array Q.LDQ &gt;= max(1, N) if JOBQ = 'Q';
LDQ &gt;= 1 otherwise.
</code></pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (2*N)
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is COMPLEX array, dimension (N)
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (max(3*N,M,P))
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dt>
<dd> Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dt>
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd> The subroutine uses LAPACK subroutine CGEQPF for the QR factorization with column pivoting to detect the effective numerical rank of the a matrix. It may be replaced by a better rank determination strategy.</dl>
<p> Definition at line 259 of file cggsvp.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
