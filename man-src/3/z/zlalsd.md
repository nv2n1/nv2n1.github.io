---
title: "zlalsd(3)"
name: "zlalsd"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlalsd/"
description: "zlalsd.f –"
---

<p>zlalsd.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlalsd</code> (UPLO, SMLSIZ, N, NRHS, D, E, B, LDB, RCOND, RANK, WORK, RWORK, IWORK, INFO)<br />
 <i></i><code>ZLALSD</code> uses the singular value decomposition of A to solve the least squares problem.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlalsd (characterUPLO, integerSMLSIZ, integerN, integerNRHS, double precision, dimension( * )D, double precision, dimension( * )E, complex*16, dimension( ldb, * )B, integerLDB, double precisionRCOND, integerRANK, complex*16, dimension( * )WORK, double precision, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p><code>ZLALSD</code> uses the singular value decomposition of A to solve the least squares problem. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLALSD uses the singular value decomposition of A to solve the least
 squares problem of finding X to minimize the Euclidean norm of each
 column of A*X-B, where A is N-by-N upper bidiagonal, and X and B
 are N-by-NRHS. The solution X overwrites B.
 The singular values of A smaller than RCOND times the largest
 singular value are treated as zero in solving the least squares
 problem; in this case a minimum norm solution is returned.
 The actual singular values are returned in D in ascending order.
 This code makes very mild assumptions about floating point
 arithmetic. It will work on machines with a guard digit in
 add/subtract, or on those binary machines without guard digits
 which subtract like the Cray XMP, Cray YMP, Cray C 90, or Cray 2.
 It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPLO</i> </p>
<pre> UPLO is CHARACTER*1
 = 'U': D and E define an upper bidiagonal matrix.
 = 'L': D and E define a lower bidiagonal matrix.</pre>
<p><i>SMLSIZ</i> </p>
<pre> SMLSIZ is INTEGER
 The maximum size of the subproblems at the bottom of the
 computation tree.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The dimension of the bidiagonal matrix. N &gt;= 0.</pre>
<p><i>NRHS</i> </p>
<pre> NRHS is INTEGER
 The number of columns of B. NRHS must be at least 1.</pre>
<p><i>D</i> </p>
<pre> D is DOUBLE PRECISION array, dimension (N)
 On entry D contains the main diagonal of the bidiagonal
 matrix. On exit, if INFO = 0, D contains its singular values.</pre>
<p><i>E</i> </p>
<pre> E is DOUBLE PRECISION array, dimension (N-1)
 Contains the super-diagonal entries of the bidiagonal matrix.
 On exit, E has been destroyed.</pre>
<p><i>B</i> </p>
<pre> B is COMPLEX*16 array, dimension (LDB,NRHS)
 On input, B contains the right hand sides of the least
 squares problem. On output, B contains the solution X.</pre>
<p><i>LDB</i> </p>
<pre> LDB is INTEGER
 The leading dimension of B in the calling subprogram.
 LDB must be at least max(1,N).</pre>
<p><i>RCOND</i> </p>
<pre> RCOND is DOUBLE PRECISION
 The singular values of A less than or equal to RCOND times
 the largest singular value are treated as zero in solving
 the least squares problem. If RCOND is negative,
 machine precision is used instead.
 For example, if diag(S)*X=B were the least squares problem,
 where diag(S) is a diagonal matrix of singular values, the
 solution would be X(i) = B(i) / S(i) if S(i) is greater than
 RCOND*max(S), and X(i) = 0 if S(i) is less than or equal to
 RCOND*max(S).</pre>
<p><i>RANK</i> </p>
<pre> RANK is INTEGER
 The number of singular values of A greater than RCOND times
 the largest singular value.</pre>
<p><i>WORK</i> </p>
<pre> WORK is COMPLEX*16 array, dimension at least
 (N * NRHS).</pre>
<p><i>RWORK</i> </p>
<pre> RWORK is DOUBLE PRECISION array, dimension at least
 (9*N + 2*N*SMLSIZ + 8*N*NLVL + 3*SMLSIZ*NRHS +
 MAX( (SMLSIZ+1)**2, N*(1+NRHS) + 2*NRHS ),
 where
 NLVL = MAX( 0, INT( LOG_2( MIN( M,N )/(SMLSIZ+1) ) ) + 1 )</pre>
<p><i>IWORK</i> </p>
<pre> IWORK is INTEGER array, dimension at least
 (3*N*NLVL + 11*N).</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: The algorithm failed to compute a singular value while
 working on the submatrix lying in rows and columns
 INFO/(N+1) through MOD(INFO,N+1).</pre>
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
<p> <code>Contributors: </code></p>
<dl>
<dd>Ming Gu and Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 188 of file zlalsd.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
