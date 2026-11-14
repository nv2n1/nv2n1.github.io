---
title: "sggev(3)"
name: "sggev"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sggev/"
description: "sggev.f –"
---

<h2 class="name">NAME</h2>
<p> sggev.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sggev</code> (JOBVL, JOBVR, N, A, LDA, B, LDB, ALPHAR, ALPHAI, BETA, VL, LDVL, VR, LDVR, WORK, LWORK, INFO)<br />
 <i></i><code> SGGEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sggev (characterJOBVL, characterJOBVR, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( * )ALPHAR, real, dimension( * )ALPHAI, real, dimension( * )BETA, real, dimension( ldvl, * )VL, integerLDVL, real, dimension( ldvr, * )VR, integerLDVR, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code> SGGEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
 SGGEV computes for a pair of N-by-N real nonsymmetric matrices (A,B)
 the generalized eigenvalues, and optionally, the left and/or right
 generalized eigenvectors.
 A generalized eigenvalue for a pair of matrices (A,B) is a scalar
 lambda or a ratio alpha/beta = lambda, such that A - lambda*B is
 singular. It is usually represented as the pair (alpha,beta), as
 there is a reasonable interpretation for beta=0, and even for both
 being zero.
 The right eigenvector v(j)
 corresponding to the eigenvalue lambda(j)
     of(A, B) satisfies
     A *v(j) = lambda(j) * B * v(j).The left eigenvector u(j)
 corresponding to the eigenvalue lambda(j)
     of(A, B) satisfies
     u(j) **H *A = lambda(j) * u(j) * *H * B.where u(j) * *H is the conjugate - transpose of u(j).
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBVL</i> </p>
<pre>
          JOBVL is CHARACTER*1
          = 'N':  do not compute the left generalized eigenvectors;
          = 'V':  compute the left generalized eigenvectors.
</pre>
<p> <i>JOBVR</i> </p>
<pre>
          JOBVR is CHARACTER*1
          = 'N':  do not compute the right generalized eigenvectors;
          = 'V':  compute the right generalized eigenvectors.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A, B, VL, and VR.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA, N)
          On entry, the matrix A in the pair (A,B).
          On exit, A has been overwritten.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB, N)
          On entry, the matrix B in the pair (A,B).
          On exit, B has been overwritten.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of B.  LDB &gt;= max(1,N).
</pre>
<p> <i>ALPHAR</i> </p>
<pre>
          ALPHAR is REAL array, dimension (N)
</pre>
<p> <i>ALPHAI</i> </p>
<pre>
          ALPHAI is REAL array, dimension (N)
</pre>
<p> <i>BETA</i> </p>
<pre>
          BETA is REAL array, dimension (N)
          On exit, (ALPHAR(j) + ALPHAI(j)*i)/BETA(j), j=1,...,N, will
          be the generalized eigenvalues.  If ALPHAI(j) is zero, then
          the j-th eigenvalue is real; if positive, then the j-th and
          (j+1)-st eigenvalues are a complex conjugate pair, with
          ALPHAI(j+1) negative.
          Note: the quotients ALPHAR(j)/BETA(j) and ALPHAI(j)/BETA(j)
          may easily over- or underflow, and BETA(j) may even be zero.
          Thus, the user should avoid naively computing the ratio
          alpha/beta.  However, ALPHAR and ALPHAI will be always less
          than and usually comparable with norm(A) in magnitude, and
          BETA always less than and usually comparable with norm(B).
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is REAL array, dimension (LDVL,N)
          If JOBVL = 'V', the left eigenvectors u(j) are stored one
          after another in the columns of VL, in the same order as
          their eigenvalues. If the j-th eigenvalue is real, then
          u(j) = VL(:,j), the j-th column of VL. If the j-th and
          (j+1)-th eigenvalues form a complex conjugate pair, then
          u(j) = VL(:,j)+i*VL(:,j+1) and u(j+1) = VL(:,j)-i*VL(:,j+1).
          Each eigenvector is scaled so the largest component has
          abs(real part)+abs(imag. part)=1.
          Not referenced if JOBVL = 'N'.
</pre>
<p> <i>LDVL</i> </p>
<pre>
          LDVL is INTEGER
          The leading dimension of the matrix VL. LDVL &gt;= 1, and
          if JOBVL = 'V', LDVL &gt;= N.
</pre>
<p> <i>VR</i> </p>
<pre>
          VR is REAL array, dimension (LDVR,N)
          If JOBVR = 'V', the right eigenvectors v(j) are stored one
          after another in the columns of VR, in the same order as
          their eigenvalues. If the j-th eigenvalue is real, then
          v(j) = VR(:,j), the j-th column of VR. If the j-th and
          (j+1)-th eigenvalues form a complex conjugate pair, then
          v(j) = VR(:,j)+i*VR(:,j+1) and v(j+1) = VR(:,j)-i*VR(:,j+1).
          Each eigenvector is scaled so the largest component has
          abs(real part)+abs(imag. part)=1.
          Not referenced if JOBVR = 'N'.
</pre>
<p> <i>LDVR</i> </p>
<pre>
          LDVR is INTEGER
          The leading dimension of the matrix VR. LDVR &gt;= 1, and
          if JOBVR = 'V', LDVR &gt;= N.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK.  LWORK &gt;= max(1,8*N).
          For good performance, LWORK must generally be larger.
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
          = 1,...,N:
                The QZ iteration failed.  No eigenvectors have been
                calculated, but ALPHAR(j), ALPHAI(j), and BETA(j)
                should be correct for j=INFO+1,...,N.
          &gt; N:  =N+1: other than QZ iteration failed in SHGEQZ.
                =N+2: error return from STGEVC.
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
<p> Definition at line 226 of file sggev.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
