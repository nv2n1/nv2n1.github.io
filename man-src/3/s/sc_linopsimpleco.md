---
title: "sc_linopsimpleco(3)"
name: "sc_linopsimpleco"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_linopsimpleco/"
description: "sc::LinOPSimpleCo –"
---

<p>sc::LinOPSimpleCo &#8211; </p>
<p> The <code>LinOPSimpleCo</code> class describes an out-of-plane component of a linear bend internal coordinate of a molecule.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;simple.h&gt;</code></pre>
<p> Inherits <code>sc::SimpleCo</code>.</p>
<h3>Public Member Functions</h3>
<p><code>LinOPSimpleCo</code> (const <code>LinOPSimpleCo</code> &amp;) </p>
<p> <code>LinOPSimpleCo</code> (const char *refr, int, int, int, const <code>SCVector3</code> &amp;u)<br />
 <i>This constructor takes a string containing a label, and three integers a, b, and c which give the indices of the atoms involved in the linear angle abc. </i><br />
 <code>LinOPSimpleCo</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 const char * <code>ctype</code> () const<br />
 <i>Always returns the string &#8216;LINIP&#8217;. </i><br />
 double <code>radians</code> () const<br />
 <i>Returns the value of the angle abc in radians. </i><br />
 double <code>degrees</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i><br />
 double <code>preferred_value</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i></p>
<h2>Detailed Description</h2>
<p>The <code>LinOPSimpleCo</code> class describes an out-of-plane component of a linear bend internal coordinate of a molecule. </p>
<p> The input is described in the documentation of its parent class <code>SimpleCo</code>. A vector, $s the keyword u, that is not colinear with either $ &#8211; lly, <code>LinOPSimpleCo</code> is used with a corresponding <code>LinIPSimpleCo</code>, which is given exactly the same u. </p>
<p> Designating the three atoms as $a$, $b$, and $c$ and their cartesian positions as $$, $nd $lue of the coordinate, $ heta_o$, is given by </p>
<p> [ b} = ac{ &#8211; nd c which give the indices of the atoms involved in the linear angle abc. The last argument, u, is a unit vector used to defined the direction perpendicular to the direction in which distortion is measured. Atom numbering begins at atom 1, not atom 0.</p>
<h3>sc::LinOPSimpleCo::LinOPSimpleCo (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. This calls the <code>SimpleCo</code> keyval constructor with an integer argument of 3.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
