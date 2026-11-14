---
title: "dgebal-f(3)"
name: "dgebal-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dgebal-f/"
description: "dgebal.f –"
---

<p>dgebal.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dgebal</code> (JOB, N, A, LDA, ILO, IHI, SCALE, INFO)<br />
 <i></i><code>DGEBAL</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dgebal (characterJOB, integerN, double precision, dimension( lda, * )A, integerLDA, integerILO, integerIHI, double precision, dimension( * )SCALE, integerINFO)</h3>
<p><code>DGEBAL</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DGEBAL balances a general real matrix A. This involves, first,
 permuting A by a similarity transformation to isolate eigenvalues
 in the first 1 to ILO-1 and last IHI+1 to N elements on the
 diagonal; and second, applying a diagonal similarity transformation
 to rows and columns ILO to IHI to make the rows and columns as
 close in norm as possible. Both steps are optional.
 Balancing may reduce the 1-norm of the matrix, and improve the
 accuracy of the computed eigenvalues and/or eigenvectors.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>JOB</i> </p>
<pre> JOB is CHARACTER*1
 Specifies the operations to be performed on A:
 = 'N': none: simply set ILO = 1, IHI = N, SCALE(I) = 1.0
 for i = 1,...,N;
 = 'P': permute only;
 = 'S': scale only;
 = 'B': both permute and scale.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>A</i> </p>
<pre> A is DOUBLE array, dimension (LDA,N)
 On entry, the input matrix A.
 On exit, A is overwritten by the balanced matrix.
 If JOB = 'N', A is not referenced.
 See Further Details.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>ILO</i> </p>
<pre> ILO is INTEGER</pre>
<p>&nbsp;<wbr><br />
 <i>IHI</i> </p>
<pre> IHI is INTEGER
 ILO and IHI are set to integers such that on exit
 A(i,j) = 0 if i &gt; j and j = 1,...,ILO-1 or I = IHI+1,...,N.
 If JOB = 'N' or 'S', ILO = 1 and IHI = N.</pre>
<p><i>SCALE</i> </p>
<pre> SCALE is DOUBLE array, dimension (N)
 Details of the permutations and scaling factors applied to
 A. If P(j) is the index of the row and column interchanged
 with row and column j and D(j) is the scaling factor
 applied to row and column j, then
 SCALE(j) = P(j) for j = 1,...,ILO-1
 = D(j) for j = ILO,...,IHI
 = P(j) for j = IHI+1,...,N.
 The order in which the interchanges are made is N to IHI+1,
 then 1 to ILO-1.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> <code>Further Details: </code></p>
<dl COMPACT>
<dd>
<pre> The permutations consist of row and column interchanges which put
 the matrix in the form
 ( T1 X Y )
 P A P = ( 0 B Z )
 ( 0 0 T2 )
 where T1 and T2 are upper triangular matrices whose eigenvalues lie
 along the diagonal. The column indices ILO and IHI mark the starting
 and ending columns of the submatrix B. Balancing consists of applying
 a diagonal similarity transformation inv(D) * B * D to make the
 1-norms of each row of B and its corresponding column nearly equal.
 The output matrix is
 ( T1 X*D Y )
 ( 0 inv(D)*B*D inv(D)*Z ).
 ( 0 0 T2 )
 Information about the permutations P and the diagonal matrix D is
 returned in the vector SCALE.
 This subroutine is based on the EISPACK routine BALANC.
 Modified by Tzu-Yi Chen, Computer Science Division, University of
 California at Berkeley, USA</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 161 of file dgebal.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
