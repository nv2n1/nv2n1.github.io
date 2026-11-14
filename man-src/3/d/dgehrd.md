---
title: "dgehrd(3)"
name: "dgehrd"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgehrd/"
description: "dgehrd.f –"
---

<h2 class="name">NAME</h2>
<p> dgehrd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgehrd</code> (N, ILO, IHI, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>DGEHRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgehrd (integerN, integerILO, integerIHI, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )TAU, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code>DGEHRD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGEHRD reduces a real general matrix A to upper Hessenberg form H by
 an orthogonal similarity transformation:  Q**T * A * Q = H .
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>ILO</i> </p>
<pre>
          ILO is INTEGER
</pre>
<p> <i>IHI</i> </p>
<pre><code>
IHI is INTEGER
            It is assumed that A is already upper triangular in rows
                and columns 1 : ILO -
                                1 and
    IHI + 1 : N.ILO and IHI are normally
                  set by a previous call to DGEBAL;
otherwise they should be
        set to 1 and
    N respectively.See Further Details.1 &lt;= ILO &lt;= IHI &lt;= N,
    if N &gt; 0;
ILO = 1 and IHI = 0, if N = 0.
</code></pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the N-by-N general matrix to be reduced.
          On exit, the upper triangle and the first subdiagonal of A
          are overwritten with the upper Hessenberg matrix H, and the
          elements below the first subdiagonal, with the array TAU,
          represent the orthogonal matrix Q as a product of elementary
          reflectors. See Further Details.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>TAU</i> </p>
<pre>
          TAU is DOUBLE PRECISION array, dimension (N-1)
          The scalar factors of the elementary reflectors (see Further
          Details). Elements 1:ILO-1 and IHI:N-1 of TAU are set to
          zero.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (LWORK)
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The length of the array WORK.  LWORK &gt;= max(1,N).
          For optimum performance LWORK &gt;= N*NB, where NB is the
          optimal blocksize.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
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
<dd>
<pre>
  The matrix Q is represented as a product of (ihi-ilo) elementary
  reflectors
     Q = H(ilo) H(ilo+1) . . . H(ihi-1).
  Each H(i) has the form
     H(i) = I - tau * v * v**T
  where tau is a real scalar, and v is a real vector with
  v(1:i) = 0, v(i+1) = 1 and v(ihi+1:n) = 0; v(i+2:ihi) is stored on
  exit in A(i+2:ihi,i), and tau in TAU(i).
  The contents of A are illustrated by the following example, with
  n = 7, ilo = 2 and ihi = 6:
  on entry,                        on exit,
  ( a   a   a   a   a   a   a )    (  a   a   h   h   h   h   a )
  (     a   a   a   a   a   a )    (      a   h   h   h   h   a )
  (     a   a   a   a   a   a )    (      h   h   h   h   h   h )
  (     a   a   a   a   a   a )    (      v2  h   h   h   h   h )
  (     a   a   a   a   a   a )    (      v2  v3  h   h   h   h )
  (     a   a   a   a   a   a )    (      v2  v3  v4  h   h   h )
  (                         a )    (                          a )
  where a denotes an element of the original matrix A, h denotes a
  modified element of the upper Hessenberg matrix H, and vi denotes an
  element of the vector defining H(i).
  This file is a slight modification of LAPACK-3.0's DGEHRD
  subroutine incorporating improvements proposed by Quintana-Orti and
  Van de Geijn (2006). (See DLAHR2.)
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 169 of file dgehrd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
