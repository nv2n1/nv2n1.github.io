---
title: "sgebak(3)"
name: "sgebak"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sgebak/"
---

<h2 class="name">NAME</h2>
 

 sgebak.f - 

<h2>SYNOPSIS</h2>

 
 

<h3>Functions/Subroutines</h3>

 

 
 subroutine <b>sgebak</b> (JOB, SIDE, N, ILO, IHI, SCALE, M, V, LDV, INFO) 
 <i></i><b>SGEBAK</b>

<h2>Function/Subroutine Documentation</h2>

 

<h3>subroutine sgebak (characterJOB, characterSIDE, integerN, integerILO, integerIHI, real, dimension( * )SCALE, integerM, real, dimension( ldv, * )V, integerLDV, integerINFO)</h3>

 

 

 <b>SGEBAK</b> 

 <b>Purpose: </b>
<dl>
<dt>
<dd> 

 

 <pre>
 SGEBAK forms the right or left eigenvectors of a real general matrix
 by backward transformation on the computed eigenvectors of the
 balanced matrix output by SGEBAL.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Parameters:</b>
<dl>
<dt>
<dd> <i>JOB</i> 

 <pre><code>
JOB is CHARACTER * 1 Specifies the type of backward transformation required : = 'N', do nothing, return immediately;
          = 'P', do backward transformation for permutation only;
          = 'S', do backward transformation for scaling only;
          = 'B', do backward transformations for both permutation and
                 scaling.
          JOB must be the same as the argument JOB supplied to SGEBAL.
</code></pre> 

 
 <i>SIDE</i> 

 <pre>
          SIDE is CHARACTER*1
          = 'R':  V contains right eigenvectors;
          = 'L':  V contains left eigenvectors.
</pre> 

 
 <i>N</i> 

 <pre>
          N is INTEGER
          The number of rows of the matrix V.  N &gt;= 0.
</pre> 

 
 <i>ILO</i> 

 <pre>
          ILO is INTEGER
</pre> 

 
 <i>IHI</i> 

 <pre><code>
IHI is INTEGER
        The integers ILO and IHI determined by SGEBAL.1 &lt;= ILO &lt;= IHI &lt;= N,
    if N &gt; 0;
ILO = 1 and IHI = 0, if N = 0.
</code></pre> 

 
 <i>SCALE</i> 

 <pre>
          SCALE is REAL array, dimension (N)
          Details of the permutation and scaling factors, as returned
          by SGEBAL.
</pre> 

 
 <i>M</i> 

 <pre>
          M is INTEGER
          The number of columns of the matrix V.  M &gt;= 0.
</pre> 

 
 <i>V</i> 

 <pre>
          V is REAL array, dimension (LDV,M)
          On entry, the matrix of right or left eigenvectors to be
          transformed, as returned by SHSEIN or STREVC.
          On exit, V is overwritten by the transformed eigenvectors.
</pre> 

 
 <i>LDV</i> 

 <pre>
          LDV is INTEGER
          The leading dimension of the array V. LDV &gt;= max(1,N).
</pre> 

 
 <i>INFO</i> 

 <pre>
          INFO is INTEGER
          = 0:  successful exit
          &lt; 0:  if INFO = -i, the i-th argument had an illegal value.
</pre> 

 
&nbsp;<wbr></dl>
 

 <b>Author:</b>
<dl>
<dt>
<dd> Univ. of Tennessee 

 Univ. of California Berkeley 

 Univ. of Colorado Denver 

 NAG Ltd.</dl>
 

 <b>Date:</b>
<dl>
<dt>
<dd> November 2011</dl>
 

 

 

 Definition at line 130 of file sgebak.f.

<h2>Author</h2>

 

 Generated automatically by Doxygen for LAPACK from the source code. 

<h2>Index</h2>


