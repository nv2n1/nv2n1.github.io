---
title: "sgeqrt-f(3)"
name: "sgeqrt-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgeqrt-f/"
description: "sgeqrt.f –"
---

<p>sgeqrt.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>sgeqrt</code> (M, N, NB, A, LDA, T, LDT, WORK, INFO)<br />
 <i></i><code>SGEQRT</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgeqrt (integerM, integerN, integerNB, real, dimension( lda, * )A, integerLDA, real, dimension( ldt, * )T, integerLDT, real, dimension( * )WORK, integerINFO)</h3>
<p><code>SGEQRT</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SGEQRT computes a blocked QR factorization of a real M-by-N matrix A
 using the compact WY representation of Q. </pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>M</i> </p>
<pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 The block size to be used in the blocked QR. MIN(M,N) &gt;= NB &gt;= 1.</pre>
<p><i>A</i> </p>
<pre> A is REAL array, dimension (LDA,N)
 On entry, the M-by-N matrix A.
 On exit, the elements on and above the diagonal of the array
 contain the min(M,N)-by-N upper trapezoidal matrix R (R is
 upper triangular if M &gt;= N); the elements below the diagonal
 are the columns of V.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>
<p><i>T</i> </p>
<pre> T is REAL array, dimension (LDT,MIN(M,N))
 The upper triangular block reflectors stored in compact form
 as a sequence of upper triangular blocks. See below
 for further details.</pre>
<p><i>LDT</i> </p>
<pre> LDT is INTEGER
 The leading dimension of the array T. LDT &gt;= NB.</pre>
<p><i>WORK</i> </p>
<pre> WORK is REAL array, dimension (NB*N)</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dd>
<pre> The matrix V stores the elementary reflectors H(i) in the i-th column
 below the diagonal. For example, if M=5 and N=3, the matrix V is
 V = ( 1 )
 ( v1 1 )
 ( v1 v2 1 )
 ( v1 v2 v3 )
 ( v1 v2 v3 )
 where the vi's represent the vectors which define H(i), which are returned
 in the matrix A. The 1's along the diagonal of V are not stored in A.
 Let K=MIN(M,N). The number of blocks is B = ceiling(K/NB), where each
 block is of order NB except for the last block, which is of order 
 IB = K - (B-1)*NB. For each of the B blocks, a upper triangular block
 reflector factor is computed: T1, T2, ..., TB. The NB-by-NB (and IB-by-IB 
 for the last block) T's are stored in the NB-by-N matrix T as
 T = (T1 T2 ... TB).</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 142 of file sgeqrt.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
