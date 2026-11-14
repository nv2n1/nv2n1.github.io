---
title: "zlaqhb(3)"
name: "zlaqhb"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlaqhb/"
description: "zlaqhb.f –"
---

<p>zlaqhb.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlaqhb</code> (UPLO, N, KD, AB, LDAB, S, SCOND, AMAX, EQUED)<br />
 <i></i><code>ZLAQHB</code> scales a Hermitian band matrix, using scaling factors computed by cpbequ.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlaqhb (characterUPLO, integerN, integerKD, complex*16, dimension( ldab, * )AB, integerLDAB, double precision, dimension( * )S, double precisionSCOND, double precisionAMAX, characterEQUED)</h3>
<p><code>ZLAQHB</code> scales a Hermitian band matrix, using scaling factors computed by cpbequ. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAQHB equilibrates a Hermitian band matrix A 
 using the scaling factors in the vector S.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 Specifies whether the upper or lower triangular part of the
 symmetric matrix A is stored.
 = 'U': Upper triangular
 = 'L': Lower triangular</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The order of the matrix A. N &gt;= 0.</pre>
<p><i>KD</i> </p>
<pre> KD is INTEGER
 The number of super-diagonals of the matrix A if UPLO = 'U',
 or the number of sub-diagonals if UPLO = 'L'. KD &gt;= 0.</pre>
<p><i>AB</i> </p>
<pre> AB is COMPLEX*16 array, dimension (LDAB,N)
 On entry, the upper or lower triangle of the symmetric band
 matrix A, stored in the first KD+1 rows of the array. The
 j-th column of A is stored in the j-th column of the array AB
 as follows:
 if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)&lt;=i&lt;=j;
 if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j&lt;=i&lt;=min(n,j+kd).
 On exit, if INFO = 0, the triangular factor U or L from the
 Cholesky factorization A = U**H *U or A = L*L**H of the band
 matrix A, in the same storage format as A.</pre>
<p><i>LDAB</i> </p>
<pre> LDAB is INTEGER
 The leading dimension of the array AB. LDAB &gt;= KD+1.</pre>
<p><i>S</i> </p>
<pre> S is DOUBLE PRECISION array, dimension (N)
 The scale factors for A.</pre>
<p><i>SCOND</i> </p>
<pre> SCOND is DOUBLE PRECISION
 Ratio of the smallest S(i) to the largest S(i).</pre>
<p><i>AMAX</i> </p>
<pre> AMAX is DOUBLE PRECISION
 Absolute value of largest matrix entry.</pre>
<p><i>EQUED</i> </p>
<pre> EQUED is CHARACTER*1
 Specifies whether or not equilibration was done.
 = 'N': No equilibration.
 = 'Y': Equilibration was done, i.e., A has been replaced by
 diag(S) * A * diag(S).</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Internal Parameters: </code></p>
<dl>
<dd>
<pre> THRESH is a threshold value used to decide if scaling should be done
 based on the ratio of the scaling factors. If SCOND &lt; THRESH,
 scaling is done.
 LARGE and SMALL are threshold values used to decide if scaling should
 be done based on the absolute size of the largest matrix element.
 If AMAX &gt; LARGE or AMAX &lt; SMALL, scaling is done.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>September 2012</dl>
<p> Definition at line 142 of file zlaqhb.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
