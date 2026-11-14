---
title: "slaexc(3)"
name: "slaexc"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaexc/"
description: "slaexc.f –"
---

<h2 class="name">NAME</h2>
<p> slaexc.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaexc</code> (WANTQ, N, T, LDT, Q, LDQ, J1, N1, N2, WORK, INFO)<br />
 <i></i><code>SLAEXC</code> swaps adjacent diagonal blocks of a real upper quasi-triangular matrix in Schur canonical form, by an orthogonal similarity transformation.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaexc (logicalWANTQ, integerN, real, dimension( ldt, * )T, integerLDT, real, dimension( ldq, * )Q, integerLDQ, integerJ1, integerN1, integerN2, real, dimension( * )WORK, integerINFO)</h3>
<p> <code>SLAEXC</code> swaps adjacent diagonal blocks of a real upper quasi-triangular matrix in Schur canonical form, by an orthogonal similarity transformation. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAEXC swaps adjacent diagonal blocks T11 and T22 of order 1 or 2 in
 an upper quasi-triangular matrix T by an orthogonal similarity
 transformation.
 T must be in Schur canonical form, that is, block upper triangular
 with 1-by-1 and 2-by-2 diagonal blocks; each 2-by-2 diagonal block
 has its diagonal elemnts equal and its off-diagonal elements of
 opposite sign.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>WANTQ</i> </p>
<pre>
          WANTQ is LOGICAL
          = .TRUE. : accumulate the transformation in the matrix Q;
          = .FALSE.: do not accumulate the transformation.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix T. N &gt;= 0.
</pre>
<p> <i>T</i> </p>
<pre>
          T is REAL array, dimension (LDT,N)
          On entry, the upper quasi-triangular matrix T, in Schur
          canonical form.
          On exit, the updated matrix T, again in Schur canonical form.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T. LDT &gt;= max(1,N).
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is REAL array, dimension (LDQ,N)
          On entry, if WANTQ is .TRUE., the orthogonal matrix Q.
          On exit, if WANTQ is .TRUE., the updated matrix Q.
          If WANTQ is .FALSE., Q is not referenced.
</pre>
<p> <i>LDQ</i> </p>
<pre><code>
LDQ is INTEGER
        The leading dimension of the array Q.LDQ &gt;= 1;
and if WANTQ is.TRUE., LDQ &gt;= N.
</code></pre>
<p> <i>J1</i> </p>
<pre>
          J1 is INTEGER
          The index of the first row of the first block T11.
</pre>
<p> <i>N1</i> </p>
<pre>
          N1 is INTEGER
          The order of the first block T11. N1 = 0, 1 or 2.
</pre>
<p> <i>N2</i> </p>
<pre>
          N2 is INTEGER
          The order of the second block T22. N2 = 0, 1 or 2.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: successful exit
          = 1: the transformed matrix T would be too far from Schur
               form; the blocks are not swapped and T and Q are
               unchanged.
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
<p> Definition at line 138 of file slaexc.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
