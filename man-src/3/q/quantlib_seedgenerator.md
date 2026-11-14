---
title: "quantlib_seedgenerator(3)"
name: "quantlib_seedgenerator"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_seedgenerator/"
description: "QuantLib::SeedGenerator – Random seed generator."
---

<p>QuantLib::SeedGenerator &#8211; Random seed generator. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/math/randomnumbers/seedgenerator.hpp&gt; </p>
<p> Inherits <code>Singleton&lt; SeedGenerator &gt;</code>. </p>
<h3>Public Member Functions</h3>
<p>unsigned long <code>get</code> () </p>
<h3>Friends</h3>
<p>class <code>Singleton&lt; SeedGenerator &gt;</code> </p>
<h2>Detailed Description</h2>
<p>Random seed generator. </p>
<p> Random number generator used for automatic generation of initialization seeds. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>correct initialization of the single instance is tested.</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
