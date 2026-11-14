---
title: "zunghr(3)"
name: "zunghr"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zunghr/"
description: "zunghr.f –"
---

<p>zunghr.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zunghr</code> (N, ILO, IHI, A, LDA, TAU, WORK, LWORK, INFO)<br />
 <i></i><code>ZUNGHR</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zunghr (integerN, integerILO, integerIHI, complex*16, dimension( lda, * )A, integerLDA, complex*16, dimension( * )TAU, complex*16, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p><code>ZUNGHR</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZUNGHR generates a complex unitary matrix Q which is defined as the
 product of IHI-ILO elementary reflectors of order N, as returned by
 ZGEHRD:
 Q = H(ilo) H(ilo+1) . . . H(ihi-1).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix Q. N &gt;= 0.</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p><i>IHI</i> </p>
<pre> IHI is INTEGER
 ILO and IHI must have the same values as in the previous call
 of ZGEHRD. Q is equal to the unit matrix except in the
 submatrix Q(ilo+1:ihi,ilo+1:ihi).
 1 &lt;= ILO &lt;= IHI &lt;= N, if N &gt; 0; ILO=1 and IHI=0, if N=0.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the vectors which define the elementary reflectors,
 as returned by ZGEHRD.
 On exit, the N-by-N unitary matrix Q.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>TAU</i> </p>
<pre> TAU is COMPLEX*16 array, dimension (N-1)
 TAU(i) must contain the scalar factor of the elementary
 reflector H(i), as returned by ZGEHRD.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension (MAX(1,LWORK))
 On exit, if INFO = 0, WORK(1) returns the optimal LWORK.</pre>
<p><i>LWORK</i> </p>
<pre> LWORK is INTEGER
 The dimension of the array WORK. LWORK &gt;= IHI-ILO.
 For optimum performance LWORK &gt;= (IHI-ILO)*NB, where NB is
 the optimal blocksize.
 If LWORK = -1, then a workspace query is assumed; the routine
 only calculates the optimal size of the WORK array, returns
 this value as the first entry of the WORK array, and no error
 message related to LWORK is issued by XERBLA.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &lt; 0: if INFO = -i, the i-th argument had an illegal value</pre>
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
<p> Definition at line 127 of file zunghr.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
