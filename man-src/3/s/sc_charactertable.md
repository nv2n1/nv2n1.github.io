---
title: "sc_charactertable(3)"
name: "sc_charactertable"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_charactertable/"
description: "sc::CharacterTable –"
---

<p>sc::CharacterTable &#8211; </p>
<p> The <code>CharacterTable</code> class provides a workable character table for all of the non-cubic <code>point</code> groups.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pointgrp.h&gt;

Public Types</code></pre>
<p> enum <code>pgroups</code> { <code>C1</code>, <code>CS</code>, <code>CI</code>, <code>CN</code>, <code>CNV</code>, <code>CNH</code>, <code>DN</code>, <code>DND</code>, <code>DNH</code>, <code>SN</code>, <code>T</code>, <code>TH</code>, <code>TD</code>, <code>O</code>, <code>OH</code>, <code>I</code>, <code>IH</code> }</p>
<h3>Public Member Functions</h3>
<p><code>CharacterTable</code> (const char *)<br />
 <i>This constructor takes the Schoenflies symbol of a </i><code>point</code> group as input.<br />
 <code>CharacterTable</code> (const char *, const <code>SymmetryOperation</code> &amp;)<br />
 <i>This is like the above, but it also takes a reference to a </i><code>SymmetryOperation</code> which is the frame of reference.<br />
 <code>CharacterTable</code> (const <code>CharacterTable</code> &amp;) </p>
<p> <code>CharacterTable</code> &amp; <code>operator=</code> (const <code>CharacterTable</code> &amp;) </p>
<p> int <code>nirrep</code> () const<br />
 <i>Returns the number of irreps. </i><br />
 int <code>order</code> () const<br />
 <i>Returns the order of the </i><code>point</code> group.<br />
 const char * <code>symbol</code> () const<br />
 <i>Returns the Schoenflies symbol for the </i><code>point</code> group.<br />
 <code>IrreducibleRepresentation</code> &amp; <code>gamma</code> (int i)<br />
 <i>Returns the i&#8217;th irrep. </i><br />
 <code>SymmetryOperation</code> &amp; <code>symm_operation</code> (int i)<br />
 <i>Returns the i&#8217;th symmetry operation. </i><br />
 int <code>complex</code> () const<br />
 <i>Cn, Cnh, Sn, T, and Th </i><code>point</code> groups have complex representations.<br />
 int <code>inverse</code> (int i) const<br />
 <i>Returns the index of the symop which is the inverse of symop[i]. </i><br />
 int <code>ncomp</code> () const </p>
<p> int <code>which_irrep</code> (int i)<br />
 <i>Returns the irrep component i belongs to. </i><br />
 int <code>which_comp</code> (int i)<br />
 <i>Returns which component i is. </i><br />
 void <code>print</code> (std::ostream &amp;=ExEnv::out0()) const<br />
 <i>This prints the irrep to the given file, or stdout if none is given. </i></p>
<h2>Detailed Description</h2>
<p>The <code>CharacterTable</code> class provides a workable character table for all of the non-cubic <code>point</code> groups. </p>
<p> While I have tried to match the ordering in Cotton&#8217;s book, I don&#8217;t guarantee that it is always followed. It shouldn&#8217;t matter anyway. Also note that I don&#8217;t lump symmetry operations of the same class together. For example, in C3v there are two distinct C3 rotations and 3 distinct reflections, each with a separate character. Thus symop has 6 elements rather than the 3 you&#8217;ll find in most published character tables.</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::CharacterTable::CharacterTable (const char *)</h3>
<p>This constructor takes the Schoenflies symbol of a <code>point</code> group as input.</p>
<h3>sc::CharacterTable::CharacterTable (const char *, const <code>SymmetryOperation</code> &amp;)</h3>
<p>This is like the above, but it also takes a reference to a <code>SymmetryOperation</code> which is the frame of reference. All symmetry operations are transformed to this frame of reference.</p>
<h2>Member Function Documentation</h2>
<h3>int sc::CharacterTable::complex () const [inline]</h3>
<p>Cn, Cnh, Sn, T, and Th <code>point</code> groups have complex representations. This function returns 1 if the <code>point</code> group has a complex representation, 0 otherwise.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
