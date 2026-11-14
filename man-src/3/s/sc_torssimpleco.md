---
title: "sc_torssimpleco(3)"
name: "sc_torssimpleco"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_torssimpleco/"
description: "sc::TorsSimpleCo –"
---

<p>sc::TorsSimpleCo &#8211; </p>
<p> The <code>TorsSimpleCo</code> class describes an torsion internal coordinate of a molecule.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;simple.h&gt;</code></pre>
<p> Inherits <code>sc::SimpleCo</code>.</p>
<h3>Public Member Functions</h3>
<p><code>TorsSimpleCo</code> (const <code>TorsSimpleCo</code> &amp;) </p>
<p> <code>TorsSimpleCo</code> (const char *refr, int, int, int, int)<br />
 <i>This constructor takes a string containing a label, and four integers a, b, c, and d which give the indices of the atoms involved in the torsion angle abcd. </i><br />
 <code>TorsSimpleCo</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 const char * <code>ctype</code> () const<br />
 <i>Always returns the string &#8216;TORS&#8217;. </i><br />
 double <code>radians</code> () const<br />
 <i>Returns the value of the angle abc in radians. </i><br />
 double <code>degrees</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i><br />
 double <code>preferred_value</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i></p>
<h2>Detailed Description</h2>
<p>The <code>TorsSimpleCo</code> class describes an torsion internal coordinate of a molecule. </p>
<p> The input is described in the documentation of its parent class <code>SimpleCo</code>. </p>
<p> Designating the four atoms as $a$, $b$, $c$, and $d$ and their cartesian positions as $$, $te, $ au$, is given by </p>
<p> [ b} = ac{ &#8211; tom 0.</p>
<h3>sc::TorsSimpleCo::TorsSimpleCo (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. This calls the <code>SimpleCo</code> keyval constructor with an integer argument of 4.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
