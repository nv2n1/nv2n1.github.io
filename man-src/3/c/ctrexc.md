---
title: "ctrexc(3)"
name: "ctrexc"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctrexc/"
description: "ctrexc.f –"
---

<h2 class="name">NAME</h2>
<p> ctrexc.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ctrexc</code> (COMPQ, N, T, LDT, Q, LDQ, IFST, ILST, INFO)<br />
 <i></i><code>CTREXC</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctrexc (characterCOMPQ, integerN, complex, dimension( ldt, * )T, integerLDT, complex, dimension( ldq, * )Q, integerLDQ, integerIFST, integerILST, integerINFO)</h3>
<p> <code>CTREXC</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CTREXC reorders the Schur factorization of a complex matrix
 A = Q*T*Q**H, so that the diagonal element of T with row index IFST
 is moved to row ILST.
 The Schur form T is reordered by a unitary similarity transformation
 Z**H*T*Z, and optionally the matrix Q of Schur vectors is updated by
 postmultplying it with Z.
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
          T is COMPLEX array, dimension (LDT,N)
          On entry, the upper triangular matrix T.
          On exit, the reordered upper triangular matrix.
</pre>
<p> <i>LDT</i> </p>
<pre>
          LDT is INTEGER
          The leading dimension of the array T. LDT &gt;= max(1,N).
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is COMPLEX array, dimension (LDQ,N)
          On entry, if COMPQ = 'V', the matrix Q of Schur vectors.
          On exit, if COMPQ = 'V', Q has been postmultiplied by the
          unitary transformation matrix Z which reorders T.
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
        Specify the reordering of the diagonal elements of T : The element with row index IFST is moved to row ILST by a
                                                                   sequence of transpositions between adjacent elements.1 &lt;= IFST &lt;= N;
1 &lt;= ILST &lt;= N.
</code></pre>
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
<dd> November 2011</dl>
<p> Definition at line 125 of file ctrexc.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
