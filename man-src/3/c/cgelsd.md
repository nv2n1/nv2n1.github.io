---
title: "cgelsd(3)"
name: "cgelsd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-cgelsd/"
description: "cgelsd.f –"
---

<h2 class="name">NAME</h2>
<p> cgelsd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>cgelsd</code> (M, N, NRHS, A, LDA, B, LDB, S, RCOND, RANK, WORK, LWORK, RWORK, IWORK, INFO)<br />
 <i></i><code> CGELSD computes the minimum-norm solution to a linear least squares problem for GE matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine cgelsd (integerM, integerN, integerNRHS, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, real, dimension( * )S, realRCOND, integerRANK, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code> CGELSD computes the minimum-norm solution to a linear least squares problem for GE matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CGELSD computes the minimum-norm solution to a real linear least
 squares problem:
     minimize 2-norm(| b - A*x |)
 using the singular value decomposition (SVD) of A. A is an M-by-N
 matrix which may be rank-deficient.
 Several right hand side vectors b and solution vectors x can be
 handled in a single call; they are stored as the columns of the
 M-by-NRHS right hand side matrix B and the N-by-NRHS solution
 matrix X.
 The problem is solved in three steps:
 (1) Reduce the coefficient matrix A to bidiagonal form with
     Householder tranformations, reducing the original problem
     into a &quot;bidiagonal least squares problem&quot; (BLS)
 (2) Solve the BLS using a divide and conquer approach.
 (3) Apply back all the Householder tranformations to solve
     the original least squares problem.
 The effective rank of A is determined by treating as zero those
 singular values which are less than RCOND times the largest singular
 value.
 The divide and conquer algorithm makes very mild assumptions about
 floating point arithmetic. It will work on machines with a guard
 digit in add/subtract, or on those binary machines without guard
 digits which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or
 Cray-2. It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A. M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrix A. N &gt;= 0.
</pre>
<p> <i>NRHS</i> </p>
<pre>
          NRHS is INTEGER
          The number of right hand sides, i.e., the number of columns
          of the matrices B and X. NRHS &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          On entry, the M-by-N matrix A.
          On exit, A has been destroyed.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,NRHS)
          On entry, the M-by-NRHS right hand side matrix B.
          On exit, B is overwritten by the N-by-NRHS solution matrix X.
          If m &gt;= n and RANK = n, the residual sum-of-squares for
          the solution in the i-th column is given by the sum of
          squares of the modulus of elements n+1:m in that column.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B.  LDB &gt;= max(1,M,N).
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension (min(M,N))
          The singular values of A in decreasing order.
          The condition number of A in the 2-norm = <a href="//www.systutorials.com/docs/linux/man/1-S/">S</a>(1)/S(min(m,n)).
</pre>
<p> <i>RCOND</i> </p>
<pre>
          RCOND is REAL
          RCOND is used to determine the effective rank of A.
          Singular values S(i) &lt;= RCOND*<a href="//www.systutorials.com/docs/linux/man/1-S/">S</a>(1) are treated as zero.
          If RCOND &lt; 0, machine precision is used instead.
</pre>
<p> <i>RANK</i> </p>
<pre>
          RANK is INTEGER
          The effective rank of A, i.e., the number of singular values
          which are greater than RCOND*<a href="//www.systutorials.com/docs/linux/man/1-S/">S</a>(1).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK. LWORK must be at least 1.
          The exact minimum amount of workspace needed depends on M,
          N and NRHS. As long as LWORK is at least
              2 * N + N * NRHS
          if M is greater than or equal to N or
              2 * M + M * NRHS
          if M is less than N, the code will execute correctly.
          For good performance, LWORK should generally be larger.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the array WORK and the
          minimum sizes of the arrays RWORK and IWORK, and returns
          these values as the first entries of the WORK, RWORK and
          IWORK arrays, and no error message related to LWORK is issued
          by XERBLA.
</pre>
<p> <i>RWORK</i> </p>
<pre><code>
RWORK is REAL array, dimension(MAX(1, LRWORK)) LRWORK &gt;= 10 * N + 2 * N *SMLSIZ + 8 * N *NLVL + 3 * SMLSIZ *NRHS + MAX((SMLSIZ + 1) * *2, N *(1 + NRHS) + 2 * NRHS) if M is greater than or equal to N or 10 * M + 2 * M *SMLSIZ + 8 * M *NLVL + 3 * SMLSIZ *NRHS + MAX((SMLSIZ + 1) * *2, N *(1 + NRHS) + 2 * NRHS) if M is less than N, the code will execute correctly.SMLSIZ is returned by ILAENV and is equal to the maximum size of the subproblems at the bottom of the computation tree(usually about 25), and NLVL = MAX(0, INT(LOG_2(MIN(M, N) / (SMLSIZ + 1))) + 1) On exit, if INFO = 0, RWORK(1) returns the minimum LRWORK.
</code></pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          LIWORK &gt;= max(1, 3*MINMN*NLVL + 11*MINMN),
          where MINMN = MIN( M,N ).
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the minimum LIWORK.
</pre>
<p> <i>INFO</i> </p>
<pre><code>
          INFO is INTEGER
          = 0: successful exit
          &lt; 0: if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  the algorithm for computing the SVD failed to converge;
          if INFO
          = i, i off - diagonal elements of an intermediate
                           bidiagonal form did not converge to zero.
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
<dd> November 2011</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Ming Gu and Ren-Cang Li, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Osni Marques, LBNL/NERSC, USA&nbsp;<wbr> </p>
<p>&nbsp;<wbr></dl>
<p> Definition at line 225 of file cgelsd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
