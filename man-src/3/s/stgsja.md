---
title: "stgsja(3)"
name: "stgsja"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stgsja/"
description: "stgsja.f –"
---

<h2 class="name">NAME</h2>
<p> stgsja.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>stgsja</code> (JOBU, JOBV, JOBQ, M, P, N, K, L, A, LDA, B, LDB, TOLA, TOLB, ALPHA, BETA, U, LDU, V, LDV, Q, LDQ, WORK, NCYCLE, INFO)<br />
 <i></i><code>STGSJA</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stgsja (characterJOBU, characterJOBV, characterJOBQ, integerM, integerP, integerN, integerK, integerL, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, realTOLA, realTOLB, real, dimension( * )ALPHA, real, dimension( * )BETA, real, dimension( ldu, * )U, integerLDU, real, dimension( ldv, * )V, integerLDV, real, dimension( ldq, * )Q, integerLDQ, real, dimension( * )WORK, integerNCYCLE, integerINFO)</h3>
<p> <code>STGSJA</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
STGSJA computes the generalized singular value decomposition(GSVD)
of two real upper triangular(or trapezoidal) matrices A and B.On entry, it is assumed that matrices A and B have the following forms, which may be obtained by the preprocessing subroutine SGGSVP from a general M - by - N matrix A and P - by - N matrix B : N - K - L K L A = K(0 A12 A13) if M - K - L &gt;= 0;
L(0 0 A23)
M - K - L(0 0 0) N - K - L K L A = K(0 A12 A13) if M - K - L &lt; 0;
M - K(0 0 A23) N - K - L K L B = L(0 0 B13)
                                         P
                                     - L(0 0 0) where the K - by - K matrix A12
                                 and L - by - L matrix B13 are nonsingular upper triangular;
A23 is L - by - L upper triangular if M - K - L &gt;= 0,
    otherwise A23 is(M - K) - by - L upper trapezoidal.On exit,
    U **T *A *Q = D1 * (0 R), V **T *B *Q = D2 * (0 R),
             where U, V and Q are orthogonal matrices.R is a nonsingular upper triangular matrix, and D1 and D2 are
 ``diagonal'' matrices, which are of the following structures : If M - K - L &gt;= 0,
             K L
             D1 = K(I 0)
                      L(0 C)
                          M
                  - K - L(0 0) K L D2 = L(0 S)
                                            P
                                        - L(0 0) N - K - L K L(0 R) = K(0 R11 R12) K
             L(0 0 R22) L
             where
             C = diag(ALPHA(K + 1), ..., ALPHA(K + L)),
             S = diag(BETA(K + 1), ..., BETA(K + L)),
             C ** 2 + S ** 2 = I.R is stored in A(1
                                                  : K + L, N - K - L + 1
                                                  : N) on exit.If M
                                   - K - L &lt;
                               0,
             K M - K K + L - M D1 = K(I 0 0)
                                        M
                                    - K(0 C 0) K M - K K + L - M D2 = M - K(0 S 0) K + L - M(0 0 I) P - L(0 0 0) N - K - L K M - K K + L - M(0 R) = K(0 R11 R12 R13)
                                                                                                                                                        M
                                                                                                                                                    - K(0 0 R22 R23) K + L - M(0 0 0 R33) where C = diag(ALPHA(K + 1), ..., ALPHA(M)),
             S = diag(BETA(K + 1), ..., BETA(M)),
             C ** 2 + S ** 2 = I.R = (R11 R12 R13)is stored in A(1
                                                                 : M, N - K - L + 1
                                                                 : N) and
                                     R33 is stored(0 R22 R23)
                                         in B(M - K + 1
                                              : L, N + M - K - L + 1
                                              : N) on exit.The computation of the orthogonal transformation matrices U,
             V or Q
                  is optional.These matrices may either be formed explicitly,
             or they
                 may be postmultiplied into input matrices U1,
             V1, or Q1.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBU</i> </p>
<pre>
          JOBU is CHARACTER*1
          = 'U':  U must contain an orthogonal matrix U1 on entry, and
                  the product U1*U is returned;
          = 'I':  U is initialized to the unit matrix, and the
                  orthogonal matrix U is returned;
          = 'N':  U is not computed.
</pre>
<p> <i>JOBV</i> </p>
<pre>
          JOBV is CHARACTER*1
          = 'V':  V must contain an orthogonal matrix V1 on entry, and
                  the product V1*V is returned;
          = 'I':  V is initialized to the unit matrix, and the
                  orthogonal matrix V is returned;
          = 'N':  V is not computed.
</pre>
<p> <i>JOBQ</i> </p>
<pre>
          JOBQ is CHARACTER*1
          = 'Q':  Q must contain an orthogonal matrix Q1 on entry, and
                  the product Q1*Q is returned;
          = 'I':  Q is initialized to the unit matrix, and the
                  orthogonal matrix Q is returned;
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
<p> <i>K</i> </p>
<pre>
          K is INTEGER
</pre>
<p> <i>L</i> </p>
<pre>
          L is INTEGER
          K and L specify the subblocks in the input matrices A and B:
          A23 = A(K+1:MIN(K+L,M),N-L+1:N) and B13 = B(1:L,N-L+1:N)
          of A and B, whose GSVD is going to be computed by STGSJA.
          See Further Details.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          On entry, the M-by-N matrix A.
          On exit, A(N-K+1:N,1:MIN(K+L,M) ) contains the triangular
          matrix R or part of R.  See Purpose for details.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,N)
          On entry, the P-by-N matrix B.
          On exit, if necessary, B(M-K+1:L,N+M-K-L+1:N) contains
          a part of R.  See Purpose for details.
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
          TOLA and TOLB are the convergence criteria for the Jacobi-
          Kogbetliantz iteration procedure. Generally, they are the
          same as used in the preprocessing step, say
              TOLA = max(M,N)*norm(A)*MACHEPS,
              TOLB = max(P,N)*norm(B)*MACHEPS.
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is REAL array, dimension (N)
</pre>
<p> <i>BETA</i> </p>
<p>BETA is REAL array, dimension(N) On exit, ALPHA and BETA contain the generalized singular value pairs of A and B;<br />
ALPHA(1<br />
      : K) = 1,<br />
        BETA(1<br />
             : K) = 0,<br />
        and if M &#8211; K &#8211; L &gt;= 0,<br />
        ALPHA(K + 1<br />
              : K + L) = diag(C),<br />
        BETA(K + 1<br />
             : K + L) = diag(S),<br />
        or if M &#8211; K &#8211; L &lt; 0,<br />
        ALPHA(K + 1<br />
              : M) = C,<br />
        ALPHA(M + 1<br />
              : K + L) = 0 BETA(K + 1<br />
                                : M) = S,<br />
        BETA(M + 1<br />
             : K + L) = 1. Furthermore,<br />
        if K + L &lt; N,<br />
        ALPHA(K + L + 1<br />
              : N) = 0 and<br />
                     BETA(K + L + 1<br />
                          : N) = 0.</p>
<p> <i>U</i> </p>
<p>U is REAL array, dimension(LDU, M) On entry, if JOBU = &#8216;U&#8217;, U must contain a matrix U1(usually the orthogonal matrix returned by SGGSVP).On exit,<br />
                                                if JOBU = &#8216;I&#8217;, U contains the orthogonal matrix U;<br />
if JOBU<br />
= &#8216;U&#8217;, U contains the product U1 *U.If JOBU = &#8216;N&#8217;, U is not referenced.</p>
<p> <i>LDU</i> </p>
<p>LDU is INTEGER<br />
        The leading dimension of the array U.LDU &gt;= max(1, M) if JOBU = &#8216;U&#8217;;<br />
LDU &gt;= 1 otherwise.</p>
<p> <i>V</i> </p>
<p>V is REAL array, dimension(LDV, P) On entry, if JOBV = &#8216;V&#8217;, V must contain a matrix V1(usually the orthogonal matrix returned by SGGSVP).On exit,<br />
                                                if JOBV = &#8216;I&#8217;, V contains the orthogonal matrix V;<br />
if JOBV<br />
= &#8216;V&#8217;, V contains the product V1 *V.If JOBV = &#8216;N&#8217;, V is not referenced.</p>
<p> <i>LDV</i> </p>
<p>LDV is INTEGER<br />
        The leading dimension of the array V.LDV &gt;= max(1, P) if JOBV = &#8216;V&#8217;;<br />
LDV &gt;= 1 otherwise.</p>
<p> <i>Q</i> </p>
<p>Q is REAL array, dimension(LDQ, N) On entry, if JOBQ = &#8216;Q&#8217;, Q must contain a matrix Q1(usually the orthogonal matrix returned by SGGSVP).On exit,<br />
                                                if JOBQ = &#8216;I&#8217;, Q contains the orthogonal matrix Q;<br />
if JOBQ<br />
= &#8216;Q&#8217;, Q contains the product Q1 *Q.If JOBQ = &#8216;N&#8217;, Q is not referenced.</p>
<p> <i>LDQ</i> </p>
<p>LDQ is INTEGER<br />
        The leading dimension of the array Q.LDQ &gt;= max(1, N) if JOBQ = &#8216;Q&#8217;;<br />
LDQ &gt;= 1 otherwise.</p>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (2*N)
</pre>
<p> <i>NCYCLE</i> </p>
<pre>
          NCYCLE is INTEGER
          The number of cycles required for convergence.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          = 1:  the procedure does not converge after MAXIT cycles.
</pre>
</dl>
<pre><code>
Internal Parameters == == == == == == == == == =
                                                   MAXIT INTEGER
                                                       MAXIT specifies the total loops that the iterative procedure
                                                           may take.If after MAXIT cycles,
                                            the routine fails to
                                                converge,
                                            we return INFO = 1..fi

                                                             Author : Univ.of Tennessee
                                                                          Univ.of California Berkeley
                                                                              Univ.of Colorado Denver
                                                                                  NAG Ltd.

                                                                      Date : November 2011

                                                                             Further Details :

    STGSJA essentially uses a variant of Kogbetliantz algorithm to reduce
        min(L, M - K) - by - L triangular(or trapezoidal) matrix A23 and L -
                                                             by - L matrix B13 to the form : U1 **T *A13 *Q1 = C1 * R1;
V1 **T *B13 *Q1 = S1 * R1,
            where U1, V1 and Q1 are orthogonal matrix, and Z **T is the transpose of Z.C1 and S1 are diagonal matrices satisfying C1 ** 2 + S1 ** 2 = I,
            and R1 is an L - by - L nonsingular upper triangular matrix.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 377 of file stgsja.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
