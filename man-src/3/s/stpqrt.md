---
title: "stpqrt(3)"
name: "stpqrt"
section: "3"
letter: "s"
url: "/docs/linux/man/3-stpqrt/"
description: "stpqrt.f –"
---

<h2 class="name">NAME</h2>
<p> stpqrt.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>stpqrt</code> (M, N, L, NB, A, LDA, B, LDB, T, LDT, WORK, INFO)<br />
 <i></i><code>STPQRT</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine stpqrt (integerM, integerN, integerL, integerNB, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( ldt, * )T, integerLDT, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>STPQRT</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 STPQRT computes a blocked QR factorization of a real 
 &quot;triangular-pentagonal&quot; matrix C, which is composed of a 
 triangular block A and pentagonal block B, using the compact 
 WY representation for Q.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix B.  
          M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix B, and the order of the
          triangular matrix A.
          N &gt;= 0.
</pre>
<p> <i>L</i> </p>
<pre>
          L is INTEGER
          The number of rows of the upper trapezoidal part of B.
          MIN(M,N) &gt;= L &gt;= 0.  See Further Details.
</pre>
<p> <i>NB</i> </p>
<pre>
          NB is INTEGER
          The block size to be used in the blocked QR.  N &gt;= NB &gt;= 1.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          On entry, the upper triangular N-by-N matrix A.
          On exit, the elements on and above the diagonal of the array
          contain the upper triangular matrix R.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,N)
          On entry, the pentagonal M-by-N matrix B.  The first M-L rows 
          are rectangular, and the last L rows are upper trapezoidal.
          On exit, B contains the pentagonal matrix V.  See Further Details.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,M).
</pre>
<p> <i>T</i> </p>
<pre>
          T is REAL array, dimension (LDT,N)
          The upper triangular block reflectors stored in compact form
          as a sequence of upper triangular blocks.  See Further Details.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T.  LDT &gt;= NB.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (NB*N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
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
<dd> November 2013</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre><code>
The input matrix C is a(N + M) - by - N matrix C = [A]
                                                       [B] where A is an upper triangular N
                                                   - by - N matrix,
                                               and B is M - by - N pentagonal matrix consisting of a(M - L) - by - N rectangular matrix B1 on top of a L - by - N upper trapezoidal matrix B2 : B = [B1] &lt; -(M - L) - by - N rectangular[B2] &lt; -L - by - N upper trapezoidal.The upper trapezoidal matrix B2 consists of the first L rows of a N - by - N upper triangular matrix, where 0 &lt;= L &lt;= MIN(M, N).If L = 0,
                                               B is rectangular M - by - N;
if M=L=N, B is upper triangular.  
  The matrix W stores the elementary reflectors H(i) in the i-th column
  below the diagonal (of A) in the (N+M)-by-N input matrix C
               C = [ A ]  &lt;- upper triangular N-by-N
                   [ B ]  &lt;- M-by-N pentagonal
  so that W can be represented as
               W = [ I ]  &lt;- identity, N-by-N
                   [ V ]  &lt;- M-by-N, same form as B.
  Thus, all of information needed for W is contained on exit in B, which
  we call V above.  Note that V has the same form as B; that is, 
               V = [ V1 ] &lt;- (M-L)-by-N rectangular
                   [ V2 ] &lt;-     L-by-N upper trapezoidal.
  The columns of V represent the vectors which define the H(i)'s.  
  The number of blocks is B = ceiling(N/NB), where each
  block is of order NB except for the last block, which is of order 
  IB = N - (B-1)*NB.  For each of the B blocks, a upper triangular block
  reflector factor is computed: T1, T2, ..., TB.  The NB-by-NB (and IB-by-IB 
  for the last block) T's are stored in the NB-by-N matrix T as
               T = [T1 T2 ... TB].
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 189 of file stpqrt.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
