---
title: "cgetc2-f(3)"
name: "cgetc2-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgetc2-f/"
description: "cgetc2.f –"
---

<p>cgetc2.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cgetc2</code> (N, A, LDA, IPIV, JPIV, INFO)<br />
 <i></i><code>CGETC2</code> computes the LU factorization with complete pivoting of the general n-by-n matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgetc2 (integerN, complex, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, integer, dimension( * )JPIV, integerINFO)</h3>
<p><code>CGETC2</code> computes the LU factorization with complete pivoting of the general n-by-n matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CGETC2 computes an LU factorization, using complete pivoting, of the
 n-by-n matrix A. The factorization has the form A = P * L * U * Q,
 where P and Q are permutation matrices, L is lower triangular with
 unit diagonal elements and U is upper triangular.
 This is a level 1 BLAS version of the algorithm.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX array, dimension (LDA, N)
 On entry, the n-by-n matrix to be factored.
 On exit, the factors L and U from the factorization
 A = P*L*U*Q; the unit diagonal elements of L are not stored.
 If U(k, k) appears to be less than SMIN, U(k, k) is given the
 value of SMIN, giving a nonsingular perturbed system.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1, N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N).
 The pivot indices; for 1 &lt;= i &lt;= N, row i of the
 matrix has been interchanged with row IPIV(i).</pre>
<p><i>JPIV</i> </p>
<pre> JPIV is INTEGER array, dimension (N).
 The pivot indices; for 1 &lt;= j &lt;= N, column j of the
 matrix has been interchanged with column JPIV(j).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &gt; 0: if INFO = k, U(k, k) is likely to produce overflow if
 one tries to solve for x in Ax = b. So U is perturbed
 to avoid the overflow.</pre>
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
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> Definition at line 112 of file cgetc2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
