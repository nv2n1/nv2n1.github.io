---
title: "dtrexc(3)"
name: "dtrexc"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtrexc/"
description: "dtrexc.f –"
---

<h2 class="name">NAME</h2>
<p> dtrexc.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtrexc</code> (COMPQ, N, T, LDT, Q, LDQ, IFST, ILST, WORK, INFO)<br />
 <i></i><code>DTREXC</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtrexc (characterCOMPQ, integerN, double precision, dimension( ldt, * )T, integerLDT, double precision, dimension( ldq, * )Q, integerLDQ, integerIFST, integerILST, double precision, dimension( * )WORK, integerINFO)</h3>
<p> <code>DTREXC</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DTREXC reorders the real Schur factorization of a real matrix
 A = Q*T*Q**T, so that the diagonal block of T with row index IFST is
 moved to row ILST.
 The real Schur form T is reordered by an orthogonal similarity
 transformation Z**T*T*Z, and optionally the matrix Q of Schur vectors
 is updated by postmultiplying it with Z.
 T must be in Schur canonical form (as returned by DHSEQR), that is,
 block upper triangular with 1-by-1 and 2-by-2 diagonal blocks; each
 2-by-2 diagonal block has its diagonal elements equal and its
 off-diagonal elements of opposite sign.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>COMPQ</i> </p>
<pre>
          COMPQ is CHARACTER*1
          = 'V':  update the matrix Q of Schur vectors;
          = 'N':  do not update Q.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrix T. N &gt;= 0.
</pre>
<p> <i>T</i> </p>
<pre>
          T is DOUBLE PRECISION array, dimension (LDT,N)
          On entry, the upper quasi-triangular matrix T, in Schur
          Schur canonical form.
          On exit, the reordered upper quasi-triangular matrix, again
          in Schur canonical form.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T. LDT &gt;= max(1,N).
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is DOUBLE PRECISION array, dimension (LDQ,N)
          On entry, if COMPQ = 'V', the matrix Q of Schur vectors.
          On exit, if COMPQ = 'V', Q has been postmultiplied by the
          orthogonal transformation matrix Z which reorders T.
          If COMPQ = 'N', Q is not referenced.
</pre>
<p> <i>LDQ</i> </p>
<pre>
          LDQ is INTEGER
          The leading dimension of the array Q.  LDQ &gt;= max(1,N).
</pre>
<p> <i>IFST</i> </p>
<pre>
          IFST is INTEGER
</pre>
<p> <i>ILST</i> </p>
<pre><code>
ILST is INTEGER
    Specify the reordering of the diagonal blocks of T.The block with row index IFST is moved to row ILST,
    by a
        sequence of transpositions between adjacent blocks.On exit,
    if IFST pointed on entry to the second row of a 2 - by - 2 block, it is changed to point to the first row;
ILST
        always points to the first row of the block in its final
        position(which may differ from its input value by + 1 or -1)
            .1 &lt;= IFST
    &lt;= N;
1 &lt;= ILST &lt;= N.
</code></pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          = 1:  two adjacent blocks were too close to swap (the problem
                is very ill-conditioned); T may have been partially
                reordered, and ILST points to the first row of the
                current position of the block being moved.
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
<p> Definition at line 146 of file dtrexc.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
