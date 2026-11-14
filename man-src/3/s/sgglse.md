---
title: "sgglse(3)"
name: "sgglse"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgglse/"
description: "sgglse.f –"
---

<h2 class="name">NAME</h2>
<p> sgglse.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sgglse</code> (M, N, P, A, LDA, B, LDB, C, D, X, WORK, LWORK, INFO)<br />
 <i></i><code> SGGLSE solves overdetermined or underdetermined systems for OTHER matrices</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgglse (integerM, integerN, integerP, real, dimension( lda, * )A, integerLDA, real, dimension( ldb, * )B, integerLDB, real, dimension( * )C, real, dimension( * )D, real, dimension( * )X, real, dimension( * )WORK, integerLWORK, integerINFO)</h3>
<p> <code> SGGLSE solves overdetermined or underdetermined systems for OTHER matrices</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
SGGLSE solves the linear equality - constrained least squares(LSE)
                                        problem : minimize
    || c - A *x || _2 subject to B *x = d where A is an M - by - N matrix,
                                   B is a P - by - N matrix, c is a given M - vector, and d is a given P - vector.It is assumed that P &lt;= N &lt;= M + P, and rank(B) = P and rank((A)) = N.((B))These conditions ensure that the LSE problem has a unique solution,
                                   which is obtained using a generalized RQ factorization of the
    matrices(B, A)
given by
    B = (0 R) * Q,
    A = Z * T * Q.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the matrix A.  M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the matrices A and B. N &gt;= 0.
</pre>
<p> <i>P</i> </p>
<pre>
          P is INTEGER
          The number of rows of the matrix B. 0 &lt;= P &lt;= N &lt;= M+P.
</pre>
<p> <i>A</i> </p>
<pre>
          A is REAL array, dimension (LDA,N)
          On entry, the M-by-N matrix A.
          On exit, the elements on and above the diagonal of the array
          contain the min(M,N)-by-N upper trapezoidal matrix T.
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,M).
</pre>
<p> <i>B</i> </p>
<pre>
          B is REAL array, dimension (LDB,N)
          On entry, the P-by-N matrix B.
          On exit, the upper triangle of the subarray B(1:P,N-P+1:N)
          contains the P-by-P upper triangular matrix R.
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1,P).
</pre>
<p> <i>C</i> </p>
<pre>
          C is REAL array, dimension (M)
          On entry, C contains the right hand side vector for the
          least squares part of the LSE problem.
          On exit, the residual sum of squares for the solution
          is given by the sum of squares of elements N-P+1 to M of
          vector C.
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (P)
          On entry, D contains the right hand side vector for the
          constrained equation.
          On exit, D is destroyed.
</pre>
<p> <i>X</i> </p>
<pre>
          X is REAL array, dimension (N)
          On exit, X is the solution of the LSE problem.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>          LWORK is INTEGER<br />
          The dimension of the array WORK. LWORK &gt;= max(1,M+N+P).<br />
          For optimum performance LWORK &gt;= P+min(M,N)+max(M,N)*NB,<br />
          where NB is an upper bound for the optimal blocksizes for<br />
          SGEQRF, SGERQF, SORMQR and SORMRQ.<br />
          If LWORK = -1, then a workspace query is assumed;<br />
          the routine<br />
              only calculates the optimal size of the WORK array,<br />
              returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.</p>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit.&lt; 0 : if INFO = -i, the i - th argument had an illegal value.= 1 : the upper triangular factor R associated with B in the
                                                                                                             generalized RQ factorization of the
                                                                                                             pair(B, A)
is
    singular,
    so that rank(B) &lt; P;
the least squares
    solution could not be computed.= 2 : the(N - P) by(N - P) part of the upper trapezoidal factor
                                             T associated with A in the generalized RQ factorization
                                                 of the
                                                 pair(B, A)
is singular, so that
                     rank((A)) &lt; N;
the least squares solution could not((B))
    be computed.
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
<p> Definition at line 180 of file sgglse.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
