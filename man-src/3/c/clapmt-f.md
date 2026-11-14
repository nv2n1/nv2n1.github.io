---
title: "clapmt-f(3)"
name: "clapmt-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clapmt-f/"
description: "clapmt.f –"
---

<p>clapmt.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>clapmt</code> (FORWRD, M, N, X, LDX, K)<br />
 <i></i><code>CLAPMT</code> performs a forward or backward permutation of the columns of a matrix.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clapmt (logicalFORWRD, integerM, integerN, complex, dimension( ldx, * )X, integerLDX, integer, dimension( * )K)</h3>
<p><code>CLAPMT</code> performs a forward or backward permutation of the columns of a matrix. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CLAPMT rearranges the columns of the M by N matrix X as specified
 by the permutation <a href="//www.systutorials.com/docs/linux/man/1-K/">K</a>(1),<a href="//www.systutorials.com/docs/linux/man/2-K/">K</a>(2),...,K(N) of the integers 1,...,N.
 If FORWRD = .TRUE., forward permutation:
 X(*,K(J)) is moved X(*,J) for J = 1,2,...,N.
 If FORWRD = .FALSE., backward permutation:
 X(*,J) is moved to X(*,K(J)) for J = 1,2,...,N.</pre>
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
<pre> K is INTEGER array, dimension (N)
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
<p> Definition at line 105 of file clapmt.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
