---
title: "dgghrd(3)"
name: "dgghrd"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgghrd/"
description: "dgghrd.f –"
---

<h2 class="name">NAME</h2>
<p> dgghrd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgghrd</code> (COMPQ, COMPZ, N, ILO, IHI, A, LDA, B, LDB, Q, LDQ, Z, LDZ, INFO)<br />
 <i></i><code>DGGHRD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgghrd (characterCOMPQ, characterCOMPZ, integerN, integerILO, integerIHI, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldq, * )Q, integerLDQ, double precision, dimension( ldz, * )Z, integerLDZ, integerINFO)</h3>
<p> <code>DGGHRD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGGHRD reduces a pair of real matrices (A,B) to generalized upper
 Hessenberg form using orthogonal transformations, where A is a
 general matrix and B is upper triangular.  The form of the
 generalized eigenvalue problem is
    A*x = lambda*B*x,
 and B is typically made upper triangular by computing its QR
 factorization and moving the orthogonal matrix Q to the left side
 of the equation.
 This subroutine simultaneously reduces A to a Hessenberg matrix H:
    Q**T*A*Z = H
 and transforms B to another upper triangular matrix T:
    Q**T*B*Z = T
 in order to reduce the problem to its standard form
    H*y = lambda*T*y
 where y = Z**T*x.
 The orthogonal matrices Q and Z are determined as products of Givens
 rotations.  They may either be formed explicitly, or they may be
 postmultiplied into input matrices Q1 and Z1, so that
      Q1 * A * Z1**T = (Q1*Q) * H * (Z1*Z)**T
      Q1 * B * Z1**T = (Q1*Q) * T * (Z1*Z)**T
 If Q1 is the orthogonal matrix from the QR factorization of B in the
 original equation A*x = lambda*B*x, then DGGHRD reduces the original
 problem to generalized Hessenberg form.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>COMPQ</i> </p>
<pre>
          COMPQ is CHARACTER*1
          = 'N': do not compute Q;
          = 'I': Q is initialized to the unit matrix, and the
                 orthogonal matrix Q is returned;
          = 'V': Q must contain an orthogonal matrix Q1 on entry,
                 and the product Q1*Q is returned.
</pre>
<p> <i>COMPZ</i> </p>
<pre>
          COMPZ is CHARACTER*1
          = 'N': do not compute Z;
          = 'I': Z is initialized to the unit matrix, and the
                 orthogonal matrix Z is returned;
          = 'V': Z must contain an orthogonal matrix Z1 on entry,
                 and the product Z1*Z is returned.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A and B.  N &gt;= 0.
</pre>
<p> <i>ILO</i> </p>
<pre>
          ILO is INTEGER
</pre>
<p> <i>IHI</i> </p>
<pre><code>
IHI is INTEGER
            ILO and IHI mark the rows and columns of A which are to be
                reduced.It is assumed that A is already upper triangular
                    in rows and columns 1 : ILO -
        1 and
    IHI + 1 : N.ILO and IHI are
                  normally set by a previous call to DGGBAL;
otherwise they
        should be set to 1 and
    N respectively.1 &lt;= ILO &lt;= IHI &lt;= N,
    if N &gt; 0;
ILO = 1 and IHI = 0, if N = 0.
</code></pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA, N)
          On entry, the N-by-N general matrix to be reduced.
          On exit, the upper triangle and the first subdiagonal of A
          are overwritten with the upper Hessenberg matrix H, and the
          rest is set to zero.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB, N)
          On entry, the N-by-N upper triangular matrix B.
          On exit, the upper triangular matrix T = Q**T B Z.  The
          elements below the diagonal are set to zero.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,N).
</pre>
<p> <i>Q</i> </p>
<p>Q is DOUBLE PRECISION array, dimension(LDQ, N) On entry, if COMPQ = &#8216;V&#8217;, the orthogonal matrix Q1,<br />
                                                            typically from the QR factorization of B.On exit, if COMPQ = &#8216;I&#8217;, the orthogonal matrix Q, and if COMPQ = &#8216;V&#8217;, the product Q1 *Q.Not referenced if COMPQ = &#8216;N&#8217;.</p>
<p> <i>LDQ</i> </p>
<p>LDQ is INTEGER<br />
        The leading dimension of the array Q.LDQ &gt;= N if COMPQ = &#8216;V&#8217; or &#8216;I&#8217;;<br />
LDQ &gt;= 1 otherwise.</p>
<p> <i>Z</i> </p>
<p>Z is DOUBLE PRECISION array, dimension(LDZ, N) On entry, if COMPZ = &#8216;V&#8217;, the orthogonal matrix Z1.On exit, if COMPZ = &#8216;I&#8217;, the orthogonal matrix Z, and if COMPZ = &#8216;V&#8217;, the product Z1 *Z.Not referenced if COMPZ = &#8216;N&#8217;.</p>
<p> <i>LDZ</i> </p>
<pre><code>
LDZ is INTEGER
        The leading dimension of the array Z.LDZ &gt;= N if COMPZ = 'V' or 'I';
LDZ &gt;= 1 otherwise.
</code></pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
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
  This routine reduces A to Hessenberg and B to triangular form by
  an unblocked reduction, as described in _Matrix_Computations_,
  by Golub and Van Loan (Johns Hopkins Press.)
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 207 of file dgghrd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
