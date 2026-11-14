---
title: "lsamen(3)"
name: "lsamen"
section: "3"
letter: "l"
url: "/docs/linux/man/3-lsamen/"
description: "lsamen.f –"
---

<h2 class="name">NAME</h2>
<p> lsamen.f &#8211; </p>
<h2>SYNOPSIS</h2>
<h3>Functions/Subroutines</h3>
<p> LOGICAL function <code>lsamen</code> (N, CA, CB)<br />
 <i></i><code>LSAMEN</code></p>
<h2>Function/Subroutine Documentation</h2>
<h3>LOGICAL function lsamen (integerN, character*( * )CA, character*( * )CB)</h3>
<p> <code>LSAMEN</code> </p>
<p> <code>Purpose: </code></p>
<dl>
<dt>
<dd>
<pre>
 LSAMEN  tests if the first N letters of CA are the same as the
 first N letters of CB, regardless of case.
 LSAMEN returns .TRUE. if CA and CB are equivalent except for case
 and .FALSE. otherwise.  LSAMEN also returns .FALSE. if LEN( CA )
 or LEN( CB ) is less than N.
</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl>
<dt>
<dd> <i>N</i> </p>
<pre>
          N is INTEGER
          The number of characters in CA and CB to be compared.
</pre>
<p> <i>CA</i> </p>
<pre>
          CA is CHARACTER*(*)
</pre>
<p> <i>CB</i> </p>
<pre>
          CB is CHARACTER*(*)
          CA and CB specify two character strings of length at least N.
          Only the first N characters of each string will be accessed.
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
<p> Definition at line 75 of file lsamen.f.</p>
<h2>Author</h2>
<p> Generated automatically by Doxygen for LAPACK from the source code. </p>
<h2>Index</h2>
