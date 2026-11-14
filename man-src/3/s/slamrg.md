---
title: "slamrg(3)"
name: "slamrg"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slamrg/"
description: "slamrg.f –"
---

<h2 class="name">NAME</h2>
<p> slamrg.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slamrg</code> (N1, N2, A, STRD1, STRD2, INDEX)<br />
 <i></i><code>SLAMRG</code> creates a permutation list to merge the entries of two independently sorted sets into a single set sorted in ascending order.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slamrg (integerN1, integerN2, real, dimension( * )A, integerSTRD1, integerSTRD2, integer, dimension( * )INDEX)</h3>
<p> <code>SLAMRG</code> creates a permutation list to merge the entries of two independently sorted sets into a single set sorted in ascending order. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAMRG will create a permutation list which will merge the elements
 of A (which is composed of two independently sorted sets) into a
 single set which is sorted in ascending order.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N1</i> </p>
<pre>
          N1 is INTEGER
</pre>
<p> <i>N2</i> </p>
<pre>
          N2 is INTEGER
         These arguements contain the respective lengths of the two
         sorted lists to be merged.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (N1+N2)
         The first N1 elements of A contain a list of numbers which
         are sorted in either ascending or descending order.  Likewise
         for the final N2 elements.
</pre>
<p> <i>STRD1</i> </p>
<pre>
          STRD1 is INTEGER
</pre>
<p> <i>STRD2</i> </p>
<pre>
          STRD2 is INTEGER
         These are the strides to be taken through the array A.
         Allowable strides are 1 and -1.  They indicate whether a
         subset of A is sorted in ascending (STRDx = 1) or descending
         (STRDx = -1) order.
</pre>
<p> <i>INDEX</i> </p>
<pre>
          INDEX is INTEGER array, dimension (N1+N2)
         On exit this array will contain a permutation such that
         if B( I ) = A( INDEX( I ) ) for I=1,N1+N2, then B will be
         sorted in ascending order.
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
<dd> September 2012</dl>
<p> Definition at line 100 of file slamrg.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
