---
title: "ctrsen(3)"
name: "ctrsen"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctrsen/"
description: "ctrsen.f –"
---

<h2 class="name">NAME</h2>
<p> ctrsen.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ctrsen</code> (JOB, COMPQ, SELECT, N, T, LDT, Q, LDQ, W, M, S, SEP, WORK, LWORK, INFO)<br />
 <i></i><code>CTRSEN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctrsen (characterJOB, characterCOMPQ, logical, dimension( * )SELECT, integerN, complex, dimension( ldt, * )T, integerLDT, complex, dimension( ldq, * )Q, integerLDQ, complex, dimension( * )W, integerM, realS, realSEP, complex, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>CTRSEN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CTRSEN reorders the Schur factorization of a complex matrix
 A = Q*T*Q**H, so that a selected cluster of eigenvalues appears in
 the leading positions on the diagonal of the upper triangular matrix
 T, and the leading columns of Q form an orthonormal basis of the
 corresponding right invariant subspace.
 Optionally the routine computes the reciprocal condition numbers of
 the cluster of eigenvalues and/or the invariant subspace.
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
          select the j-th eigenvalue, SELECT(j) must be set to .TRUE..
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix T. N &gt;= 0.
</pre>
<p> <i>T</i> </p>
<pre>
          T is COMPLEX array, dimension (LDT,N)
          On entry, the upper triangular matrix T.
          On exit, T is overwritten by the reordered matrix T, with the
          selected eigenvalues as the leading diagonal elements.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T. LDT &gt;= max(1,N).
</pre>
<p> <i>Q</i> </p>
<p>Q is COMPLEX array, dimension(LDQ, N) On entry, if COMPQ = &#8216;V&#8217;, the matrix Q of Schur vectors.On exit, if COMPQ = &#8216;V&#8217;, Q has been postmultiplied by the unitary transformation matrix which reorders T; the leading M<br />
          columns of Q form an orthonormal basis for the specified<br />
          invariant subspace.<br />
          If COMPQ = &#8216;N&#8217;, Q is not referenced.</p>
<p> <i>LDQ</i> </p>
<p>LDQ is INTEGER<br />
        The leading dimension of the array Q.LDQ &gt;= 1;<br />
and if COMPQ = &#8216;V&#8217;, LDQ &gt;= N.</p>
<p> <i>W</i> </p>
<pre>
          W is COMPLEX array, dimension (N)
          The reordered eigenvalues of T, in the same order as they
          appear on the diagonal of T.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The dimension of the specified invariant subspace.
          0 &lt;= M &lt;= N.
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
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre><code>
LWORK is INTEGER
    The dimension of the array WORK.If JOB = 'N',
                                       LWORK &gt;= 1;
if JOB
    = 'E', LWORK = max(1, M *(N - M));
if JOB
    = 'V' or 'B', LWORK &gt;= max(1, 2 * M * (N - M)).If LWORK = -1, then a workspace query is assumed;
the routine
    only calculates the optimal size of the WORK array,
    returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.
</code></pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<dd>
<pre>
  CTRSEN first collects the selected eigenvalues by computing a unitary
  transformation Z to move them to the top left corner of T. In other
  words, the selected eigenvalues are the eigenvalues of T11 in:
          Z**H * T * Z = ( T11 T12 ) n1
                         (  0  T22 ) n2
                            n1  n2
  where N = n1+n2. The first
  n1 columns of Z span the specified invariant subspace of T.
  If T has been obtained from the Schur factorization of a matrix
  A = Q*T*Q**H, then the reordered Schur factorization of A is given by
  A = (Q*Z)*(Z**H*T*Z)*(Q*Z)**H, and the first n1 columns of Q*Z span the
  corresponding invariant subspace of A.
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
<p> Definition at line 264 of file ctrsen.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
