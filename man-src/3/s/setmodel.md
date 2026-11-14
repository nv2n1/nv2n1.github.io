---
title: "setmodel(3)"
name: "setmodel"
section: "3"
letter: "s"
url: "/docs/linux/man/3-setmodel/"
description: "QuantLib::GenericModelEngine – Base class for some pricing engine on a particular model."
---

<p>QuantLib::GenericModelEngine &#8211; Base class for some pricing engine on a particular model. </p>
<h2>Synopsis</h2>
<pre><code>
#include &lt;ql/pricingengines/genericmodelengine.hpp&gt;</code></pre>
<p> Inherits <code>GenericEngine&lt; ArgumentsType, ResultsType &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>GenericModelEngine</code> (const boost::shared_ptr&lt; ModelType &gt; &amp;model) </p>
<p> void <code>setModel</code> (const boost::shared_ptr&lt; ModelType &gt; &amp;model)</p>
<h3>Protected Attributes</h3>
<p>boost::shared_ptr&lt; ModelType &gt; <code>model_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class ModelType, class ArgumentsType, class ResultsType&gt; class QuantLib::GenericModelEngine&lt; ModelType, ArgumentsType, ResultsType &gt;</h3>
<p>Base class for some pricing engine on a particular model. </p>
<p> Derived engines only need to implement the calculate() method</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
