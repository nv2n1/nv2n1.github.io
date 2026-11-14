---
title: "cupgtr-f(3)"
name: "cupgtr-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cupgtr-f/"
description: "cupgtr.f –"
---

<p>cupgtr.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>cupgtr</code> (UPLO, N, AP, TAU, Q, LDQ, WORK, INFO)<br />
 <i></i><code>CUPGTR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cupgtr (characterUPLO, integerN, complex, dimension( * )AP, complex, dimension( * )TAU, complex, dimension( ldq, * )Q, integerLDQ, complex, dimension( * )WORK, integerINFO)</h3>
<p><code>CUPGTR</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> CUPGTR generates a complex unitary matrix Q which is defined as the
 product of n-1 elementary reflectors H(i) of order n, as returned by
 CHPTRD using packed storage:
 if UPLO = 'U', Q = H(n-1) . . . H(2) H(1),
 if UPLO = 'L', Q = H(1) H(2) . . . H(n-1).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': Upper triangular packed storage used in previous
 call to CHPTRD;
 = 'L': Lower triangular packed storage used in previous
 call to CHPTRD.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix Q. N &gt;= 0.</pre>
<p><i>AP</i> </p>
<pre> AP is COMPLEX array, dimension (N*(N+1)/2)
 The vectors which define the elementary reflectors, as
 returned by CHPTRD.</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX array, dimension (N-1)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by CHPTRD.</pre>
<p><i>Q</i> </p>
<pre> Q is COMPLEX array, dimension (LDQ,N)
 The N-by-N unitary matrix Q.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N).</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX array, dimension (N-1)</pre>
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
<dd>November 2011</dl>
<p> Definition at line 115 of file cupgtr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
