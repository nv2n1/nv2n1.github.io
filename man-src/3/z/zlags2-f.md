---
title: "zlags2-f(3)"
name: "zlags2-f"
section: "3"
letter: "z"
url: "/docs/linux/man/3-zlags2-f/"
description: "zlags2.f –"
---

<p>zlags2.f &#8211;</p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>zlags2</code> (UPPER, A1, A2, A3, B1, B2, B3, CSU, SNU, CSV, SNV, CSQ, SNQ)<br />
 <i></i><code>ZLAGS2</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine zlags2 (logicalUPPER, double precisionA1, complex*16A2, double precisionA3, double precisionB1, complex*16B2, double precisionB3, double precisionCSU, complex*16SNU, double precisionCSV, complex*16SNV, double precisionCSQ, complex*16SNQ)</h3>
<p><code>ZLAGS2</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dd>
<pre> ZLAGS2 computes 2-by-2 unitary matrices U, V and Q, such
 that if ( UPPER ) then
 U**H *A*Q = U**H *( A1 A2 )*Q = ( x 0 )
 ( 0 A3 ) ( x x )
 and
 V**H*B*Q = V**H *( B1 B2 )*Q = ( x 0 )
 ( 0 B3 ) ( x x )
 or if ( .NOT.UPPER ) then
 U**H *A*Q = U**H *( A1 0 )*Q = ( x x )
 ( A2 A3 ) ( 0 x )
 and
 V**H *B*Q = V**H *( B1 0 )*Q = ( x x )
 ( B2 B3 ) ( 0 x )
 where
 U = ( CSU SNU ), V = ( CSV SNV ),
 ( -SNU**H CSU ) ( -SNV**H CSV )
 Q = ( CSQ SNQ )
 ( -SNQ**H CSQ )
 The rows of the transformed A and B are parallel. Moreover, if the
 input 2-by-2 matrix A is not zero, then the transformed (1,1) entry
 of A is not zero. If the input matrices A and B are both not zero,
 then the transformed (2,2) element of B is not zero, except when the
 first rows of input A and B are parallel and the second rows are
 zero.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dd><i>UPPER</i> </p>
<pre> UPPER is LOGICAL
 = .TRUE.: the input matrices A and B are upper triangular.
 = .FALSE.: the input matrices A and B are lower triangular.</pre>
<p><i>A1</i> </p>
<pre> A1 is DOUBLE PRECISION</pre>
<p><i>A2</i> </p>
<pre> A2 is COMPLEX*16</pre>
<p><i>A3</i> </p>
<pre> A3 is DOUBLE PRECISION
 On entry, A1, A2 and A3 are elements of the input 2-by-2
 upper (lower) triangular matrix A.</pre>
<p><i>B1</i> </p>
<pre> B1 is DOUBLE PRECISION</pre>
<p><i>B2</i> </p>
<pre> B2 is COMPLEX*16</pre>
<p><i>B3</i> </p>
<pre> B3 is DOUBLE PRECISION
 On entry, B1, B2 and B3 are elements of the input 2-by-2
 upper (lower) triangular matrix B.</pre>
<p><i>CSU</i> </p>
<pre> CSU is DOUBLE PRECISION</pre>
<p><i>SNU</i> </p>
<pre> SNU is COMPLEX*16
 The desired unitary matrix U.</pre>
<p><i>CSV</i> </p>
<pre> CSV is DOUBLE PRECISION</pre>
<p><i>SNV</i> </p>
<pre> SNV is COMPLEX*16
 The desired unitary matrix V.</pre>
<p><i>CSQ</i> </p>
<pre> CSQ is DOUBLE PRECISION</pre>
<p><i>SNQ</i> </p>
<pre> SNQ is COMPLEX*16
 The desired unitary matrix Q.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl>
<dd>November 2011</dl>
<p> Definition at line 158 of file zlags2.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
