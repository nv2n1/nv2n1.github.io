---
title: "ctgsna(3)"
name: "ctgsna"
section: "3"
letter: "c"
url: "/docs/linux/man/3-ctgsna/"
description: "ctgsna.f –"
---

<h2 class="name">NAME</h2>
<p> ctgsna.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>ctgsna</code> (JOB, HOWMNY, SELECT, N, A, LDA, B, LDB, VL, LDVL, VR, LDVR, S, DIF, MM, M, WORK, LWORK, IWORK, INFO)<br />
 <i></i><code>CTGSNA</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine ctgsna (characterJOB, characterHOWMNY, logical, dimension( * )SELECT, integerN, complex, dimension( lda, * )A, integerLDA, complex, dimension( ldb, * )B, integerLDB, complex, dimension( ldvl, * )VL, integerLDVL, complex, dimension( ldvr, * )VR, integerLDVR, real, dimension( * )S, real, dimension( * )DIF, integerMM, integerM, complex, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>CTGSNA</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CTGSNA estimates reciprocal condition numbers for specified
 eigenvalues and/or eigenvectors of a matrix pair (A, B).
 (A, B) must be in generalized Schur canonical form, that is, A and
 B are both upper triangular.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOB</i> </p>
<pre><code>
          JOB is CHARACTER*1
          Specifies whether condition numbers are required for
          eigenvalues (S) or eigenvectors (DIF):
          = 'E': for eigenvalues only (S);
          = 'V': for eigenvectors only (DIF);
          = 'B': for both eigenvalues and eigenvectors (S and DIF).
</code></pre>
<p> <i>HOWMNY</i> </p>
<pre>
          HOWMNY is CHARACTER*1
          = 'A': compute condition numbers for all eigenpairs;
          = 'S': compute condition numbers for selected eigenpairs
                 specified by the array SELECT.
</pre>
<p> <i>SELECT</i> </p>
<pre>
          SELECT is LOGICAL array, dimension (N)
          If HOWMNY = 'S', SELECT specifies the eigenpairs for which
          condition numbers are required. To select condition numbers
          for the corresponding j-th eigenvalue and/or eigenvector,
          SELECT(j) must be set to .TRUE..
          If HOWMNY = 'A', SELECT is not referenced.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the square matrix pair (A, B). N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is COMPLEX array, dimension (LDA,N)
          The upper triangular matrix A in the pair (A,B).
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is COMPLEX array, dimension (LDB,N)
          The upper triangular matrix B in the pair (A, B).
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1,N).
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is COMPLEX array, dimension (LDVL,M)
          IF JOB = 'E' or 'B', VL must contain left eigenvectors of
          (A, B), corresponding to the eigenpairs specified by HOWMNY
          and SELECT.  The eigenvectors must be stored in consecutive
          columns of VL, as returned by CTGEVC.
          If JOB = 'V', VL is not referenced.
</pre>
<p> <i>LDVL</i> </p>
<pre>
          LDVL is INTEGER
          The leading dimension of the array VL. LDVL &gt;= 1; and
          If JOB = 'E' or 'B', LDVL &gt;= N.
</pre>
<p> <i>VR</i> </p>
<pre>
          VR is COMPLEX array, dimension (LDVR,M)
          IF JOB = 'E' or 'B', VR must contain right eigenvectors of
          (A, B), corresponding to the eigenpairs specified by HOWMNY
          and SELECT.  The eigenvectors must be stored in consecutive
          columns of VR, as returned by CTGEVC.
          If JOB = 'V', VR is not referenced.
</pre>
<p> <i>LDVR</i> </p>
<pre>
          LDVR is INTEGER
          The leading dimension of the array VR. LDVR &gt;= 1;
          If JOB = 'E' or 'B', LDVR &gt;= N.
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension (MM)
          If JOB = 'E' or 'B', the reciprocal condition numbers of the
          selected eigenvalues, stored in consecutive elements of the
          array.
          If JOB = 'V', S is not referenced.
</pre>
<p> <i>DIF</i> </p>
<pre>
          DIF is REAL array, dimension (MM)
          If JOB = 'V' or 'B', the estimated reciprocal condition
          numbers of the selected eigenvectors, stored in consecutive
          elements of the array.
          If the eigenvalues cannot be reordered to compute DIF(j),
          DIF(j) is set to 0; this can only occur when the true value
          would be very small anyway.
          For each eigenvalue/vector specified by SELECT, DIF stores
          a Frobenius norm-based estimate of Difl.
          If JOB = 'E', DIF is not referenced.
</pre>
<p> <i>MM</i> </p>
<pre>
          MM is INTEGER
          The number of elements in the arrays S and DIF. MM &gt;= M.
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of elements of the arrays S and DIF used to store
          the specified condition numbers; for each selected eigenvalue
          one element is used. If HOWMNY = 'A', M is set to N.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is COMPLEX array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK. LWORK &gt;= max(1,N).
          If JOB = 'V' or 'B', LWORK &gt;= max(1,2*N*N).
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N+2)
          If JOB = 'E', IWORK is not referenced.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0: Successful exit
          &lt; 0: If INFO = -i, the i-th argument had an illegal value
</pre>
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
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd>
<p>The reciprocal of the condition number of the i &#8211; th generalized<br />
                                                      eigenvalue w = (a, b)is defined as S(I) = (| v * *HAu | **2 + | v * *HBu | **2) * *(1 / 2) / (norm(u) * norm(v)) where u and v are the right and left eigenvectors of(A, B)<br />
corresponding to w;<br />
| z | denotes the absolute value of the complex number, and norm(u) denotes the 2 &#8211; norm of the vector u.The pair(a, b)<br />
corresponds to an eigenvalue w = a / b(= v * *HAu / v * *HBu) of the<br />
                                         matrix<br />
                                         pair(A, B)<br />
                                             .If both a and<br />
                                 b equal zero,<br />
                             then(A, B) is<br />
                             singular and S(I) = -1 is returned.An approximate error bound on the chordal distance between the i &#8211; th<br />
                                                     computed generalized eigenvalue w<br />
                                                 and the corresponding exact<br />
                                                         eigenvalue lambda is<br />
                                                         chord(w, lambda) &lt;= EPS * norm(A, B) / S(I),<br />
                             where EPS is the machine precision.The reciprocal of the condition number of the right eigenvector u<br />
                                 and left eigenvector v corresponding to the generalized eigenvalue w<br />
                             is defined as follows.Suppose(A, B) = (a *)(b *)1(0 A22),<br />
                             (0 B22)n &#8211; 1 1 n &#8211; 1 1 n &#8211; 1 Then the reciprocal condition number DIF(I) is<br />
          Difl[(a, b), (A22, B22)]  = sigma-min( Zl )<br />
  where sigma-min(Zl) denotes the smallest singular value of<br />
         Zl = [ kron(a, In-1) -kron(1, A22) ]<br />
              [ kron(b, In-1) -kron(1, B22) ].<br />
  Here In-1 is the identity matrix of size n-1 and X**H is the conjugate<br />
  transpose of X. kron(X, Y) is the Kronecker product between the<br />
  matrices X and Y.<br />
  We approximate the smallest singular value of Zl with an upper<br />
  bound. This is done by CLATDF.<br />
  An approximate error bound for a computed eigenvector VL(i) or<br />
  VR(i) is given by<br />
                      EPS * norm(A, B) / DIF(i).<br />
  See ref. [2-3] for more details and further references.</p>
<p>&nbsp;<wbr></dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Bo Kagstrom and Peter Poromaa, Department of Computing Science, Umea University, S-901 87 Umea, Sweden.</dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd>
<pre><code>
[1] B.Kagstrom; A Direct Method for Reordering Eigenvalues in the
      Generalized Real Schur Form of a Regular Matrix Pair (A, B), in
      M.S. Moonen et al (eds), Linear Algebra for Large Scale and
      Real-Time Applications, Kluwer Academic Publ. 1993, pp 195-218.
  [2] B. Kagstrom and P. Poromaa; Computing Eigenspaces with Specified
      Eigenvalues of a Regular Matrix Pair (A, B) and Condition
      Estimation: Theory, Algorithms and Software, Report
      UMINF - 94.04, Department of Computing Science, Umea University,
      S-901 87 Umea, Sweden, 1994. Also as LAPACK Working Note 87.
      To appear in Numerical Algorithms, 1996.
  [3] B. Kagstrom and P. Poromaa, LAPACK-Style Algorithms and Software
      for Solving the Generalized Sylvester Equation and Estimating the
      Separation between Regular Matrix Pairs, Report UMINF - 93.23,
      Department of Computing Science, Umea University, S-901 87 Umea,
      Sweden, December 1993, Revised April 1994, Also as LAPACK Working
      Note 75.
      To appear in ACM Trans. on Math. Software, Vol 22, No 1, 1996.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 310 of file ctgsna.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
