---
title: "sensitivityanalysis(3)"
name: "sensitivityanalysis"
section: "3"
letter: "s"
url: "/docs/linux/man/3-sensitivityanalysis/"
description: "ql/experimental/risk/sensitivityanalysis.hpp – sensitivity analysis function"
---

<p>ql/experimental/risk/sensitivityanalysis.hpp &#8211; sensitivity analysis function </p>
<h2>Synopsis</h2>
<pre><code>Real aggregateNPV (const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities)


utility fuction for weighted sum of NPVs


std::pair&lt; Real, Real &gt; parallelAnalysis (const std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())


parallel shift sensitivity analysis for a SimpleQuote vector


std::pair&lt; Real, Real &gt; parallelAnalysis (const std::vector&lt; std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())


parallel shift sensitivity analysis for a SimpleQuote matrix


std::pair&lt; Real, Real &gt; bucketAnalysis (Handle&lt; SimpleQuote &gt; quote, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())


(bucket) sensitivity analysis for a (single) SimpleQuote


std::pair&lt; std::vector&lt; Real &gt;, std::vector&lt; Real &gt; &gt; bucketAnalysis (const std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered)


bucket sensitivity analysis for a SimpleQuote vector


std::pair&lt; std::vector&lt; std::vector&lt; Real &gt; &gt;, std::vector&lt; std::vector&lt; Real &gt; &gt; &gt; bucketAnalysis (const std::vector&lt; std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered)


bucket sensitivity analysis for a SimpleQuote matrix</code></pre>
<h3>Enumerations</h3>
<p>enum <code>SensitivityAnalysis</code> { <code>OneSide</code>, <code>Centered</code> }<br />
 <i>Finite differences calculation. </i></p>
<h3>Functions</h3>
<pre><code>Real aggregateNPV (const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities)


utility fuction for weighted sum of NPVs


std::pair&lt; Real, Real &gt; parallelAnalysis (const std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())


parallel shift sensitivity analysis for a SimpleQuote vector


std::pair&lt; Real, Real &gt; parallelAnalysis (const std::vector&lt; std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())


parallel shift sensitivity analysis for a SimpleQuote matrix


std::pair&lt; Real, Real &gt; bucketAnalysis (Handle&lt; SimpleQuote &gt; quote, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())


(bucket) sensitivity analysis for a (single) SimpleQuote


std::pair&lt; std::vector&lt; Real &gt;, std::vector&lt; Real &gt; &gt; bucketAnalysis (const std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered)


bucket sensitivity analysis for a SimpleQuote vector


std::pair&lt; std::vector&lt; std::vector&lt; Real &gt; &gt;, std::vector&lt; std::vector&lt; Real &gt; &gt; &gt; bucketAnalysis (const std::vector&lt; std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered)


bucket sensitivity analysis for a SimpleQuote matrix</code></pre>
<h2>Detailed Description</h2>
<p>sensitivity analysis function</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
