---
title: "chgeqz(3)"
name: "chgeqz"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chgeqz/"
description: "chgeqz.f –"
---

<h2 class="name">NAME</h2>
<p> chgeqz.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chgeqz</code> (JOB, COMPQ, COMPZ, N, ILO, IHI, H, LDH, T, LDT, ALPHA, BETA, Q, LDQ, Z, LDZ, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code>CHGEQZ</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chgeqz (characterJOB, characterCOMPQ, characterCOMPZ, integerN, integerILO, integerIHI, complex, dimension( ldh, * )H, integerLDH, complex, dimension( ldt, * )T, integerLDT, complex, dimension( * )ALPHA, complex, dimension( * )BETA, complex, dimension( ldq, * )Q, integerLDQ, complex, dimension( ldz, * )Z, integerLDZ, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code>CHGEQZ</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
CHGEQZ computes the eigenvalues of a complex matrix pair(H, T),
    where H is an upper Hessenberg matrix and T is upper triangular,
    using the single - shift QZ method.Matrix pairs of this type are produced by the reduction to
                       generalized upper Hessenberg form of a complex matrix pair(A, B)
    :

      A = Q1 * H * Z1 * *H,
      B = Q1 * T * Z1 * *H,

      as computed by CGGHRD.

      If JOB = 'S',
      then the Hessenberg - triangular pair(H, T)
is
    also reduced to generalized Schur form,

    H = Q * S * Z * *H, T = Q * P * Z * *H,

    where Q and Z are unitary matrices and S and P are upper triangular.

    Optionally,
    the unitary matrix Q from the generalized Schur
        factorization may be postmultiplied into an input matrix Q1,
    and the
            unitary matrix Z may be postmultiplied into an input matrix Z1.If Q1 and Z1 are the unitary matrices from CGGHRD that reduced
                the matrix
                pair(A, B)
to generalized Hessenberg form, then the output matrices Q1 *Q and Z1 *Z are the unitary factors from the generalized Schur factorization of(A, B)
    :

      A = (Q1 * Q) * S * (Z1 * Z) * *H,
      B = (Q1 * Q) * P * (Z1 * Z) * *H.

                                     To avoid overflow,
      eigenvalues of the matrix pair(H, T)(equivalently, of(A, B)) are computed as a pair of complex values(alpha, beta).If beta is nonzero, lambda = alpha / beta is an
                                                                                                                                                      eigenvalue of the generalized nonsymmetric eigenvalue problem(GNEP)
    A*x = lambda*B*x
 and if alpha is nonzero, mu = beta / alpha is an eigenvalue of the
 alternate form of the GNEP
    mu*A*y = B*y.
 The values of alpha and beta for the i-th eigenvalue can be read
 directly from the generalized Schur form:  alpha = S(i,i),
 beta = P(i,i).
 Ref: C.B. Moler &amp; G.W. Stewart, "An Algorithm for Generalized Matrix
      Eigenvalue Problems", SIAM J. Numer. Anal., 10(1973),
      pp. 241--256.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOB</i> </p>
<pre>
          JOB is CHARACTER*1
          = 'E': Compute eigenvalues only;
          = 'S': Computer eigenvalues and the Schur form.
</pre>
<p> <i>COMPQ</i> </p>
<p>COMPQ is CHARACTER * 1 = &#8216;N&#8217; : Left Schur vectors(Q)<br />
are not computed;<br />
= &#8216;I&#8217; : Q is initialized to the unit matrix and the matrix Q<br />
                                                    of left Schur vectors<br />
                                                    of(H, T)<br />
is returned;<br />
= &#8216;V&#8217; : Q must contain a unitary matrix Q1 on entry and<br />
        the product Q1 * Q is returned.</p>
<p> <i>COMPZ</i> </p>
<p>COMPZ is CHARACTER * 1 = &#8216;N&#8217; : Right Schur vectors(Z)<br />
are not computed;<br />
= &#8216;I&#8217; : Q is initialized to the unit matrix and the matrix Z<br />
                                                    of right Schur vectors<br />
                                                    of(H, T)<br />
is returned;<br />
= &#8216;V&#8217; : Z must contain a unitary matrix Z1 on entry and<br />
        the product Z1 * Z is returned.</p>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices H, T, Q, and Z.  N &gt;= 0.
</pre>
<p> <i>ILO</i> </p>
<pre>
          ILO is INTEGER
</pre>
<p> <i>IHI</i> </p>
<pre>
          IHI is INTEGER
          ILO and IHI mark the rows and columns of H which are in
          Hessenberg form.  It is assumed that A is already upper
          triangular in rows and columns 1:ILO-1 and IHI+1:N.
          If N &gt; 0, 1 &lt;= ILO &lt;= IHI &lt;= N; if N = 0, ILO=1 and IHI=0.
</pre>
<p> <i>H</i> </p>
<pre>
          H is COMPLEX array, dimension (LDH, N)
          On entry, the N-by-N upper Hessenberg matrix H.
          On exit, if JOB = 'S', H contains the upper triangular
          matrix S from the generalized Schur factorization.
          If JOB = 'E', the diagonal of H matches that of S, but
          the rest of H is unspecified.
</pre>
<p> <i>LDH</i> </p>
<pre>
          LDH is INTEGER
          The leading dimension of the array H.  LDH &gt;= max( 1, N ).
</pre>
<p> <i>T</i> </p>
<pre>
          T is COMPLEX array, dimension (LDT, N)
          On entry, the N-by-N upper triangular matrix T.
          On exit, if JOB = 'S', T contains the upper triangular
          matrix P from the generalized Schur factorization.
          If JOB = 'E', the diagonal of T matches that of P, but
          the rest of T is unspecified.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T.  LDT &gt;= max( 1, N ).
</pre>
<p> <i>ALPHA</i> </p>
<pre>
          ALPHA is COMPLEX array, dimension (N)
          The complex scalars alpha that define the eigenvalues of
          GNEP.  ALPHA(i) = S(i,i) in the generalized Schur
          factorization.
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is COMPLEX array, dimension (N)
          The real non-negative scalars beta that define the
          eigenvalues of GNEP.  BETA(i) = P(i,i) in the generalized
          Schur factorization.
          Together, the quantities alpha = ALPHA(j) and beta = BETA(j)
          represent the j-th eigenvalue of the matrix pair (A,B), in
          one of the forms lambda = alpha/beta or mu = beta/alpha.
          Since either lambda or mu may overflow, they should not,
          in general, be computed.
</pre>
<p> <i>Q</i> </p>
<p>Q is COMPLEX array, dimension(LDQ, N) On entry, if COMPZ = &#8216;V&#8217;, the unitary matrix Q1 used in the reduction of(A, B)<br />
to generalized Hessenberg form.On exit, if COMPZ = &#8216;I&#8217;, the unitary matrix of left Schur vectors of(H, T), and if COMPZ = &#8216;V&#8217;, the unitary matrix of left Schur vectors of(A, B).Not referenced if COMPZ = &#8216;N&#8217;.</p>
<p> <i>LDQ</i> </p>
<pre>
          LDQ is INTEGER
          The leading dimension of the array Q.  LDQ &gt;= 1.
          If COMPQ='V' or 'I', then LDQ &gt;= N.
</pre>
<p> <i>Z</i> </p>
<pre><code>
Z is COMPLEX array, dimension(LDZ, N) On entry, if COMPZ = 'V', the unitary matrix Z1 used in the reduction of(A, B)
to generalized Hessenberg form.On exit, if COMPZ = 'I', the unitary matrix of right Schur vectors of(H, T), and if COMPZ = 'V', the unitary matrix of right Schur vectors of(A, B).Not referenced if COMPZ = 'N'.
</code></pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1.
          If COMPZ='V' or 'I', then LDZ &gt;= N.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO &gt;= 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.  LWORK &gt;= max(1,N).
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          = 1,...,N: the QZ iteration did not converge.  (H,T) is not
                     in Schur form, but ALPHA(i) and BETA(i),
                     i=INFO+1,...,N should be correct.
          = N+1,...,2*N: the shift calculation failed.  (H,T) is not
                     in Schur form, but ALPHA(i) and BETA(i),
                     i=INFO-N+1,...,N should be correct.
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
<dd> April 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  We assume that complex ABS works as long as its value is less than
  overflow.
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 283 of file chgeqz.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
