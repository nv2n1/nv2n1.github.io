---
title: "sc_stresimpleco(3)"
name: "sc_stresimpleco"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_stresimpleco/"
description: "sc::StreSimpleCo –"
---

<p>sc::StreSimpleCo &#8211; </p>
<p> The <code>StreSimpleCo</code> class describes an stretch internal coordinate of a molecule.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;simple.h&gt;</code></pre>
<p> Inherits <code>sc::SimpleCo</code>.</p>
<h3>Public Member Functions</h3>
<p><code>StreSimpleCo</code> (const <code>StreSimpleCo</code> &amp;) </p>
<p> <code>StreSimpleCo</code> (const char *, int, int)<br />
 <i>This constructor takes a string containing a label, and two integers which are the indices of the atoms we&#8217;re measuring the distance between. </i><br />
 <code>StreSimpleCo</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 const char * <code>ctype</code> () const<br />
 <i>Always returns the string &#8216;STRE&#8217;. </i><br />
 double <code>bohr</code> () const<br />
 <i>Returns the distance between the two atoms in atomic units. </i><br />
 double <code>angstrom</code> () const<br />
 <i>Returns the distance between the two atoms in angstrom units. </i><br />
 double <code>preferred_value</code> () const<br />
 <i>Returns the distance between the two atoms in angstrom units. </i></p>
<h2>Detailed Description</h2>
<p>The <code>StreSimpleCo</code> class describes an stretch internal coordinate of a molecule. </p>
<p> The input is described in the documentation of its parent class <code>SimpleCo</code>. </p>
<p> Designating the two atoms as $a$ and $b$ and their cartesian positions as $$ and $lue of the coordinate, $r$, is [ r = &#8211; tion&quot;</p>
<h3>sc::StreSimpleCo::StreSimpleCo (const char *, int, int)</h3>
<p>This constructor takes a string containing a label, and two integers which are the indices of the atoms we&#8217;re measuring the distance between. Atom numbering begins at atom 1, not atom 0.</p>
<h3>sc::StreSimpleCo::StreSimpleCo (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)</h3>
<p>The <code>KeyVal</code> constructor. This calls the <code>SimpleCo</code> keyval constructor with an integer argument of 2.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
