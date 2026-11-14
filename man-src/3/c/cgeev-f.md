---
title: "cgeev-f(3)"
name: "cgeev-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgeev-f/"
description: "cgeev.f –"
---

<p>cgeev.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgeev</code> (JOBVL, JOBVR, N, A, LDA, W, VL, LDVL, VR, LDVR, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code> CGEEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgeev (characterJOBVL, characterJOBVR, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( * )W, complex, dimension( ldvl, * )VL, integerLDVL, complex, dimension( ldvr, * )VR, integerLDVR, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code> CGEEV computes the eigenvalues and, optionally, the left and/or right eigenvectors for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGEEV computes for an N-by-N complex nonsymmetric matrix A, the
 eigenvalues and, optionally, the left and/or right eigenvectors.
 The right eigenvector v(j) of A satisfies
 A * v(j) = lambda(j) * v(j)
 where lambda(j) is its eigenvalue.
 The left eigenvector u(j) of A satisfies
 u(j)**H * A = lambda(j) * u(j)**H
 where u(j)**H denotes the conjugate transpose of u(j).
 The computed eigenvectors are normalized to have Euclidean norm
 equal to 1 and largest component real.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOBVL</i> </p>
<pre> JOBVL is CHARACTER*1
 = 'N': left eigenvectors of A are not computed;
 = 'V': left eigenvectors of are computed.</pre>
<p><i>JOBVR</i> </p>
<pre> JOBVR is CHARACTER*1
 = 'N': right eigenvectors of A are not computed;
 = 'V': right eigenvectors of A are computed.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the N-by-N matrix A.
 On exit, A has been overwritten.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>W</i> </p>
<pre> W is COMPLEX array, dimension (N)
 W contains the computed eigenvalues.</pre>
<p><i>VL</i> </p>
<pre> VL is COMPLEX array, dimension (LDVL,N)
 If JOBVL = 'V', the left eigenvectors u(j) are stored one
 after another in the columns of VL, in the same order
 as their eigenvalues.
 If JOBVL = 'N', VL is not referenced.
 u(j) = VL(:,j), the j-th column of VL.</pre>
<p><i>LDVL</i> </p>
<pre> LDVL is INTEGER
 The leading dimension of the array VL. LDVL &gt;= 1; if
 JOBVL = 'V', LDVL &gt;= N.</pre>
<p><i>VR</i> </p>
<pre> VR is COMPLEX array, dimension (LDVR,N)
 If JOBVR = 'V', the right eigenvectors v(j) are stored one
 after another in the columns of VR, in the same order
 as their eigenvalues.
 If JOBVR = 'N', VR is not referenced.
 v(j) = VR(:,j), the j-th column of VR.</pre>
<p><i>LDVR</i> </p>
<pre> LDVR is INTEGER
 The leading dimension of the array VR. LDVR &gt;= 1; if
 JOBVR = 'V', LDVR &gt;= N.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= max(1,2*N).
 For good performance, LWORK must generally be larger.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (2*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = i, the QR algorithm failed to compute all the
 eigenvalues, and no eigenvectors have been computed;
 elements and i+1:N of W contain eigenvalues which have
 converged.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 177 of file cgeev.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
