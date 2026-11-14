---
title: "sc_vdwshape(3)"
name: "sc_vdwshape"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_vdwshape/"
description: "sc::VDWShape –"
---

<p>sc::VDWShape &#8211; </p>
<p> The <code>VDWShape</code> class describes the surface of a molecule as the union of atom centered spheres, each the van der Waals radius of the atom.</p>
<h2>Synopsis</h2>
<pre><code>

#include &lt;molshape.h&gt;</code></pre>
<p> Inherits <code>sc::UnionShape</code>.</p>
<h3>Public Member Functions</h3>
<p><code>VDWShape</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;) </p>
<p> <code>VDWShape</code> (const <code>Ref</code>&lt; <code>KeyVal</code> &gt; &amp;) </p>
<p> void <code>initialize</code> (const <code>Ref</code>&lt; <code>Molecule</code> &gt; &amp;)</p>
<h2>Detailed Description</h2>
<p>The <code>VDWShape</code> class describes the surface of a molecule as the union of atom centered spheres, each the van der Waals radius of the atom.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
