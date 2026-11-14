---
title: "sbdsdc-f(3)"
name: "sbdsdc-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sbdsdc-f/"
description: "sbdsdc.f –"
---

<p>sbdsdc.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sbdsdc</code> (UPLO, COMPQ, N, D, E, U, LDU, VT, LDVT, Q, IQ, WORK, IWORK, INFO)<br />
 <i></i><code>SBDSDC</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sbdsdc (characterUPLO, characterCOMPQ, integerN, real, dimension( * )D, real, dimension( * )E, real, dimension( ldu, * )U, integerLDU, real, dimension( ldvt, * )VT, integerLDVT, real, dimension( * )Q, integer, dimension( * )IQ, real, dimension( * )WORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>SBDSDC</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SBDSDC computes the singular value decomposition (SVD) of a real
 N-by-N (upper or lower) bidiagonal matrix B: B = U * S * VT,
 using a divide and conquer method, where S is a diagonal matrix
 with non-negative diagonal elements (the singular values of B), and
 U and VT are orthogonal matrices of left and right singular vectors,
 respectively. SBDSDC can be used to compute all singular values,
 and optionally, singular vectors or singular vectors in compact form.
 This code makes very mild assumptions about floating point
 arithmetic. It will work on machines with a guard digit in
 add/subtract, or on those binary machines without guard digits
 which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or Cray-2.
 It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none. See SLASD3 for details.
 The code currently calls SLASDQ if singular values only are desired.
 However, it can be slightly modified to compute singular values
 using the divide and conquer method.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': B is upper bidiagonal.
 = 'L': B is lower bidiagonal.</pre>
<p><i>COMPQ</i> </p>
<pre> COMPQ is CHARACTER*1
 Specifies whether singular vectors are to be computed
 as follows:
 = 'N': Compute singular values only;
 = 'P': Compute singular values and compute singular
 vectors in compact form;
 = 'I': Compute singular values and singular vectors.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix B. N &gt;= 0.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 On entry, the n diagonal elements of the bidiagonal matrix B.
 On exit, if INFO=0, the singular values of B.</pre>
<p><i>E</i> </p>
<pre> E is REAL array, dimension (N-1)
 On entry, the elements of E contain the offdiagonal
 elements of the bidiagonal matrix whose SVD is desired.
 On exit, E has been destroyed.</pre>
<p><i>U</i> </p>
<pre> U is REAL array, dimension (LDU,N)
 If COMPQ = 'I', then:
 On exit, if INFO = 0, U contains the left singular vectors
 of the bidiagonal matrix.
 For other values of COMPQ, U is not referenced.</pre>
<p><i>LDU</i> </p>
<pre> LDU is INTEGER
 The leading dimension of the array U. LDU &gt;= 1.
 If singular vectors are desired, then LDU &gt;= max( 1, N ).</pre>
<p><i>VT</i> </p>
<pre> VT is REAL array, dimension (LDVT,N)
 If COMPQ = 'I', then:
 On exit, if INFO = 0, VT**T contains the right singular
 vectors of the bidiagonal matrix.
 For other values of COMPQ, VT is not referenced.</pre>
<p><i>LDVT</i> </p>
<pre> LDVT is INTEGER
 The leading dimension of the array VT. LDVT &gt;= 1.
 If singular vectors are desired, then LDVT &gt;= max( 1, N ).</pre>
<p><i>Q</i> </p>
<pre> Q is REAL array, dimension (LDQ)
 If COMPQ = 'P', then:
 On exit, if INFO = 0, Q and IQ contain the left
 and right singular vectors in a compact form,
 requiring O(N log N) space instead of 2*N**2.
 In particular, Q contains all the REAL data in
 LDQ &gt;= N*(11 + 2*SMLSIZ + 8*INT(LOG_2(N/(SMLSIZ+1))))
 words of memory, where SMLSIZ is returned by ILAENV and
 is equal to the maximum size of the subproblems at the
 bottom of the computation tree (usually about 25).
 For other values of COMPQ, Q is not referenced.</pre>
<p><i>IQ</i> </p>
<pre> IQ is INTEGER array, dimension (LDIQ)
 If COMPQ = 'P', then:
 On exit, if INFO = 0, Q and IQ contain the left
 and right singular vectors in a compact form,
 requiring O(N log N) space instead of 2*N**2.
 In particular, IQ contains all INTEGER data in
 LDIQ &gt;= N*(3 + 3*INT(LOG_2(N/(SMLSIZ+1))))
 words of memory, where SMLSIZ is returned by ILAENV and
 is equal to the maximum size of the subproblems at the
 bottom of the computation tree (usually about 25).
 For other values of COMPQ, IQ is not referenced.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (MAX(1,LWORK))
 If COMPQ = 'N' then LWORK &gt;= (4 * N).
 If COMPQ = 'P' then LWORK &gt;= (6 * N).
 If COMPQ = 'I' then LWORK &gt;= (3 * N**2 + 4 * N).</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension (8*N)</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: The algorithm failed to compute a singular value.
 The update process of divide and conquer failed.</pre>
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
<p> Definition at line 205 of file sbdsdc.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
