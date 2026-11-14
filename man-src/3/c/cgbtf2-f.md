---
title: "cgbtf2-f(3)"
name: "cgbtf2-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgbtf2-f/"
description: "cgbtf2.f –"
---

<p>cgbtf2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgbtf2</code> (M, N, KL, KU, AB, LDAB, IPIV, INFO)<br />
 <i></i><code>CGBTF2</code> computes the LU factorization of a general band matrix using the unblocked version of the algorithm.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgbtf2 (integerM, integerN, integerKL, integerKU, complex, dimension( ldab, * )AB, integerLDAB, integer, dimension( * )IPIV, integerINFO)</h3>
<p><code>CGBTF2</code> computes the LU factorization of a general band matrix using the unblocked version of the algorithm. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGBTF2 computes an LU factorization of a complex m-by-n band matrix
 A using partial pivoting with row interchanges.
 This is the unblocked version of the algorithm, calling Level 2 BLAS.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The number of subdiagonals within the band of A. KL &gt;= 0.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The number of superdiagonals within the band of A. KU &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX array, dimension (LDAB,N)
 On entry, the matrix A in band storage, in rows KL+1 to
 2*KL+KU+1; rows 1 to KL of the array need not be set.
 The j-th column of A is stored in the j-th column of the
 array AB as follows:
 AB(kl+ku+1+i-j,j) = A(i,j) for max(1,j-ku)&lt;=i&lt;=min(m,j+kl)
 On exit, details of the factorization: U is stored as an
 upper triangular band matrix with KL+KU superdiagonals in
 rows 1 to KL+KU+1, and the multipliers used during the
 factorization are stored in rows KL+KU+2 to 2*KL+KU+1.
 See below for further details.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= 2*KL+KU+1.</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (min(M,N))
 The pivot indices; for 1 &lt;= i &lt;= min(M,N), row i of the
 matrix was interchanged with row IPIV(i).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value
 &gt; 0: if INFO = +i, U(i,i) is exactly zero. The factorization
 has been completed, but the factor U is exactly
 singular, and division by zero will occur if it is used
 to solve a system of equations.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> The band storage scheme is illustrated by the following example, when
 M = N = 6, KL = 2, KU = 1:
 On entry: On exit:
 * * * + + + * * * u14 u25 u36
 * * + + + + * * u13 u24 u35 u46
 * a12 a23 a34 a45 a56 * u12 u23 u34 u45 u56
 a11 a22 a33 a44 a55 a66 u11 u22 u33 u44 u55 u66
 a21 a32 a43 a54 a65 * m21 m32 m43 m54 m65 *
 a31 a42 a53 a64 * * m31 m42 m53 m64 * *
 Array elements marked * are not used by the routine; elements marked
 + need not be set on entry, but are required by the routine to store
 elements of U, because of fill-in resulting from the row
 interchanges.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 146 of file cgbtf2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
