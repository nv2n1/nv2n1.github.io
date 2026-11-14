---
title: "dlaset-f(3)"
name: "dlaset-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlaset-f/"
---

dlaset.f - 

<h2>Synopsis</h2><h3>Functions/Subroutines</h3>subroutine <b>dlaset</b> (UPLO, M, N, ALPHA, BETA, A, LDA) 
 <i></i><b>DLASET</b> initializes the off-diagonal elements and the diagonal elements of a matrix to given values.
<h2>Function/Subroutine Documentation</h2><h3>subroutine dlaset (characterUPLO, integerM, integerN, double precisionALPHA, double precisionBETA, double precision, dimension( lda, * )A, integerLDA)</h3><b>DLASET</b> initializes the off-diagonal elements and the diagonal elements of a matrix to given values. 

 <b>Purpose: </b>
<dl COMPACT><dd><pre> DLASET initializes an m-by-n matrix A to BETA on the diagonal and
 ALPHA on the offdiagonals.</pre>&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl COMPACT><dd><i>UPLO</i> 

 <pre> UPLO is CHARACTER*1
 Specifies the part of the matrix A to be set.
 = 'U': Upper triangular part is set; the strictly lower
 triangular part of A is not changed.
 = 'L': Lower triangular part is set; the strictly upper
 triangular part of A is not changed.
 Otherwise: All of the matrix A is set.</pre><i>M</i> 

 <pre> M is INTEGER
 The number of rows of the matrix A. M &gt;= 0.</pre><i>N</i> 

 <pre> N is INTEGER
 The number of columns of the matrix A. N &gt;= 0.</pre><i>ALPHA</i> 

 <pre> ALPHA is DOUBLE PRECISION
 The constant to which the offdiagonal elements are to be set.</pre><i>BETA</i> 

 <pre> BETA is DOUBLE PRECISION
 The constant to which the diagonal elements are to be set.</pre><i>A</i> 

 <pre> A is DOUBLE PRECISION array, dimension (LDA,N)
 On exit, the leading m-by-n submatrix of A is set as follows:
 if UPLO = 'U', A(i,j) = ALPHA, 1&lt;=i&lt;=j-1, 1&lt;=j&lt;=n,
 if UPLO = 'L', A(i,j) = ALPHA, j+1&lt;=i&lt;=m, 1&lt;=j&lt;=n,
 otherwise, A(i,j) = ALPHA, 1&lt;=i&lt;=m, 1&lt;=j&lt;=n, i.ne.j,
 and, for all UPLO, A(i,i) = BETA, 1&lt;=i&lt;=min(m,n).</pre><i>LDA</i> 

 <pre> LDA is INTEGER
 The leading dimension of the array A. LDA &gt;= max(1,M).</pre>&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl COMPACT><dd>Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl COMPACT><dd>September 2012</dl>
 

 

 

 Definition at line 111 of file dlaset.f.
<h2>Author</h2>Generated automatically by Doxygen for LAPACK from the source code.
