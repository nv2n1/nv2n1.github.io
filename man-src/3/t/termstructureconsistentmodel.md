---
title: "termstructureconsistentmodel(3)"
name: "termstructureconsistentmodel"
section: "3"
letter: "t"
url: "/docs/linux/man/3-termstructureconsistentmodel/"
description: "QuantLib::TermStructureConsistentModel – Term-structure consistent model class."
---

<p>QuantLib::TermStructureConsistentModel &#8211; Term-structure consistent model class. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/models/model.hpp&gt; </p>
<p> Inherits <code>QuantLib::Observable</code>. </p>
<p> Inherited by <code>BlackKarasinski</code>, <code>ExtendedCoxIngersollRoss</code>, <code>G2</code>, and <code>HullWhite</code>. </p>
<h3>Public Member Functions</h3>
<p><code>TermStructureConsistentModel</code> (const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp;termStructure) </p>
<p> const <code>Handle</code>&lt; <code>YieldTermStructure</code> &gt; &amp; <code>termStructure</code> () const </p>
<h2>Detailed Description</h2>
<p>Term-structure consistent model class. </p>
<p> This is a base class for models that can reprice exactly any discount bond. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
