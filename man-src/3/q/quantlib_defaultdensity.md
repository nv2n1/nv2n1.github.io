---
title: "quantlib_defaultdensity(3)"
name: "quantlib_defaultdensity"
section: "3"
letter: "q"
url: "/docs/linux/man/3-quantlib_defaultdensity/"
description: "QuantLib::DefaultDensity – Default-density-curve traits."
---

<p>QuantLib::DefaultDensity &#8211; Default-density-curve traits. </p>
<h2>Synopsis</h2>
<p>#include &lt;ql/termstructures/credit/probabilitytraits.hpp&gt; </p>
<h3>Public Types</h3>
<p>typedef <code>BootstrapHelper</code>&lt; <code>DefaultProbabilityTermStructure</code> &gt; <code>helper</code> </p>
<h3>Static Public Member Functions</h3>
<p>static <code>Date</code> <code>initialDate</code> (const <code>DefaultProbabilityTermStructure</code> *c) </p>
<p> static <code>Real</code> <code>initialValue</code> (const <code>DefaultProbabilityTermStructure</code> *) </p>
<p> static bool <code>dummyInitialValue</code> () </p>
<p> static <code>Real</code> <code>initialGuess</code> () </p>
<p> static <code>Real</code> <code>guess</code> (const <code>DefaultProbabilityTermStructure</code> *c, const <code>Date</code> &amp;d) </p>
<p> static <code>Real</code> <code>minValueAfter</code> (Size, const std::vector&lt; <code>Real</code> &gt; &amp;) </p>
<p> static <code>Real</code> <code>maxValueAfter</code> (Size, const std::vector&lt; <code>Real</code> &gt; &amp;data) </p>
<p> static void <code>updateGuess</code> (std::vector&lt; <code>Real</code> &gt; &amp;data, <code>Real</code> density, Size i) </p>
<p> static Size <code>maxIterations</code> () </p>
<h2>Detailed Description</h2>
<p>Default-density-curve traits. </p>
<h2>Author</h2>
<p>Generated automatically by Doxygen for QuantLib from the source code.</p>
