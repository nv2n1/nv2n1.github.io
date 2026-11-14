---
title: "slags2-f(3)"
name: "slags2-f"
section: "3"
letter: "s"
url: "/docs/linux/man/3-slags2-f/"
description: "slags2.f –"
---

<p>slags2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>slags2</code> (UPPER, A1, A2, A3, B1, B2, B3, CSU, SNU, CSV, SNV, CSQ, SNQ)<br />
 <i></i><code>SLAGS2</code> computes 2-by-2 orthogonal matrices U, V, and Q, and applies them to matrices A and B such that the rows of the transformed A and B are parallel.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine slags2 (logicalUPPER, realA1, realA2, realA3, realB1, realB2, realB3, realCSU, realSNU, realCSV, realSNV, realCSQ, realSNQ)</h3>
<p><code>SLAGS2</code> computes 2-by-2 orthogonal matrices U, V, and Q, and applies them to matrices A and B such that the rows of the transformed A and B are parallel. </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> SLAGS2 computes 2-by-2 orthogonal matrices U, V and Q, such
 that if ( UPPER ) then
 U**T *A*Q = U**T *( A1 A2 )*Q = ( x 0 )
 ( 0 A3 ) ( x x )
 and
 V**T*B*Q = V**T *( B1 B2 )*Q = ( x 0 )
 ( 0 B3 ) ( x x )
 or if ( .NOT.UPPER ) then
 U**T *A*Q = U**T *( A1 0 )*Q = ( x x )
 ( A2 A3 ) ( 0 x )
 and
 V**T*B*Q = V**T*( B1 0 )*Q = ( x x )
 ( B2 B3 ) ( 0 x )
 The rows of the transformed A and B are parallel, where
 U = ( CSU SNU ), V = ( CSV SNV ), Q = ( CSQ SNQ )
 ( -SNU CSU ) ( -SNV CSV ) ( -SNQ CSQ )
 Z**T denotes the transpose of Z.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPPER</i> </p>
<pre> UPPER is LOGICAL
 = .TRUE.: the input matrices A and B are upper triangular.
 = .FALSE.: the input matrices A and B are lower triangular.</pre>
<p><i>A1</i> </p>
<pre> A1 is REAL</pre>
<p><i>A2</i> </p>
<pre> A2 is REAL</pre>
<p><i>A3</i> </p>
<pre> A3 is REAL
 On entry, A1, A2 and A3 are elements of the input 2-by-2
 upper (lower) triangular matrix A.</pre>
<p><i>B1</i> </p>
<pre> B1 is REAL</pre>
<p><i>B2</i> </p>
<pre> B2 is REAL</pre>
<p><i>B3</i> </p>
<pre> B3 is REAL
 On entry, B1, B2 and B3 are elements of the input 2-by-2
 upper (lower) triangular matrix B.</pre>
<p><i>CSU</i> </p>
<pre> CSU is REAL</pre>
<p><i>SNU</i> </p>
<pre> SNU is REAL
 The desired orthogonal matrix U.</pre>
<p><i>CSV</i> </p>
<pre> CSV is REAL</pre>
<p><i>SNV</i> </p>
<pre> SNV is REAL
 The desired orthogonal matrix V.</pre>
<p><i>CSQ</i> </p>
<pre> CSQ is REAL</pre>
<p><i>SNQ</i> </p>
<pre> SNQ is REAL
 The desired orthogonal matrix Q.</pre>
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
<p> Definition at line 152 of file slags2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
