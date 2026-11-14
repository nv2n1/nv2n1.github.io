---
title: "sc_irreduciblerepresentation(3)"
name: "sc_irreduciblerepresentation"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_irreduciblerepresentation/"
description: "sc::IrreducibleRepresentation –"
---

<p>sc::IrreducibleRepresentation &#8211; </p>
<p> The <code>IrreducibleRepresentation</code> class provides information associated with a particular irreducible representation of a <code>point</code> group.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;pointgrp.h&gt;

Public Member Functions
IrreducibleRepresentation (const IrreducibleRepresentation &amp;)



IrreducibleRepresentation (int, int, const char *, const char *=0)


This constructor takes as arguments the order of the point group, the degeneracy of the irrep, and the Mulliken symbol of the irrep.


IrreducibleRepresentation &amp; operator= (const IrreducibleRepresentation &amp;)



void init (int=0, int=0, const char *=0, const char *=0)


Initialize the order, degeneracy, and Mulliken symbol of the irrep.


int order () const


Returns the order of the group.


int degeneracy () const


Returns the degeneracy of the irrep.


int complex () const


Returns the value of complex_.


int nproj () const


Returns the number of projection operators for the irrep.


int nrot () const


Returns the number of rotations associated with the irrep.


int ntrans () const


Returns the number of translations associated with the irrep.


const char * symbol () const


Returns the Mulliken symbol for the irrep.


const char * symbol_ns () const


Returns the Mulliken symbol for the irrep without special characters.


double character (int i) const


Returns the character for the i'th symmetry operation of the point group.


double p (int x1, int x2, int i) const


Returns the element (x1,x2) of the i'th representation matrix.


double p (int d, int i) const


Returns the character for the d'th contribution to the i'th representation matrix.


void print (std::ostream &amp;=ExEnv::out0()) const


This prints the irrep to the given file, or stdout if none is given.



Friends</code></pre>
<p> class <code>CharacterTable</code></p>
<h2>Detailed Description</h2>
<p>The <code>IrreducibleRepresentation</code> class provides information associated with a particular irreducible representation of a <code>point</code> group. </p>
<p> This includes the Mulliken symbol for the irrep, the degeneracy of the irrep, the characters which represent the irrep, and the number of translations and rotations in the irrep. The order of the <code>point</code> group is also provided (this is equal to the number of characters in an irrep).</p>
<h2>Constructor &amp; Destructor Documentation</h2>
<h3>sc::IrreducibleRepresentation::IrreducibleRepresentation (int, int, const char *, const char * = 0)</h3>
<p>This constructor takes as arguments the order of the <code>point</code> group, the degeneracy of the irrep, and the Mulliken symbol of the irrep. The Mulliken symbol is copied internally.</p>
<h2>Member Function Documentation</h2>
<h3>double sc::IrreducibleRepresentation::character (int i) const [inline]</h3>
<p>Returns the character for the i&#8217;th symmetry operation of the <code>point</code> group. </p>
<p> References sc::SymRep::trace().</p>
<h3>double sc::IrreducibleRepresentation::p (int d, int i) const [inline]</h3>
<p>Returns the character for the d&#8217;th <code>contribution</code> to the i&#8217;th representation matrix.</p>
<h3>void sc::IrreducibleRepresentation::print (std::ostream &amp; = ExEnv::out0()) const</h3>
<p>This prints the irrep to the given file, or stdout if none is given. The second argument is an optional string of spaces to offset by.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
