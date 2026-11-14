---
title: "slasq2(3)"
name: "slasq2"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slasq2/"
description: "slasq2.f –"
---

<h2 class="name">NAME</h2>
<p> slasq2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slasq2</code> (N, Z, INFO)<br />
 <i></i><code>SLASQ2</code> computes all the eigenvalues of the symmetric positive definite tridiagonal matrix associated with the qd Array Z to high relative accuracy. Used by sbdsqr and sstegr.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slasq2 (integerN, real, dimension( * )Z, integerINFO)</h3>
<p> <code>SLASQ2</code> computes all the eigenvalues of the symmetric positive definite tridiagonal matrix associated with the qd Array Z to high relative accuracy. Used by sbdsqr and sstegr. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLASQ2 computes all the eigenvalues of the symmetric positive 
 definite tridiagonal matrix associated with the qd array Z to high
 relative accuracy are computed to high relative accuracy, in the
 absence of denormalization, underflow and overflow.
 To see the relation of Z to the tridiagonal matrix, let L be a
 unit lower bidiagonal matrix with subdiagonals Z(2,4,6,,..) and
 let U be an upper bidiagonal matrix with 1's above and diagonal
 Z(1,3,5,,..). The tridiagonal is L*U or, if you prefer, the
 symmetric tridiagonal to which it is similar.
 Note : SLASQ2 defines a logical variable, IEEE, which is true
 on machines which follow ieee-754 floating-point standard in their
 handling of infinities and NaNs, and false otherwise. This variable
 is passed to SLASQ3.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
        The number of rows and columns in the matrix. N &gt;= 0.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is REAL array, dimension ( 4*N )
        On entry Z holds the qd array. On exit, entries 1 to N hold
        the eigenvalues in decreasing order, Z( 2*N+1 ) holds the
        trace, and Z( 2*N+2 ) holds the sum of the eigenvalues. If
        N &gt; 2, then Z( 2*N+3 ) holds the iteration count, Z( 2*N+4 )
        holds NDIVS/NIN^2, and Z( 2*N+5 ) holds the percentage of
        shifts that failed.
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if the i - th argument is a scalar and had an illegal
                                                                                       value,
        then INFO = -i, if the i - th argument is an array and the j - entry had an illegal value, then INFO = -(i * 100 + j) &gt; 0 : the algorithm failed = 1, a split was marked by a positive value in E = 2, current block of Z not diagonalized after 100 * N iterations(in inner while loop).On exit Z holds a qd array with the same eigenvalues as the given Z.= 3, termination criterion of outer while loop not met(program created more than N unreduced blocks)
</code></pre>
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
<pre>
  Local Variables: I0:N0 defines a current unreduced segment of Z.
  The shifts are accumulated in SIGMA. Iteration count is in ITER.
  Ping-pong is controlled by PP (alternates between 0 and 1).
</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 113 of file slasq2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
