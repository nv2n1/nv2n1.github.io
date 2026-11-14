---
title: "dtpqrt2(3)"
name: "dtpqrt2"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtpqrt2/"
description: "dtpqrt2.f –"
---

<h2 class="name">NAME</h2>
<p> dtpqrt2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtpqrt2</code> (M, N, L, A, LDA, B, LDB, T, LDT, INFO)<br />
 <i></i><code>DTPQRT2</code> computes a QR factorization of a real or complex &#8216;triangular-pentagonal&#8217; matrix, which is composed of a triangular block and a pentagonal block, using the compact WY representation for Q.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtpqrt2 (integerM, integerN, integerL, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldt, * )T, integerLDT, integerINFO)</h3>
<p> <code>DTPQRT2</code> computes a QR factorization of a real or complex &#8216;triangular-pentagonal&#8217; matrix, which is composed of a triangular block and a pentagonal block, using the compact WY representation for Q. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DTPQRT2 computes a QR factorization of a real &quot;triangular-pentagonal&quot;
 matrix C, which is composed of a triangular block A and pentagonal block B, 
 using the compact WY representation for Q.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The total number of rows of the matrix B.  
          M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix B, and the order of
          the triangular matrix A.
          N &gt;= 0.
</pre>
<p> <i>L</i> </p>
<pre>
          L is INTEGER
          The number of rows of the upper trapezoidal part of B.  
          MIN(M,N) &gt;= L &gt;= 0.  See Further Details.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
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
          B is DOUBLE PRECISION array, dimension (LDB,N)
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
          T is DOUBLE PRECISION array, dimension (LDT,N)
          The N-by-N upper triangular factor T of the block reflector.
          See Further Details.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T.  LDT &gt;= max(1,N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
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
  we call V above.  Note that V has the same form as B;
that is,
    V = [V1] &lt; -(M - L) - by - N rectangular[V2] &lt; -L - by - N upper trapezoidal.The columns of V represent the vectors which define the H(i)'s.   The(M + N) - by - (M + N) block reflector H is then given by H = I - W * T * W * *T where W ^ H is the conjugate transpose of W and T is the upper triangular
                                                                                                                                                                                                                                                                                           factor of the block reflector.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 174 of file dtpqrt2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
