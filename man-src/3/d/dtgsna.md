---
title: "dtgsna(3)"
name: "dtgsna"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dtgsna/"
description: "dtgsna.f –"
---

<h2 class="name">NAME</h2>
<p> dtgsna.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>dtgsna</code> (JOB, HOWMNY, SELECT, N, A, LDA, B, LDB, VL, LDVL, VR, LDVR, S, DIF, MM, M, WORK, LWORK, IWORK, INFO)<br />
 <i></i><code>DTGSNA</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dtgsna (characterJOB, characterHOWMNY, logical, dimension( * )SELECT, integerN, double precision, dimension( lda, * )A, integerLDA, double precision, dimension( ldb, * )B, integerLDB, double precision, dimension( ldvl, * )VL, integerLDVL, double precision, dimension( ldvr, * )VR, integerLDVR, double precision, dimension( * )S, double precision, dimension( * )DIF, integerMM, integerM, double precision, dimension( * )WORK, integerLWORK, integer, dimension( * )IWORK, integerINFO)</h3>
<p> <code>DTGSNA</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 DTGSNA estimates reciprocal condition numbers for specified
 eigenvalues and/or eigenvectors of a matrix pair (A, B) in
 generalized real Schur canonical form (or of any matrix pair
 (Q*A*Z**T, Q*B*Z**T) with orthogonal matrices Q and Z, where
 Z**T denotes the transpose of Z.
 (A, B) must be in generalized real Schur form (as returned by DGGES),
 i.e. A is block upper triangular with 1-by-1 and 2-by-2 diagonal
 blocks. B is upper triangular.
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
          for the eigenpair corresponding to a real eigenvalue w(j),
          SELECT(j) must be set to .TRUE.. To select condition numbers
          corresponding to a complex conjugate pair of eigenvalues w(j)
          and w(j+1), either SELECT(j) or SELECT(j+1) or both, must be
          set to .TRUE..
          If HOWMNY = 'A', SELECT is not referenced.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The order of the square matrix pair (A, B). N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<pre>
          A is DOUBLE PRECISION array, dimension (LDA,N)
          The upper quasi-triangular matrix A in the pair (A,B).
</pre>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A. LDA &gt;= max(1,N).
</pre>
<p> <i>B</i> </p>
<pre>
          B is DOUBLE PRECISION array, dimension (LDB,N)
          The upper triangular matrix B in the pair (A,B).
</pre>
<p> <i>LDB</i> </p>
<pre>
          LDB is INTEGER
          The leading dimension of the array B. LDB &gt;= max(1,N).
</pre>
<p> <i>VL</i> </p>
<pre>
          VL is DOUBLE PRECISION array, dimension (LDVL,M)
          If JOB = 'E' or 'B', VL must contain left eigenvectors of
          (A, B), corresponding to the eigenpairs specified by HOWMNY
          and SELECT. The eigenvectors must be stored in consecutive
          columns of VL, as returned by DTGEVC.
          If JOB = 'V', VL is not referenced.
</pre>
<p> <i>LDVL</i> </p>
<pre>
          LDVL is INTEGER
          The leading dimension of the array VL. LDVL &gt;= 1.
          If JOB = 'E' or 'B', LDVL &gt;= N.
</pre>
<p> <i>VR</i> </p>
<pre>
          VR is DOUBLE PRECISION array, dimension (LDVR,M)
          If JOB = 'E' or 'B', VR must contain right eigenvectors of
          (A, B), corresponding to the eigenpairs specified by HOWMNY
          and SELECT. The eigenvectors must be stored in consecutive
          columns ov VR, as returned by DTGEVC.
          If JOB = 'V', VR is not referenced.
</pre>
<p> <i>LDVR</i> </p>
<pre>
          LDVR is INTEGER
          The leading dimension of the array VR. LDVR &gt;= 1.
          If JOB = 'E' or 'B', LDVR &gt;= N.
</pre>
<p> <i>S</i> </p>
<pre>
          S is DOUBLE PRECISION array, dimension (MM)
          If JOB = 'E' or 'B', the reciprocal condition numbers of the
          selected eigenvalues, stored in consecutive elements of the
          array. For a complex conjugate pair of eigenvalues two
          consecutive elements of S are set to the same value. Thus
          S(j), DIF(j), and the j-th columns of VL and VR all
          correspond to the same eigenpair (but not in general the
          j-th eigenpair, unless all eigenpairs are selected).
          If JOB = 'V', S is not referenced.
</pre>
<p> <i>DIF</i> </p>
<pre>
          DIF is DOUBLE PRECISION array, dimension (MM)
          If JOB = 'V' or 'B', the estimated reciprocal condition
          numbers of the selected eigenvectors, stored in consecutive
          elements of the array. For a complex eigenvector two
          consecutive elements of DIF are set to the same value. If
          the eigenvalues cannot be reordered to compute DIF(j), DIF(j)
          is set to 0; this can only occur when the true value would be
          very small anyway.
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
          the specified condition numbers; for each selected real
          eigenvalue one element is used, and for each selected complex
          conjugate pair of eigenvalues, two elements are used.
          If HOWMNY = 'A', M is set to N.
</pre>
<p> <i>WORK</i> </p>
<pre>
          WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK))
          On exit, if INFO = 0, WORK(1) returns the optimal LWORK.
</pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
          The dimension of the array WORK. LWORK &gt;= max(1,N).
          If JOB = 'V' or 'B' LWORK &gt;= 2*N*(N+2)+16.
          If LWORK = -1, then a workspace query is assumed; the routine
          only calculates the optimal size of the WORK array, returns
          this value as the first entry of the WORK array, and no error
          message related to LWORK is issued by XERBLA.
</pre>
<p> <i>IWORK</i> </p>
<pre>
          IWORK is INTEGER array, dimension (N + 6)
          If JOB = 'E', IWORK is not referenced.
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          =0: Successful exit
          &lt;0: If INFO = -i, the i-th argument had an illegal value
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
<p>The reciprocal of the condition number of a generalized eigenvalue<br />
    w = (a, b)is defined as S(w) = (| u * *TAv | **2 + | u * *TBv | **2) * *(1 / 2) / (norm(u) * norm(v)) where u and v are the left and right eigenvectors of(A, B)<br />
corresponding to w;<br />
| z | denotes the absolute value of the complex number, and norm(u) denotes the 2 &#8211; norm of the vector u.The pair(a, b)<br />
corresponds to an eigenvalue w = a / b(= u * *TAv / u * *TBv)<br />
                                         of the matrix<br />
                                         pair(A, B)<br />
                                             .If both a and<br />
                                 b equal zero,<br />
                             then(A B) is<br />
                             singular and S(I) = -1 is returned.An approximate error bound on the chordal distance between the i &#8211; th<br />
                                                     computed generalized eigenvalue w<br />
                                                 and the corresponding exact<br />
                                                         eigenvalue lambda is<br />
                                                         chord(w, lambda) &lt;= EPS * norm(A, B) / S(I) where EPS is the machine precision.The reciprocal of the condition number DIF(i) of right eigenvector u<br />
  and left eigenvector v corresponding to the generalized eigenvalue w<br />
  is defined as follows:<br />
  a) If the i-th eigenvalue w = (a,b) is real<br />
     Suppose U and V are orthogonal transformations such that<br />
              U**T*(A, B)*V  = (S, T) = ( a   *  ) ( b  *  )  1<br />
                                        ( 0  S22 ),( 0 T22 )  n-1<br />
                                          1  n-1     1 n-1<br />
     Then the reciprocal condition number DIF(i) is<br />
                Difl((a, b), (S22, T22)) = sigma-min( Zl ),<br />
     where sigma-min(Zl) denotes the smallest singular value of the<br />
     2(n-1)-by-2(n-1) matrix<br />
         Zl = [ kron(a, In-1)  -kron(1, S22) ]<br />
              [ kron(b, In-1)  -kron(1, T22) ] .<br />
     Here In-1 is the identity matrix of size n-1. kron(X, Y) is the<br />
     Kronecker product between the matrices X and Y.<br />
     Note that if the default method for computing DIF(i)<br />
is wanted(see DLATDF), then the parameter DIFDRI(see below) should be<br />
                       changed from 3 to 4(routine DLATDF(IJOB = 2 will be used))<br />
                           .See DTGSYL for more details.b) If the i<br />
    &#8211; th and (i + 1) &#8211; th eigenvalues are complex conjugate pair,<br />
    Suppose U and V are orthogonal transformations such that<br />
    U **T *(A, B) *V = (S, T) = (S11 *)(T11 *)2(0 S22),<br />
                  (0 T22)n &#8211; 2 2 n &#8211; 2 2 n &#8211; 2 and (S11, T11) corresponds to the complex conjugate eigenvalue<br />
    pair(w, conjg(w))<br />
        .There exist unitary matrices U1 and V1 such<br />
    that<br />
    U1 **T *S11 *V1 = (s11 s12) and U1 **T *T11 *V1 = (t11 t12)(0 s22)(0 t22)<br />
        where the generalized eigenvalues w = s11 /<br />
    t11 and<br />
    conjg(w) = s22 / t22.Then the reciprocal condition number DIF(i) is bounded by<br />
         min( d1, max( 1, |real(s11)/real(s22)| )*d2 )<br />
     where, d1 = Difl((s11, t11), (s22, t22)) = sigma-min(Z1), where<br />
     Z1 is the complex 2-by-2 matrix<br />
              Z1 =  [ s11  -s22 ]<br />
                    [ t11  -t22 ],<br />
     This is done by computing (using real arithmetic) the<br />
     roots of the characteristical polynomial det(Z1**T * Z1 &#8211; lambda I),<br />
     where Z1**T denotes the transpose of Z1 and det(X) denotes<br />
     the determinant of X.<br />
     and d2 is an upper bound on Difl((S11, T11), (S22, T22)), i.e. an<br />
     upper bound on sigma-min(Z2), where Z2 is (2n-2)-by-(2n-2)<br />
              Z2 = [ kron(S11**T, In-2)  -kron(I2, S22) ]<br />
                   [ kron(T11**T, In-2)  -kron(I2, T22) ]<br />
     Note that if the default method for computing DIF is wanted (see<br />
     DLATDF), then the parameter DIFDRI (see below) should be changed<br />
     from 3 to 4 (routine DLATDF(IJOB = 2 will be used)). See DTGSYL<br />
     for more details.<br />
  For each eigenvalue/vector specified by SELECT, DIF stores a<br />
  Frobenius norm-based estimate of Difl.<br />
  An approximate error bound for the i-th computed eigenvector VL(i) or<br />
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
      Estimation: Theory, Algorithms and Software,
      Report UMINF - 94.04, Department of Computing Science, Umea
      University, S-901 87 Umea, Sweden, 1994. Also as LAPACK Working
      Note 87. To appear in Numerical Algorithms, 1996.
  [3] B. Kagstrom and P. Poromaa, LAPACK-Style Algorithms and Software
      for Solving the Generalized Sylvester Equation and Estimating the
      Separation between Regular Matrix Pairs, Report UMINF - 93.23,
      Department of Computing Science, Umea University, S-901 87 Umea,
      Sweden, December 1993, Revised April 1994, Also as LAPACK Working
      Note 75.  To appear in ACM Trans. on Math. Software, Vol 22,
      No 1, 1996.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> Definition at line 380 of file dtgsna.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
