---
title: "quantlib_jumpdiffusionengine(3)"
name: "quantlib_jumpdiffusionengine"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_jumpdiffusionengine/"
description: "QuantLib::JumpDiffusionEngine – Jump-diffusion engine for vanilla options."
---

<p>QuantLib::JumpDiffusionEngine &#8211; Jump-diffusion engine for vanilla options. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/pricingengines/vanilla/jumpdiffusionengine.hpp&gt; </p>
<p> Inherits VanillaOption::engine. </p>
<h3>Public Member Functions</h3>
<p><code>JumpDiffusionEngine</code> (const boost::shared_ptr&lt; <code>Merton76Process</code> &gt; &amp;, <code>Real</code> relativeAccuracy_=1e-4, Size maxIterations=100) </p>
<p> void <code>calculate</code> () const </p>
<h2>Detailed Description</h2>
<p>Jump-diffusion engine for vanilla options. </p>
<p> <code>Tests</code></p>
<dl COMPACT>
<dd>
<dl COMPACT>
<dt>*</p>
<dd>the correctness of the returned value is tested by reproducing results available in literature.</p>
<dt>*</p>
<dd>the correctness of the returned greeks is tested by reproducing numerical derivatives.</dl>
</dl>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
