---
title: "clapmr-f(3)"
name: "clapmr-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clapmr-f/"
description: "clapmr.f –"
---

<p>clapmr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>clapmr</code> (FORWRD, M, N, X, LDX, K)<br />
 <i></i><code>CLAPMR</code> rearranges rows of a matrix as specified by a permutation vector.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clapmr (logicalFORWRD, integerM, integerN, complex, dimension( ldx, * )X, integerLDX, integer, dimension( * )K)</h3>
<p><code>CLAPMR</code> rearranges rows of a matrix as specified by a permutation vector. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLAPMR rearranges the rows of the M by N matrix X as specified
 by the permutation <a href="//www.systutorials.com/docs/linux/man/1-K/">K</a>(1),<a href="//www.systutorials.com/docs/linux/man/2-K/">K</a>(2),...,K(M) of the integers 1,...,M.
 If FORWRD = .TRUE., forward permutation:
 X(K(I),*) is moved X(I,*) for I = 1,2,...,M.
 If FORWRD = .FALSE., backward permutation:
 X(I,*) is moved to X(K(I),*) for I = 1,2,...,M.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>FORWRD</i> </p>
<pre> FORWRD is LOGICAL
 = .TRUE., forward permutation
 = .FALSE., backward permutation</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix X. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix X. N &gt;= 0.</pre>
<p><i>X</i> </p>
<pre> X is COMPLEX array, dimension (LDX,N)
 On entry, the M by N matrix X.
 On exit, X contains the permuted matrix X.</pre>
<p><i>LDX</i> </p>
<pre> LDX is INTEGER
 The leading dimension of the array X, LDX &gt;= MAX(1,M).</pre>
<p><i>K</i> </p>
<pre> K is INTEGER array, dimension (M)
 On entry, K contains the permutation vector. K is used as
 internal workspace, but reset to its original value on
 output.</pre>
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
<p> Definition at line 105 of file clapmr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
