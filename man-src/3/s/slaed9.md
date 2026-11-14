---
title: "slaed9(3)"
name: "slaed9"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slaed9/"
description: "slaed9.f –"
---

<h2 class="name">NAME</h2>
<p> slaed9.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>slaed9</code> (K, KSTART, KSTOP, N, D, Q, LDQ, RHO, DLAMDA, W, S, LDS, INFO)<br />
 <i></i><code>SLAED9</code> used by sstedc. Finds the roots of the secular equation and updates the eigenvectors. Used when the original matrix is dense.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slaed9 (integerK, integerKSTART, integerKSTOP, integerN, real, dimension( * )D, real, dimension( ldq, * )Q, integerLDQ, realRHO, real, dimension( * )DLAMDA, real, dimension( * )W, real, dimension( lds, * )S, integerLDS, integerINFO)</h3>
<p> <code>SLAED9</code> used by sstedc. Finds the roots of the secular equation and updates the eigenvectors. Used when the original matrix is dense. </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 SLAED9 finds the roots of the secular equation, as defined by the
 values in D, Z, and RHO, between KSTART and KSTOP.  It makes the
 appropriate calls to SLAED4 and then stores the new matrix of
 eigenvectors for use in calculating the next level of Z vectors.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>K</i> </p>
<pre>
          K is INTEGER
          The number of terms in the rational function to be solved by
          SLAED4.  K &gt;= 0.
</pre>
<p> <i>KSTART</i> </p>
<pre>
          KSTART is INTEGER
</pre>
<p> <i>KSTOP</i> </p>
<pre><code>
KSTOP is INTEGER
    The updated eigenvalues
    Lambda(I),
    KSTART &lt;= I &lt;= KSTOP
                   are to be computed.1 &lt;= KSTART
        &lt;= KSTOP &lt;= K.
</code></pre>
<p> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of rows and columns in the Q matrix.
          N &gt;= K (delation may result in N &gt; K).
</pre>
<p> <i>D</i> </p>
<pre>
          D is REAL array, dimension (N)
          D(I) contains the updated eigenvalues
          for KSTART &lt;= I &lt;= KSTOP.
</pre>
<p> <i>Q</i> </p>
<pre>
          Q is REAL array, dimension (LDQ,N)
</pre>
<p> <i>LDQ</i> </p>
<pre>
          LDQ is INTEGER
          The leading dimension of the array Q.  LDQ &gt;= max( 1, N ).
</pre>
<p> <i>RHO</i> </p>
<pre>
          RHO is REAL
          The value of the parameter in the rank one update equation.
          RHO &gt;= 0 required.
</pre>
<p> <i>DLAMDA</i> </p>
<pre>
          DLAMDA is REAL array, dimension (K)
          The first K elements of this array contain the old roots
          of the deflated updating problem.  These are the poles
          of the secular equation.
</pre>
<p> <i>W</i> </p>
<pre>
          W is REAL array, dimension (K)
          The first K elements of this array contain the components
          of the deflation-adjusted updating vector.
</pre>
<p> <i>S</i> </p>
<pre>
          S is REAL array, dimension (LDS, K)
          Will contain the eigenvectors of the repaired matrix which
          will be stored for subsequent Z vector calculation and
          multiplied by the previously accumulated eigenvectors
          to update the system.
</pre>
<p> <i>LDS</i> </p>
<pre>
          LDS is INTEGER
          The leading dimension of S.  LDS &gt;= max( 1, K ).
</pre>
<p> <i>INFO</i> </p>
<pre>
          INFO is INTEGER
          = 0:  successful exit.
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
          &gt; 0:  if INFO = 1, an eigenvalue did not converge
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
<p> <code>Contributors: </code></p>
<dl>
<dt>
<dd> Jeff Rutter, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 156 of file slaed9.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
