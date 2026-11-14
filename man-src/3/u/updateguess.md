---
title: "updateguess(3)"
name: "updateguess"
section: "3"
letter: "u"
url: "/docs/linux/man/3-updateguess/"
description: "QuantLib::HazardRate – Hazard-rate-curve traits."
---

<p>QuantLib::HazardRate &#8211; Hazard-rate-curve traits. </p>
<h2>Synopsis</h2>
<pre><code>static Date initialDate (const DefaultProbabilityTermStructure *c)



static Real initialValue (const DefaultProbabilityTermStructure *)



static bool dummyInitialValue ()



static Real initialGuess ()



static Real guess (const DefaultProbabilityTermStructure *c, const Date &amp;d)



static Real minValueAfter (Size, const std::vector&lt; Real &gt; &amp;)



static Real maxValueAfter (Size, const std::vector&lt; Real &gt; &amp;data)



static void updateGuess (std::vector&lt; Real &gt; &amp;data, Real rate, Size i)



static Size maxIterations ()</code></pre>
<h3>Public Types</h3>
<p>typedef <code>BootstrapHelper</code>&lt; <code>DefaultProbabilityTermStructure</code> &gt; <code>helper</code></p>
<h3>Static Public Member Functions</h3>
<pre><code>static Date initialDate (const DefaultProbabilityTermStructure *c)



static Real initialValue (const DefaultProbabilityTermStructure *)



static bool dummyInitialValue ()



static Real initialGuess ()



static Real guess (const DefaultProbabilityTermStructure *c, const Date &amp;d)



static Real minValueAfter (Size, const std::vector&lt; Real &gt; &amp;)



static Real maxValueAfter (Size, const std::vector&lt; Real &gt; &amp;data)



static void updateGuess (std::vector&lt; Real &gt; &amp;data, Real rate, Size i)



static Size maxIterations ()</code></pre>
<h2>Detailed Description</h2>
<p>Hazard-rate-curve traits.</p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
