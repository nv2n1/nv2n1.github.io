---
title: "chbgvx(3)"
name: "chbgvx"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chbgvx/"
description: "chbgvx.f –"
---

<h2 class="name">NAME</h2>
<p> chbgvx.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chbgvx</code> (JOBZ, RANGE, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, Q, LDQ, VL, VU, IL, IU, ABSTOL, M, W, Z, LDZ, WORK, RWORK, IWORK, IFAIL, INFO)<br />
 <i></i><code>CHBGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chbgvx (characterJOBZ, characterRANGE, characterUPLO, integerN, integerKA, integerKB, complex, dimension( ldab, * )AB, integerLDAB, complex, dimension( ldbb, * )BB, integerLDBB, complex, dimension( ldq, * )Q, integerLDQ, realVL, realVU, integerIL, integerIU, realABSTOL, integerM, real, dimension( * )W, complex, dimension( ldz, * )Z, integerLDZ, complex, dimension( * )WORK, real, dimension( * )RWORK, integer, dimension( * )IWORK, integer, dimension( * )IFAIL, integerINFO)</h3>
<p> <code>CHBGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHBGVX computes all the eigenvalues, and optionally, the eigenvectors
 of a complex generalized Hermitian-definite banded eigenproblem, of
 the form A*x=(lambda)*B*x. Here A and B are assumed to be Hermitian
 and banded, and B is also positive definite.  Eigenvalues and
 eigenvectors can be selected by specifying either all eigenvalues,
 a range of values or a range of indices for the desired eigenvalues.
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
<p> <i>RANGE</i> </p>
<pre>
          RANGE is CHARACTER*1
          = 'A': all eigenvalues will be found;
          = 'V': all eigenvalues in the half-open interval (VL,VU]
                 will be found;
          = 'I': the IL-th through IU-th eigenvalues will be found.
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
<p> <i>Q</i> </p>
<pre>
          Q is COMPLEX array, dimension (LDQ, N)
          If JOBZ = 'V', the n-by-n matrix used in the reduction of
          A*x = (lambda)*B*x to standard form, i.e. C*x = (lambda)*x,
          and consequently C to tridiagonal form.
          If JOBZ = 'N', the array Q is not referenced.
</pre>
<p> <i>LDQ</i> </p>
<pre>
          LDQ is INTEGER
          The leading dimension of the array Q.  If JOBZ = 'N',
          LDQ &gt;= 1. If JOBZ = 'V', LDQ &gt;= max(1,N).
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is REAL
</pre>
<p> <i>VU</i> </p>
<pre>
          VU is REAL
          If RANGE='V', the lower and upper bounds of the interval to
          be searched for eigenvalues. VL &lt; VU.
          Not referenced if RANGE = 'A' or 'I'.
</pre>
<p> <i>IL</i> </p>
<pre>
          IL is INTEGER
</pre>
<p> <i>IU</i> </p>
<p>IU is INTEGER<br />
    If RANGE = &#8216;I&#8217;,<br />
       the indices(in ascending order) of the<br />
           smallest and largest eigenvalues to be returned.1 &lt;= IL<br />
           &lt;= IU &lt;= N,<br />
       if N &gt; 0;<br />
IL = 1 and IU = 0 if N = 0. Not referenced if RANGE = &#8216;A&#8217; or &#8216;V&#8217;.</p>
<p> <i>ABSTOL</i> </p>
<pre>
          ABSTOL is REAL
          The absolute error tolerance for the eigenvalues.
          An approximate eigenvalue is accepted as converged
          when it is determined to lie in an interval [a,b]
          of width less than or equal to
                  ABSTOL + EPS *   max( |a|,|b| ) ,
          where EPS is the machine precision.  If ABSTOL is less than
          or equal to zero, then  EPS*|T|  will be used in its place,
          where |T| is the 1-norm of the tridiagonal matrix obtained
          by reducing AP to tridiagonal form.
          Eigenvalues will be computed most accurately when ABSTOL is
          set to twice the underflow threshold 2*SLAMCH('S'), not zero.
          If this routine returns with INFO&gt;0, indicating that some
          eigenvectors did not converge, try setting ABSTOL to
          2*SLAMCH('S').
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The total number of eigenvalues found.  0 &lt;= M &lt;= N.
          If RANGE = 'A', M = N, and if RANGE = 'I', M = IU-IL+1.
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
          WORK is COMPLEX array, dimension (N)
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (7*N)
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (5*N)
</pre>
<p> <i>IFAIL</i> </p>
<pre>
          IFAIL is INTEGER array, dimension (N)
          If JOBZ = 'V', then if INFO = 0, the first M elements of
          IFAIL are zero.  If INFO &gt; 0, then IFAIL contains the
          indices of the eigenvectors that failed to converge.
          If JOBZ = 'N', then IFAIL is not referenced.
</pre>
<p> <i>INFO</i> </p>
<pre><code>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value
          &gt; 0:  if INFO = i, and i is:
             &lt;= N:  then i eigenvectors failed to converge.  Their
                    indices are stored in array IFAIL.
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
<p> Definition at line 290 of file chbgvx.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
