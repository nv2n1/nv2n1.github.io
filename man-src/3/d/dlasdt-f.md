---
title: "dlasdt-f(3)"
name: "dlasdt-f"
section: "3"
letter: "d"
url: "/docs/linux/man/3-dlasdt-f/"
description: "dlasdt.f –"
---

<p>dlasdt.f &#8211; </p>
<h2>Synopsis</h2>
<h3>Functions/Subroutines</h3>
<p>subroutine <code>dlasdt</code> (N, LVL, ND, INODE, NDIML, NDIMR, MSUB)<br />
 <i></i><code>DLASDT</code> creates a tree of subproblems for bidiagonal divide and conquer. Used by sbdsdc.</p>
<h2>Function/Subroutine Documentation</h2>
<h3>subroutine dlasdt (integerN, integerLVL, integerND, integer, dimension( * )INODE, integer, dimension( * )NDIML, integer, dimension( * )NDIMR, integerMSUB)</h3>
<p><code>DLASDT</code> creates a tree of subproblems for bidiagonal divide and conquer. Used by sbdsdc. </p>
<p> <code>Purpose: </code></p>
<dl COMPACT>
<dd>
<pre> DLASDT creates a tree of subproblems for bidiagonal divide and
 conquer.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Parameters:</code></p>
<dl COMPACT>
<dd><i>N</i> </p>
<pre> N is INTEGER
 On entry, the number of diagonal elements of the
 bidiagonal matrix.</pre>
<p><i>LVL</i> </p>
<pre> LVL is INTEGER
 On exit, the number of levels on the computation tree.</pre>
<p><i>ND</i> </p>
<pre> ND is INTEGER
 On exit, the number of nodes on the tree.</pre>
<p><i>INODE</i> </p>
<pre> INODE is INTEGER array, dimension ( N )
 On exit, centers of subproblems.</pre>
<p><i>NDIML</i> </p>
<pre> NDIML is INTEGER array, dimension ( N )
 On exit, row dimensions of left children.</pre>
<p><i>NDIMR</i> </p>
<pre> NDIMR is INTEGER array, dimension ( N )
 On exit, row dimensions of right children.</pre>
<p><i>MSUB</i> </p>
<pre> MSUB is INTEGER
 On entry, the maximum row dimension each subproblem at the
 bottom of the tree can be of.</pre>
<p>&nbsp;<wbr></dl>
<p> <code>Author:</code></p>
<dl COMPACT>
<dd>Univ. of Tennessee </p>
<p> Univ. of California Berkeley </p>
<p> Univ. of Colorado Denver </p>
<p> NAG Ltd.</dl>
<p> <code>Date:</code></p>
<dl COMPACT>
<dd>September 2012</dl>
<p> <code>Contributors: </code></p>
<dl COMPACT>
<dd>Ming Gu and Huan Ren, Computer Science Division, University of California at Berkeley, USA</dl>
<p> Definition at line 106 of file dlasdt.f.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for LAPACK from the source code.</p>
