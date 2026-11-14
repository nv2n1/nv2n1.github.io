---
title: "clags2(3)"
name: "clags2"
section: "3"
letter: "c"
url: "/docs/linux/man/3-clags2/"
description: "clags2.f –"
---

<h2 class="name">NAME</h2>
<p> clags2.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> subroutine <code>clags2</code> (UPPER, A1, A2, A3, B1, B2, B3, CSU, SNU, CSV, SNV, CSQ, SNQ)<br />
 <i></i><code>CLAGS2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine clags2 (logicalUPPER, realA1, complexA2, realA3, realB1, complexB2, realB3, realCSU, complexSNU, realCSV, complexSNV, realCSQ, complexSNQ)</h3>
<p> <code>CLAGS2</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 CLAGS2 computes 2-by-2 unitary matrices U, V and Q, such
 that if ( UPPER ) then
           U**H *A*Q = U**H *( A1 A2 )*Q = ( x  0  )
                             ( 0  A3 )     ( x  x  )
 and
           V**H*B*Q = V**H *( B1 B2 )*Q = ( x  0  )
                            ( 0  B3 )     ( x  x  )
 or if ( .NOT.UPPER ) then
           U**H *A*Q = U**H *( A1 0  )*Q = ( x  x  )
                             ( A2 A3 )     ( 0  x  )
 and
           V**H *B*Q = V**H *( B1 0  )*Q = ( x  x  )
                             ( B2 B3 )     ( 0  x  )
 where
   U = (   CSU    SNU ), V = (  CSV    SNV ),
       ( -SNU**H  CSU )      ( -SNV**H CSV )
   Q = (   CSQ    SNQ )
       ( -SNQ**H  CSQ )
 The rows of the transformed A and B are parallel. Moreover, if the
 input 2-by-2 matrix A is not zero, then the transformed (1,1) entry
 of A is not zero. If the input matrices A and B are both not zero,
 then the transformed (2,2) element of B is not zero, except when the
 first rows of input A and B are parallel and the second rows are
 zero.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>UPPER</i> </p>
<pre>
          UPPER is LOGICAL
          = .TRUE.: the input matrices A and B are upper triangular.
          = .FALSE.: the input matrices A and B are lower triangular.
</pre>
<p> <i>A1</i> </p>
<pre>
          A1 is REAL
</pre>
<p> <i>A2</i> </p>
<pre>
          A2 is COMPLEX
</pre>
<p> <i>A3</i> </p>
<pre>
          A3 is REAL
          On entry, A1, A2 and A3 are elements of the input 2-by-2
          upper (lower) triangular matrix A.
</pre>
<p> <i>B1</i> </p>
<pre>
          B1 is REAL
</pre>
<p> <i>B2</i> </p>
<pre>
          B2 is COMPLEX
</pre>
<p> <i>B3</i> </p>
<pre>
          B3 is REAL
          On entry, B1, B2 and B3 are elements of the input 2-by-2
          upper (lower) triangular matrix B.
</pre>
<p> <i>CSU</i> </p>
<pre>
          CSU is REAL
</pre>
<p> <i>SNU</i> </p>
<pre>
          SNU is COMPLEX
          The desired unitary matrix U.
</pre>
<p> <i>CSV</i> </p>
<pre>
          CSV is REAL
</pre>
<p> <i>SNV</i> </p>
<pre>
          SNV is COMPLEX
          The desired unitary matrix V.
</pre>
<p> <i>CSQ</i> </p>
<pre>
          CSQ is REAL
</pre>
<p> <i>SNQ</i> </p>
<pre>
          SNQ is COMPLEX
          The desired unitary matrix Q.
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
<p> Definition at line 158 of file clags2.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
