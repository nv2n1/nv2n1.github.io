---
title: "sc_redundantcartesianiter(3)"
name: "sc_redundantcartesianiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_redundantcartesianiter/"
description: "sc::RedundantCartesianIter –"
---

<p>sc::RedundantCartesianIter &#8211; </p>
<p> <code>RedundantCartesianIter</code> objects loop through all possible combinations of a given number of axes.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;cartiter.h&gt;</code></pre>
<p> Inherited by <code>sc::RedundantCartesianIterCCA</code>, <code>sc::RedundantCartesianIterCints</code>, and <code>sc::RedundantCartesianIterV3</code>.</p>
<h3>Public Member Functions</h3>
<p><code>RedundantCartesianIter</code> (int l)<br />
 <i>Create a object for the given angular momentum. </i><br />
 virtual int <code>bfn</code> ()=0<br />
 <i>Return the current Cartesian basis function number. </i><br />
 void <code>start</code> ()<br />
 <i>Initialize the iterator. </i><br />
 void <code>next</code> ()<br />
 <i>Move to the next combination of axes. </i><br />
 <code>operator int</code> ()<br />
 <i>Returns nonzero if the iterator currently hold valid data. </i><br />
 int <code>a</code> ()<br />
 <i>The current exponent of x. </i><br />
 int <code>b</code> ()<br />
 <i>The current exponent of y. </i><br />
 int <code>c</code> ()<br />
 <i>The current exponent of z. </i><br />
 int <code>l</code> ()<br />
 <i>The angular momentum. </i><br />
 int <code>l</code> (int i)<br />
 <i>Returns </i><code>a()</code> if i==0, <code>b()</code> if i==1, and <code>c()</code> if i==2.<br />
 int <code>axis</code> (int i)<br />
 <i>Return the i&#8217;th axis. </i></p>
<h2>Detailed Description</h2>
<p><code>RedundantCartesianIter</code> objects loop through all possible combinations of a given number of axes. </p>
<p> This is used to compute the transformation matrices that maps a set of Cartesian functions to another set of Cartesian functions in a rotated coordinate system.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
