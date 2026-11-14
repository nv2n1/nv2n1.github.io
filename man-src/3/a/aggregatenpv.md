---
title: "aggregatenpv(3)"
name: "aggregatenpv"
section: "3"
letter: "a"
url: "/docs/linux/man/3-aggregatenpv/"
description: "ql/experimental/risk/sensitivityanalysis.hpp – sensitivity analysis function"
---

<p>ql/experimental/risk/sensitivityanalysis.hpp &#8211; sensitivity analysis function </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/types.hpp&gt;<br />
 #include &lt;ql/utilities/null.hpp&gt;<br />
 #include &lt;boost/shared_ptr.hpp&gt;<br />
 #include &lt;vector&gt; </p>
<h3>Enumerations</h3>
<p>enum <code>SensitivityAnalysis</code> { <code>OneSide</code>, <code>Centered</code> }<br />
 <i>Finite differences calculation. </i></p>
<h3>Functions</h3>
<p>Real <code>aggregateNPV</code> (const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities)<br />
 <i>utility fuction for weighted sum of NPVs </i><br />
 std::pair&lt; Real, Real &gt; <code>parallelAnalysis</code> (const std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())<br />
 <i>parallel shift sensitivity analysis for a </i><code>SimpleQuote</code> vector<br />
 std::pair&lt; Real, Real &gt; <code>parallelAnalysis</code> (const std::vector&lt; std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())<br />
 <i>parallel shift sensitivity analysis for a </i><code>SimpleQuote</code> matrix<br />
 std::pair&lt; Real, Real &gt; <code>bucketAnalysis</code> (Handle&lt; SimpleQuote &gt; quote, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered, Real referenceNpv=Null&lt; Real &gt;())<br />
 <i>(bucket) sensitivity analysis for a (single) </i><code>SimpleQuote</code><br />
 std::pair&lt; std::vector&lt; Real &gt;, std::vector&lt; Real &gt; &gt; <code>bucketAnalysis</code> (const std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered)<br />
 <i>bucket sensitivity analysis for a </i><code>SimpleQuote</code> vector<br />
 std::pair&lt; std::vector&lt; std::vector&lt; Real &gt; &gt;, std::vector&lt; std::vector&lt; Real &gt; &gt; &gt; <code>bucketAnalysis</code> (const std::vector&lt; std::vector&lt; Handle&lt; SimpleQuote &gt; &gt; &gt; &amp;, const std::vector&lt; boost::shared_ptr&lt; Instrument &gt; &gt; &amp;, const std::vector&lt; Real &gt; &amp;quantities, Real shift=0.0001, SensitivityAnalysis type=Centered)<br />
 <i>bucket sensitivity analysis for a </i><code>SimpleQuote</code> matrix</p>
<h2>Detailed Description</h2>
<p>sensitivity analysis function </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
