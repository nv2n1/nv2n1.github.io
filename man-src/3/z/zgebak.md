---
title: "zgebak(3)"
name: "zgebak"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zgebak/"
description: "zgebak.f –"
---

<p>zgebak.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zgebak</code> (JOB, SIDE, N, ILO, IHI, SCALE, M, V, LDV, INFO)<br />
 <i></i><code>ZGEBAK</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zgebak (characterJOB, characterSIDE, integerN, integerILO, integerIHI, double precision, dimension( * )SCALE, integerM, complex*16, dimension( ldv, * )V, integerLDV, integerINFO)</h3>
<p><code>ZGEBAK</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZGEBAK forms the right or left eigenvectors of a complex general
 matrix by backward transformation on the computed eigenvectors of the
 balanced matrix output by ZGEBAL.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>JOB</i> </p>
<pre> JOB is CHARACTER*1
 Specifies the type of backward transformation required:
 = 'N', do nothing, return immediately;
 = 'P', do backward transformation for permutation only;
 = 'S', do backward transformation for scaling only;
 = 'B', do backward transformations for both permutation and
 scaling.
 JOB must be the same as the argument JOB supplied to ZGEBAL.</pre>
<p><i>SIDE</i> </p>
<pre> SIDE is CHARACTER*1
 = 'R': V contains right eigenvectors;
 = 'L': V contains left eigenvectors.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of rows of the matrix V. N &gt;= 0.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 The integers ILO and IHI determined by ZGEBAL.
 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0; ILO=1 and IHI=0, if N=0.</pre>
<p><i>SCALE</i> </p>
<pre> SCALE is DOUBLE PRECISION array, dimension (N)
 Details of the permutation and scaling factors, as returned
 by ZGEBAL.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of columns of the matrix V. M &gt;= 0.</pre>
<p><i>V</i> </p>
<pre> V is COMPLEX*16 array, dimension (LDV,M)
 On entry, the matrix of right or left eigenvectors to be
 transformed, as returned by ZHSEIN or ZTREVC.
 On exit, V is overwritten by the transformed eigenvectors.</pre>
<p><i>LDV</i> </p>
<pre> LDV is INTEGER
 The leading dimension of the array V. LDV &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 131 of file zgebak.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
