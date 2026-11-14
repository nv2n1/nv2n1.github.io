---
title: "cgesvd-f(3)"
name: "cgesvd-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgesvd-f/"
description: "cgesvd.f –"
---

<p>cgesvd.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgesvd</code> (JOBU, JOBVT, M, N, A, LDA, S, U, LDU, VT, LDVT, WORK, LWORK, RWORK, INFO)<br />
 <i></i><code> CGESVD computes the singular value decomposition (SVD) for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgesvd (characterJOBU, characterJOBVT, integerM, integerN, complex, dimension( lda, * )A, integerLDA, real, dimension( * )S, complex, dimension( ldu, * )U, integerLDU, complex, dimension( ldvt, * )VT, integerLDVT, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integerINFO)</h3>
<p><code> CGESVD computes the singular value decomposition (SVD) for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGESVD computes the singular value decomposition (SVD) of a complex
 M-by-N matrix A, optionally computing the left and/or right singular
 vectors. The SVD is written
 A = U * SIGMA * conjugate-transpose(V)
 where SIGMA is an M-by-N matrix which is zero except for its
 min(m,n) diagonal elements, U is an M-by-M unitary matrix, and
 V is an N-by-N unitary matrix. The diagonal elements of SIGMA
 are the singular values of A; they are real and non-negative, and
 are returned in descending order. The first min(m,n) columns of
 U and V are the left and right singular vectors of A.
 Note that the routine returns V**H, not V.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOBU</i> </p>
<pre> JOBU is CHARACTER*1
 Specifies options for computing all or part of the matrix U:
 = 'A': all M columns of U are returned in array U:
 = 'S': the first min(m,n) columns of U (the left singular
 vectors) are returned in the array U;
 = 'O': the first min(m,n) columns of U (the left singular
 vectors) are overwritten on the array A;
 = 'N': no columns of U (no left singular vectors) are
 computed.</pre>
<p><i>JOBVT</i> </p>
<pre> JOBVT is CHARACTER*1
 Specifies options for computing all or part of the matrix
 V**H:
 = 'A': all N rows of V**H are returned in the array VT;
 = 'S': the first min(m,n) rows of V**H (the right singular
 vectors) are returned in the array VT;
 = 'O': the first min(m,n) rows of V**H (the right singular
 vectors) are overwritten on the array A;
 = 'N': no rows of V**H (no right singular vectors) are
 computed.
 JOBVT and JOBU cannot both be 'O'.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the input matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the input matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit,
 if JOBU = 'O', A is overwritten with the first min(m,n)
 columns of U (the left singular vectors,
 stored columnwise);
 if JOBVT = 'O', A is overwritten with the first min(m,n)
 rows of V**H (the right singular vectors,
 stored rowwise);
 if JOBU .ne. 'O' and JOBVT .ne. 'O', the contents of A
 are destroyed.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>S</i> </p>
<pre> S is REAL array, dimension (min(M,N))
 The singular values of A, sorted so that S(i) &gt;= S(i+1).</pre>
<p><i>U</i> </p>
<pre> U is COMPLEX array, dimension (LDU,UCOL)
 (LDU,M) if JOBU = 'A' or (LDU,min(M,N)) if JOBU = 'S'.
 If JOBU = 'A', U contains the M-by-M unitary matrix U;
 if JOBU = 'S', U contains the first min(m,n) columns of U
 (the left singular vectors, stored columnwise);
 if JOBU = 'N' or 'O', U is not referenced.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= 1; if
 JOBU = 'S' or 'A', LDU &gt;= M.</pre>
<p><i>VT</i> </p>
<pre> VT is COMPLEX array, dimension (LDVT,N)
 If JOBVT = 'A', VT contains the N-by-N unitary matrix
 V**H;
 if JOBVT = 'S', VT contains the first min(m,n) rows of
 V**H (the right singular vectors, stored rowwise);
 if JOBVT = 'N' or 'O', VT is not referenced.</pre>
<p><i>LDVT</i> </p>
<pre> LDVT is INTEGER
 The leading dimension of the array VT. LDVT &gt;= 1; if
 JOBVT = 'A', LDVT &gt;= N; if JOBVT = 'S', LDVT &gt;= min(M,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK.
 LWORK &gt;= MAX(1,2*MIN(M,N)+MAX(M,N)).
 For good performance, LWORK should generally be larger.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is REAL array, dimension (5*min(M,N))
 On exit, if INFO &gt; 0, RWORK(1:MIN(M,N)-1) contains the
 unconverged superdiagonal elements of an upper bidiagonal
 matrix B whose diagonal is in S (not necessarily sorted).
 B satisfies A = U * B * VT, so it has the same singular
 values as A, and singular vectors related by U and VT.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if CBDSQR did not converge, INFO specifies how many
 superdiagonals of an intermediate bidiagonal form B
 did not converge to zero. See the description of RWORK
 above for details.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>April 2012</dl>
<p> Definition at line 214 of file cgesvd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
