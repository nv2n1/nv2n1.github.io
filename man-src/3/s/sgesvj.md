---
title: "sgesvj(3)"
name: "sgesvj"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgesvj/"
description: "sgesvj.f –"
---

<h2 class="name">NAME</h2>
<p> sgesvj.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>sgesvj</code> (JOBA, JOBU, JOBV, M, N, A, LDA, SVA, MV, V, LDV, WORK, LWORK, INFO)<br />
 <i></i><code>SGESVJ</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine sgesvj (character*1JOBA, character*1JOBU, character*1JOBV, integerM, integerN, real, dimension( lda, * )A, integerLDA, real, dimension( n )SVA, integerMV, real, dimension( ldv, * )V, integerLDV, real, dimension( lwork )WORK, integerLWORK, integerINFO)</h3>
<p> <code>SGESVJ</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre><code>
SGESVJ computes the singular value decomposition(SVD)
of a real
        M -
    by - N matrix A,
    where M &gt;= N.The SVD of A is written as
                   [++][xx][x0][xx] A = U * SIGMA * V ^ t,
                                    [++] = [xx] *[ox] *[xx]
                                               [++][xx] where SIGMA is an N -
                                           by - N diagonal matrix,
                                    U is an M - by - N orthonormal matrix, and V is an N - by - N orthogonal matrix.The diagonal elements of SIGMA are the singular values of A.The columns of U and V are the left and the right singular vectors of A, respectively.
</code></pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>JOBA</i> </p>
<pre>
          JOBA is CHARACTER* 1
          Specifies the structure of A.
          = 'L': The input matrix A is lower triangular;
          = 'U': The input matrix A is upper triangular;
          = 'G': The input matrix A is general M-by-N matrix, M &gt;= N.
</pre>
<p> <i>JOBU</i> </p>
<pre>
          JOBU is CHARACTER*1
          Specifies whether to compute the left singular vectors
          (columns of U):
          = 'U': The left singular vectors corresponding to the nonzero
                 singular values are computed and returned in the leading
                 columns of A. See more details in the description of A.
                 The default numerical orthogonality threshold is set to
                 approximately TOL=CTOL*EPS, CTOL=SQRT(M), EPS=SLAMCH('E').
          = 'C': Analogous to JOBU='U', except that user can control the
                 level of numerical orthogonality of the computed left
                 singular vectors. TOL can be set to TOL = CTOL*EPS, where
                 CTOL is given on input in the array WORK.
                 No CTOL smaller than ONE is allowed. CTOL greater
                 than 1 / EPS is meaningless. The option 'C'
                 can be used if M*EPS is satisfactory orthogonality
                 of the computed left singular vectors, so CTOL=M could
                 save few sweeps of Jacobi rotations.
                 See the descriptions of A and WORK(1).
          = 'N': The matrix U is not computed. However, see the
                 description of A.
</pre>
<p> <i>JOBV</i> </p>
<pre>
          JOBV is CHARACTER*1
          Specifies whether to compute the right singular vectors, that
          is, the matrix V:
          = 'V' : the matrix V is computed and returned in the array V
          = 'A' : the Jacobi rotations are applied to the MV-by-N
                  array V. In other words, the right singular vector
                  matrix V is not computed explicitly; instead it is
                  applied to an MV-by-N matrix initially stored in the
                  first MV rows of V.
          = 'N' : the matrix V is not computed and the array V is not
                  referenced
</pre>
<p> <i>M</i> </p>
<pre>
          M is INTEGER
          The number of rows of the input matrix A. 1/SLAMCH('E') &gt; M &gt;= 0.
</pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of columns of the input matrix A.
          M &gt;= N &gt;= 0.
</pre>
<p> <i>A</i> </p>
<p>A is REAL array, dimension(LDA, N) On entry, the M &#8211; by &#8211; N matrix A.On exit,<br />
    If JOBU.EQ.&#8217;U&#8217;.OR.JOBU.EQ.&#8217;C&#8217; : If INFO.EQ.0 : RANKA orthonormal columns of U are returned in the<br />
                                                   leading RANKA columns of the array A.Here RANKA<br />
            &lt;= N<br />
               is the number of computed singular values of A that are<br />
               above the underflow threshold SLAMCH(&#8216;S&#8217;)<br />
                   .The singular<br />
               vectors corresponding to underflowed<br />
        or zero singular<br />
           values are not computed.The value of RANKA is returned<br />
           in the array WORK as RANKA = NINT(WORK(2)).Also see the<br />
                                        descriptions of SVA and WORK.The computed columns of U<br />
                                        are mutually numerically orthogonal up to approximately<br />
                                        TOL = SQRT(M) * EPS(default);<br />
or TOL = CTOL * EPS(JOBU.EQ.&#8217;C&#8217;),<br />
   see the description of JOBU.If INFO.GT.0,<br />
   the procedure SGESVJ did not converge in the given number<br />
       of<br />
       iterations(sweeps)<br />
           .In that case,<br />
   the computed<br />
       columns of U may not be orthogonal up to TOL.The output<br />
       U(stored in A),<br />
   SIGMA(given by the computed singular<br />
             values in SVA(1<br />
                           : N)) and<br />
           V is still a decomposition of the<br />
           input matrix A in the sense that the residual<br />
       || A &#8211; SCALE *U *SIGMA *V ^ T || _2 / || A || _2 is small.If JOBU.EQ.&#8217;N&#8217; : If INFO.EQ.0 : Note that the left singular vectors are &#8216;for free&#8217; in the one &#8211; sided Jacobi SVD algorithm.However,<br />
   if only the<br />
    singular values are needed,<br />
   the level of numerical<br />
       orthogonality of U is not an issue<br />
       and iterations are<br />
               stopped when the columns of the iterated matrix are<br />
               numerically orthogonal up to approximately M<br />
               * EPS.Thus,<br />
   on exit, A contains the columns of U scaled with the corresponding singular values.If INFO.GT.0 : the procedure SGESVJ did not converge in the given number of iterations(sweeps).</p>
<p> <i>LDA</i> </p>
<pre>
          LDA is INTEGER
          The leading dimension of the array A.  LDA &gt;= max(1,M).
</pre>
<p> <i>SVA</i> </p>
<pre>
          SVA is REAL array, dimension (N)
          On exit,
          If INFO .EQ. 0 :
          depending on the value SCALE = WORK(1), we have:
                 If SCALE .EQ. ONE:
                 SVA(1:N) contains the computed singular values of A.
                 During the computation SVA contains the Euclidean column
                 norms of the iterated matrices in the array A.
                 If SCALE .NE. ONE:
                 The singular values of A are SCALE*SVA(1:N), and this
                 factored representation is due to the fact that some of the
                 singular values of A might underflow or overflow.
          If INFO .GT. 0 :
          the procedure SGESVJ did not converge in the given number of
          iterations (sweeps) and SCALE*SVA(1:N) may not be accurate.
</pre>
<p> <i>MV</i> </p>
<pre>
          MV is INTEGER
          If JOBV .EQ. 'A', then the product of Jacobi rotations in SGESVJ
          is applied to the first MV rows of V. See the description of JOBV.
</pre>
<p> <i>V</i> </p>
<pre>
          V is REAL array, dimension (LDV,N)
          If JOBV = 'V', then V contains on exit the N-by-N matrix of
                         the right singular vectors;
          If JOBV = 'A', then V contains the product of the computed right
                         singular vector matrix and the initial matrix in
                         the array V.
          If JOBV = 'N', then V is not referenced.
</pre>
<p> <i>LDV</i> </p>
<pre>
          LDV is INTEGER
          The leading dimension of the array V, LDV .GE. 1.
          If JOBV .EQ. 'V', then LDV .GE. max(1,N).
          If JOBV .EQ. 'A', then LDV .GE. max(1,MV) .
</pre>
<p> <i>WORK</i> </p>
<pre><code>
          WORK is REAL array, dimension max(4,M+N).
          On entry,
          If JOBU .EQ. 'C' :
          WORK(1) = CTOL, where CTOL defines the threshold for convergence.
                    The process stops if all columns of A are mutually
                    orthogonal up to CTOL*EPS, EPS=SLAMCH('E').
                    It is required that CTOL &gt;= ONE, i.e. it is not
                    allowed to force the routine to obtain orthogonality
                    below EPSILON.
          On exit,
          WORK(1) = SCALE is the scaling factor such that SCALE*SVA(1:N)
                    are the computed singular vcalues of A.
                    (See description of SVA().)
          WORK(2) = NINT(WORK(2)) is the number of the computed nonzero
                    singular values.
          WORK(3) = NINT(WORK(3)) is the number of the computed singular
                    values that are larger than the underflow threshold.
          WORK(4) = NINT(WORK(4)) is the number of sweeps of Jacobi
                    rotations needed for numerical convergence.
          WORK(5) = max_{i.NE.j} |COS(A(:,i),A(:,j))| in the last sweep.
                    This is useful information in cases when SGESVJ did
                    not converge, as it can be used to estimate whether
                    the output is stil useful and for post festum analysis.
          WORK(6) = the largest absolute value over all sines of the
                    Jacobi rotation angles in the last sweep. It can be
                    useful for a post festum analysis.
</code></pre>
<p> <i>LWORK</i> </p>
<pre>
          LWORK is INTEGER
         length of WORK, WORK &gt;= MAX(6,M+N)
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0 : successful exit.
          &lt; 0 : if INFO = -i, then the i-th argument had an illegal value
          &gt; 0 : SGESVJ did not converge in the maximal allowed number (30)
                of sweeps. The output may still be useful. See the
                description of WORK.
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
<dd> September 2012</dl>
<p> <code>Further Details: </code></p>
<dl>
<dt>
<dd> The orthogonal N-by-N matrix V is obtained as a product of Jacobi plane rotations. The rotations are implemented as fast scaled rotations of Anda and Park [1]. In the case of underflow of the Jacobi angle, a modified Jacobi transformation of Drmac [4] is used. Pivot strategy uses column interchanges of de Rijk [2]. The relative accuracy of the computed singular values and the accuracy of the computed singular vectors (in angle metric) is as guaranteed by the theory of Demmel and Veselic [3]. The condition number that determines the accuracy in the full rank case is essentially min_{D=diag} kappa(A*D), where kappa(.) is the spectral condition number. The best performance of this Jacobi SVD procedure is achieved if used in an accelerated version of Drmac and Veselic [5,6], and it is the kernel routine in the SIGMA library [7]. Some tunning parameters (marked with [TP]) are available for the implementer. </p>
<p>&nbsp;<wbr>The computational range for the nonzero singular values is the machine number interval&nbsp;<wbr>(&nbsp;<wbr>UNDERFLOW , OVERFLOW&nbsp;<wbr>). In extreme cases, even denormalized singular values can be computed with the corresponding gradual loss of accurate digits.</dl>
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Zlatko Drmac (Zagreb, Croatia) and Kresimir Veselic (Hagen, Germany)</dl>
<p> <code>References: </code></p>
<dl>
<dt>
<dd> [1] A. A. Anda and H. Park: Fast plane rotations with dynamic scaling. </p>
<p>&nbsp;<wbr>SIAM J. matrix Anal. Appl., Vol. 15&nbsp;<wbr>(1994), pp. 162-174.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[2]&nbsp;<wbr>P. P. M. De Rijk: A one-sided Jacobi algorithm for computing the singular value decomposition on a vector computer.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>SIAM J. Sci. Stat. Comp., Vol. 10&nbsp;<wbr>(1998), pp. 359-371.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[3]&nbsp;<wbr>J. Demmel and K. Veselic: Jacobi method is more accurate than QR.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[4]&nbsp;<wbr>Z. Drmac: Implementation of Jacobi rotations for accurate singular value computation in floating point arithmetic.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>SIAM J. Sci. Comp., Vol. 18&nbsp;<wbr>(1997), pp. 1200-1222.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[5]&nbsp;<wbr>Z. Drmac and K. Veselic: New fast and accurate Jacobi SVD algorithm I.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>SIAM J. Matrix Anal. Appl. Vol. 35, No. 2&nbsp;<wbr>(2008), pp. 1322-1342.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>LAPACK Working note 169.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[6]&nbsp;<wbr>Z. Drmac and K. Veselic: New fast and accurate Jacobi SVD algorithm II.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>SIAM J. Matrix Anal. Appl. Vol. 35, No. 2&nbsp;<wbr>(2008), pp. 1343-1362.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>LAPACK Working note 170.&nbsp;<wbr> </p>
<p>&nbsp;<wbr>[7]&nbsp;<wbr>Z. Drmac: SIGMA &#8211; mathematical software library for accurate SVD, PSV, QSVD,&nbsp;<wbr>(H,K)-SVD computations. </p>
<p>&nbsp;<wbr>Department of Mathematics, University of Zagreb, 2008.</dl>
<p> <code>Bugs, Examples and Comments: </code></p>
<dl>
<dt>
<dd> Please report all bugs and send interesting test examples and comments to drmac [at] math.hr. Thank you.</dl>
<p> Definition at line 321 of file sgesvj.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
