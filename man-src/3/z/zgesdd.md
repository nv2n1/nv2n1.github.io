---
title: "zgesdd(3)"
name: "zgesdd"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgesdd/"
description: "zgesdd.f –"
---

<p>zgesdd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgesdd</code> (JOBZ, M, N, A, LDA, S, U, LDU, VT, LDVT, WORK, LWORK, RWORK, IWORK, INFO)<br />
 <i></i><code>ZGESDD</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgesdd (characterJOBZ, integerM, integerN, complex*16, dimension( lda, * )A, integerLDA, double precision, dimension( * )S, complex*16, dimension( ldu, * )U, integerLDU, complex*16, dimension( ldvt, * )VT, integerLDVT, complex*16, dimension( * )WORK, integerLWORK, double precision, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>ZGESDD</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGESDD computes the singular value decomposition (SVD) of a complex
 M-by-N matrix A, optionally computing the left and/or right singular
 vectors, by using divide-and-conquer method. The SVD is written
 A = U * SIGMA * conjugate-transpose(V)
 where SIGMA is an M-by-N matrix which is zero except for its
 min(m,n) diagonal elements, U is an M-by-M unitary matrix, and
 V is an N-by-N unitary matrix. The diagonal elements of SIGMA
 are the singular values of A; they are real and non-negative, and
 are returned in descending order. The first min(m,n) columns of
 U and V are the left and right singular vectors of A.
 Note that the routine returns VT = V**H, not V.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOBZ</i> </p>
<pre> JOBZ is CHARACTER*1
 Specifies options for computing all or part of the matrix U:
 = 'A': all M columns of U and all N rows of V**H are
 returned in the arrays U and VT;
 = 'S': the first min(M,N) columns of U and the first
 min(M,N) rows of V**H are returned in the arrays U
 and VT;
 = 'O': If M &gt;= N, the first N columns of U are overwritten
 in the array A and all rows of V**H are returned in
 the array VT;
 otherwise, all columns of U are returned in the
 array U and the first M rows of V**H are overwritten
 in the array A;
 = 'N': no columns of U or rows of V**H are computed.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the input matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the input matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit,
 if JOBZ = 'O', A is overwritten with the first N columns
 of U (the left singular vectors, stored
 columnwise) if M &gt;= N;
 A is overwritten with the first M rows
 of V**H (the right singular vectors, stored
 rowwise) otherwise.
 if JOBZ .ne. 'O', the contents of A are destroyed.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION array, dimension (min(M,N))
 The singular values of A, sorted so that S(i) &gt;= S(i+1).</pre>
<p><i>U</i> </p>
<pre> U is COMPLEX*16 array, dimension (LDU,UCOL)
 UCOL = M if JOBZ = 'A' or JOBZ = 'O' and M &lt; N;
 UCOL = min(M,N) if JOBZ = 'S'.
 If JOBZ = 'A' or JOBZ = 'O' and M &lt; N, U contains the M-by-M
 unitary matrix U;
 if JOBZ = 'S', U contains the first min(M,N) columns of U
 (the left singular vectors, stored columnwise);
 if JOBZ = 'O' and M &gt;= N, or JOBZ = 'N', U is not referenced.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= 1; if
 JOBZ = 'S' or 'A' or JOBZ = 'O' and M &lt; N, LDU &gt;= M.</pre>
<p><i>VT</i> </p>
<pre> VT is COMPLEX*16 array, dimension (LDVT,N)
 If JOBZ = 'A' or JOBZ = 'O' and M &gt;= N, VT contains the
 N-by-N unitary matrix V**H;
 if JOBZ = 'S', VT contains the first min(M,N) rows of
 V**H (the right singular vectors, stored rowwise);
 if JOBZ = 'O' and M &lt; N, or JOBZ = 'N', VT is not referenced.</pre>
<p><i>LDVT</i> </p>
<pre> LDVT is INTEGER
 The leading dimension of the array VT. LDVT &gt;= 1; if
 JOBZ = 'A' or JOBZ = 'O' and M &gt;= N, LDVT &gt;= N;
 if JOBZ = 'S', LDVT &gt;= min(M,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= 1.
 if JOBZ = 'N', LWORK &gt;= 2*min(M,N)+max(M,N).
 if JOBZ = 'O',
 LWORK &gt;= 2*min(M,N)*min(M,N)+2*min(M,N)+max(M,N).
 if JOBZ = 'S' or 'A',
 LWORK &gt;= min(M,N)*min(M,N)+2*min(M,N)+max(M,N).
 For good performance, LWORK should generally be larger.
 If LWORK = -1, a workspace query is assumed. The optimal
 size for the WORK array is calculated and stored in WORK(1),
 and no other work except argument checking is performed.</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension (MAX(1,LRWORK))
 If JOBZ = 'N', LRWORK &gt;= 5*min(M,N).
 Otherwise,
 LRWORK &gt;= min(M,N)*max(5*min(M,N)+7,2*max(M,N)+2*min(M,N)+1)</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (8*min(M,N))</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: The updating process of DBDSDC did not converge.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 222 of file zgesdd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
