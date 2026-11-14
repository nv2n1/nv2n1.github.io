---
title: "chla_transtype-f(3)"
name: "chla_transtype-f"
section: "3"
letter: "c"
url: "/docs/linux/man/3-chla_transtype-f/"
description: "chla_transtype.f –"
---

<p>chla_transtype.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>CHARACTER *1 function <code>chla_transtype</code> (TRANS)<br />
 <i></i><code>CHLA_TRANSTYPE</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>CHARACTER*1 function chla_transtype (integerTRANS)</h3>
<p><code>CHLA_TRANSTYPE</code> </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> This subroutine translates from a BLAST-specified integer constant to
 the character string specifying a transposition operation.
 CHLA_TRANSTYPE returns an CHARACTER*1. If CHLA_TRANSTYPE is 'X',
 then input is not an integer indicating a transposition operator.
 Otherwise CHLA_TRANSTYPE returns the constant value corresponding to
 TRANS.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>November 2011</dl>
<p> Definition at line 59 of file chla_transtype.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
