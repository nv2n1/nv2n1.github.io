---
title: "sspgvd(3)"
name: "sspgvd"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sspgvd/"
description: "sspgvd.f –"
---

<h2 class="name">NAME</h2>
<p> sspgvd.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sspgvd</code> (ITYPE, JOBZ, UPLO, N, AP, BP, W, Z, LDZ, WORK, LWORK, IWORK, LIWORK, INFO)<br />
 <i></i><code>SSPGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sspgvd (integerITYPE, characterJOBZ, characterUPLO, integerN, real, dimension( * )AP, real, dimension( * )BP, real, dimension( * )W, real, dimension( ldz, * )Z, integerLDZ, real, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerLIWORK, integerINFO)</h3>
<p> <code>SSPGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SSPGVD computes all the eigenvalues, and optionally, the eigenvectors
 of a real generalized symmetric-definite eigenproblem, of the form
 A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.  Here A and
 B are assumed to be symmetric, stored in packed format, and B is also
 positive definite.
 If eigenvectors are desired, it uses a divide and conquer algorithm.
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
<dd> <i>ITYPE</i> </p>
<pre>
          ITYPE is INTEGER
          Specifies the problem type to be solved:
          = 1:  A*x = (lambda)*B*x
          = 2:  A*B*x = (lambda)*x
          = 3:  B*A*x = (lambda)*x
</pre>
<p> <i>JOBZ</i> </p>
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
<p> <i>AP</i> </p>
<pre><code>
          AP is REAL array, dimension (N*(N+1)/2)
          On entry, the upper or lower triangle of the symmetric matrix
          A, packed columnwise in a linear array.  The j-th column of A
          is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          On exit, the contents of AP are destroyed.
</code></pre>
<p> <i>BP</i> </p>
<p>          BP is REAL array, dimension (N*(N+1)/2)<br />
          On entry, the upper or lower triangle of the symmetric matrix<br />
          B, packed columnwise in a linear array.  The j-th column of B<br />
          is stored in the array BP as follows:<br />
          if UPLO = &#8216;U&#8217;, BP(i + (j-1)*j/2) = B(i,j) for 1&lt;=i&lt;=j;<br />
          if UPLO = &#8216;L&#8217;, BP(i + (j-1)*(2*n-j)/2) = B(i,j) for j&lt;=i&lt;=n.<br />
          On exit, the triangular factor U or L from the Cholesky<br />
          factorization B = U**T*U or B = L*L**T, in the same storage<br />
          format as B.</p>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          If INFO = 0, the eigenvalues in ascending order.
</pre>
<p> <i>Z</i> </p>
<p>Z is REAL array, dimension(LDZ, N) If JOBZ = &#8216;V&#8217;, then if INFO = 0, Z contains the matrix Z of eigenvectors.The eigenvectors are normalized as follows : if ITYPE = 1 or 2, Z **T *B *Z = I;<br />
if ITYPE<br />
= 3, Z **T *inv(B) *Z = I.If JOBZ = &#8216;N&#8217;, then Z is not referenced.</p>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1, and if
          JOBZ = 'V', LDZ &gt;= max(1,N).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is REAL array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the required LWORK.
</pre>
<p> <i>LWORK</i> </p>
<p>LWORK is INTEGER<br />
        The dimension of the array WORK.If N &lt;= 1,<br />
    LWORK &gt;= 1. If JOBZ = &#8216;N&#8217; and N &gt; 1, LWORK &gt;= 2 *N.If JOBZ = &#8216;V&#8217; and N &gt; 1, LWORK &gt;= 1 + 6 *N + 2 *N ** 2. If LWORK = -1, then a workspace query is assumed;<br />
the routine<br />
    only calculates the required sizes of the WORK and IWORK<br />
        arrays,<br />
    returns these values as the first entries of the WORK<br />
        and IWORK arrays,<br />
    and no error message related to LWORK or<br />
        LIWORK is issued by XERBLA.</p>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (MAX(1,LIWORK))
          On exit, if INFO = 0, <a href="//www.systutorials.com/docs/linux/man/1-IWORK/">IWORK</a>(1) returns the required LIWORK.
</pre>
<p> <i>LIWORK</i> </p>
<p>LIWORK is INTEGER<br />
    The dimension of the array IWORK.If JOBZ = &#8216;N&#8217; or N &lt;= 1,<br />
                                        LIWORK &gt;= 1. If JOBZ = &#8216;V&#8217; and N &gt; 1, LIWORK &gt;= 3 + 5 *N.If LIWORK = -1, then a workspace query is assumed;<br />
the<br />
    routine only calculates the required sizes of the WORK and<br />
        IWORK arrays,<br />
    returns these values as the first entries of<br />
        the WORK and IWORK arrays,<br />
    and no error message related to<br />
            LWORK or<br />
        LIWORK is issued by XERBLA.</p>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : SPPTRF or SSPEVD returned an error code : &lt;= N : if INFO = i, SSPEVD failed to converge;
i off - diagonal elements of an intermediate
            tridiagonal form did not converge to zero;
             &gt; N:   if INFO = N + i, for 1 &lt;= i &lt;= N, then the leading
                    minor of order i of B is not positive definite.
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
<p> Definition at line 210 of file sspgvd.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
