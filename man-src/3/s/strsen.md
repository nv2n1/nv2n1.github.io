---
title: "strsen(3)"
name: "strsen"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strsen/"
description: "strsen.f –"
---

<h2 class="name">NAME</h2>
<p> strsen.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>strsen</code> (JOB, COMPQ, SELECT, N, T, LDT, Q, LDQ, WR, WI, M, S, SEP, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>STRSEN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine strsen (characterJOB, characterCOMPQ, logical, dimension( * )SELECT, integerN, real, dimension( ldt, * )T, integerLDT, real, dimension( ldq, * )Q, integerLDQ, real, dimension( * )WR, real, dimension( * )WI, integerM, realS, realSEP, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p> <code>STRSEN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 STRSEN reorders the real Schur factorization of a real matrix
 A = Q*T*Q**T, so that a selected cluster of eigenvalues appears in
 the leading diagonal blocks of the upper quasi-triangular matrix T,
 and the leading columns of Q form an orthonormal basis of the
 corresponding right invariant subspace.
 Optionally the routine computes the reciprocal condition numbers of
 the cluster of eigenvalues and/or the invariant subspace.
 T must be in Schur canonical form (as returned by SHSEQR), that is,
 block upper triangular with 1-by-1 and 2-by-2 diagonal blocks; each
 2-by-2 diagonal block has its diagonal elements equal and its
 off-diagonal elements of opposite sign.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOB</i> </p>
<pre><code>
          JOB is CHARACTER*1
          Specifies whether condition numbers are required for the
          cluster of eigenvalues (S) or the invariant subspace (SEP):
          = 'N': none;
          = 'E': for eigenvalues only (S);
          = 'V': for invariant subspace only (SEP);
          = 'B': for both eigenvalues and invariant subspace (S and
                 SEP).
</code></pre>
<p> <i>COMPQ</i> </p>
<pre>
          COMPQ is CHARACTER*1
          = 'V': update the matrix Q of Schur vectors;
          = 'N': do not update Q.
</pre>
<p> <i>SELECT</i> </p>
<pre>
          SELECT is LOGICAL array, dimension (N)
          SELECT specifies the eigenvalues in the selected cluster. To
          select a real eigenvalue w(j), SELECT(j) must be set to
          .TRUE.. To select a complex conjugate pair of eigenvalues
          w(j) and w(j+1), corresponding to a 2-by-2 diagonal block,
          either SELECT(j) or SELECT(j+1) or both must be set to
          .TRUE.; a complex conjugate pair of eigenvalues must be
          either both included in the cluster or both excluded.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix T. N &gt;= 0.
</pre>
<p> <i>T</i> </p>
<pre>
          T is REAL array, dimension (LDT,N)
          On entry, the upper quasi-triangular matrix T, in Schur
          canonical form.
          On exit, T is overwritten by the reordered matrix T, again in
          Schur canonical form, with the selected eigenvalues in the
          leading diagonal blocks.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T. LDT &gt;= max(1,N).
</pre>
<p> <i>Q</i> </p>
<p>Q is REAL array, dimension(LDQ, N) On entry, if COMPQ = &#8216;V&#8217;, the matrix Q of Schur vectors.On exit, if COMPQ = &#8216;V&#8217;, Q has been postmultiplied by the orthogonal transformation matrix which reorders T; the<br />
          leading M columns of Q form an orthonormal basis for the<br />
          specified invariant subspace.<br />
          If COMPQ = &#8216;N&#8217;, Q is not referenced.</p>
<p> <i>LDQ</i> </p>
<p>LDQ is INTEGER<br />
        The leading dimension of the array Q.LDQ &gt;= 1;<br />
and if COMPQ = &#8216;V&#8217;, LDQ &gt;= N.</p>
<p> <i>WR</i> </p>
<pre>
          WR is REAL array, dimension (N)
</pre>
<p> <i>WI</i> </p>
<pre>
          WI is REAL array, dimension (N)
          The real and imaginary parts, respectively, of the reordered
          eigenvalues of T. The eigenvalues are stored in the same
          order as on the diagonal of T, with WR(i) = T(i,i) and, if
          T(i:i+1,i:i+1) is a 2-by-2 diagonal block, WI(i) &gt; 0 and
          WI(i+1) = -WI(i). Note that if a complex eigenvalue is
          sufficiently ill-conditioned, then its value may differ
          significantly from its value before reordering.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The dimension of the specified invariant subspace.
          0 &lt; = M &lt;= N.
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL
          If JOB = 'E' or 'B', S is a lower bound on the reciprocal
          condition number for the selected cluster of eigenvalues.
          S cannot underestimate the true reciprocal condition number
          by more than a factor of sqrt(N). If M = 0 or N, S = 1.
          If JOB = 'N' or 'V', S is not referenced.
</pre>
<p> <i>SEP</i> </p>
<pre>
          SEP is REAL
          If JOB = 'V' or 'B', SEP is the estimated reciprocal
          condition number of the specified invariant subspace. If
          M = 0 or N, SEP = norm(T).
          If JOB = 'N' or 'E', SEP is not referenced.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>LWORK is INTEGER<br />
    The dimension of the array WORK.If JOB = &#8216;N&#8217;,<br />
                                       LWORK &gt;= max(1, N);<br />
if JOB<br />
    = &#8216;E&#8217;, LWORK &gt;= max(1, M *(N &#8211; M));<br />
if JOB<br />
    = &#8216;V&#8217; or &#8216;B&#8217;, LWORK &gt;= max(1, 2 * M * (N &#8211; M)).If LWORK = -1, then a workspace query is assumed;<br />
the routine<br />
    only calculates the optimal size of the WORK array,<br />
    returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.</p>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.
</pre>
<p> <i>LIWORK</i> </p>
<p>LIWORK is INTEGER<br />
    The dimension of the array IWORK.If JOB = &#8216;N&#8217; or &#8216;E&#8217;,<br />
                                        LIWORK &gt;= 1;<br />
if JOB<br />
    = &#8216;V&#8217; or &#8216;B&#8217;, LIWORK &gt;= max(1, M *(N &#8211; M)).If LIWORK = -1, then a workspace query is assumed;<br />
the<br />
    routine only calculates the optimal size of the IWORK array,<br />
    returns this value as the first entry of the IWORK array, and no error message related to LIWORK is issued by XERBLA.</p>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value = 1 : reordering of T failed because some eigenvalues are too
                                                                                                             close to
                                                                                                             separate(the problem is very ill - conditioned);
T may have been partially reordered, and WR and WI
                                         contain the eigenvalues in the same order as in T;
S and
    SEP(if requested) are set to zero.
</code></pre>
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
  STRSEN first collects the selected eigenvalues by computing an
  orthogonal transformation Z to move them to the top left corner of T.
  In other words, the selected eigenvalues are the eigenvalues of T11
  in:
          Z**T * T * Z = ( T11 T12 ) n1
                         (  0  T22 ) n2
                            n1  n2
  where N = n1+n2 and Z**T means the transpose of Z. The first n1 columns
  of Z span the specified invariant subspace of T.
  If T has been obtained from the real Schur factorization of a matrix
  A = Q*T*Q**T, then the reordered real Schur factorization of A is given
  by A = (Q*Z)*(Z**T*T*Z)*(Q*Z)**T, and the first n1 columns of Q*Z span
  the corresponding invariant subspace of A.
  The reciprocal condition number of the average of the eigenvalues of
  T11 may be returned in S. S lies between 0 (very badly conditioned)
  and 1 (very well conditioned). It is computed as follows. First we
  compute R so that
                         P = ( I  R ) n1
                             ( 0  0 ) n2
                               n1 n2
  is the projector on the invariant subspace associated with T11.
  R is the solution of the Sylvester equation:
                        T11*R - R*T22 = T12.
  Let F-norm(M) denote the Frobenius-norm of M and 2-norm(M) denote
  the two-norm of M. Then S is computed as the lower bound
                      (1 + F-norm(R)**2)**(-1/2)
  on the reciprocal of 2-norm(P), the true reciprocal condition number.
  S cannot underestimate 1 / 2-norm(P) by more than a factor of
  sqrt(N).
  An approximate error bound for the computed average of the
  eigenvalues of T11 is
                         EPS * norm(T) / S
  where EPS is the machine precision.
  The reciprocal condition number of the right invariant subspace
  spanned by the first n1 columns of Z (or of Q*Z) is returned in SEP.
  SEP is defined as the separation of T11 and T22:
                     sep( T11, T22 ) = sigma-min( C )
  where sigma-min(C) is the smallest singular value of the
  n1*n2-by-n1*n2 matrix
     C  = kprod( I(n2), T11 ) - kprod( transpose(T22), I(n1) )
  I(m) is an m by m identity matrix, and kprod denotes the Kronecker
  product. We estimate sigma-min(C) by the reciprocal of an estimate of
  the 1-norm of inverse(C). The true reciprocal 1-norm of inverse(C)
  cannot differ from sigma-min(C) by more than a factor of sqrt(n1*n2).
  When SEP is small, small changes in T can cause large changes in
  the invariant subspace. An approximate bound on the maximum angular
  error in the computed right invariant subspace is
                      EPS * norm(T) / SEP
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 314 of file strsen.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
