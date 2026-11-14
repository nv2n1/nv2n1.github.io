---
title: "sc_renderedmolecule(3)"
name: "sc_renderedmolecule"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_renderedmolecule/"
description: "sc::RenderedMolecule –"
---

<p>sc::RenderedMolecule &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::RenderedObject</code>. Inherited by <code>sc::RenderedBallMolecule</code>, <code>sc::RenderedMolecularSurface</code>, and <code>sc::RenderedStickMolecule</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>RenderedMolecule (const Ref&lt; KeyVal &gt; &amp;keyval)



Ref&lt; Molecule &gt; molecule ()



virtual void init ()=0



void render (const Ref&lt; Render &gt; &amp;)



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>RenderedObject</code> &gt; <code>object_</code> </p>
<p> <code>Ref</code>&lt; <code>Molecule</code> &gt; <code>mol_</code> </p>
<p> <code>Ref</code>&lt; <code>AtomInfo</code> &gt; <code>atominfo_</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
