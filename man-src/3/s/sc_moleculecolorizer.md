---
title: "sc_moleculecolorizer(3)"
name: "sc_moleculecolorizer"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_moleculecolorizer/"
description: "sc::MoleculeColorizer –"
---

<p>sc::MoleculeColorizer &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::DescribedClass</code>. Inherited by <code>sc::AtomProximityColorizer</code>, <code>sc::DensityColorizer</code>, and <code>sc::GradDensityColorizer</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>MoleculeColorizer (const Ref&lt; Molecule &gt; &amp;)



MoleculeColorizer (const Ref&lt; KeyVal &gt; &amp;)



virtual void colorize (const Ref&lt; RenderedPolygons &gt; &amp;)=0



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>Molecule</code> &gt; <code>mol_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
