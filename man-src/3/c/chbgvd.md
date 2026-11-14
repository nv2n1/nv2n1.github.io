---
title: "chbgvd(3)"
name: "chbgvd"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chbgvd/"
description: "chbgvd.f –"
---

<h2 class="name">NAME</h2>
<p> chbgvd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chbgvd</code> (JOBZ, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, W, Z, LDZ, WORK, LWORK, RWORK, LRWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>CHBGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chbgvd (characterJOBZ, characterUPLO, integerN, integerKA, integerKB, complex, dimension( ldab, * )AB, integerLDAB, complex, dimension( ldbb, * )BB, integerLDBB, real, dimension( * )W, complex, dimension( ldz, * )Z, integerLDZ, complex, dimension( * )WORK, integerLWORK, real, dimension( * )RWORK, integerLRWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p> <code>CHBGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHBGVD computes all the eigenvalues, and optionally, the eigenvectors
 of a complex generalized Hermitian-definite banded eigenproblem, of
 the form A*x=(lambda)*B*x. Here A and B are assumed to be Hermitian
 and banded, and B is also positive definite.  If eigenvectors are
 desired, it uses a divide and conquer algorithm.
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
<dd> <i>JOBZ</i> </p>
<pre>
          JOBZ is CHARACTER*1
          = 'N':  Compute eigenvalues only;
          = 'V':  Compute eigenvalues and eigenvectors.
</pre>
<p> <i>UPLO</i> </p>
<pre>
          UPLO is CHARACTER*1
          = 'U':  Upper triangles of A and B are stored;
          = 'L':  Lower triangles of A and B are stored.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the matrices A and B.  N &gt;= 0.
</pre>
<p> <i>KA</i> </p>
<pre>
          KA is INTEGER
          The number of superdiagonals of the matrix A if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'. KA &gt;= 0.
</pre>
<p> <i>KB</i> </p>
<pre>
          KB is INTEGER
          The number of superdiagonals of the matrix B if UPLO = 'U',
          or the number of subdiagonals if UPLO = 'L'. KB &gt;= 0.
</pre>
<p> <i>AB</i> </p>
<pre><code>
          AB is COMPLEX array, dimension (LDAB, N)
          On entry, the upper or lower triangle of the Hermitian band
          matrix A, stored in the first ka+1 rows of the array.  The
          j-th column of A is stored in the j-th column of the array AB
          as follows:
          if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)&lt;=i&lt;=j;
          if UPLO = 'L', AB(1+i-j,j)    = A(i,j) for j&lt;=i&lt;=min(n,j+ka).
          On exit, the contents of AB are destroyed.
</code></pre>
<p> <i>LDAB</i> </p>
<pre>
          LDAB is INTEGER
          The leading dimension of the array AB.  LDAB &gt;= KA+1.
</pre>
<p> <i>BB</i> </p>
<p>          BB is COMPLEX array, dimension (LDBB, N)<br />
          On entry, the upper or lower triangle of the Hermitian band<br />
          matrix B, stored in the first kb+1 rows of the array.  The<br />
          j-th column of B is stored in the j-th column of the array BB<br />
          as follows:<br />
          if UPLO = &#8216;U&#8217;, BB(kb+1+i-j,j) = B(i,j) for max(1,j-kb)&lt;=i&lt;=j;<br />
          if UPLO = &#8216;L&#8217;, BB(1+i-j,j)    = B(i,j) for j&lt;=i&lt;=min(n,j+kb).<br />
          On exit, the factor S from the split Cholesky factorization<br />
          B = S**H*S, as returned by CPBSTF.</p>
<p> <i>LDBB</i> </p>
<pre>
          LDBB is INTEGER
          The leading dimension of the array BB.  LDBB &gt;= KB+1.
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          If INFO = 0, the eigenvalues in ascending order.
</pre>
<p> <i>Z</i> </p>
<pre>
          Z is COMPLEX array, dimension (LDZ, N)
          If JOBZ = 'V', then if INFO = 0, Z contains the matrix Z of
          eigenvectors, with the i-th column of Z holding the
          eigenvector associated with W(i). The eigenvectors are
          normalized so that Z**H*B*Z = I.
          If JOBZ = 'N', then Z is not referenced.
</pre>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1, and if
          JOBZ = 'V', LDZ &gt;= N.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO=0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>LWORK is INTEGER<br />
        The dimension of the array WORK.If N &lt;= 1,<br />
    LWORK &gt;= 1. If JOBZ = &#8216;N&#8217; and N &gt; 1, LWORK &gt;= N.If JOBZ = &#8216;V&#8217; and N &gt; 1, LWORK &gt;= 2 *N ** 2. If LWORK = -1, then a workspace query is assumed;<br />
the routine<br />
    only calculates the optimal sizes of the WORK,<br />
    RWORK and<br />
        IWORK arrays,<br />
    returns these values as the first entries of<br />
        the WORK,<br />
    RWORK and IWORK arrays, and no error message related to LWORK or LRWORK or LIWORK is issued by XERBLA.</p>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (MAX(1,LRWORK))
          On exit, if INFO=0, <a href="//www.systutorials.com/docs/linux/man/1-RWORK/">RWORK</a>(1) returns the optimal LRWORK.
</pre>
<p> <i>LRWORK</i> </p>
<p>LRWORK is INTEGER<br />
        The dimension of array RWORK.If N &lt;= 1,<br />
    LRWORK &gt;= 1. If JOBZ = &#8216;N&#8217; and N &gt; 1, LRWORK &gt;= N.If JOBZ = &#8216;V&#8217; and N &gt; 1, LRWORK &gt;= 1 + 5 *N + 2 *N ** 2. If LRWORK = -1, then a workspace query is assumed;<br />
the<br />
    routine only calculates the optimal sizes of the WORK,<br />
    RWORK<br />
        and IWORK arrays,<br />
    returns these values as the first entries<br />
        of the WORK,<br />
    RWORK and IWORK arrays, and no error message related to LWORK or LRWORK or LIWORK is issued by XERBLA.</p>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO=0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the optimal LIWORK.
</pre>
<p> <i>LIWORK</i> </p>
<p>LIWORK is INTEGER<br />
    The dimension of array IWORK.If JOBZ = &#8216;N&#8217; or N &lt;= 1,<br />
                                    LIWORK &gt;= 1. If JOBZ = &#8216;V&#8217; and N &gt; 1, LIWORK &gt;= 3 + 5 *N.If LIWORK = -1, then a workspace query is assumed;<br />
the<br />
    routine only calculates the optimal sizes of the WORK,<br />
    RWORK<br />
        and IWORK arrays,<br />
    returns these values as the first entries<br />
        of the WORK,<br />
    RWORK and IWORK arrays, and no error message related to LWORK or LRWORK or LIWORK is issued by XERBLA.</p>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : if INFO = i, and i is : &lt;= N : the algorithm failed to converge : i off - diagonal elements of an intermediate tridiagonal form did not converge to zero;
             &gt; N:   if INFO = N + i, for 1 &lt;= i &lt;= N, then CPBSTF
                    returned INFO = i: B is not positive definite.
                    The factorization of B could not be completed and
                    no eigenvalues or eigenvectors were computed.
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
<dd> Mark Fahey, Department of Mathematics, Univ. of Kentucky, USA</dl>
<p> Definition at line 251 of file chbgvd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
