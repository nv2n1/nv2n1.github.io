---
title: "sc_symmonebodyintiter(3)"
name: "sc_symmonebodyintiter"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sc_symmonebodyintiter/"
description: "sc::SymmOneBodyIntIter –"
---

<p>sc::SymmOneBodyIntIter &#8211;</p>
<h2>Synopsis</h2>
<p> Inherits <code>sc::OneBodyIntIter</code>.</p>
<h3>Public Member Functions</h3>
<pre><code>SymmOneBodyIntIter (const Ref&lt; OneBodyInt &gt; &amp;, const Ref&lt; PetiteList &gt; &amp;)



void start (int ist=0, int jst=0, int ien=0, int jen=0)



void next ()



double scale () const



bool cloneable ()



Ref&lt; OneBodyIntIter &gt; clone ()



Protected Attributes</code></pre>
<p> <code>Ref</code>&lt; <code>PetiteList</code> &gt; <code>pl</code> </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for MPQC from the source code.</p>
