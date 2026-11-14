---
title: "ssptrf(3)"
name: "ssptrf"
section: "3"
letter: "s"
url: "/docs/linux/man/3-ssptrf/"
description: "ssptrf.f –"
---

<h2 class="name">NAME</h2>
<p> ssptrf.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ssptrf</code> (UPLO, N, AP, IPIV, INFO)<br />
 <i></i><code>SSPTRF</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ssptrf (characterUPLO, integerN, real, dimension( * )AP, integer, dimension( * )IPIV, integerINFO)</h3>
<p> <code>SSPTRF</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSPTRF computes the factorization of a real symmetric matrix A stored
 in packed format using the Bunch-Kaufman diagonal pivoting method:
    A = U*D*U**T  or  A = L*D*L**T
 where U (or L) is a product of permutation and unit upper (lower)
 triangular matrices, and D is symmetric and block diagonal with
 1-by-1 and 2-by-2 diagonal blocks.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangle of A is stored;
          = 'L':  Lower triangle of A is stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix A.  N &gt;= 0.
</pre>
<p> <i>AP</i> </p>
<pre><code>
          AP is REAL array, dimension (N*(N+1)/2)
          On entry, the upper or lower triangle of the symmetric matrix
          A, packed columnwise in a linear array.  The j-th column of A
          is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          On exit, the block diagonal matrix D and the multipliers used
          to obtain the factor U or L, stored as a packed triangular
          matrix overwriting A (see below for further details).
</code></pre>
<p> <i>IPIV</i> </p>
<pre>
          IPIV is INTEGER array, dimension (N)
          Details of the interchanges and the block structure of D.
          If IPIV(k) &gt; 0, then rows and columns k and IPIV(k) were
          interchanged and D(k,k) is a 1-by-1 diagonal block.
          If UPLO = 'U' and IPIV(k) = IPIV(k-1) &lt; 0, then rows and
          columns k-1 and -IPIV(k) were interchanged and D(k-1:k,k-1:k)
          is a 2-by-2 diagonal block.  If UPLO = 'L' and IPIV(k) =
          IPIV(k+1) &lt; 0, then rows and columns k+1 and -IPIV(k) were
          interchanged and D(k:k+1,k:k+1) is a 2-by-2 diagonal block.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value
          &gt; 0: if INFO = i, D(i,i) is exactly zero.  The factorization
               has been completed, but the block diagonal matrix D is
               exactly singular, and division by zero will occur if it
               is used to solve a system of equations.
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
<dd> November 2011</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<pre>
  5-96 - Based on modifications by J. Lewis, Boeing Computer Services
         Company
  If UPLO = 'U', then A = U*D*U**T, where
     U = H(n)*H(n)* ... *P(k)U(k)* ...,
  i.e., U is a product of terms P(k)*U(k), where k decreases from n to
  1 in steps of 1 or 2, and D is a block diagonal matrix with 1-by-1
  and 2-by-2 diagonal blocks D(k).  P(k) is a permutation matrix as
  defined by IPIV(k), and U(k) is a unit upper triangular matrix, such
  that if the diagonal block D(k) is of order s (s = 1 or 2), then
             (   I    v    0   )   k-s
     U(k) =  (   0    I    0   )   s
             (   0    0    I   )   n-k
                k-s   s   n-k
  If s = 1, D(k) overwrites A(k,k), and v overwrites A(1:k-1,k).
  If s = 2, the upper triangle of D(k) overwrites A(k-1,k-1), A(k-1,k),
  and A(k,k), and v overwrites A(1:k-2,k-1:k).
  If UPLO = 'L', then A = L*D*L**T, where
     L = <a href="//www.systutorials.com/docs/linux/man/1-P/">P</a>(1)*<a href="//www.systutorials.com/docs/linux/man/1-L/">L</a>(1)* ... *P(k)*L(k)* ...,
  i.e., L is a product of terms P(k)*L(k), where k increases from 1 to
  n in steps of 1 or 2, and D is a block diagonal matrix with 1-by-1
  and 2-by-2 diagonal blocks D(k).  P(k) is a permutation matrix as
  defined by IPIV(k), and L(k) is a unit lower triangular matrix, such
  that if the diagonal block D(k) is of order s (s = 1 or 2), then
             (   I    0     0   )  k-1
     L(k) =  (   0    I     0   )  s
             (   0    v     I   )  n-k-s+1
                k-1   s  n-k-s+1
  If s = 1, D(k) overwrites A(k,k), and v overwrites A(k+1:n,k).
  If s = 2, the lower triangle of D(k) overwrites A(k,k), A(k+1,k),
  and A(k+1,k+1), and v overwrites A(k+2:n,k:k+1).
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 158 of file ssptrf.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
