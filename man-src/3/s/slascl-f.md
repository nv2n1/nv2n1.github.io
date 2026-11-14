---
title: "slascl-f(3)"
name: "slascl-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slascl-f/"
description: "slascl.f –"
---

<p>slascl.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slascl</code> (TYPE, KL, KU, CFROM, CTO, M, N, A, LDA, INFO)<br />
 <i></i><code>SLASCL</code> multiplies a general rectangular matrix by a real scalar defined as cto/cfrom.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slascl (characterTYPE, integerKL, integerKU, realCFROM, realCTO, integerM, integerN, real, dimension( lda, * )A, integerLDA, integerINFO)</h3>
<p><code>SLASCL</code> multiplies a general rectangular matrix by a real scalar defined as cto/cfrom. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLASCL multiplies the M by N real matrix A by the real scalar
 CTO/CFROM. This is done without over/underflow as long as the final
 result CTO*A(I,J)/CFROM does not over/underflow. TYPE specifies that
 A may be full, upper triangular, lower triangular, upper Hessenberg,
 or banded.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>TYPE</i> </p>
<pre> TYPE is CHARACTER*1
 TYPE indices the storage type of the input matrix.
 = 'G': A is a full matrix.
 = 'L': A is a lower triangular matrix.
 = 'U': A is an upper triangular matrix.
 = 'H': A is an upper Hessenberg matrix.
 = 'B': A is a symmetric band matrix with lower bandwidth KL
 and upper bandwidth KU and with the only the lower
 half stored.
 = 'Q': A is a symmetric band matrix with lower bandwidth KL
 and upper bandwidth KU and with the only the upper
 half stored.
 = 'Z': A is a band matrix with lower bandwidth KL and upper
 bandwidth KU. See SGBTRF for storage details.</pre>
<p><i>KL</i> </p>
<pre> KL is INTEGER
 The lower bandwidth of A. Referenced only if TYPE = 'B',
 'Q' or 'Z'.</pre>
<p><i>KU</i> </p>
<pre> KU is INTEGER
 The upper bandwidth of A. Referenced only if TYPE = 'B',
 'Q' or 'Z'.</pre>
<p><i>CFROM</i> </p>
<pre> CFROM is REAL</pre>
<p><i>CTO</i> </p>
<pre> CTO is REAL
 The matrix A is multiplied by CTO/CFROM. A(I,J) is computed
 without over/underflow if the final result CTO*A(I,J)/CFROM
 can be represented without over/underflow. CFROM must be
 nonzero.</pre>
<p><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 The matrix to be multiplied by CTO/CFROM. See TYPE for the
 storage type.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 0 - successful exit
 &lt;0 - if INFO = -i, the i-th argument had an illegal value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 140 of file slascl.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
