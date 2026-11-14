---
title: "ctftri(3)"
name: "ctftri"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctftri/"
description: "ctftri.f –"
---

<h2 class="name">NAME</h2>
<p> ctftri.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ctftri</code> (TRANSR, UPLO, DIAG, N, A, INFO)<br />
 <i></i><code>CTFTRI</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctftri (characterTRANSR, characterUPLO, characterDIAG, integerN, complex, dimension( 0: * )A, integerINFO)</h3>
<p> <code>CTFTRI</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CTFTRI computes the inverse of a triangular matrix A stored in RFP
 format.
 This is a Level 3 BLAS version of the algorithm.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>TRANSR</i> </p>
<pre>
          TRANSR is CHARACTER*1
          = 'N':  The Normal TRANSR of RFP A is stored;
          = 'C':  The Conjugate-transpose TRANSR of RFP A is stored.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  A is upper triangular;
          = 'L':  A is lower triangular.
</pre>
<p> <i>DIAG</i> </p>
<pre>
          DIAG is CHARACTER*1
          = 'N':  A is non-unit triangular;
          = 'U':  A is unit triangular.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre><code>
A is COMPLEX array, dimension(N *(N + 1) / 2);
On entry, the triangular matrix A in RFP format.RFP format is described by TRANSR, UPLO, and N as follows : If TRANSR = 'N' then RFP A is(0
                                                                                                                                          : N, 0
                                                                                                                                          : k - 1) when N is even;
k = N / 2. RFP A is(0
                    : N - 1, 0
                    : k) when N is odd;
k = N / 2. IF TRANSR = 'C' then RFP is
                           the Conjugate -
                       transpose of RFP A as defined when
                           TRANSR = 'N'.The contents of RFP A are defined by UPLO as follows : If UPLO = 'U' the RFP A contains the nt elements of
                           upper packed A; If UPLO = 'L' the RFP A contains the nt
          elements of lower packed A. The LDA of RFP A is (N+1)/2 when
          TRANSR = 'C'. When TRANSR is 'N' the LDA is N+1 when N is
          even and N is odd. See the Note below for more details.
          On exit, the (triangular) inverse of the original matrix, in
          the same storage format.
</code></pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          &gt; 0: if INFO = i, A(i,i) is exactly zero.  The triangular
               matrix is singular and its inverse can not be computed.
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
<pre><code>
We first consider Standard Packed Format when N is even.We give an example where N = 6. AP is Upper AP is Lower 00 01 02 03 04 05 00 11 12 13 14 15 10 11 22 23 24 25 20 21 22 33 34 35 30 31 32 33 44 45 40 41 42 43 44 55 50 51 52 53 54 55 Let TRANSR = 'N'.RFP holds AP as follows : For UPLO = 'U' the upper trapezoid A(0 : 5, 0 : 2) consists of the last
                                                                                                                                                                                                                                                                                                        three columns of AP upper.The lower triangle A(4 : 6, 0 : 2) consists of
                                                                                                                                                                                                                                                                                                            conjugate -
                                                                                                                                                                                                                                                                                                    transpose of the first three columns of AP upper.For UPLO = 'L' the lower trapezoid A(1 : 6, 0 : 2) consists of the first
                                                                                                                                                                                                                                                                                                                                                                    three columns of AP lower.The upper triangle A(0 : 2, 0 : 2) consists of
                                                                                                                                                                                                                                                                                                                                                                        conjugate -
                                                                                                                                                                                                                                                                                                                                                                transpose of the last three columns of AP lower.To denote conjugate we place-- above the element.This covers the case N even and TRANSR = 'N'.RFP A RFP A-- -- --03 04 05 33 43 53 -- --13 14 15 00 44 54 --23 24 25 10 11 55 33 34 35 20 21 22 --00 44 45 30 31 32 -- --01 11 55 40 41 42 -- -- --02 12 22 50 51 52 Now let TRANSR = 'C'.RFP A in both UPLO cases is just the conjugate -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      transpose of RFP A above.One therefore gets : RFP A RFP A-- -- -- -- -- -- -- -- -- --03 13 23 33 00 01 02 33 00 10 20 30 40 50 -- -- -- -- -- -- -- -- -- --04 14 24 34 44 11 12 43 44 11 21 31 41 51 -- -- -- -- -- -- -- -- -- --05 15 25 35 45 55 22 53 54 55 22 32 42 52 We next consider Standard Packed Format when N is odd.We give an example where N = 5. AP is Upper AP is Lower 00 01 02 03 04 00 11 12 13 14 10 11 22 23 24 20 21 22 33 34 30 31 32 33 44 40 41 42 43 44 Let TRANSR = 'N'.RFP holds AP as follows : For UPLO = 'U' the upper trapezoid A(0 : 4, 0 : 2) consists of the last
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      three columns of AP upper.The lower triangle A(3 : 4, 0 : 1) consists of
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          conjugate -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  transpose of the first two columns of AP upper.For UPLO = 'L' the lower trapezoid A(0 : 4, 0 : 2) consists of the first
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                three columns of AP lower.The upper triangle A(0 : 1, 1 : 2) consists of
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    conjugate -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            transpose of the last two columns of AP lower.To denote conjugate we place-- above the element.This covers the case N odd and TRANSR = 'N'.RFP A RFP A-- --02 03 04 00 33 43 --12 13 14 10 11 44 22 23 24 20 21 22 --00 33 34 30 31 32 -- --01 11 44 40 41 42 Now let TRANSR = 'C'.RFP A in both UPLO cases is just the conjugate -
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           transpose of RFP A above.One therefore gets : RFP A RFP A-- -- -- -- -- -- -- -- --02 12 22 00 01 00 10 20 30 40 50 -- -- -- -- -- -- -- -- --03 13 23 33 11 33 11 21 31 41 51 -- -- -- -- -- -- -- -- --04 14 24 34 44 43 44 22 32 42 52
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 222 of file ctftri.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
