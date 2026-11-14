---
title: "strttf-f(3)"
name: "strttf-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-strttf-f/"
description: "strttf.f –"
---

<p>strttf.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>strttf</code> (TRANSR, UPLO, N, A, LDA, ARF, INFO)<br />
 <i></i><code>STRTTF</code> copies a triangular matrix from the standard full format (TR) to the rectangular full packed format (TF).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine strttf (characterTRANSR, characterUPLO, integerN, real, dimension( 0: lda-1, 0: * )A, integerLDA, real, dimension( 0: * )ARF, integerINFO)</h3>
<p><code>STRTTF</code> copies a triangular matrix from the standard full format (TR) to the rectangular full packed format (TF). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> STRTTF copies a triangular matrix A from standard full format (TR)
 to rectangular full packed format (TF) .</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>TRANSR</i> </p>
<pre> TRANSR is CHARACTER*1
 = 'N': ARF in Normal form is wanted;
 = 'T': ARF in Transpose form is wanted.</pre>
<p><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangle of A is stored;
 = 'L': Lower triangle of A is stored.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N).
 On entry, the triangular matrix A. If UPLO = 'U', the
 leading N-by-N upper triangular part of the array A contains
 the upper triangular matrix, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading N-by-N lower triangular part of the array A contains
 the lower triangular matrix, and the strictly upper
 triangular part of A is not referenced.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the matrix A. LDA &gt;= max(1,N).</pre>
<p><i>ARF</i> </p>
<pre> ARF is REAL array, dimension (NT).
 NT=N*(N+1)/2. On exit, the triangular matrix A in RFP format.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> We first consider Rectangular Full Packed (RFP) Format when N is
 even. We give an example where N = 6.
 AP is Upper AP is Lower
 00 01 02 03 04 05 00
 11 12 13 14 15 10 11
 22 23 24 25 20 21 22
 33 34 35 30 31 32 33
 44 45 40 41 42 43 44
 55 50 51 52 53 54 55
 Let TRANSR = 'N'. RFP holds AP as follows:
 For UPLO = 'U' the upper trapezoid A(0:5,0:2) consists of the last
 three columns of AP upper. The lower triangle A(4:6,0:2) consists of
 the transpose of the first three columns of AP upper.
 For UPLO = 'L' the lower trapezoid A(1:6,0:2) consists of the first
 three columns of AP lower. The upper triangle A(0:2,0:2) consists of
 the transpose of the last three columns of AP lower.
 This covers the case N even and TRANSR = 'N'.
 RFP A RFP A
 03 04 05 33 43 53
 13 14 15 00 44 54
 23 24 25 10 11 55
 33 34 35 20 21 22
 00 44 45 30 31 32
 01 11 55 40 41 42
 02 12 22 50 51 52
 Now let TRANSR = 'T'. RFP A in both UPLO cases is just the
 transpose of RFP A above. One therefore gets:
 RFP A RFP A
 03 13 23 33 00 01 02 33 00 10 20 30 40 50
 04 14 24 34 44 11 12 43 44 11 21 31 41 51
 05 15 25 35 45 55 22 53 54 55 22 32 42 52
 We then consider Rectangular Full Packed (RFP) Format when N is
 odd. We give an example where N = 5.
 AP is Upper AP is Lower
 00 01 02 03 04 00
 11 12 13 14 10 11
 22 23 24 20 21 22
 33 34 30 31 32 33
 44 40 41 42 43 44
 Let TRANSR = 'N'. RFP holds AP as follows:
 For UPLO = 'U' the upper trapezoid A(0:4,0:2) consists of the last
 three columns of AP upper. The lower triangle A(3:4,0:1) consists of
 the transpose of the first two columns of AP upper.
 For UPLO = 'L' the lower trapezoid A(0:4,0:2) consists of the first
 three columns of AP lower. The upper triangle A(0:1,1:2) consists of
 the transpose of the last two columns of AP lower.
 This covers the case N odd and TRANSR = 'N'.
 RFP A RFP A
 02 03 04 00 33 43
 12 13 14 10 11 44
 22 23 24 20 21 22
 00 33 34 30 31 32
 01 11 44 40 41 42
 Now let TRANSR = 'T'. RFP A in both UPLO cases is just the
 transpose of RFP A above. One therefore gets:
 RFP A RFP A
 02 12 22 00 01 00 10 20 30 40 50
 03 13 23 33 11 33 11 21 31 41 51
 04 14 24 34 44 43 44 22 32 42 52</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 195 of file strttf.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
