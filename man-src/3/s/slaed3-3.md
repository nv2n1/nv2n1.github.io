---
title: "slaed3-3(3)"
name: "slaed3-3"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaed3-3/"
description: "slaed3.f –"
---

<p>slaed3.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slaed3</code> (K, N, N1, D, Q, LDQ, RHO, DLAMDA, Q2, INDX, CTOT, W, S, INFO)<br />
 <i></i><code>SLAED3</code> used by sstedc. Finds the roots of the secular equation and updates the eigenvectors. Used when the original matrix is tridiagonal.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaed3 (integerK, integerN, integerN1, real, dimension( * )D, real, dimension( ldq, * )Q, integerLDQ, realRHO, real, dimension( * )DLAMDA, real, dimension( * )Q2, integer, dimension( * )INDX, integer, dimension( * )CTOT, real, dimension( * )W, real, dimension( * )S, integerINFO)</h3>
<p><code>SLAED3</code> used by sstedc. Finds the roots of the secular equation and updates the eigenvectors. Used when the original matrix is tridiagonal. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAED3 finds the roots of the secular equation, as defined by the
 values in D, W, and RHO, between 1 and K. It makes the
 appropriate calls to SLAED4 and then updates the eigenvectors by
 multiplying the matrix of eigenvectors of the pair of eigensystems
 being combined by the matrix of eigenvectors of the K-by-K system
 which is solved here.
 This code makes very mild assumptions about floating point
 arithmetic. It will work on machines with a guard digit in
 add/subtract, or on those binary machines without guard digits
 which subtract like the Cray X-MP, Cray Y-MP, Cray C-90, or Cray-2.
 It could conceivably fail on hexadecimal or decimal machines
 without guard digits, but we know of none.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>K</i> </p>
<pre> K is INTEGER
 The number of terms in the rational function to be solved by
 SLAED4. K &gt;= 0.</pre>
<p><i>N</i> </p>
<pre> N is INTEGER
 The number of rows and columns in the Q matrix.
 N &gt;= K (deflation may result in N&gt;K).</pre>
<p><i>N1</i> </p>
<pre> N1 is INTEGER
 The location of the last eigenvalue in the leading submatrix.
 min(1,N) &lt;= N1 &lt;= N/2.</pre>
<p><i>D</i> </p>
<pre> D is REAL array, dimension (N)
 D(I) contains the updated eigenvalues for
 1 &lt;= I &lt;= K.</pre>
<p><i>Q</i> </p>
<pre> Q is REAL array, dimension (LDQ,N)
 Initially the first K columns are used as workspace.
 On output the columns 1 to K contain
 the updated eigenvectors.</pre>
<p><i>LDQ</i> </p>
<pre> LDQ is INTEGER
 The leading dimension of the array Q. LDQ &gt;= max(1,N).</pre>
<p><i>RHO</i> </p>
<pre> RHO is REAL
 The value of the parameter in the rank one update equation.
 RHO &gt;= 0 required.</pre>
<p><i>DLAMDA</i> </p>
<pre> DLAMDA is REAL array, dimension (K)
 The first K elements of this array contain the old roots
 of the deflated updating problem. These are the poles
 of the secular equation. May be changed on output by
 having lowest order bit set to zero on Cray X-MP, Cray Y-MP,
 Cray-2, or Cray C-90, as described above.</pre>
<p><i>Q2</i> </p>
<pre> Q2 is REAL array, dimension (LDQ2, N)
 The first K columns of this matrix contain the non-deflated
 eigenvectors for the split problem.</pre>
<p><i>INDX</i> </p>
<pre> INDX is INTEGER array, dimension (N)
 The permutation used to arrange the columns of the deflated
 Q matrix into three groups (see SLAED2).
 The rows of the eigenvectors found by SLAED4 must be likewise
 permuted before the matrix multiply can take place.</pre>
<p><i>CTOT</i> </p>
<pre> CTOT is INTEGER array, dimension (4)
 A count of the total number of the various types of columns
 in Q, as described in INDX. The fourth column type is any
 column which has been deflated.</pre>
<p><i>W</i> </p>
<pre> W is REAL array, dimension (K)
 The first K elements of this array contain the components
 of the deflation-adjusted updating vector. Destroyed on
 output.</pre>
<p><i>S</i> </p>
<pre> S is REAL array, dimension (N1 + 1)*K
 Will contain the eigenvectors of the repaired matrix which
 will be multiplied by the previously accumulated eigenvectors
 to update the system.</pre>
<p><i>INFO</i> </p>
<pre> INFO is INTEGER
 = 0: successful exit.
 &lt; 0: if INFO = -i, the i-th argument had an illegal value.
 &gt; 0: if INFO = 1, an eigenvalue did not converge</pre>
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
<dd>Jeff Rutter, Computer Science Division, University of California at Berkeley, USA </p>
<p>&nbsp;<wbr>Modified by Francoise Tisseur, University of Tennessee&nbsp;<wbr></dl>
<p> Definition at line 185 of file slaed3.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
