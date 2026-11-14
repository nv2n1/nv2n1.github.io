---
title: "sc_molecularformula(3)"
name: "sc_molecularformula"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_molecularformula/"
description: "sc::MolecularFormula –"
---

<p>sc::MolecularFormula &#8211; </p>
<p> The <code>MolecularFormula</code> class is used to calculate the molecular formula of a <code>Molecule</code>.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;formula.h&gt;

Public Member Functions</code></pre>
<p> <code>MolecularFormula</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;m)<br />
 <i>Constructors. The argument must be nonnull. </i><br />
 <code>MolecularFormula</code> (const <code>Molecule</code> *m) </p>
<p> const char * <code>formula</code> () const<br />
 <i>Returns a null terminated string containing the molecular formula. </i><br />
 int <code>natomtypes</code> ()<br />
 <i>Returns the number of atomtypes. </i><br />
 int <code>Z</code> (int itype)<br />
 <i>Returns atomic number of given atomtypeindex. </i><br />
 int <code>nZ</code> (int itype)<br />
 <i>Returns number of atoms of given atomtypeindex. </i></p>
<h2>Detailed Description</h2>
<p>The <code>MolecularFormula</code> class is used to calculate the molecular formula of a <code>Molecule</code>. </p>
<p> There is only one constructor which takes <code>Ref&lt;Molecule&gt;</code> as input.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
