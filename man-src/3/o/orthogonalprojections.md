---
title: "orthogonalprojections(3)"
name: "orthogonalprojections"
section: "3"
letter: "o"
url: "/docs/linux/man/3-orthogonalprojections/"
description: "QuantLib::OrthogonalProjections –"
---

<p>QuantLib::OrthogonalProjections &#8211; </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/matrixutilities/basisincompleteordered.hpp&gt; </p>
<h3>Public Member Functions</h3>
<p><code>OrthogonalProjections</code> (const <code>Matrix</code> &amp;originalVectors, <code>Real</code> multiplierCutOff, <code>Real</code> tolerance) </p>
<p> const std::vector&lt; bool &gt; &amp; <code>validVectors</code> () const </p>
<p> const std::vector&lt; <code>Real</code> &gt; &amp; <code>GetVector</code> (Size index) const </p>
<p> Size <code>numberValidVectors</code> () const </p>
<h2>Detailed Description</h2>
<p>Given a collection of vectors, w_i, find a collection of vectors x_i such that x_i is orthogonal to w_j for i != j, and &lt;x_i, w_i&gt; = &lt;w_i, w_i&gt; </p>
<p> This is done by performing GramSchmidt on the other vectors and then projecting onto the orthogonal space. </p>
<p> This class is tested in </p>
<p> MatricesTest::testOrthogonalProjection(); </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
