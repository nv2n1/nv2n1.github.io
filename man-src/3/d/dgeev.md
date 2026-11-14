---
title: "dgeev(3)"
name: "dgeev"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgeev/"
description: "dgeev.f –"
---

<h2 class="name">NAME</h2>
<p> dgeev.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dgeev</code> (JOBVL, JOBVR, N, A, LDA, WR, WI, VL, LDVL, VR, LDVR, WORK, LWORK, INFO)<br />
 <i></i><code> DGEEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgeev (characterJOBVL, characterJOBVR, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( * )WR, double precision, dimension( * )WI, double precision, dimension( ldvl, * )VL, integerLDVL, double precision, dimension( ldvr, * )VR, integerLDVR, double precision, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code> DGEEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DGEEV computes for an N-by-N real nonsymmetric matrix A, the
 eigenvalues and, optionally, the left and/or right eigenvectors.
 The right eigenvector v(j) of A satisfies
                  A * v(j) = lambda(j) * v(j)
 where lambda(j) is its eigenvalue.
 The left eigenvector u(j) of A satisfies
               u(j)**H * A = lambda(j) * u(j)**H
 where u(j)**H denotes the conjugate-transpose of u(j).
 The computed eigenvectors are normalized to have Euclidean norm
 equal to 1 and largest component real.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBVL</i> </p>
<pre>
          JOBVL is CHARACTER*1
          = 'N': left eigenvectors of A are not computed;
          = 'V': left eigenvectors of A are computed.
</pre>
<p> <i>JOBVR</i> </p>
<pre>
          JOBVR is CHARACTER*1
          = 'N': right eigenvectors of A are not computed;
          = 'V': right eigenvectors of A are computed.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A. N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          On entry, the N-by-N matrix A.
          On exit, A has been overwritten.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>WR</i> </p>
<pre>
          WR is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>WI</i> </p>
<pre>
          WI is DOUBLE PRECISION array, dimension (N)
          WR and WI contain the real and imaginary parts,
          respectively, of the computed eigenvalues.  Complex
          conjugate pairs of eigenvalues appear consecutively
          with the eigenvalue having the positive imaginary part
          first.
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is DOUBLE PRECISION array, dimension (LDVL,N)
          If JOBVL = 'V', the left eigenvectors u(j) are stored one
          after another in the columns of VL, in the same order
          as their eigenvalues.
          If JOBVL = 'N', VL is not referenced.
          If the j-th eigenvalue is real, then u(j) = VL(:,j),
          the j-th column of VL.
          If the j-th and (j+1)-st eigenvalues form a complex
          conjugate pair, then u(j) = VL(:,j) + i*VL(:,j+1) and
          u(j+1) = VL(:,j) - i*VL(:,j+1).
</pre>
<p> <i>LDVL</i> </p>
<pre><code>
LDVL is INTEGER
        The leading dimension of the array VL.LDVL &gt;= 1;
if JOBVL
= 'V', LDVL &gt;= N.
</code></pre>
<p> <i>VR</i> </p>
<pre>
          VR is DOUBLE PRECISION array, dimension (LDVR,N)
          If JOBVR = 'V', the right eigenvectors v(j) are stored one
          after another in the columns of VR, in the same order
          as their eigenvalues.
          If JOBVR = 'N', VR is not referenced.
          If the j-th eigenvalue is real, then v(j) = VR(:,j),
          the j-th column of VR.
          If the j-th and (j+1)-st eigenvalues form a complex
          conjugate pair, then v(j) = VR(:,j) + i*VR(:,j+1) and
          v(j+1) = VR(:,j) - i*VR(:,j+1).
</pre>
<p> <i>LDVR</i> </p>
<p>LDVR is INTEGER<br />
        The leading dimension of the array VR.LDVR &gt;= 1;<br />
if JOBVR<br />
= &#8216;V&#8217;, LDVR &gt;= N.</p>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre><code>
LWORK is INTEGER
        The dimension of the array WORK.LWORK &gt;= max(1, 3 * N),
    and if JOBVL = 'V' or JOBVR = 'V', LWORK &gt;= 4 * N.For good performance, LWORK must generally be larger.If LWORK = -1, then a workspace query is assumed;
the routine
    only calculates the optimal size of the WORK array,
    returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.
</code></pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  if INFO = i, the QR algorithm failed to compute all the
                eigenvalues, and no eigenvectors have been computed;
                elements i+1:N of WR and WI contain eigenvalues which
                have converged.
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
<dd> September 2012</dl>
<p> Definition at line 189 of file dgeev.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
