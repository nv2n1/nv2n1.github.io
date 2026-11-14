---
title: "sc_redundmolecularcoor(3)"
name: "sc_redundmolecularcoor"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_redundmolecularcoor/"
description: "sc::RedundMolecularCoor –"
---

<p>sc::RedundMolecularCoor &#8211; </p>
<p> The <code>RedundMolecularCoor</code> class provides a redundant set of simple internal coordinates.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;coor.h&gt;</code></pre>
<p> Inherits <code>sc::IntMolecularCoor</code>.</p>
<h3>Public Member Functions</h3>
<p><code>RedundMolecularCoor</code> (<code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;mol) </p>
<p> <code>RedundMolecularCoor</code> (<code>StateIn</code> &amp;) </p>
<p> <code>RedundMolecularCoor</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;)<br />
 <i>The </i><code>KeyVal</code> constructor.<br />
 void <code>save_data_state</code> (<code>StateOut</code> &amp;)<br />
 <i>Save the base classes (with save_data_state) and the members in the same order that the </i><code>StateIn</code> CTOR initializes them.<br />
 void <code>form_coordinates</code> (int keep_variable=0)<br />
 <i>Actually form the variable and constant internal coordinates from the simple internal coordinates. </i><br />
 void <code>guess_hessian</code> (<code>RefSymmSCMatrix</code> &amp;hessian)<br />
 <i>Form the approximate hessian. </i><br />
 <code>RefSymmSCMatrix</code> <code>inverse_hessian</code> (<code>RefSymmSCMatrix</code> &amp;)<br />
 <i>Invert the hessian. </i></p>
<h2>Detailed Description</h2>
<p>The <code>RedundMolecularCoor</code> class provides a redundant set of simple internal coordinates.</p>
<h2>Member Function Documentation</h2>
<h3>void sc::RedundMolecularCoor::form_coordinates (int keep_variable = 0) [virtual]</h3>
<p>Actually form the variable and constant internal coordinates from the simple internal coordinates. </p>
<p> Implements <code>sc::IntMolecularCoor</code>.</p>
<h3>void sc::RedundMolecularCoor::save_data_state (<code>StateOut</code> &amp;) [virtual]</h3>
<p>Save the base classes (with save_data_state) and the members in the same order that the <code>StateIn</code> CTOR initializes them. This must be implemented by the derived class if the class has data. </p>
<p> Reimplemented from <code>sc::IntMolecularCoor</code>.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
