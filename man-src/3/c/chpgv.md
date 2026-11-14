---
title: "chpgv(3)"
name: "chpgv"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chpgv/"
description: "chpgv.f –"
---

<h2 class="name">NAME</h2>
<p> chpgv.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>chpgv</code> (ITYPE, JOBZ, UPLO, N, AP, BP, W, Z, LDZ, WORK, RWORK, INFO)<br />
 <i></i><code>CHPGST</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine chpgv (integerITYPE, characterJOBZ, characterUPLO, integerN, complex, dimension( * )AP, complex, dimension( * )BP, real, dimension( * )W, complex, dimension( ldz, * )Z, integerLDZ, complex, dimension( * )WORK, real, dimension( * )RWORK, integerINFO)</h3>
<p> <code>CHPGST</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CHPGV computes all the eigenvalues and, optionally, the eigenvectors
 of a complex generalized Hermitian-definite eigenproblem, of the form
 A*x=(lambda)*B*x,  A*Bx=(lambda)*x,  or B*A*x=(lambda)*x.
 Here A and B are assumed to be Hermitian, stored in packed format,
 and B is also positive definite.
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
          AP is COMPLEX array, dimension (N*(N+1)/2)
          On entry, the upper or lower triangle of the Hermitian matrix
          A, packed columnwise in a linear array.  The j-th column of A
          is stored in the array AP as follows:
          if UPLO = 'U', AP(i + (j-1)*j/2) = A(i,j) for 1&lt;=i&lt;=j;
          if UPLO = 'L', AP(i + (j-1)*(2*n-j)/2) = A(i,j) for j&lt;=i&lt;=n.
          On exit, the contents of AP are destroyed.
</code></pre>
<p> <i>BP</i> </p>
<p>          BP is COMPLEX array, dimension (N*(N+1)/2)<br />
          On entry, the upper or lower triangle of the Hermitian matrix<br />
          B, packed columnwise in a linear array.  The j-th column of B<br />
          is stored in the array BP as follows:<br />
          if UPLO = &#8216;U&#8217;, BP(i + (j-1)*j/2) = B(i,j) for 1&lt;=i&lt;=j;<br />
          if UPLO = &#8216;L&#8217;, BP(i + (j-1)*(2*n-j)/2) = B(i,j) for j&lt;=i&lt;=n.<br />
          On exit, the triangular factor U or L from the Cholesky<br />
          factorization B = U**H*U or B = L*L**H, in the same storage<br />
          format as B.</p>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (N)
          If INFO = 0, the eigenvalues in ascending order.
</pre>
<p> <i>Z</i> </p>
<p>Z is COMPLEX array, dimension(LDZ, N) If JOBZ = &#8216;V&#8217;, then if INFO = 0, Z contains the matrix Z of eigenvectors.The eigenvectors are normalized as follows : if ITYPE = 1 or 2, Z **H *B *Z = I;<br />
if ITYPE<br />
= 3, Z **H *inv(B) *Z = I.If JOBZ = &#8216;N&#8217;, then Z is not referenced.</p>
<p> <i>LDZ</i> </p>
<pre>
          LDZ is INTEGER
          The leading dimension of the array Z.  LDZ &gt;= 1, and if
          JOBZ = 'V', LDZ &gt;= max(1,N).
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (max(1, 2*N-1))
</pre>
<p> <i>RWORK</i> </p>
<pre>
          RWORK is REAL array, dimension (max(1, 3*N-2))
</pre>
<p> <i>INFO</i> </p>
<pre><code>
INFO is INTEGER = 0 : successful exit &lt; 0 : if INFO = -i, the i - th argument had an illegal value &gt; 0 : CPPTRF or CHPEV returned an error code : &lt;= N : if INFO = i, CHPEV failed to converge;
i off - diagonal elements of an intermediate
            tridiagonal form did not convergeto zero;
             &gt; N:   if INFO = N + i, for 1 &lt;= i &lt;= n, then the leading
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
<p> Definition at line 165 of file chpgv.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
