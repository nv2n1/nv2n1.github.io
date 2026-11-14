---
title: "zlahef(3)"
name: "zlahef"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlahef/"
description: "zlahef.f –"
---

<p>zlahef.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlahef</code> (UPLO, N, NB, KB, A, LDA, IPIV, W, LDW, INFO)<br />
 <i></i><code>ZLAHEF</code> computes a partial factorization of a complex Hermitian indefinite matrix using the Bunch-Kaufman diagonal pivoting method (blocked algorithm, calling Level 3 BLAS).</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlahef (characterUPLO, integerN, integerNB, integerKB, complex*16, dimension( lda, * )A, integerLDA, integer, dimension( * )IPIV, complex*16, dimension( ldw, * )W, integerLDW, integerINFO)</h3>
<p><code>ZLAHEF</code> computes a partial factorization of a complex Hermitian indefinite matrix using the Bunch-Kaufman diagonal pivoting method (blocked algorithm, calling Level 3 BLAS). </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAHEF computes a partial factorization of a complex Hermitian
 matrix A using the Bunch-Kaufman diagonal pivoting method. The
 partial factorization has the form:
 A = ( I U12 ) ( A11 0 ) ( I 0 ) if UPLO = 'U', or:
 ( 0 U22 ) ( 0 D ) ( U12**H U22**H )
 A = ( L11 0 ) ( D 0 ) ( L11**H L21**H ) if UPLO = 'L'
 ( L21 I ) ( 0 A22 ) ( 0 I )
 where the order of D is at most NB. The actual order is returned in
 the argument KB, and is either NB or NB-1, or N if N &lt;= NB.
 Note that U**H denotes the conjugate transpose of U.
 ZLAHEF is an auxiliary routine called by ZHETRF. It uses blocked code
 (calling Level 3 BLAS) to update the submatrix A11 (if UPLO = 'U') or
 A22 (if UPLO = 'L').</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 Hermitian matrix A is stored:
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>NB</i> </p>
<pre> NB is INTEGER
 The maximum number of columns of the matrix A that should be
 factored. NB should be at least 2 to allow for 2-by-2 pivot
 blocks.</pre>
<p><i>KB</i> </p>
<pre> KB is INTEGER
 The number of columns of A that were actually factored.
 KB is either NB-1 or NB, or N if N &lt;= NB.</pre>
<p><i>A</i> </p>
<pre> A is COMPLEX*16 array, dimension (LDA,N)
 On entry, the Hermitian matrix A. If UPLO = 'U', the leading
 n-by-n upper triangular part of A contains the upper
 triangular part of the matrix A, and the strictly lower
 triangular part of A is not referenced. If UPLO = 'L', the
 leading n-by-n lower triangular part of A contains the lower
 triangular part of the matrix A, and the strictly upper
 triangular part of A is not referenced.
 On exit, A contains details of the partial factorization.</pre>
<p><i>LDA</i> </p>
<pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,N).</pre>
<p><i>IPIV</i> </p>
<pre> IPIV is INTEGER array, dimension (N)
 Details of the interchanges and the block structure of D.
 If UPLO = 'U':
 Only the last KB elements of IPIV are set.
 If IPIV(k) &gt; 0, then rows and columns k and IPIV(k) were
 interchanged and D(k,k) is a 1-by-1 diagonal block.
 If IPIV(k) = IPIV(k-1) &lt; 0, then rows and columns
 k-1 and -IPIV(k) were interchanged and D(k-1:k,k-1:k)
 is a 2-by-2 diagonal block.
 If UPLO = 'L':
 Only the first KB elements of IPIV are set.
 If IPIV(k) &gt; 0, then rows and columns k and IPIV(k) were
 interchanged and D(k,k) is a 1-by-1 diagonal block.
 If IPIV(k) = IPIV(k+1) &lt; 0, then rows and columns
 k+1 and -IPIV(k) were interchanged and D(k:k+1,k:k+1)
 is a 2-by-2 diagonal block.</pre>
<p><i>W</i> </p>
<pre> W is COMPLEX*16 array, dimension (LDW,NB)</pre>
<p><i>LDW</i> </p>
<pre> LDW is INTEGER
 The leading dimension of the array W. LDW &gt;= max(1,N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit
 &gt; 0: if INFO = k, D(k,k) is exactly zero. The factorization
 has been completed, but the block diagonal matrix D is
 exactly singular.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2013</dl>
<p> <code>Contributors: </code></p>
<dl>
<dd>
<pre> November 2013, Igor Kozachenko,
 Computer Science Division,
 University of California, Berkeley</pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 178 of file zlahef.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
