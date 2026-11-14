---
title: "originalengine_(3)"
name: "originalengine_"
section: "3"
letter: "o"
url: "/docs/linux/man/3-originalengine_/"
description: "QuantLib::ForwardVanillaEngine – Forward engine for vanilla options"
---

<p>QuantLib::ForwardVanillaEngine &#8211; Forward engine for vanilla options </p>
<h2>Synopsis</h2>
<pre><code>void setup () const



void getOriginalResults () const



Protected Attributes</code></pre>
<p> Inherits <code>GenericEngine&lt; ForwardOptionArguments&lt; VanillaOption::arguments &gt;, VanillaOption::results &gt;</code>.</p>
<h3>Public Member Functions</h3>
<p><code>ForwardVanillaEngine</code> (const boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; &amp;) </p>
<p> void <code>calculate</code> () const</p>
<h3>Protected Member Functions</h3>
<pre><code>void setup () const



void getOriginalResults () const



Protected Attributes</code></pre>
<p> boost::shared_ptr&lt; <code>GeneralizedBlackScholesProcess</code> &gt; <code>process_</code> </p>
<p> boost::shared_ptr&lt; Engine &gt; <code>originalEngine_</code> </p>
<p> <code>VanillaOption::arguments</code> * <code>originalArguments_</code> </p>
<p> const VanillaOption::results * <code>originalResults_</code></p>
<h2>Detailed Description</h2>
<h3>template&lt;class Engine&gt; class QuantLib::ForwardVanillaEngine&lt; Engine &gt;</h3>
<p>Forward engine for vanilla options </p>
<p> <code>Tests</code></p>
<dl>
<dd>
<dl>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
