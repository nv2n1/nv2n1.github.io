---
title: "dlasrt-f(3)"
name: "dlasrt-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasrt-f/"
description: "dlasrt.f –"
---

<p>dlasrt.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlasrt</code> (ID, N, D, INFO)<br />
 <i></i><code>DLASRT</code> sorts numbers in increasing or decreasing order.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasrt (characterID, integerN, double precision, dimension( * )D, integerINFO)</h3>
<p><code>DLASRT</code> sorts numbers in increasing or decreasing order. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> Sort the numbers in D in increasing order (if ID = 'I') or
 in decreasing order (if ID = 'D' ).
 Use Quick Sort, reverting to Insertion sort on arrays of
 size &lt;= 20. Dimension of STACK limits N to about 2**32.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>ID</i> </p>
<pre> ID is CHARACTER*1
 = 'I': sort D in increasing order;
 = 'D': sort D in decreasing order.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The length of the array D.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry, the array to be sorted.
 On exit, D has been sorted into increasing order
 (<a href="//www.systutorials.com/docs/linux/man/1-D/">D</a>(1) &lt;= ... &lt;= D(N) ) or into decreasing order
 (<a href="//www.systutorials.com/docs/linux/man/1-D/">D</a>(1) &gt;= ... &gt;= D(N) ), depending on ID.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> Definition at line 89 of file dlasrt.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
