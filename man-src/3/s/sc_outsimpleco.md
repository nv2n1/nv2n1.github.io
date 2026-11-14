---
title: "sc_outsimpleco(3)"
name: "sc_outsimpleco"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_outsimpleco/"
description: "sc::OutSimpleCo –"
---

<p>sc::OutSimpleCo &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::SimpleCo</code>.</p>
<h3>Public Member Functions</h3>
<p><code>OutSimpleCo</code> (const <code>OutSimpleCo</code> &amp;) </p>
<p> <code>OutSimpleCo</code> (const char *refr, int, int, int, int)<br />
 <i>This constructor takes a string containing a label, and four integers a, b, c, and d which give the indices of the atoms involved in the out-of-plane angle abcd. </i><br />
 <code>OutSimpleCo</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 const char * <code>ctype</code> () const<br />
 <i>Always returns the string &#8216;OUT&#8217;. </i><br />
 double <code>radians</code> () const<br />
 <i>Returns the value of the angle abc in radians. </i><br />
 double <code>degrees</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i><br />
 double <code>preferred_value</code> () const<br />
 <i>Returns the value of the angle abc in degrees. </i></p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::OutSimpleCo::OutSimpleCo (const char * refr, int, int, int, int)</h3>
<p>This constructor takes a string containing a label, and four integers a, b, c, and d which give the indices of the atoms involved in the out-of-plane angle abcd. Atom numbering begins at atom 1, not atom 0.</p>
<h3>sc::OutSimpleCo::OutSimpleCo (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. This calls the <code>SimpleCo</code> keyval constructor with an integer argument of 4.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
