---
title: "dlaruv-f(3)"
name: "dlaruv-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaruv-f/"
description: "dlaruv.f –"
---

<p>dlaruv.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlaruv</code> (ISEED, N, X)<br />
 <i></i><code>DLARUV</code> returns a vector of n random real numbers from a uniform distribution.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlaruv (integer, dimension( 4 )ISEED, integerN, double precision, dimension( n )X)</h3>
<p><code>DLARUV</code> returns a vector of n random real numbers from a uniform distribution. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLARUV returns a vector of n random real numbers from a uniform (0,1)
 distribution (n &lt;= 128).
 This is an auxiliary routine called by DLARNV and ZLARNV.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ISEED</i> </p>
<pre> ISEED is INTEGER array, dimension (4)
 On entry, the seed of the random number generator; the array
 elements must be between 0 and 4095, and <a href="//www.systutorials.com/docs/linux/man/4-ISEED/">ISEED</a>(4) must be
 odd.
 On exit, the seed is updated.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of random numbers to be generated. N &lt;= 128.</pre>
<p><i>X</i> </p>
<pre> X is DOUBLE PRECISION array, dimension (N)
 The generated random numbers.</pre>
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
<pre> This routine uses a multiplicative congruential method with modulus
 2**48 and multiplier 33952834046453 (see G.S.Fishman,
 'Multiplicative congruential random number generators with modulus
 2**b: an exhaustive analysis for b = 32 and a partial analysis for
 b = 48', Math. Comp. 189, pp 331-344, 1990).
 48-bit integers are stored in 4 integer array elements with 12 bits
 per element. Hence the routine is portable across machines with
 integers of 32 bits or more.</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 96 of file dlaruv.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
