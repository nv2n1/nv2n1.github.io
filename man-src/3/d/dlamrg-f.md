---
title: "dlamrg-f(3)"
name: "dlamrg-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlamrg-f/"
description: "dlamrg.f –"
---

<p>dlamrg.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlamrg</code> (N1, N2, A, DTRD1, DTRD2, INDEX)<br />
 <i></i><code>DLAMRG</code> creates a permutation list to merge the entries of two independently sorted sets into a single set sorted in ascending order.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlamrg (integerN1, integerN2, double precision, dimension( * )A, integerDTRD1, integerDTRD2, integer, dimension( * )INDEX)</h3>
<p><code>DLAMRG</code> creates a permutation list to merge the entries of two independently sorted sets into a single set sorted in ascending order. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLAMRG will create a permutation list which will merge the elements
 of A (which is composed of two independently sorted sets) into a
 single set which is sorted in ascending order.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N1</i> </p>
<pre> N1 is INTEGER</pre>
<p><i>N2</i> </p>
<pre> N2 is INTEGER
 These arguements contain the respective lengths of the two
 sorted lists to be merged.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE PRECISION array, dimension (N1+N2)
 The first N1 elements of A contain a list of numbers which
 are sorted in either ascending or descending order. Likewise
 for the final N2 elements.</pre>
<p><i>DTRD1</i> </p>
<pre> DTRD1 is INTEGER</pre>
<p><i>DTRD2</i> </p>
<pre> DTRD2 is INTEGER
 These are the strides to be taken through the array A.
 Allowable strides are 1 and -1. They indicate whether a
 subset of A is sorted in ascending (DTRDx = 1) or descending
 (DTRDx = -1) order.</pre>
<p><i>INDEX</i> </p>
<pre> INDEX is INTEGER array, dimension (N1+N2)
 On exit this array will contain a permutation such that
 if B( I ) = A( INDEX( I ) ) for I=1,N1+N2, then B will be
 sorted in ascending order.</pre>
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
<p> Definition at line 100 of file dlamrg.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
